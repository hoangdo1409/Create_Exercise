from PIL import Image
from pix2tex.cli import LatexOCR
from jinja2 import Template
from dotenv import load_dotenv
import os, time
import openai
import os
from pdf2image import convert_from_path
import pytesseract

load_dotenv()
api_key = os.getenv('API_KEY')
max_tokens = os.getenv('MAX_TOKEN')

def generate_questions(question_sample: str, request: str, api_key=api_key, max_tokens=max_tokens):
    openai.api_key = (api_key)
    prompt = question_sample + '\n' + request

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    ) 
    return response.choices[0].text



def pdf_to_latex(pdf_path):
    images = convert_from_path(pdf_path, 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(temp_dir, f"page_{i+1}.png")
        image.save(image_path, "PNG")
        image_paths.append(image_path)

    text = ""
    for image_path in image_paths:
        text += pytesseract.image_to_string(image_path, lang="vie")

    for image_path in image_paths:
        os.remove(image_path)
    os.rmdir(temp_dir)

    latex_text = text.replace("&", "\&").replace("%", "\%")

    return latex_text

def save_to_txt(text: str, path_file: str) -> None:
    with open(path_file, 'w', encoding='utf-8', errors='ignore') as txt_file:
        txt_file.write(text)


def main():

    image_path = 'math.png'

    img = Image.open(image_path)

    model = LatexOCR()

    result = ""
    request = """
    Reformat the above formula to the standard form of latex mathematical formula
    """

    result = result + generate_questions(model(img), request)

    # pdf_path = "exam_math.pdf"

    # latex_code = pdf_to_latex(pdf_path)

    # result = latex_code

    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Hiển thị công thức toán học với MathJax</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js"></script>
    </head>
    <body>
    <p>Công thức toán học: {{result}}</p>
    </body>
    </html>

    ''' 

    # Tạo đối tượng Template từ template HTML
    template = Template(html_template)

    # Render template và chèn giá trị của result vào
    rendered_html = template.render(result=result)
    save_to_txt(result, 'data.txt')

    # Ghi kết quả vào file HTML
    with open('result.html', 'w', encoding='utf-8') as file:
        file.write(rendered_html)

    print("Đã tạo file result.html")

if __name__ == '__main__':
    main()


# Nhưng hiện tại thời hạn cũng sắp hết nên em nghĩ là mình không đủ thời gian để làm được tiếp nên em xin phép viết báo cáo để nộp thầy luôn ạ