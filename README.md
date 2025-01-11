# AI-Powered Resume Analyzer and Enhancer

This application is an AI-powered tool that analyzes and enhances resumes based on job descriptions. It uses advanced language models to provide detailed insights and improvements for job seekers.

## Features

- Resume upload (DOCX format)
- Job description input
- Quick and in-depth resume analysis
- Resume enhancement
- Output in multiple formats (DOCX, HTML)

## Architecture

The application follows this high-level flow:

1. Start Application
2. Upload DOCX Resume
3. Input Job Description
4. Input GROQ API Key
5. Choose Action (Analyze or Enhance)
6. If Analyze:
   - Choose Analysis Type (Quick or In-Depth)
   - Perform Analysis
   - Display Results
7. If Enhance:
   - Perform In-Depth Analysis
   - Enhance Resume
   - Generate Enhanced Outputs

## Key Components

- **Streamlit**: For the web interface
- **python-docx**: To process DOCX files
- **GROQ API**: For accessing AI models
- **LLaMA 3 70B**: Large language model for analysis and enhancement
- **Graphviz**: For generating the architecture diagram

## Setup and Installation

1. Clone the repository
2. Install required packages: `pip install - r requirements.txt`
3. Set up a GROQ API account and obtain an API key from here (https://console.groq.com/keys?_gl=1*1ozbol6*_gcl_au*MTc1ODk5MDQ0Mi4xNzM2NTgwNTgx*_ga*NDM2OTA5NjI1LjE3MzY1ODA1ODA.*_ga_4TD0X2GEZG*MTczNjU4MDU4MC4xLjAuMTczNjU4MDU4MC42MC4wLjA.)

## Usage

1. Run the Streamlit app: `streamlit run app.py`
2. Upload your resume (DOCX format)
3. Enter the job description
4. Provide your GROQ API key
5. Choose to analyze or enhance your resume
6. View the results or download the enhanced resume

## Modules

- `app.py`: Main Streamlit application
- `prompts.py`: Prompts for handling resume parsing and formatting
- `flowhchart.py`: Flow chart vizualization

## Dependencies

- Streamlit
- python-docx
- groq
- graphviz
- docx2txt

## Note

Ensure you have a valid GROQ API key and sufficient credits for using the LLaMA 3 70B model. The application's performance depends on the quality and availability of the AI model.
