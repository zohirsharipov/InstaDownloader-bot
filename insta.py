import requests
import json
def instadownLoader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
	              "X-RapidAPI-Key": "34ebf11671msh4cf28a67261df00p1fd5bbjsnb5798629ddea",
	              "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
              }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
      return "Ishlamaydi!"
    else:
        dict ={}
        if rest['Type'] == 'Post-Image':
          dict['type']='image'
          dict['media']=rest['media']
          return dict
        elif rest['Type'] == 'Post-Video':
          dict['type']='video'
          dict['media']=rest['media']
          return dict
        elif rest['Type'] == 'Carousel':
          dict['type']='carousel'
          dict['media']=rest['media']
          return dict
        else:
          return "Ishlamaydi!"
