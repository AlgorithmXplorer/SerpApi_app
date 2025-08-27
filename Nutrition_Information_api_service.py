
import json as js
import requests

class Nutrition_Information_api:
    def __init__(self,params):
        self.params:dict = params
        self.url = None
        self.datas = None
        self.json = None
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
            self.url = datas["url"] + f"api_key={datas['api_key']}&"
        str_params = [f"{key}={value}" for key,value in self.params.items()]
        join_params = "&".join(str_params)
        self.url += join_params

    def datas_taker(self):
        self.json = js.loads(requests.get(self.url).text)
        try:
            self.datas = self.json["nutrition_information"]
        except KeyError:
            self.datas = None

    def clear_data_maker(self):
        def tryer_func(will_search:str):
            pass
    #t yazılacak parametreler
    #* description
    #* calories
    #* amount_per
    #* source
    #* source_link
    #* protein
    #* total_fat
    #* total_carbohydrate
