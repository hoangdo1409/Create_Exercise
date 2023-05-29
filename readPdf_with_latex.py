from PIL import Image
from pix2tex.cli import LatexOCR
from jinja2 import Template
from dotenv import load_dotenv
import os, time
import openai

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


def main():

    # Đường dẫn tới file ảnh
    image_path = 'math.png'

    # Mở ảnh
    img = Image.open(image_path)

    # Khởi tạo model LatexOCR
    model = LatexOCR()

    # Nhận dạng công thức toán học từ ảnh
    result = ""
    request = """
    Reformat the above formula to the standard form of latex mathematical formula
    """

    result = result + generate_questions(model(img), request)

    # Template HTML
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

    # Ghi kết quả vào file HTML
    with open('result.html', 'w', encoding='utf-8') as file:
        file.write(rendered_html)

    print("Đã tạo file result.html")

if __name__ == '__main__':
    main()


# Nhưng hiện tại thời hạn cũng sắp hết nên em nghĩ là mình không đủ thời gian để làm được tiếp nên em xin phép viết báo cáo để nộp thầy luôn ạ