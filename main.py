import streamlit as st
import groq
import docx2txt
from prompts import quick_analyze_resume, in_depth_analyze_resume, enhance_resume, generate_formatted_resume_html
from flowchart import display_architecture_diagram
import docx
from io import BytesIO
from diff_match_patch import diff_match_patch

def create_docx(content):
    doc = docx.Document()
    doc.add_paragraph(content)
    doc_io = BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

def show_diff(text1, text2):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(text1, text2)
    dmp.diff_cleanupSemantic(diffs)
    
    html = []
    for (op, data) in diffs:
        if op == 1:  # insertion
            html.append(f'<span style="background-color: #aaffaa">{data}</span>')
        elif op == -1:  # deletion
            html.append(f'<span style="text-decoration: line-through; background-color: #ffaaaa">{data}</span>')
        else:  # equal
            html.append(data)
            
    return ''.join(html)

def main():
    # Streamlit UI with clean layout
    st.set_page_config(layout="wide", page_title="Resume Analyzer and Enhancer")

    # Add custom CSS for better spacing and organization
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            margin-top: 1rem;
        }
        .st-emotion-cache-16idsys p {
            margin-bottom: 0.5rem;
        }
        .main-container {
            padding: 2rem;
        }
        </style>
        """, unsafe_allow_html=True)

    with st.container():
        st.title("Resume Analyzer and Enhancer")
        
        # Toggle for architecture diagram with better spacing
        if st.toggle('Show System Architecture', False):
            st.subheader("System Architecture Diagram")
            graph = display_architecture_diagram()
            st.graphviz_chart(graph)

        # File upload section with clear separation
        col1, col2 = st.columns([1, 1])
        with col1:
            uploaded_file = st.file_uploader("Upload your resume (DOCX format)", type="docx")
        with col2:
            if uploaded_file is not None:
                resume_text = docx2txt.process(uploaded_file)
            else:
                resume_text = st.text_area(
                    "Or paste your resume text here:",
                    placeholder="Enter your resume content...",
                    height=200
                )

        # Job description and API key in separate columns
        col3, col4 = st.columns([2, 1])
        with col3:
            job_description = st.text_area("Paste the job description here:", height=150)
        with col4:
            key = st.text_input("Enter your GROQ key:", type="password")

        # Initialize Groq client
        if key:
            client = groq.Client(api_key=key)

            # Action selection with better organization
            action = st.radio("Choose an action:", ("Analyze Resume", "Enhance Resume"))

            if action == "Analyze Resume":
                analysis_type = st.radio("Choose analysis type:", ("Quick Comparison", "In-Depth Analysis"))
                
                if st.button("Analyze"):
                    if resume_text and job_description:
                        with st.spinner("Analyzing resume..."):
                            if analysis_type == "Quick Comparison":
                                analysis = quick_analyze_resume(client, resume_text, job_description)
                            else:
                                analysis = in_depth_analyze_resume(client, resume_text, job_description)
                            st.subheader("Analysis Results")
                            st.markdown(analysis)
                    else:
                        st.warning("Please provide both resume and job description.")
            else:
                if st.button("Enhance Resume"):
                    if resume_text and job_description:
                        with st.spinner("Analyzing and enhancing resume..."):
                            analysis = in_depth_analyze_resume(client, resume_text, job_description)
                            enhanced_resume = enhance_resume(client, analysis, resume_text)
                            formatted_html = generate_formatted_resume_html(client, enhanced_resume)

                            # Create tabs for different views
                            tab1, tab2, tab3, tab4 = st.tabs(["Plain Text", "Formatted HTML", "Comparison", "Download Options"])
                            
                            with tab1:
                                st.text_area("Enhanced Resume Text:", enhanced_resume, height=400)
                            
                            with tab2:
                                # Open in new window button
                                if st.button("Open in New Window"):
                                    html_content = f"""
                                    <!DOCTYPE html>
                                    <html>
                                    <head>
                                        <title>Enhanced Resume</title>
                                    </head>
                                    <body>
                                        {formatted_html}
                                    </body>
                                    </html>
                                    """
                                    st.components.v1.html(html_content, height=800, scrolling=True)
                                    st.markdown(f'<a href="data:text/html;base64,{html_content}" target="_blank">Open in New Window</a>', unsafe_allow_html=True)
                                
                                st.components.v1.html(formatted_html, height=800, scrolling=True)
                            
                            with tab3:
                                st.subheader("Changes Highlighted")
                                diff_html = show_diff(resume_text, enhanced_resume)
                                st.components.v1.html(diff_html, height=800, scrolling=True)
                            
                            with tab4:
                                # Download options
                                docx_file = create_docx(enhanced_resume)
                                
                                col5, col6, col7 = st.columns(3)
                                with col5:
                                    st.download_button(
                                        label="Download as DOCX",
                                        data=docx_file,
                                        file_name="enhanced_resume.docx",
                                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                    )
                                with col6:
                                    st.download_button(
                                        label="Download as HTML",
                                        data=formatted_html,
                                        file_name="enhanced_resume.html",
                                        mime="text/html"
                                    )
                                with col7:
                                    st.download_button(
                                        label="Download as Text",
                                        data=enhanced_resume,
                                        file_name="enhanced_resume.txt",
                                        mime="text/plain"
                                    )
                    else:
                        st.warning("Please provide both resume and job description.")
        else:
            st.warning("Please enter your GROQ API key to proceed.")

if __name__=="__main__":
    main()