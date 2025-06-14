# main.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def fetch_nodes():
    url = "https://free-ss.site"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")

    # 抓取所有 ss:// 或 vmess:// 開頭的節點
    pattern = re.compile(r'(ss://[a-zA-Z0-9\-_:=@.]+|vmess://[a-zA-Z0-9+/=]+)')
    matches = pattern.findall(soup.text)

    # 去重
    matches = list(set(matches))

    # 儲存到檔案
    with open("nodes.txt", "w", encoding="utf-8") as f:
        f.write(f"# 自動更新時間：{datetime.utcnow()} UTC\n\n")
        for node in matches:
            f.write(node + "\n")

    print(f"共抓取 {len(matches)} 個節點。")

if __name__ == "__main__":
    fetch_nodes()
