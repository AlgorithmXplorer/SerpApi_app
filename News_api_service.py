import requests
import json as js

class news_api:
    def __init__(self,params:dict):
        self.params = params
        self.url:str = None
        self.datas = None
        self.json = None

    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
            self.url =  datas["url"] + f"api_key={datas['api_key']}&"
        str_params = [f"{key}={value}"for key,value  in self.params.items()]
        str_params = "&".join(str_params)

        self.url += str_params

