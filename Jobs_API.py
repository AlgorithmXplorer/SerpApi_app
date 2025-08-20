
import requests as rq
import json as js


class Jobs_apı:
    def __init__(self,params:dict,job_count:int):
        self.params = params
        self.url = None
        self.datas = None
        self.job_count = job_count

    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file: 
            url_datas = js.load(file)
        url = url_datas["url"]
        url += f"api_key={ url_datas['api_key'] }&" 
        str_params = [ f"{a}={i}" for a,i in self.params.items()]
        str_params = "&".join(str_params)
        self.url = url + str_params 
    def data_taker(self):
        pass
    def data_count_controller(self):
        pass
    #t data taker ile veri aldıktan sonra alınan veri sayısı yeterli mi diye kontrol edicez
    #* self.datas eleman sayısının self.job_count'dan küçükü mü diye karşılaştırcağız 