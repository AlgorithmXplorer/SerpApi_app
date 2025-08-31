import json as js
import requests
import time


class Popular_Destinations_api:
    def __init__(self,params, destination_count):
        self.params:int = params
        self.json:dict = None
        self.url:str = None
        self.datas:list = None
        self.destination_count:int = destination_count
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
            self.url = datas["url"] + f"api_key={datas['api_key']}&"
        str_params = [f"{key}={value}" for key , value in self.params.items()]
        self.url += "&".join(str_params)

    #t iş api servisinde olduğu gibi burdada birden fazla sayfa linki var.
    #! ayrıca bu iki servise yeterli sayıda veri gelmezse elde olanları çıktı edip alta mesaj yaz
    #! mesela: anca bu kadar veri çıktı

    def data_taker(self,is_it_enough = True):
            def organic():
                datas = self.json["organic_results"]
                params = []
                for data in datas:
                     params.append(
                          {
                              "Title" : data["title"],
                              "Description" : data["snippet"],
                              "Price" : "UNKNOWN",
                              "Link" : data["link"]                               
                          }
                     )
                return params

            def top_sights():
                datas = self.json["top_sights"]["sights"]
                params = []
                for data in datas:
                    params.append(
                         {
                              "Title" : data["title"],
                              "Description" : data["description"],
                              "Price" : data["price"],
                              "Link" : "UNKNOWN"
                         }   
                    )
                return params
            
            self.json = js.loads(requests.get(url=self.url).text)

            if is_it_enough :
                if "top_sights" in self.json.keys():
                    datas = top_sights()
                    self.datas = datas
                else:
                    datas = organic()
                    self.datas = datas
            else:
                if "top_sights" in self.json.keys():
                    datas = top_sights()
                    self.datas += datas
                else:
                    datas = organic()
                    self.datas += datas
                

    def data_count(self):
        while not (len(self.datas) > self.destination_count):
            with open("api_key/api.json","r+",encoding="utf-8") as file:
                api_key = js.load(file)["api_key"]

            if len(self.datas) < self.destination_count:
                self.url = self.json["serpapi_pagination"]["next_link"] + f"&api_key={api_key}"
                for data in self.datas:
                    print(data,end="\n\n\n")
                self.data_taker(is_it_enough = False)
            else:
                break
            


    


