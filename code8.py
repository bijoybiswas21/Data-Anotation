import os
from fpdf import FPDF
from tkinter import Tk, filedialog
import docx2txt
import PyPDF2
from gtts import gTTS
from playsound import playsound
import tempfile

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
    for line in text.split('\n'):
        # Handle encoding for FPDF (latin-1 only)
        clean_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(0, 10, txt=clean_line, ln=True)
    pdf.output(output_filename)
    print(f"📄 PDF created: {os.path.abspath(output_filename)}")

def speak_text(text):
    """Convert text to speech and play it using gTTS + playsound"""
    if not text.strip():
        print("⚠️ No text to speak.")
        return

    print("\n🔊 Reading document aloud...\n")
    
    # Limit to 5000 characters (gTTS free limit)
    text_to_speak = text[:5000]
    
    try:
        tts = gTTS(text=text_to_speak, lang='en', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            temp_file = tmp.name
        tts.save(temp_file)
        playsound(temp_file)
        os.unlink(temp_file)  # Delete temp file after playing
    except Exception as e:
        print(f"❌ Speech error: {e}")

def main():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a document to upload and read aloud",
        filetypes=[
            ("Text files", "*.txt"),
            ("PDF files", "*.pdf"),
            ("Word files", "*.docx"),
            ("All files", "*.*")
        ]
    )

    if not file_path:
        print("❌ No file selected.")
        return

    print(f"📁 Selected file: {file_path}")
    content = read_file_content(file_path)

    if content.startswith("Error"):
        print(content)
        return

    # Preview content
    preview = content[:500] + "..." if len(content) > 500 else content
    print("\n📝 Extracted content:\n")
    print(preview)

    # 🔊 Speak the content
    speak_text(content)

    # 📄 Save as PDF
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_name = f"converted_{base_name}.pdf"
    create_pdf(content, output_name)

if __name__ == "__main__":
    main()