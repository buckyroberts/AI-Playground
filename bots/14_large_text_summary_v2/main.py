import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_summary(text):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant. Summarize the text provided.'},
            {'role': 'user', 'content': f'{text}'}
        ],
        max_tokens=1_000,
    )
    summary = response.choices[0].message['content'].strip()
    print(summary)
    print('*' * 120)
    return summary


def split_text_into_chunks(text, chunk_size=32_000):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def main():
    with open('./ukraine.txt', 'r') as file:
        content = file.read()

    # Split the content into chunks
    chunks = split_text_into_chunks(content)

    # Generate summaries for each chunk
    chunk_summaries = [generate_summary(chunk) for chunk in chunks]

    # Combine chunk summaries and generate a final summary
    combined_text = ' '.join(chunk_summaries)
    final_summary = generate_summary(combined_text)
    print('Final Summary:\n', final_summary)


if __name__ == '__main__':
    main()
