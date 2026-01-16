import os
from fpdf import FPDF
from tkinter import Tk, filedialog
import docx2txt  # For .docx files
import PyPDF2    # For .pdf files

def read_file_content(file_path):
    """Read text from .txt, .pdf, or .docx files"""
    ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
                
        elif ext == '.pdf':
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                return text
                
        elif ext == '.docx':
            return docx2txt.process(file_path)
            
        else:
            raise ValueError(f"Unsupported file type: {ext}")
            
    except Exception as e:
        return f"Error reading file: {str(e)}"

def create_pdf(text, output_filename="output.pdf"):
    """Create a PDF from given text"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Handle multi-line text
    for line in text.split('\n'):
        pdf.cell(0, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)
    
    pdf.output(output_filename)
    print(f"PDF created: {os.path.abspath(output_filename)}")

def main():
    # Hide tkinter root window
    root = Tk()
    root.withdraw()
    
    # File selection dialog
    file_path = filedialog.askopenfilename(
        title="Select a document to upload",
        filetypes=[
            ("Text files", "*.txt"),
            ("PDF files", "*.pdf"),
            ("Word files", "*.docx"),
            ("All files", "*.*")
        ]
    )
    
    if not file_path:
        print("No file selected.")
        return
    
    print(f"Selected file: {file_path}")
    
    # Read content
    content = read_file_content(file_path)
    print("\nExtracted content:\n")
    print(content[:500] + "..." if len(content) > 500 else content)  # Preview
    
    # Create PDF from extracted content
    output_name = "converted_" + os.path.splitext(os.path.basename(file_path))[0] + ".pdf"
    create_pdf(content, output_name)

if __name__ == "__main__":
    main()