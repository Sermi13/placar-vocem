from flask import Flask, render_template, request
import re
import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def get_soup():
    url = unquote(request.args.get("link"))

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.text, 'html.parser')
    div = soup.find('div', class_=re.compile('table-classification--group'))
    rendered_html = render_template('index.html', soup=div)
    return rendered_html


# if __name__ == '__main__':
    # app.run(debug=True, port=8080)
