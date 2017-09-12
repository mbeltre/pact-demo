import random

from flask import Flask, render_template

from memes_service_client import MemesServiceClient


app = Flask(__name__)

client = MemesServiceClient('http://localhost:5000/')

@app.route('/index')
def index():
    meme_id = random.randint(0, 2)
    meme = client.get_meme(meme_id)
    return render_template('index.html', meme_url=meme['url'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=5001)