import streamlit
import graphviz

def display_architecture_diagram():
    # Create a directed graph
    graph = graphviz.Digraph()
    
    # Define common node styles
    action_style = {'style': 'filled', 'fillcolor': '#90EE90'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#87CEEB'}
    process_style = {'shape': 'box', 'style': 'filled', 'fillcolor': '#DDA0DD'}
    input_style = {'style': 'filled', 'fillcolor': '#FFA500'}
    
    # Add nodes - Input Section
    graph.node('Start Application', **action_style)
    graph.node('Upload DOCX Resume', **action_style)
    graph.node('Resume Uploaded?', **decision_style)
    graph.node('Convert DOCX to Text', **input_style)
    graph.node('Manual Text Input', **input_style)
    graph.node('Input Job Description', **input_style)
    graph.node('Input GROQ API Key', **input_style)
    
    # Add decision nodes
    graph.node('Choose Action', **decision_style)
    graph.node('Analysis Type', **decision_style)
    
    # Add process nodes with detailed descriptions
    graph.node('Quick Analysis', '''Quick Analysis Flow:
    - Skills Match Rating
    - Experience Alignment
    - Pros and Cons
    - Match Percentage''', **process_style)
    
    graph.node('In-Depth Analysis', '''In-Depth Analysis Flow:
    - Skill Gap Analysis
    - Experience Analysis
    - Optimization Tips
    - Strategic Recommendations''', **process_style)
    
    graph.node('Enhancement Process', '''Enhancement Process:
    - Run In-Depth Analysis
    - Generate Improvements
    - Format Content
    - Create Multiple Formats''', **process_style)
    
    # Add output nodes with formats
    graph.node('Display Results', '''Output Options:
    - Analysis Results
    - Recommendations
    - Action Items''', **process_style)
    
    graph.node('Enhanced Resume Outputs', '''Available Formats:
    - Plain Text
    - Formatted HTML
    - DOCX Download
    - Side-by-Side Comparison
    - Highlighted Changes''', **process_style)
    
    # Add edges - Basic Flow
    graph.edge('Start Application', 'Upload DOCX Resume')
    graph.edge('Upload DOCX Resume', 'Resume Uploaded?')
    graph.edge('Resume Uploaded?', 'Convert DOCX to Text', 'Yes')
    graph.edge('Resume Uploaded?', 'Manual Text Input', 'No')
    
    # Add edges - Input Processing
    graph.edge('Convert DOCX to Text', 'Input Job Description')
    graph.edge('Manual Text Input', 'Input Job Description')
    graph.edge('Input Job Description', 'Input GROQ API Key')
    graph.edge('Input GROQ API Key', 'Choose Action')
    
    # Add edges - Analysis Paths
    graph.edge('Choose Action', 'Analysis Type', 'Analyze')
    graph.edge('Choose Action', 'Enhancement Process', 'Enhance')
    graph.edge('Analysis Type', 'Quick Analysis', 'Quick')
    graph.edge('Analysis Type', 'In-Depth Analysis', 'In-Depth')
    
    # Add edges - Output Paths
    graph.edge('Quick Analysis', 'Display Results')
    graph.edge('In-Depth Analysis', 'Display Results')
    graph.edge('Enhancement Process', 'Enhanced Resume Outputs')
    
    # Add optional paths
    graph.edge('Display Results', 'Choose Action', 'Start New Analysis')
    graph.edge('Enhanced Resume Outputs', 'Choose Action', 'Start New Analysis')
    
    # Configure graph attributes
    graph.attr(rankdir='TB')
    graph.attr(splines='ortho')
    graph.attr(nodesep='0.5')
    graph.attr(ranksep='0.5')
    
    return graph