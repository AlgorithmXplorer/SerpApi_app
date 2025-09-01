import json as js
import requests

class courses_api:

    def __init__(self,params,course_count):
        self.params:dict = params
        self.json:dict = None
        self.url:str = None
        self.datas:list[dict] = None
        self.course_count:int = course_count 

    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
        
        str_params = "&".join([f"{key}={value}" for key,value in self.params.items()])
        self.url = datas["url"] + f"api_key={datas['api_key']}&"

        self.url += str_params
    
    def data_taker(self,extra_data=False):
        self.json = js.loads(requests.get(url=self.url).text)
        def inner(json_data):
            datas = json_data["organic_results"]
            params = []
            for data in datas:
                params.append(
                    {
                        "Title": data["title"],
                        "Description": data["snippet"],
                        "Source": data["source"],
                        "Link": data["link"],
                    }
                )
            return params

        if not extra_data:
            params = inner(self.json)
            self.datas = params
        else:
            params = inner(self.json)
            self.datas += params
        
    def count_controller(self):
        while len(self.datas) < self.course_count:
            with open("api_key/api.json","r+",encoding="utf-8") as file:
                api_key = f"&api_key={js.load(file)['api_key']}"

            self.url = self.json["serpapi_pagination"]["next_link"] + api_key
            self.data_taker(extra_data=True)
    
    def clear_data_maker(self) -> str:
        self.datas = self.datas[:self.course_count]
        clear_data = []
        for data in self.datas:
            params = [f"{key} : {value}" for key , value in data.items()]
            params = "\n".join(params)
            clear_data.append(params)
        return  f"\n\n{'-'*40}\n\n".join(clear_data)



