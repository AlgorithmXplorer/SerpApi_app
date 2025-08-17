
import requests as rq
from parameter_bringer import Immersive_Products_parameters
import json as js

class Immersive_Products:
    def __init__(self,parameters):
        self.params = parameters
        self.url = None
        self.datas = None
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)

        str_params = [f"{name}={param}" for name,param in self.params.items()]
        self.url = datas["url"] + f"api_key={datas['api_key']}&" + "&".join(str_params)  


    def data_taker(self):
        request = rq.get(url=self.url)
        datas = js.loads(request.text)
        self.datas = js.dumps(datas,indent=4)

    def clear_data_maker(self):
        clear_versions = []
        for product in js.loads(self.datas)["immersive_products"]:
            str_infos = product["title"] + "\n"
            try:
                str_infos = str_infos + f"PRİCE: {product['price']}" + "\n"
            except KeyError:
                str_infos = str_infos + f"PRİCE: UNKNOW"+ "\n"
            try:
                str_infos = str_infos + f"RATİNG: {product['rating']}" + "\n"
            except KeyError:
                str_infos = str_infos + f"RATİNG: UNKNOW"+ "\n"
            str_infos = str_infos + f"SOURCE: {product['source']}"
            clear_versions.append(str_infos)
        return clear_versions

        

params = Immersive_Products_parameters()
product = Immersive_Products(parameters=params)
product.url_maker()
product.data_taker()
product.clear_data_maker()


