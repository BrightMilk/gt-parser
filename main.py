import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

def findAllTopicsOnPage(soup):
    content = soup.find('div', class_='forum').find('td', class_='mainbg').find('table', class_='main6').findAll('h2',
                                                                                                                 class_='web')

    topicnames = []

    for topic in content:
        topicname = topic.find('a').text

        if len(topicname) != 0 and topicname != "COMPARISONS INDEX":
            topicnames.append(topicname)

    return topicnames

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Cookie": "cat=991970; resolution=1536x864; cf_clearance=kNMZTM7eCA3KymBk50.05Ut_vcSQmRaot9nuowRvYW8-1691316652-0-1-c7d8df41.d999c03.90d980a1-160.0.0; login-from=https%253A%252F%252Fgranturismo.forumfree.it%252F%253Ft%253D79623509; session_id=81faf298888f61f2143762bc3f709af9; pop1=1"
}

page = requests.get(os.getenv('URL'), headers=headers)

soup = BeautifulSoup(page.content, 'html5lib')

names = findAllTopicsOnPage(soup)
