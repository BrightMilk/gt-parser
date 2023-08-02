import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.0.2199 Yowser/2.5 Safari/537.36"
}

page = requests.get(os.getenv('URL'), headers=headers)

soup = BeautifulSoup(page.content, 'html5lib')

content = soup.find('table', class_='main6').find('td', class_='right')

images = content.findAll('img')

print(images)
