
import requests as rq
import json as js


class Jobs_apı:
    def __init__(self,params:dict,job_count:int):
        self.params = params
        self.url = None
        self.json = None
        self.datas:list = None
        self.job_count = job_count

    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file: 
            url_datas = js.load(file)
        url = url_datas["url"]
        url += f"api_key={ url_datas['api_key'] }&" 
        str_params = [ f"{a}={i}" for a,i in self.params.items()]
        str_params = "&".join(str_params)
        self.url = url + str_params 

    def data_taker(self,next_page_token=None):
        if next_page_token == None:  
            datas = js.loads(rq.get(url=self.url).text)
            self.json = datas
            jobs = datas["jobs_results"]
            self.datas = jobs
        
        else:
            datas = js.loads(rq.get(url=self.url + f"&next_page_token={next_page_token}").text)
            self.json = datas
            jobs = datas["jobs_results"]
            return jobs
        
        
    def data_count_controller(self):
        if len(self.datas) < self.job_count:
        
            page_token = self.json["serpapi_pagination"]["next_page_token"]
            datas = self.data_taker(next_page_token=page_token)
        
            self.datas += datas
            self.datas = self.datas[:self.job_count]
        
    #t data taker ile veri aldıktan sonra alınan veri sayısı yeterli mi diye kontrol edicez
    #* self.datas eleman sayısının self.job_count'dan küçükü mü diye karşılaştırcağız 

    def clear_data_maker(self):
        pass
