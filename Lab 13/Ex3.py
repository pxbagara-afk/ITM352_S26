#Create a simple Flask application to retrieve memes from a link.

from flask import Flask, render_template, request, redirect, url_for
import requests

url = "https://meme-api.com/gimme/wholesomememes"

app = Flask(__name__, template_folder='Template')

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('meme'))

@app.route('/meme', methods=['GET'])
def meme():
    response = requests.get(url)    # Make a GET request to the meme API
    data = response.json()
    meme_url = data['url']
    title = data['title']
    return render_template('meme.html', meme_url=meme_url, title=title)

if __name__ == '__main__':
    app.run(debug=True)