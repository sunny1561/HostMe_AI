import os
import json
import streamlit as st
from dotenv import load_dotenv
from together import Together
from hostme_prompt import system_prompt, job_prompt, skill_prompt
import pdfplumber
import docx2txt
from io import BytesIO

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")
client = Together(api_key=api_key)

# Initialize Streamlit app
st.title("Resume/CV Parser and Job Fit Finder")
st.markdown("Upload your resume or CV to extract details and find suitable job roles.")

# File uploader for PDF or DOCX files
uploaded_file = st.file_uploader("Upload your Resume/CV (PDF or DOCX)", type=['pdf', 'docx'])

# Check if a file has been uploaded
if uploaded_file is not None:
    # To Display success message
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

def extract_cv_info(uploaded_file):
    if uploaded_file is None:
        return {"error": "No file uploaded."}

    file_name = uploaded_file.name
    if not (file_name.lower().endswith('.pdf') or file_name.lower().endswith('.docx')):  ## handling error if file is not either docx or pdf
        return {"error": "The provided file is not a PDF or DOCX. Please upload a valid file."}

    try:
        if file_name.lower().endswith('.pdf'):
            with pdfplumber.open(uploaded_file) as pdf:
                pages = pdf.pages
                extracted_text = ""
                for page in pages:
                    extracted_text += page.extract_text() + "\n"  # Extract text from each page
                print(extracted_text)
                return extracted_text if extracted_text else "No text found in the PDF."

        else:  # DOCX file
            extracted_text = docx2txt.process(uploaded_file)
            return extracted_text if extracted_text else "No text found in the DOCX."

    except Exception as e:
        return {"error": str(e)}

def Extract_Info(input_query, system):
    try:
        message = [
            {"role": "system", "content": system},
            {"role": "user", "content": input_query}
        ]
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            messages=message,
            max_tokens=512,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}

def get_all_relevant_details():
    extracted_content = extract_cv_info(uploaded_file)
    extract_relevent_details = Extract_Info(extracted_content, system_prompt)
    return extract_relevent_details

def get_suitable_role():
    extracted_content = extract_cv_info(uploaded_file)
    extract_relevent_details = Extract_Info(extracted_content, system_prompt)
    output = Extract_Info(extract_relevent_details, skill_prompt)
    suitable_role = Extract_Info(output, job_prompt)
    return suitable_role

# Creating buttons for extracting details and finding job fit
if st.button("Parse CV"):
    with st.spinner("Extracting details..."):
        details = get_all_relevant_details()
        st.write("### Candidate's CV Details")
        st.write(details)
        # Creating  a text file and provided a download link
        text_buffer = BytesIO()
        text_buffer.write(details.encode('utf-8'))  # Convert details to bytes
        text_buffer.seek(0)  # Move to the beginning of the BytesIO buffer

        st.download_button(
            label="Download CV Details as Text File",
            data=text_buffer,
            file_name="cv_details.txt",
            mime="text/plain"
        )

if st.button("Find Best Fit Job Role"):
    with st.spinner("Finding suitable job role..."):
        suitable_role = get_suitable_role()
        st.write("### Candidate's Suitable Job Role")
        st.write(suitable_role)





