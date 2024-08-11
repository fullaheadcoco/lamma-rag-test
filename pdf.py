import fitz  # PyMuPDF
import pickle
import os

def extract_text_from_pdf(pdf_path):
    """PDF 파일에서 텍스트 추출"""
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    pdf_name = os.path.basename(pdf_path)
    with open(f'{pdf_name}.pkl','wb') as f:
        pickle.dump(text, f)
    return text