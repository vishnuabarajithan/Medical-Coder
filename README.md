# Medical Coding Software Documentation

The program uses **prompt engineering** to automate medical coding tasks using OpenAI's GPT-3.5-turbo model. It generates appropriate ICD-10 and CPT codes based on the information provided in medical reports.

## Prerequisites

Before using the Medical Coding Software, ensure that you have the following prerequisites installed:

- Python 3.x
- Streamlit
- Pillow (PIL)
- PyPDF2
- OpenAI Python API
- ReportLab

Install the required packages using the following command:

```bash
pip install streamlit pillow PyPDF2 openai reportlab
```

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vishnuabarajithan/medical-coding-software.git
   cd medical-coding-software
   ```

2. **Set OpenAI API Key:**
   Set your OpenAI API key as an environment variable.
   ```bash
   export OPENAI_API_KEY=your-api-key
   ```

3. **Run the Application:**
   ```bash
   streamlit run medical_coding_app.py
   ```

4. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8501`. You should see the Medical Coding Software interface.

## Usage Instructions

1. **Input Options:**
   - **Upload a File:** Use the file uploader to select a text file (`.txt`), a PDF file (`.pdf`), or an image file (`.png`, `.jpg`, `.jpeg`) containing the medical report.
   - **Text Area:** Manually enter the medical report text in the provided text area.

2. **Configuration:**
   - **PDF Type:** If your PDF is an image-based PDF, check the "Check if the PDF is an image-based PDF" checkbox.

3. **Submit:**
   - Click the "Submit" button to process the input and generate the medical coding output.

4. **Output Format:**
   - The output will be structured with the patient's name and appropriate admission or day care or emergency CPT code at the top.
   - Relevant information will be filled under specific sub-headings.

5. **Download Result:**
   - After processing, click the "Download result as PDF" link to download the result as a PDF file.

## Important Guidelines

- The software will only perform medical coding tasks and respond in English.
- It will not answer questions or perform other tasks.
- If the input does not resemble a medical report, the software will notify the user.
- Clear communication is maintained, and prompt injection is discouraged.

## Support and Issues

If you encounter any issues or have questions, feel free to [create an issue](https://github.com/vishnuabarajithan/medical-coding-software/issues) on the repository. We appreciate your feedback and contributions.

Thank you for using the Medical Coding Software!
