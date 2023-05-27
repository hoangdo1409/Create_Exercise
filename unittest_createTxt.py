import unittest
from createTxt import *

class TestFunctions(unittest.TestCase):
    def test_read_pdf(self):
        pdf_path = 'data.pdf'  # Đường dẫn tới file PDF
        expected_text = "Sample text"  # Kết quả dự kiến sau khi đọc file PDF
        
        result = read_pdf(pdf_path)
        
        self.assertEqual(result, expected_text)
    
    
    def test_get_question_options(self):
        text = "Câu 1: Option 1\nCâu 2: Option 2"  # Văn bản đầu vào
        pattern = r"(Câu \d+:.+?)(?=(Câu \d+:)|$)"  # Pattern để tìm câu hỏi và tùy chọn
        
        expected_options = ["Câu 1: Option 1", "Câu 2: Option 2"]  # Kết quả dự kiến
        
        result = get_question_options(text, pattern)
        
        self.assertEqual(result, expected_options)

if __name__ == '__main__':
    unittest.main()
