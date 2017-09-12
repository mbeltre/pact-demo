import json

from flask import Flask, request

from memes import ALL_MEMES


app = Flask(__name__)

def find_meme(meme_id):
    try:
        return next(m for m in ALL_MEMES if m['id'] == meme_id)
    except StopIteration:
        return None

@app.route('/meme/<id>')
def get_meme(id):
    meme_id = int(id)
    meme = find_meme(meme_id)
    if meme:
        return json.dumps(meme)
    else:
        return json.dumps({'error': f'Meme with id {meme_id} not found.'}), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)