import json as js
import requests



class Popular_Destinations_api:
    def __init__(self,params:dict):
        self.params = params
        self.json = None
        self.url = None
        self.datas = None
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
            self.url = datas["url"] + f"api_key={datas['api_key']}&"
        str_params = [f"{key}={value}" for key , value in self.params.items()]
        self.url += "&".join(str_params)

    #t iş api servisinde olduğu gibi burdada birden fazla sayfa linki var.
    #! ayrıca bu iki servise yeterli sayıda veri gelmezse elde olanları çıktı edip alta mesaj yaz
    #! mesela: anca bu kadar veri çıktı


    


