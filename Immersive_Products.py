
import requests as rq
from parameter_bringer import Immersive_Products_parameters
import json as js

class Immersive_Products:
    def __init__(self,parameters):
        self.params = parameters
        self.url = None
        self.Datas = None
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)

        str_params = [f"{name}={param}" for name,param in self.params.items()]
        self.url = datas["url"] + f"api_key={datas['api_key']}&" + "&".join(str_params)  

params = Immersive_Products_parameters()
product = Immersive_Products(parameters=params)
product.url_maker()


