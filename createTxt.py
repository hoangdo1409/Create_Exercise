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

def get_question_options(text: str, pattern):
    matches = re.findall(pattern, text, re.DOTALL)

    list_quest_op = []

    for match in matches:
        questions_options = match[0].strip()
        list_quest_op.append(questions_options)
    return list_quest_op

def print_to_txt(text, path_file) -> None:
    with open(path_file, 'w', encoding='utf-8', errors='ignore') as txt_file:
        txt_file.write(text)

def main():
    load_dotenv()
    pdf_path = 'exam_hh.pdf'
    txt_path = 'question.txt'

    # pattern_pdf = r"(Câu \d+..+?)(?=(Câu \d+.)|$)"
    pattern_pdf = r"(Câu \d+:.+?)(?=(Câu \d+:)|$)"

    if pdf_path.endswith(".pdf"):
        content_extract = read_pdf(pdf_path)

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

if __name__ == '__main__':
    main()