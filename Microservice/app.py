from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

nyt = feedparser.parse('https://rss.nytimes.com/services/xml/rss/nyt/World.xml')

cnn_e = feedparser.parse('http://rss.cnn.com/rss/edition_entertainment.rss')
cnn_t = feedparser.parse('http://rss.cnn.com/rss/edition.rss')

@app.route("/")
def main():
    return "<html><h1>Hi This is a microservice for CS361. You can access the latest news here</h1><ul><li><a href='./nytimes'>New York Times</a>" \
           "<li><a href='./cnn_top'>CNN Top News</a>" \
           "<li><a href='./cnn_entertainment'>CNN Entertainment</a></ul></html>"

@app.route("/nytimes")
def nytimes():
    return nyt

@app.route("/cnn_top")
def cnn_top():
    return cnn_t

@app.route("/cnn_entertainment")
def cnn_entertainment():
    return cnn_e

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    app.run(debug=True)