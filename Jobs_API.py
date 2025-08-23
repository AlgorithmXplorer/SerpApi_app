
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
        print(self.url)

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
        
    
    def clear_data_maker(self):
        params = []
        for job in self.datas:
            Necessary_paramas = {
                "job title":job["title"],
                "job company_name" : job["company_name"],
                "job location": job["location"],
                "job extensions" : "  //  ".join(job["extensions"]),
                }
            try:
                Necessary_paramas.update({"job salary" : job["detected_extensions"]["salary"]})
            except KeyError:
                Necessary_paramas.update({"job salary" : "UNKNOWN"})
                pass
            
            try:
            
                Necessary_paramas.update({"job shedule type" : job["detected_extensions"]["schedule_type"]})
            except KeyError:
                Necessary_paramas.update({"job shedule type" : "UNKNOWN"})
                pass
            
            try:
                items = ["\n-" + item for item in job["job_highlights"][0]["items"]]
                Necessary_paramas.update({"job Qualifications items" : "".join(items)})
            except KeyError:
                Necessary_paramas.update({"job Qualifications items" : "UNKNOWN"})
                
            try:
                clear_link = []
                links = job["apply_options"]

                for link in links:
                    clear_link.append(f"\n-{link['title']} :  {link['link']}")
                
                Necessary_paramas.update({"job posting urls" : "".join(clear_link)})
            except KeyError:
                Necessary_paramas.update({"job urls" : "UNKNOWN"})
            

            params.append(Necessary_paramas)
        
        clear_data = []
        for job in params:
            temp = [f"{key} : {value}"for key,value in job.items()] 
            clear_data.append("\n\n".join(temp))
            
        return f"\n\n\n{'-' * 40}\n\n\n".join(clear_data)
    
    #t data_taker ve job count funcs ile alınan verileri clear_data_maker ile düzgün hale getiricez
    #t yazılcak iş parametreleri
    #* title
    #*location
    #*company_name
    #*extensions
    #* detected_extensions[salary - schedule_type ]
    #* description


