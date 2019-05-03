import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_pig(fact):
    """Converts text to pig latin
    param1: text to be converted
    returns: url for converted pig latin text
    """
    payload = {'input_text': fact}
    response = requests.post(
        'https://hidden-journey-62459.herokuapp.com/piglatinize/', data=payload).url
    return response


def get_fact():
    """Returns random fact from unkno.com"""
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact()
    return get_pig(fact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
