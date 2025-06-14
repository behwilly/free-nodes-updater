# main.py
import requests
from bs4 import BeautifulSoup
import base64

try:
    url = 'https://free-ss.site'
    resp = requests.get(url, timeout=15)
    soup = BeautifulSoup(resp.text, 'html.parser')

    raw_nodes = []
    for link in soup.find_all('a'):
        href = link.get('href', '')
        if any(href.startswith(proto) for proto in ['vmess://', 'ss://', 'trojan://']):
            raw_nodes.append(href.strip())

    # 輸出 nodes.txt
    with open('nodes.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(raw_nodes))

    # 輸出 base64.txt
    all_nodes_text = '\n'.join(raw_nodes)
    encoded = base64.b64encode(all_nodes_text.encode('utf-8')).decode('utf-8')

    with open('base64.txt', 'w', encoding='utf-8') as f:
        f.write(encoded)

    print(f"✅ 抓取完成，共 {len(raw_nodes)} 個節點")

except Exception as e:
    print(f"❌ 發生錯誤：{e}")
