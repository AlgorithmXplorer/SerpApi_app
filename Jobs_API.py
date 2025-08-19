
import requests as rq
import json as js


class Jobs_apı:
    def __init__(self,params:dict):
        self.params = params
        self.url = None
        self.datas = None

    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file: 
            url_datas = js.load(file)
        url = url_datas["url"]
        url += f"api_key={ url_datas['api_key'] }&" 
        str_params = [ f"{a}={i}" for a,i in self.params.items()]
        str_params = "&".join(str_params)
        self.url = url + str_params 
    #t job api servisinde gelen veriler içerisinde diğer sayfa yani ekstra iş leri görebileceğimiz bir token veriliyor
    #t bu verilen token ile istenilen kadar iş alabiliriz
    #t bu iş sayısının öyğrenilmesini ise parametr_bringer dosyasında bir tane daha fonkisyona hazırlayarak yapıcaz

