import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

input_file_path = 'Input.xlsx'
input_data = pd.read_excel(input_file_path)

def extract_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1').get_text()

    article = soup.find_all('p')
    article_text = '\n'.join([para.get_text() for para in article])

    return title, article_text

output_dir = 'articles extracted'
os.makedirs(output_dir, exist_ok=True)

for index, row in input_data.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    try:
        title, text = extract_article(url)
        file_path = os.path.join(output_dir, f'{url_id}.txt')

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n{text}")

        print(f"Successfully extracted the articles: {url_id}")

    except Exception as e:
        print(f"Failed to extract {url_id}: {e}")

print("articles extraction complete.")
