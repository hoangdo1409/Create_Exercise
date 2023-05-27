import unittest
from unittest.mock import patch
from main import *

class YourModuleTestCase(unittest.TestCase):
    def test_convert_list_to_str(self):
        input_list = ['Hello', 'World']
        expected_output = 'HelloWorld'
        self.assertEqual(convert_list_to_str(input_list), expected_output)

    def test_save_to_txt(self):
        text = 'Hello, World!'
        path_file = 'output.txt'
        save_to_txt(text, path_file)
        
        with open(path_file, 'r') as file:
            content = file.read()
        self.assertEqual(content, text)

    def test_read_file_lines(self):
        file_path = 'data.txt'
        expected_output = ["""Câu 1: Chương trình khai thác thuộc địa lần thứ hai của thực dân Pháp đã dẫn tới sự xuất hiện của những giai cấp nào dưới đây? A. Nông dân, công nhân B. Tư sản, tiểu tư sản, công nhân C. Địa chủ, tư sản, tiểu tư sản D. Tư sản, tiểu tư sản\n""", 
                           """Câu 2: Ngày 1-10-1949, nước Cộng hòa Nhân dân Trung Hoa ra đời là kết quả của: A. quá trình đàm phán giữa Mĩ và Liên Xô B. quá trình đấu tranh giải phóng dân tộc C. cuộc nội chiến Quốc Cộng lần 2 (1946-1949) D. quá trình nổi dậy của nhân dân Trung Quốc\n""", 
                           """Câu 3: Đặc đểm nổi bật của phong trào dân tộc, dân chủ ở Việt Nam giai đoạn 1919 – 1930 là: A. cuộc đấu tranh giành quyền cai trị ở Việt Nam giữa thực dân Pháp và vương triều Nguyễn diễn ra mạnh mẽ, quyết liệt B. sự phát triển mạnh mẽ về kinh tế, chính trị, xã hội dẫn đến sự phát triển mạnh mẽ của phong trào đấu tranh theo khuynh hướng cách mạng vô sản ở Việt Nam C. cuộc đấu tranh giành quyền lãnh đạo giữa khuynh hướng cách mạng vô sản và khuynh hướng cách mạng dân chủ tư sản D. sự phát triển mạnh mẽ của phong trào tư sản, tiểu tư sản từng bước khẳng định vai trò lãnh đạo của họ\n"""]
        self.assertEqual(read_file_lines(file_path), expected_output)

    def test_generate_questions(self):
        question_sample = 'Câu 1: Chương trình khai thác thuộc địa lần thứ hai của thực dân Pháp đã dẫn tới sự xuất hiện của những giai cấp nào dưới đây?\nA. Nông dân, công nhân\nB. Tư sản, tiểu tư sản, công nhân\nC. Địa chủ, tư sản, tiểu tư sản\nD. Tư sản, tiểu tư sản\n'
        request = """Create a list of 5 questions and 4 answers with each question, each on the same topic as the questions above, of the form:
    Question: 
    A.  
    B. 
    C.  
    D. """
        response = generate_questions(question_sample, request, api_key, max_tokens)
        self.assertIsInstance(response, str)

    @patch('main.open')
    @patch('main.generate_questions')
    @patch('main.save_to_txt')
    @patch('main.read_file_lines')
    def test_main(self, mock_read_file_lines, mock_save_to_txt, mock_generate_questions, mock_open):
        mock_read_file_lines.return_value = [
            "Câu 1: Chương trình khai thác thuộc địa lần thứ hai của thực dân Pháp đã dẫn tới sự xuất hiện của những giai cấp nào dưới đây?\nA. Nông dân, công nhân\nB. Tư sản, tiểu tư sản, công nhân\nC. Địa chủ, tư sản, tiểu tư sản\nD. Tư sản, tiểu tư sản\n",
            "Câu 2: Ngày 1-10-1949, nước Cộng hòa Nhân dân Trung Hoa ra đời là kết quả của:\nA. quá trình đàm phán giữa Mĩ và Liên Xô\nB. quá trình đấu tranh giải phóng dân tộc\nC. cuộc nội chiến Quốc Cộng lần 2 (1946-1949)\nD. quá trình nổi dậy của nhân dân Trung Quốc\n"
        ]

        mock_generate_questions.return_value = "Generated questions"

        main()

        mock_read_file_lines.assert_called_once_with('question.txt')
        self.assertEqual(mock_generate_questions.call_count, 2)
        mock_save_to_txt.assert_called_once_with('Generated questionsGenerated questions', 'similar_question.txt')
        mock_open.assert_called_once_with('similar_question.txt', 'w')

if __name__ == '__main__':
    unittest.main()
