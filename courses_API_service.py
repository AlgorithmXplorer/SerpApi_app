import json as js
import requests

class courses_api:

    def __init__(self,params):
        self.params:dict = params
        self.json = None
        self.url = None
        self.datas = None

    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
        
        str_params = "&".join([f"{key}={value}" for key,value in self.params.items()])
        self.url = datas["url"] + f"api_key={datas['api_key']}&"

        self.url += str_params
    #T ADET BİLGİSİ ALINACAK YİNE



