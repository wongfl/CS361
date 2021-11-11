import requests

response =requests.get('https://microservice-news-app.herokuapp.com/cnn_entertainment')
data = response.json()
entry1 = data['entries'][0]
entry1_title = data['entries'][0]['title']
entry1_summary = data['entries'][0]['summary']
entry1_image = data['entries'][0]['media_content'][9]['url']
entry1_published = data['entries'][0]['published']
entry1_url = data['entries'][0]['id']
print(entry1)
print(entry1_title)
print(entry1_summary)
print(entry1_image)
print(entry1_published)
print(entry1_url)

data = response.json()
entry2 = data['entries'][2]
entry2_title = data['entries'][2]['title']
entry2_summary = data['entries'][2]['summary']
entry2_image = data['entries'][2]['media_content'][9]['url']
entry2_published = data['entries'][2]['published']
print('-----------------------------------------')
print(entry2)
print(entry2_title)
print(entry2_summary)
print(entry2_image)
print(entry2_published)