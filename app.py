from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/my_list.html")
def my_list():
    celeb1 ="Kristen Stewart"
    celeb2 = "Justin Bieber"
    celeb3 = "Zac Efron"
    celeb4 = "Britney Spears"
    celeb5 = "Blackpink"
    celeb6 = "BTS"
    response1 = requests.get("https://microservice-wiki-image-link.herokuapp.com/wiki_image/"+celeb1)
    response2 = requests.get("https://microservice-wiki-image-link.herokuapp.com/wiki_image/"+celeb2)
    response3 = requests.get("https://microservice-wiki-image-link.herokuapp.com/wiki_image/"+celeb3)
    response4 = requests.get("https://microservice-wiki-image-link.herokuapp.com/wiki_image/"+celeb4)
    response5 = requests.get("https://microservice-wiki-image-link.herokuapp.com/wiki_image/"+celeb5)
    response6 = requests.get("https://microservice-wiki-image-link.herokuapp.com/wiki_image/"+celeb6)

    return render_template('my_list.html',value1 =response1.text,value2=response2.text,value3=response3.text, value4=response4.text,value5=response5.text,value6=response6.text)

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/main.html")
def main():
    response = requests.get('https://microservice-news-app.herokuapp.com/cnn_entertainment')
    data = response.json()

    entry1_title = data['entries'][0]['title']
    entry1_summary = data['entries'][0]['summary']
    entry1_image = data['entries'][0]['media_content'][9]['url']
    entry1_published = data['entries'][0]['published']
    entry1_url = data['entries'][0]['id']

    entry2_title = data['entries'][2]['title']
    entry2_summary = data['entries'][2]['summary']
    entry2_image = data['entries'][2]['media_content'][9]['url']
    entry2_published = data['entries'][2]['published']
    entry2_url = data['entries'][2]['id']

    entry3_title = data['entries'][4]['title']
    entry3_summary = data['entries'][4]['summary']
    entry3_image = data['entries'][4]['media_content'][9]['url']
    entry3_published = data['entries'][4]['published']
    entry3_url = data['entries'][4]['id']
    return render_template('main.html',entry1_title=entry1_title,entry1_summary=entry1_summary,entry1_image=entry1_image,entry1_published = entry1_published,entry1_url=entry1_url,
                           entry2_title=entry2_title,entry2_summary=entry2_summary,entry2_image=entry2_image,entry2_published=entry2_published, entry2_url=entry2_url,
                           entry3_title=entry3_title,entry3_summary=entry3_summary,entry3_image=entry3_image,entry3_published=entry3_published, entry3_url=entry3_url)

@app.route("/privacy_policy.html")
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route("/faq.html")
def faq():
    return render_template('faq.html')



if __name__ == "__main__":
    app.run()