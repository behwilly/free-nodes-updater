# main.py
import requests
from bs4 import BeautifulSoup
import base64

# ========= 抓取節點（以 free-ss.site 為例） =========

url = 'https://free-ss.site'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# 節點內容以 vmess://, ss://, trojan:// 開頭
raw_nodes = []
for link in soup.find_all('a'):
    href = link.get('href', '')
    if any(href.startswith(proto) for proto in ['vmess://', 'ss://', 'trojan://']):
        raw_nodes.append(href.strip())

# ========= 輸出 nodes.txt =========

with open('nodes.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(raw_nodes))

# ========= 輸出 base64.txt =========

all_nodes_text = '\n'.join(raw_nodes)
encoded = base64.b64encode(all_nodes_text.encode('utf-8')).decode('utf-8')

with open('base64.txt', 'w', encoding='utf-8') as f:
    f.write(encoded)
