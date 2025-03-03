import requests

def get_redirect_url(short_url):
    response = requests.get(short_url, allow_redirects=True)
    return response.url

short_url = "http://xhslink.com/a/jm9e1rxVTdz5"
real_url = get_redirect_url(short_url)
print("真实URL:", real_url)

from bs4 import BeautifulSoup
import json
import re


def get_note_content(real_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(real_url, headers=headers)
    print(response.content)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找包含笔记数据的脚本
    script_tag = soup.find("script", text=re.compile(r'window\.__INITIAL_STATE__'))
    if script_tag:
        script_text = script_tag.string
        json_str = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', script_text).group(1)
        data = json.loads(json_str)
        return data
    return None


note_data = get_note_content(real_url)
print(note_data)