import unittest
from unittest.mock import patch
from main import main

class YourModuleTestCase(unittest.TestCase):
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
