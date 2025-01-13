def quick_analyze_resume(_client, resume, job_description):
    prompt = f"""
    Conduct a quick analysis of the resume against the job description.
    Provide a concise summary including:
    1. Skills Match:
    • List top 5 required skills and rate candidate's proficiency (None/Basic/Intermediate/Advanced)
    • Identify critical missing skills
    2. Experience Alignment:
    • Compare required experience vs. demonstrated experience
    • Highlight most relevant roles/achievements
    3. Pros and Cons:
    • List top 3 strengths of the candidate for this role
    • List top 3 areas for improvement
    4. Match Percentage:
    • Provide an overall match percentage based on skills, experience, and qualifications
    • Briefly explain the rationale for this percentage
    Resume: {resume}
    Job Description: {job_description}
    Provide a concise, bullet-point response focusing on key insights and actionable information.
    """

    response = _client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content

def in_depth_analyze_resume(_client, resume, job_description):
    prompt = f"""
    Conduct a detailed analysis of the resume against the job description.
    Your response should follow this structured format:
    PART 1: INITIAL SKILL GAP ANALYSIS
    1. Core Technical Skills Match:
    • List each required technical skill from the job description
    • Rate the candidate's demonstrated proficiency (None/Basic/Intermediate/Advanced)
    • Flag critical missing skills
    • Suggest specific ways to demonstrate or acquire missing skills
    PART 2: EXPERIENCE AND IMPACT ANALYSIS
    2. Professional Experience Alignment:
    • Compare years and type of experience required vs. demonstrated
    • Analyze relevance of each role to the target position
    • Identify experience gaps and how to address them
    • Suggest better ways to present existing experience
    3. Achievement Impact Enhancement:
    • Review current achievement statements
    • Provide specific rewording suggestions using the STAR method
    • Add missing quantifiable metrics where possible
    • Suggest additional achievements to highlight based on job requirements
    PART 3: OPTIMIZATION RECOMMENDATIONS
    4. Content Enhancement:
    • Analyze each resume section for relevance and impact
    • Suggest specific additions or deletions
    • Provide word-for-word revisions for weak bullet points
    • Recommend additional sections if needed
    PART 4: STRATEGIC RECOMMENDATIONS
    5. Competitive Edge Analysis:
    • Identify unique qualifications that set the candidate apart
    • Suggest ways to emphasize distinctive experiences
    • Recommend positioning strategies for potential weaknesses
    • Outline talking points for addressing experience gaps
    6. Application Strategy:
    • Suggest customization strategies for this specific role
    • Outline key talking points for cover letter
    • Provide interview preparation recommendations
    • List potential references or endorsements to seek
    7. Overall Match Percentage:
    • Provide an overall match percentage based on skills, experience, and qualifications
    • Explain the rationale for this percentage
    Resume: {resume}
    Job Description: {job_description}
    For each suggestion, include:
    • What to change
    • How to change it
    • Why it matters
    • Example of the improved version (concise and clear)
    """

    response = _client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        max_tokens=32768,
        temperature=0.7,
    )
    return response.choices[0].message.content

def enhance_resume(_client, analysis, resume):
    prompt = f"""
    Based on the following in-depth analysis and the original resume, create an enhanced version of the resume.
    Focus on addressing the suggestions and improvements mentioned in the analysis.
    Provide a complete, well-formatted resume text that includes all sections (Professional Experience, Projects, Education, Core Competencies, Achievements).
    Ensure proper formatting and arrangement of sections, especially for projects and other key areas.
    Only modify the sections that need changes according to the analysis.
    For sections that don't require changes, keep the original content.
    Analysis: {analysis}
    Original Resume: {resume}
    The enhanced resume should be ready to use, with all sections properly formatted and content optimized based on the analysis.
    Clearly indicate which sections have been modified and explain the changes made.
    """

    response = _client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        max_tokens=32768,
        temperature=0.7,
    )
    return response.choices[0].message.content




def generate_formatted_resume_html(_client, enhanced_resume):
    prompt = f"""
    Convert the enhanced resume into a single-page HTML document optimized for ATS and human readability.
    
    **Content and Formatting Requirements**:
    1. **Structure**:
       - Use semantic HTML5 elements (e.g., <header>, <section>, <footer>) for clarity.
       - Create a main container div with class "resume-container".
       - Include distinct sections for:
         - Contact Information (e.g., Name, Email, Phone, LinkedIn)
         - Summary/Objective
         - Professional Experience
         - Projects (highlight tech stack, methodologies, and measurable achievements)
         - Education
         - Technical Skills
       - Present projects and achievements in detail, including combined tech stack information for a polished look.
    
    2. **CSS Styling**:
       - Page width: 8.5in (US Letter).
       - Margins: 0.5in on all sides.
       - Font: Use professional, readable fonts (e.g., Arial, Helvetica, sans-serif).
       - Font-size: 12px for body, 14-16px for headings.
       - Line-height: 1.4-1.6 for readability.
       - Apply a print media query to ensure the entire resume fits on one page when printed.
       - Use subtle styling to differentiate sections (e.g., bold section titles, slight background shading for headers).

    3. **Ensure Valid HTML**:
       - Include the following exact elements:
         1. <!DOCTYPE html>
         2. <html lang="en">
         3. <head> with:
            - Character encoding meta tag
            - Title tag
            - Style tag for CSS
         4. <body> with the structured resume content.
    
    Resume Content to Convert: {enhanced_resume}
    
    IMPORTANT: Provide a complete, valid HTML document. Ensure all sections are properly nested and visually appealing.
    """
    
    response = _client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        max_tokens=32768,
        temperature=0.7,
    )
    return response.choices[0].message.content
