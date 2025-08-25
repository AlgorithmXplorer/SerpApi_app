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
    
    def data_taker(self):
        news_list:list[dict] = js.loads(requests.get(url=self.url).text)["news_results"]
        neccessary_params = []

        def param_taker(news:dict):
            news_params = {
                "News Title" : news["title"],
                "News Link" : news["link"]
            }
            try: 
                news_params.update({
                    "Source Name" : news["source"]["name"]
                })
            except:
                news_params.update({
                    "Source Name" : "UNKNOWN"
                })
            try: 
                news_params.update({
                    "Authors" : " - ".join(news["source"]["authors"])
                })
            except:
                news_params.update({
                    "Authors" : "UNKNOWN"
                })

            try: 
                news_params.update({
                    "Release Date" : news["date"].split(", ")[0]
                })
            except:
                news_params.update({
                    "Release Date" : "UNKNOWN"
                })
            return news_params

        for news in news_list:
            if "stories" in news.keys():
                for  inner_news in news["stories"]:
                    params = param_taker(inner_news)
                    neccessary_params.append(params)
            else:
                params = param_taker(news=news)
                neccessary_params.append(params)
        self.datas = neccessary_params

    #t alınacak olan parametreler
    #! NOTE:Çok nadir olsada bazıları birden fazla haber anlatıyor . bunlarıda "stories" key altında veriyor. ama çok nadir yani 94 tane içinde 4 tane falan var
    #* title
    #* link
    #* source["name"]
    #* source["authors"]
    #* date
    #* herbirinde title ve link kesin var
