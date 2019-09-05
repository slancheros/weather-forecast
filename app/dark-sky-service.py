import requests
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/darksky/<location>/<units>')
def get_darksky(location,units):
    resp = requests.get('https://api.darksky.net/forecast/cb34ba299e9b2a3cb4d291e03d4f52d3/37.8267,-122.4233')
    if resp.status_code != 200:
        return "error"
    else:
        return str(resp.json())

@app.route('/info_dark_sky')
def get_info_dark_sky():

    resp = requests.get('https://localhost:80/darksky')
    if resp.status_code != 200:
        return "error"
    else:
        user = resp.json()['publicId']
        name = resp.json()['name']
        photo = resp.json()['picture']
        headline = resp.json()['professionalHeadline']
        return render_template('index.html', user=user, name=name, photo=photo, headline = headline)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)


