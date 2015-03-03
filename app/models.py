from app import app
from flask import render_template
import requests
import json
from datetime import datetime


class Weather(object):

    # def comicsList(self, comics_list):
    #     creators_list_url = app.config['CREATORS_COMICS_URL']
    #     creators_list = requests.get(str(creators_list_url), auth=(app.config['CREATORS_COMICS_USERNAME'], app.config['CREATORS_COMICS_PASSWORD']))
    #     self.creators_list_data = json.loads(creators_list.content)
    #     for cnt in range(0, len(self.creators_list_data)):
    #         strip_id = self.creators_list_data[cnt]['file_code']
    #         comics_list[strip_id] = self.creators_list_data[cnt]['title']
    #     universal_list_url = app.config['UNIVERSAL_COMICS_URL'] + 'features.json'
    #     universal_list = requests.get(str(universal_list_url), auth=(app.config['UNIVERSAL_COMICS_USERNAME'], app.config['UNIVERSAL_COMICS_PASSWORD']))
    #     self.universal_list_data = json.loads(universal_list.content).get("features")
    #     for cnt in range(0, len(self.universal_list_data)):
    #         strip_json_name = self.universal_list_data[cnt]['feature_url'].rsplit('/',1)[1]
    #         strip_id = strip_json_name.rsplit('.',1)[0]
    #         comics_list[strip_id] =  self.universal_list_data[cnt]['name']
    #     kings_list_url = app.config['KINGS_COMICS_URL'] + "config.json"
    #     kings_list = requests.get(str(kings_list_url))
    #     if kings_list.status_code == 200:
    #         self.kings_list_data = json.loads(kings_list.content)
    #         for cnt in range(0, len(self.kings_list_data['KING-COMICS'])):
    #             strip_id = self.kings_list_data['KING-COMICS'][cnt]['id']
    #             comics_list[strip_id] = self.kings_list_data['KING-COMICS'][cnt]['title']
    #     return sorted(comics_list.items(), key=lambda v: v[::-1])

    # @classmethod
    # def featuredList(self):
    #     self.uclick_list = {}
    #     featured_list_url = app.config['FEATURED_COMICS_URL'] + "config.json"
    #     featured_list = requests.get(str(featured_list_url))
    #     featured_list_data = json.loads(featured_list.content)
    #     uclick_date_url = datetime.strftime(datetime.now(), "%Y") + "/" + datetime.strftime(datetime.now(), "%m") + "/" + datetime.strftime(datetime.now(), "%d")
    #     # pull image from uclick
    #     for cnt in range(0, len(featured_list_data['FEATURED-COMICS'])):
    #         strip_id = featured_list_data['FEATURED-COMICS'][cnt]['id']
    #         uclick_url = app.config['UNIVERSAL_COMICS_URL']  + "feature/" + strip_id + "/" + uclick_date_url + ".json"
    #         response = requests.get(str(uclick_url), auth=(app.config['UNIVERSAL_COMICS_USERNAME'], app.config['UNIVERSAL_COMICS_PASSWORD']))
    #         uclick_data = json.loads(response.content)
    #         try:
    #             cid = strip_id 
    #             name = uclick_data['feature']['name']
    #             img_url = uclick_data['feature']['feature_items'][0]['assets'][0]['image_link']
    #             img_date = datetime.strptime(uclick_data['feature']['feature_items'][0]['date'][:-6], '%Y-%m-%dT%H:%M:%S').strftime('%B %d, %Y')
    #             self.uclick_list[cnt] = {'id': cid, 'name': name, 'img_url': img_url, 'img_date': img_date}
    #         except IndexError:
    #             pass
    #     return
