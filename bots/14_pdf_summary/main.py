from PyPDF2 import PdfReader


def pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_texts = []

    for page in reader.pages:
        extracted_texts.append(page.extract_text())

    text = ' '.join(extracted_texts)  # join all the extracted text fragments with spaces in between
    text = text.replace('\n', ' ')  # replace all newline characters with spaces

    return text


def run():
    pdf_path = './ants.pdf'
    output_text = pdf_to_text(pdf_path)
    print(output_text)


if __name__ == '__main__':
    run()
