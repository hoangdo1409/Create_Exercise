# Create_Exercise
Create Exercise là một chương trình Python thực hiện trích xuất các câu hỏi từ một đề thi và sử dụng thư viện openai tạo ra các câu hỏi với nội dung tương tự.
## Overview
Create Exercise có đầu vào là một file chứa các câu hỏi (pdf) và đầu ra là một file txt chứa các câu hỏi có nội dung tương tự.
Chương trình đọc toàn bộ nội dung của file câu hỏi pdf và xử lý lại format câu hỏi rồi đưa vào file txt để lưu lại.
Sau đó, sử dụng thư viện openai và dựa trên ví dụ Parse unstructured data, đưa vào request lần lượt từng câu hỏi và đáp án để từ đó sẽ tạo ra lần lượt 5 câu hỏi cùng các đáp án có nội dung tương tự.
* Các cài đặt được sử dụng trong API request:
```python
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.5,
  max_tokens=3000,
  top_p=1,
```
Giải thích:
```python
model="text-davinci-003"
```
* text-davinci-003 thuộc model GPT-3.5, nó giúp thực hiện yêu cầu với ngôn ngữ tự nhiên dễ dàng hơn, chất lượng tốt hơn, đầu ra có kích thước lớn hơn.
```python
prompt=prompt
```
* prompt: chứa nội dung là yêu cầu mà bạn muốn thực hiện
```python
  temperature=0.5
```
* temperature: kiểm soát tính ngẫu nhiên mà kết quả đưa ra. Với giá trị 0 thì kết quả tạo ra sẽ xác định và lặp đi lặp lại. Với nhiều lần kiểm tra thì ở đây đặt giá trị là 0.5 để với 1 câu hỏi có thể tạo ra nhiều câu hỏi khác có nội dung tương tự nhưng phong phú và có sự khác biệt lẫn nhau nhiều hơn.
```python
  max_tokens=3000
```
* max_tokens: chiều dài tối đa của các ký tự nhập vào bao gồm cả câu hỏi đưa vào, phần prompt và kết quả trả về. Số ký tự này bị giới hạn với các tài khoản (dùng free hay trả phí). Ở đây với 3000 ký tự nên cho phép đưa vào 1 câu hỏi có 4 đáp án, prompt và kết quả trả về là 5 câu hỏi, đáp án tương tự.
```python
  top_p=1
```
* Kiểm soát tính đa dạng, 1 là lấy tất cả các tùy chọn được xem xét.

* Sử dụng một vài đề thi trắc nghiệm để làm đầu vào, với mỗi một câu hỏi 4 đáp án sẽ được nạp lần lượt vào request và nhận lại 5 câu hỏi khác ban đầu nhưng mức độ kiến thức và nội dung câu hỏi vẫn sát với câu hỏi đưa vào.


