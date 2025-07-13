from docx import Document

def extract_text(docx_path):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            full_text.append(text)
    return "\n".join(full_text)

# Test the function
if __name__ == "__main__":
    path = r"C:\Users\DELL\OneDrive\Desktop\Resume.docx"
    text = extract_text(path)
    print(text)