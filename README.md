<br />
<div align="center">
  <h1 align="center">Create Exercise</h1>

  <p align="center">
    Dự án tạo các câu hỏi mới từ một câu hỏi mẫu  
   </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Mục lục</summary>
  <ol>
    <li>
      <a href="#about-the-project">Về Dự Án</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Bắt đầu</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About the project
Create Exercise là một dự án Python thực hiện trích xuất các câu hỏi từ một file đề thi và tạo ra các câu hỏi với nội dung gần với câu hỏi mẫu.
Chương trình đọc toàn bộ nội dung của file câu hỏi pdf và xử lý lại format câu hỏi rồi đưa vào file txt để lưu lại.
Sau đó, sử dụng thư viện openai và dựa trên ví dụ Parse unstructured data, đưa vào request lần lượt từng câu hỏi và đáp án để từ đó sẽ tạo ra lần lượt 5 câu hỏi cùng các đáp án có nội dung tương tự.

### Built With
Phần mềm được xây dựng bởi ngôn ngữ Python

## Getting Started
Để tạo và chạy một bản sao dự án, hãy làm theo các bước như sau.

### Prerequisites
Trước tiên, bạn cần có Python để có thể chạy được dự án. Phiên bản python hiện tại đang được dùng trong dự ấn này là 3.7.9
* Python
  * Bạn có thể tải về phiên bản 3.7.9 ở đây: [Python 3.7.9](https://www.python.org/downloads/release/python-379/)
  * Hoặc có thể tải phiên bản mới nhất của Python tại: [Newest Python](https://www.python.org/downloads/)

### Installation
Dự án này đang sử dụng thư viện Openai nên bạn cần có API Key xác thực được cấp bởi OpenAI
1. Clone repo
```sh
git clone https://github.com/hoangdo1409/Create_Exercise.git
```

2. Cần tải xuống các thư viện cần thiết được khai báo trong file requirement.txt với lệnh sau:
  ```sh
  	pip install -r requirement.txt
  ```
  
3. Đăng ký và lấy mã API Key tại đây:  [API Keys](https://platform.openai.com/account/api-keys/) 

4. Tạo 1 file .env với các giá trị:
```python
API_KEY="api_key"
MAX_TOKENS=1600
ENGINE="davinci"
PDF_PATH='exam_history.pdf'
```

<!-- USAGE EXAMPLES -->
## Usage
Dự án này trước tiên cần đọc dữ liệu câu hỏi từ 1 file pdf, vậy nên bạn cần thêm 1 file pdf muốn sử dụng làm cơ sở ddeer tạo thêm các câu hỏi khác vào dự án. Hiện tại, đang có 1 file mặc định là exam_history.pdf được đặt sẵn để có thể chạy thử nghiệm. Hoặc bạn có thể thêm 1 file pdf khác và thay đổi giá trị biến ```PDF_PATH``` trong file <i>.env</i>.

* Để đọc toàn bộ nội dung câu hỏi từ file pdf, chạy lệnh sau:
  ```sh
  py createTxt.py
  ```
  Toàn bộ nội dung của file pdf sẽ được đọc vào file <i> question.txt </i>.
  
* Sau đó, để tạo thêm các câu hỏi từ các câu hỏi có sẵn, ta thực hiện chạy hàm main với lệnh:
  ```sh
  py main.py
  ```
  Do việc tạo câu hỏi mất khá nhiều thời gian nên cần phải tách thành 2 lệnh chạy là để có thể kiển tra nội dung file đọc được từ pdf đã ổn hay không, nếu thất bại có thể thực hiện đọc lại mà chưa tạo câu hỏi.
  
* Kết quả sẽ được lưu trong file <i> similar_question.txt </i>

