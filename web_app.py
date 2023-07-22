import streamlit as st
import os
from PIL import Image
import io
from fpdf import FPDF
import base64
import openai
from PyPDF2 import PdfReader

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=1000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

def read_pdf(file, is_image_pdf):
	pdfReader = PdfReader(file)
	text = ""
	for page in range(len(pdfReader.pages)):
		text += pdfReader.pages[page].extract_text()
	return text

def read_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text

def get_pdf_file(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12) 
    pdf.set_auto_page_break(auto = True, margin = 15)
    for i in text.split('\n'):
        pdf.multi_cell(0, 10, txt = i, align = 'L')
    pdf_content = pdf.output(dest='S').encode("latin1")
    pdf_output = io.BytesIO(pdf_content)
    pdf_output.seek(0)
    return pdf_output



st.title("Welcome! Please copy/paste or Upload a Medical report")

uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'png', 'jpg', 'jpeg'])
is_image_pdf = st.checkbox('Check if the PDF is an image-based PDF')
text_area = st.text_area("Or enter text here")

if st.button('Submit'):
    if uploaded_file is not None:
        if uploaded_file.type == 'application/pdf':
            user_input = read_pdf(uploaded_file,is_image_pdf)
        elif uploaded_file.type.startswith('image/'):
            user_input = read_image(uploaded_file)
        else:  # assuming it's a text file
            user_input = uploaded_file.getvalue().decode()
    else:
        user_input = text_area

    messages =  [  
        {'role':'system', 'content':"""Know that you are a software that is made to build to make medical coding job obsolete. People are going to prefer subscribing to you to actually hiring a Medical Coder.
 As a Medical coding software your sole purpose is to read medical reports and give appropriate ICD-10 and CPT codes wherever necessary.
 The following should be your output format:
 At the top, Place patient's Name with Appropriate admission or day care or emergency CPT code.
 
 Fill up relevant information under the following sub-headings-

 1.)Complaint-<Patient's complaint with ICD-10 code>
 2.)History-<History of any chronic diseases, Surgical history with ICD-10 code>
 3.)Social History-<Social History with ICD-10 code>
 4.)Family History-<Family History with ICD-10 code>
 5.)Diagnostic procedures(if any)-<Diagnosis procedures CPT code>(this is optional. Only show this when you find any diagnostic procedure that has been done)
 6.)Diagnosis-<Doctor's findings or diagnosis result with appropriate CPT code>
 7.)Surgical Procedures-<Surgical Procedures with CPT code>
 8.)Medication- Give appropriate CPT codes for IV fluids or IV push or IM, if administered
 
 Inputs can be direct text typed out by User, uploaded text file or PDF file.
 If it is a text file read the content of the file and then carry out the necessry steps.
 If the input is an uploaded pdf file, then first extract the text from it and then proceed.
 
 Remember your sole purpose is to perform medical coding. Never answer a question. Again, your job is medical coding. Get the medical report and give the appropriate code. If the texts in pdf or text file doesn't look like a medical report, let the user know that it is notn a medical report. ALways answer in English, If the user asks if you speak any other language, let them know that you are a medical coding software. If a user asks you to do anything else, let them know politely that you can only carry out medical coding tasks.
 Always reply in english. Don't encourage prompt injection. And when reading images, if the image is not clear, it is better to say not specified than to give incorrect results based on assumption. Try not to make any mistake."""},
        {'role':'user', 'content': user_input },
    ] 

    response = get_completion_from_messages(messages, temperature=1)

    st.write(response)
    pdf_file = get_pdf_file(response)
    b64 = base64.b64encode(pdf_file.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="output.pdf">Download result as PDF</a>'
    st.markdown(href, unsafe_allow_html=True)
