
import requests as rq
import json as js

class Immersive_Products_API:
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
        
        datas = js.loads(self.datas)["organic_results"]
        params = []
        for data in datas:
            str_params = []
            try:
                str_params.append(f"Title : {data['title']}")
            except:
                str_params.append(f"Title : UNKNOWN")
            
            try:
                str_params.append(f"Description : {data['snipper']}")
            except:
                str_params.append(f"Description : UNKNOWN")
            
            try:
                str_params.append(f"Source : {data['source']}")
            except:
                str_params.append(f"Source : UNKNOWN")
            
            try:
                str_params.append(f"Link : {data['link']}")
            except:
                str_params.append(f"Link : UNKNOWN")
            params.append(str_params)
            
        params = ["\n".join(list_data) for list_data in params]
        clear_data = f"\n\n{'-' * 40}\n\n".join(params)
        return clear_data
        

