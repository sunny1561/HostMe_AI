
 # Project OverView (There is No Regex or String search or Key Word Search used here only agents used  powered by LLM)
 
#  a. CV Parsing & Data Extraction    (Kindly See the Demo Screenshot in the Repository to see the working of Web Application)
# HostMe_AI extracts and organizes essential details from resumes, which include:

# 1. Personal Information
First Name \
Last Name \
Email Address \
Phone Number

# 2. Education History
All educational qualifications listed in the CV

# 3. Work Experience Summary
Details of all professional experiences, including internships (if any)

# 4. Skills
Lists all skills mentioned in the resume



# 5. Years of Experience
Calculates the total years of professional experience by summing up the durations of each work experience

# b. Job Role Matching
The tool utilizes the parsed details to recommend three best-fit roles based on: 

Skills \
Current Position \
Working Experience 
# The tool also suggests closely aligned roles for candidates, enhancing the job search experience with targeted recommendations.

# Deployment Platform: The application is deployed on the free version of Render.
# API Service: Using the Together API (free version), which supports up to 60 requests per minute—currently sufficient for our usage.
# Access the  Application  through below link
https://hostme-ai-1.onrender.com/

# for testing you can use  the pdf and docx file here in drive 

https://drive.google.com/drive/folders/1wKYh6K3YHLiayT5EW9cZdDb3vBnoFeXR?usp=sharing


# Recommended to use Visual Studio Code
# Just Clone using 
!git clone  https://github.com/sunny1561/HostMe_AI.git

# SetUp  and How to Run the Streamlit in your system
API_KEY="Your Together AI API" (I HAVE PUT IT INTO .env file) (place into .env file and load using os.getenv(API_KEY))

# Install all required Package and Library using 
pip install -r requirements.txt  

# Run application using 
streamlit run hostme.py

 # 5. All used Prompts are in Hostme_prompt.py

# limitations and assumptions of the current implementation
1.File Type: Only PDF or DOCX files are supported for upload. \
2 .Together AI API Limit: Using the Together AI free version API (60 requests per minute, $7 credit free). Sufficient for now, but scaling may require a paid version. \
3. Required Information: The PDF or DOCX must include all necessary details to parse; missing information will be marked as Unavailable. \
4. File Size: Parsing long documents (1-2+ pages) may take longer. LLaMA 3.1-70B’s 128k context window handles large inputs, but excessive information may affect accuracy. \
5. Deployment Limits: Deployed on the free version of Render, which may have limitations affecting performance .


# Future Improvements.
 1.Expanded File Support: Add support for other file types, such as text and CSV files,.rtf. \
2. Integration with Ollama: Use Ollama for models like LLaMA 3.1, GEMMA, and NEMOTRON without requiring an API key, simplifying access to open-source models. \
3. Chunking Strategy: Implement a chunking strategy via LangChain to handle and process larger files more efficiently. \
4. Upgraded Deployment: Consider a paid version of Render or Vercel to reduce latency and enhance speed for a smoother user experience.









