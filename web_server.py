from flask import Flask, render_template
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
url = 'https://www.futebolinterior.com.br/campeonato/paulista-a4-2024/'


@app.route('/')
def get_soup():
    url = 'https://www.futebolinterior.com.br/campeonato/campeonato-paulista-2a-divisao-2023/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.text, 'html.parser')
    div = soup.find('div', class_=re.compile('table-classification--group'))
    rendered_html = render_template('index.html', soup=div)
    return rendered_html


# if __name__ == '__main__':
#     app.run(debug=False, host="0.0.0.0",port=8080)
