import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_summary(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'Summarize the following into a single paragraph:\n{text}',
        max_tokens=250,
    )
    print(response.choices[0].text.strip())
    print()
    return response.choices[0].text.strip()


def split_text_into_chunks(text, chunk_size=10_000):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def main():
    with open('./bill.txt', 'r') as file:
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
