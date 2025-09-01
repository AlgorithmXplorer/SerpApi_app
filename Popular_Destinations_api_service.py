import json as js
import requests
import time


class Popular_Destinations_api:
    def __init__(self,params, destination_count):
        self.params:dict = params
        self.json:dict = None
        self.url:str = None
        self.datas:list[dict] = None
        self.destination_count:int = destination_count
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
            self.url = datas["url"] + f"api_key={datas['api_key']}&"
        str_params = [f"{key}={value}" for key , value in self.params.items()]
        self.url += "&".join(str_params)

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

            self.url = self.json["serpapi_pagination"]["next_link"] + f"&api_key={api_key}"
            self.data_taker(is_it_enough = False)
    
    def clear_data_maker(self) -> str:
        self.datas = self.datas[:self.destination_count]
        clear_data = []
        for data in self.datas:
            params = [f"{key} : {value}" for key , value in data.items()]
            params = "\n".join(params)
            clear_data.append(params)

        return f"\n\n{'-'*40}\n\n".join(clear_data)


    


