from dotenv import load_dotenv
import os, time
import math
import re
import pandas as pd
import docx
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

PDF_PATH= os.getenv('PDF_PATH')


def read_pdf(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as in_file:
        res_mgr = PDFResourceManager()
        device = TextConverter(res_mgr, output_string, codec='utf-8')
        interpreter = PDFPageInterpreter(res_mgr, device)

        for page in PDFPage.get_pages(in_file, check_extractable=True):
            interpreter.process_page(page)
        text = output_string.getvalue()

    return text

def read_docx(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def get_question_options(text: str, pattern):
    # pattern = r"(Câu \d+:.+?)(?=(Câu \d+:)|$)"
    matches = re.findall(pattern, text, re.DOTALL)

    list_quest_op = []

    for match in matches:
        questions_options = match[0].strip()
        list_quest_op.append(questions_options)
    return list_quest_op

def print_to_txt(text, path_file) -> None:
    with open(path_file, 'w', encoding='utf-8', errors='ignore') as txt_file:
        txt_file.write(text)

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    max_tokens = os.getenv('MAX_TOKENS')
    pdf_path = PDF_PATH
    txt_path = 'question.txt'
    # doc_path = 'document.docx'

    # pattern_pdf = r"(Câu \d+\..+?)(?=(Câu \d+.)|$)"
    pattern_pdf = r"(Câu \d+:.+?)(?=(Câu \d+:)|$)"


    path = pdf_path
    if path.endswith(".pdf"):
        content_extract = read_pdf(path)
    elif path.endswith(".docx") or path.endswith(".doc"):
        content_extract = read_docx(path)

    quest_option = get_question_options(content_extract, pattern_pdf)

    str_formated = ""
    for j in range(0, len(quest_option)):
        try:

            str_formated += quest_option[j] + "\n"
        except:
            time.sleep(3)
            j -= 1      
            continue

    print_to_txt((str_formated), txt_path)

    