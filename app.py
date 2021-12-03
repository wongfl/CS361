from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/my_list.html")
def my_list():
    """
    This function calls the microservice to get the wiki images and then renders the celebrity list template.
    """
    celeb1 ="Kristen Stewart"
    celeb2 = "Justin Bieber"
    celeb3 = "Machine_Gun_Kelly_(musician)"
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
    """
    This function calls the microservice to get the latest and trending news and render the home template.
    Also gets the news from the followed celebrities.
    """
    response = requests.get('https://microservice-news-app.herokuapp.com/cnn_entertainment')
    data = response.json()
    # latest news
    latest1_summary = data['entries'][3]['title']
    latest1_image = data['entries'][3]['media_content'][8]['url']
    latest1_url = data['entries'][3]['id']

    latest2_summary = data['entries'][5]['title']
    latest2_image = data['entries'][5]['media_content'][9]['url']
    latest2_url = data['entries'][5]['id']

    latest3_summary = data['entries'][6]['title']
    latest3_image = data['entries'][6]['media_content'][9]['url']
    latest3_url = data['entries'][6]['id']

    # trending news
    trending1_summary = data['entries'][7]['title']
    trending1_image = data['entries'][7]['media_content'][9]['url']
    trending1_url = data['entries'][7]['id']

    trending2_summary = data['entries'][8]['title']
    trending2_image = data['entries'][8]['media_content'][9]['url']
    trending2_url = data['entries'][8]['id']

    trending3_summary = data['entries'][9]['title']
    trending3_image = data['entries'][9]['media_content'][9]['url']
    trending3_url = data['entries'][9]['id']

    response = requests.get('https://microservice-news-app.herokuapp.com/e_entertainment')
    data_e = response.json()

    celeb1 ='Machine'
    for i in range(len(data_e['entries'])):
        title = data_e['entries'][i]['title']
        if celeb1 in title:
            news_pos1= i

    celeb2 = 'Britney'
    for i in range(len(data_e['entries'])):
        title = data_e['entries'][i]['title']
        if celeb2 in title:
            news_pos2= i

    entry1_title = data_e['entries'][news_pos1]['title']
    entry1_published = data_e['entries'][news_pos1]['published']
    entry1_url = data_e['entries'][news_pos1]['link']

    entry2_title = data_e['entries'][news_pos2]['title']
    entry2_published = data_e['entries'][news_pos2]['published']
    entry2_url = data_e['entries'][news_pos2]['link']


    return render_template('home.html',latest1_summary=latest1_summary,latest1_image=latest1_image,latest1_url=latest1_url,
                           latest2_summary=latest2_summary,latest2_image=latest2_image, latest2_url=latest2_url,
                           latest3_summary=latest3_summary,latest3_image=latest3_image, latest3_url=latest3_url,
                           trending1_summary=trending1_summary, trending1_image=trending1_image, trending1_url=trending1_url,
                           trending2_summary=trending2_summary, trending2_image=trending2_image, trending_url=trending2_url,
                           trending3_summary=trending3_summary, trending3_image=trending3_image, trending3_url=trending3_url,
                           entry1_title=entry1_title,entry1_published=entry1_published,entry1_url=entry1_url,entry2_title=entry2_title,
                           entry2_published=entry2_published,entry2_url=entry2_url, celeb1 = celeb1, celeb2=celeb2)

@app.route("/main.html")
def main():
    """
    This function calls the microservice to get the hot news and renders the main page.
    """
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
    """
    This function returns the privacy_policy page.
    """
    return render_template('privacy_policy.html')

@app.route("/faq.html")
def faq():
    """
    This function returns the faq page.
    """
    return render_template('faq.html')

if __name__ == "__main__":
    app.run()