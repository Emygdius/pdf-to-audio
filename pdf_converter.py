import PyPDF2
import pyttsx3
import os

def pdf_to_audio(pdf_path, output_audio_path):
    """
    Reads a PDF file and converts its text to an audio file (MP3).
    """
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file {pdf_path} was not found.")
        return

    # Initialize the PDF reader
    try:
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Initialize the speaker
        speaker = pyttsx3.init()
        
        # Adjust speed (optional)
        speaker.setProperty('rate', 150) 

        full_text = ""
        
        print(f"Reading {len(pdf_reader.pages)} pages...")

        # Extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                full_text += text
        
        # Clean up text (remove extra newlines)
        clean_text = full_text.replace('\n', ' ')

        # Save to audio file
        print(f"Converting to audio... Saving to {output_audio_path}")
        speaker.save_to_file(clean_text, output_audio_path)
        speaker.runAndWait()
        
        print("Success! Audio file created.")
        pdf_file.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Create a dummy PDF for testing if one doesn't exist
    if not os.path.exists("sample.pdf"):
        from reportlab.pdfgen import canvas
        c = canvas.Canvas("sample.pdf")
        c.drawString(100, 750, "Hello Adams! This is your PDF to Audio converter working successfully.")
        c.save()
        print("Created sample.pdf for testing.")

    # Run the converter
    pdf_to_audio("sample.pdf", "audiobook.mp3")
