from asyncore import write
from bs4 import BeautifulSoup
import requests,time

def get_info(url):
    cookies = {
        'TinyMCE_toggle': 'id',
        '_ga': '',
        '_gid': '',
        '_gcl_au': '',
        'MoodleSession': '273q8v7pnotiuopeuaesep7u4a',
    }
    
    headers = {
        'authority': 'fdrcr',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.6',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    response = requests.get(url, cookies=cookies, headers=headers).content
    user = BeautifulSoup(response, "html.parser")
    for foo in user.find_all("div", class_="userprofile"):
        content = foo.find_all('li', class_='contentnode')
        if "TOWN" in content[1].text:
            nome = foo.find('h2').text.replace('  ',' ')
            email = content[0].find('dd').text
            print(f"{nome}:{email}")
            with open('emails_alunos.txt','a') as fp:
                fp.write(f"{nome}:{email}\n")

with open("index.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp)

i = 0
for a in soup.find_all('a', href=True):
    print(a['href'])
    get_info(a['href'])

    print(i)
    i += 1


