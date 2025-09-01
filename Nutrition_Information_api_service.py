
import json as js
import requests

class Nutrition_Information_api:
    def __init__(self,params):
        self.params:dict = params
        self.url:str = None
        self.datas:list[dict] = None
        self.json:dict = None
    
    def url_maker(self):
        with open("api_key/api.json","r+",encoding="utf-8") as file:
            datas = js.load(file)
            self.url = datas["url"] + f"api_key={datas['api_key']}&"
        str_params = [f"{key}={value}" for key,value in self.params.items()]
        join_params = "&".join(str_params)
        self.url += join_params

    def datas_taker(self):
        self.json = js.loads(requests.get(self.url).text)
        try:
            self.datas = self.json["nutrition_information"]
        except KeyError:
            self.datas = None

    def clear_data_maker(self):
        clear_data = []
        
        def tryer_func(will_search:str):
            try:    
                data = self.datas[will_search]
                if type(data) == list:
                    return f"{will_search.capitalize()} : {' , '.join(data)}"
                else:
                    return f"{will_search.capitalize()} : {data}"
            except:
                return f"{will_search.capitalize()} : UNKNOWN"

        descp = tryer_func("description")
        clear_data.append(descp)

        calories = tryer_func("calories")
        clear_data.append(calories)

        amount_per = tryer_func("amount_per")
        clear_data.append(amount_per)

        source = tryer_func("source")
        clear_data.append(source)

        source_link = tryer_func("source_link")
        clear_data.append(source_link)

        protein = tryer_func("protein")
        clear_data.append(protein)

        total_fat = tryer_func("total_fat")
        clear_data.append(total_fat)

        total_carbohydrate = tryer_func("total_carbohydrate")
        clear_data.append(total_carbohydrate)

        return f"\n\n{'-'*40}\n\n".join(clear_data)

