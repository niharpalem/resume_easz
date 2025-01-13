import graphviz
import streamlit as st

def display_architecture_diagram():
    # Create a directed graph
    graph = graphviz.Digraph(format='png')
    
    # Define node styles
    styles = {
        'start': {'shape': 'cylinder', 'style': 'filled', 'fillcolor': '#22c55e', 'fontcolor': 'white'},
        'input': {'shape': 'box', 'style': 'filled', 'fillcolor': '#f97316', 'fontcolor': 'white'},
        'decision': {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#0ea5e9', 'fontcolor': 'white'},
        'process': {'shape': 'box', 'style': 'filled', 'fillcolor': '#8b5cf6', 'fontcolor': 'white'},
        'output': {'shape': 'box', 'style': 'filled', 'fillcolor': '#ec4899', 'fontcolor': 'white'}
    }

    # Add nodes
    graph.node('Start', '🚀 Start\nApplication', **styles['start'])
    graph.node('Upload', '📄 Upload DOCX\nResume', **styles['input'])
    graph.node('JobDesc', '💼 Input Job\nDescription', **styles['input'])
    graph.node('ApiKey', '🔑 Input GROQ\nAPI Key', **styles['input'])
    graph.node('ChooseAction', '🔄 Choose\nAction', **styles['decision'])
    graph.node('AnalysisType', '📊 Analysis\nType', **styles['decision'])
    
    # Add process nodes with detailed content
    quick_analysis = """Quick Analysis
──────────────
• Skills Match Rating
• Experience Alignment
• Pros and Cons
• Match Percentage"""
    graph.node('QuickAnalysis', quick_analysis, **styles['process'])
    
    in_depth = """In-Depth Analysisc
──────────────
• Comprehensive Skill Gap
• Detailed Experience Review
• Career Path Alignment
• Strategic Recommendations"""
    graph.node('InDepthAnalysis', in_depth, **styles['process'])
    
    enhancement = """Resume Enhancement
──────────────
• In-Depth Analysis
• Format Optimization
• Content Improvement
• Design Enhancement"""
    graph.node('Enhancement', enhancement, **styles['process'])
    
    # Add output nodes
    results = """Analysis Results
──────────────
📊 Analysis Summary
📝 Recommendations
✅ Action Items"""
    graph.node('Results', results, **styles['output'])
    
    enhanced = """Enhanced Resume
──────────────
📑 Optimized DOCX
🖍️ Text Highlighting Changes
🌐 HTML Version"""
    graph.node('EnhancedOutputs', enhanced, **styles['output'])

    # Add edges
    graph.edge('Start', 'Upload')
    graph.edge('Upload', 'JobDesc')
    graph.edge('JobDesc', 'ApiKey')
    graph.edge('ApiKey', 'ChooseAction')
    graph.edge('ChooseAction', 'AnalysisType', 'Analyze')
    graph.edge('ChooseAction', 'Enhancement', 'Enhance')
    graph.edge('AnalysisType', 'QuickAnalysis', 'Quick')
    graph.edge('AnalysisType', 'InDepthAnalysis', 'In-Depth')
    graph.edge('QuickAnalysis', 'Results')
    graph.edge('InDepthAnalysis', 'Results')
    graph.edge('Enhancement', 'EnhancedOutputs')
    graph.edge('Results', 'ChooseAction', 'New Analysis')
    graph.edge('EnhancedOutputs', 'ChooseAction', 'New Analysis')

    # Graph settings
    graph.attr(rankdir='TB', splines='ortho')
    
    return graph
