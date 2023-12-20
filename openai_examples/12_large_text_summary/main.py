from PyPDF2 import PdfReader
from openai import OpenAI

client = OpenAI()

def generate_summary(text):
    """
    Generates a summary of the provided text using the OpenAI GPT-3.5 Turbo model.
    
    Args:
        text (str): Text to be summarized.

    Returns:
        str: Summary of the text.
    """
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant. Summarize the text provided.'},
            {'role': 'user', 'content': text}
        ],
        max_tokens=1024
    )
    summary = response.choices[0].message.content.strip()
    return summary

def split_text_into_chunks(text, chunk_size=4000):
    """
    Splits text into smaller chunks.

    Args:
        text (str): Text to be split.
        chunk_size (int, optional): Size of each chunk. Defaults to 4,000.

    Returns:
        list[str]: List of text chunks.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_large_content(content):
    """
    Generates a summary for large content.

    Args:
        content (str): Large content to be summarized.

    Returns:
        str: Summary of the large content.
    """
    chunks = split_text_into_chunks(content)
    # print(f'This document has {len(chunks)} chunk{"" if len(chunks) == 1 else "s"}.')
    chunk_summaries = [generate_summary(chunk) for chunk in chunks]
    combined_text = ' '.join(chunk_summaries)
    return generate_summary(combined_text)

def summarize_document(file_path, is_pdf=False):
    """
    Generates a summary of a text or PDF document.

    Args:
        file_path (str): Path to the document.
        is_pdf (bool, optional): Flag to indicate if the document is a PDF. Defaults to False.
    """
    if is_pdf:
        content = pdf_to_text(file_path)
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

    summary = summarize_large_content(content)
    print('Document Summary:\n', summary)

if __name__ == '__main__':
    summarize_document('./woodpecker.txt')
    print('*' * 120)
    summarize_document('./ants.pdf', is_pdf=True)
