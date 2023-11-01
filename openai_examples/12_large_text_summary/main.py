import os

import openai
from PyPDF2 import PdfReader

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_summary(text):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant. Summarize the text provided.'},
            {'role': 'user', 'content': text}
        ],
        max_tokens=1_000,
    )
    summary = response.choices[0].message['content'].strip()
    print(summary)
    print('-' * 120)
    return summary


def pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_texts = []

    for page in reader.pages:
        extracted_texts.append(page.extract_text())

    text = ' '.join(extracted_texts)  # join all the extracted text fragments with spaces in between
    text = text.replace('\n', ' ')  # replace all newline characters with spaces

    return text


def summarize_large_content(content):
    # Split the content into chunks
    chunks = split_text_into_chunks(content)

    # Generate summaries for each chunk
    chunk_summaries = [generate_summary(chunk) for chunk in chunks]

    # Combine chunk summaries and generate a final summary
    combined_text = ' '.join(chunk_summaries)

    return generate_summary(combined_text)


def split_text_into_chunks(text, chunk_size=32_000):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def summarize_txt_document(txt_path):
    with open(txt_path, 'r') as file:
        content = file.read()

    summary = summarize_large_content(content)
    print('Text Summary:\n', summary)


def summarize_pdf_document(pdf_path):
    content = pdf_to_text(pdf_path)
    summary = summarize_large_content(content)
    print('PDF Summary:\n', summary)


if __name__ == '__main__':
    summarize_txt_document('./woodpecker.txt')
    print('*' * 120)
    summarize_pdf_document('./ants.pdf')
