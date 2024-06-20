import re
from pdfminer.high_level import extract_text

class PdfParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def extract_text(self):
        text = extract_text(self.filepath)
        return text

    @staticmethod
    def clean_text(text):
        text = re.sub(r"(\n+)", " ", text)  # Replace newlines with a space
        text = re.sub(r"[^\w\s/@]", '', text)  # Remove non-alphanumeric characters except space, slash, at
        text = re.sub(r"(\s){2,}", " ", text)  # Replace multiple spaces with a single space
        text = re.sub(r"[•\t▪➢❖\-\/]", '', text)  # Remove specific unwanted characters
        return text.strip()

# Example usage
parser = PdfParser("data/pdfs/Ch1.pdf")
raw_text = parser.extract_text()
cleaned_text = parser.clean_text(raw_text)
print(cleaned_text)
