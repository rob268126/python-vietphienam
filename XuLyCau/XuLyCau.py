import re

class XuLyCau:
    """Tách câu thành danh sách các từ, loại bỏ dấu câu"""
    @staticmethod
    def tach_tu(text):
        # Regex xóa các ký tự đặc biệt (.,!?;:"...), giữ lại chữ cái và số
        text_clean = re.sub(r'[^\w\s]', '', text)
        # Tách từ bằng khoảng trắng
        return [word.lower() for word in text_clean.split()]