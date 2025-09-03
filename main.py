from file_funcs import *
from parameter_bringer import *

from Immersive_Products_api_service import *
from Jobs_API_service import *
from News_api_service import *
from Nutrition_Information_api_service import * 
from Popular_Destinations_api_service import *
from courses_API_service import *

class main:
    def __init__(self,param_taker_func , domain_setter_func , data_writter_func):
        self.param_taker_func = param_taker_func
        self.data_writter_func = data_writter_func
        self.domain_setter_func = domain_setter_func

    def panel(self):
        panel_questions = ""
        
        

    def Immersive_Products(self):
        params = Immersive_Products_param_taker(self.param_taker_func , self.domain_setter_func)
     
        obje = Immersive_Products_API(parameters=params)
        obje.url_maker()
        obje.data_taker()
     
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        self.panel
    
    
    def Jobs(self):
        params = Jobs_param_taker(self.param_taker_func , self.domain_setter_func)
        count_of_job = job_count(self.param_taker_func)
       
        obje = Jobs_apı(params=params,job_count=count_of_job)
        obje.url_maker()
        obje.data_taker()
        obje.data_count_controller()
       
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        self.panel
    
    
    def News(self):
        params = News_param_taker(self.param_taker_func , self.domain_setter_func)
        
        obje = news_api(params=params)
        obje.url_maker()
        obje.data_taker()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
                
        self.panel
    
    
    def Nutrition_Information(self):
        params = Nutrition_Information_param_taker(self.param_taker_func , self.domain_setter_func)
        
        obje = Nutrition_Information_api(params=params)
        obje.url_maker()
        obje.data_taker()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)     
        
        self.panel
    
    
    def Popular_Destinations(self):
        params = Popular_Destinations_parameters(self.param_taker_func , self.domain_setter_func)
        destination_count = count_Destination(param_taker=self.param_taker_func)
        
        obje = Popular_Destinations_api(params=params,destination_count=destination_count)
        obje.url_maker()
        obje.data_taker()
        obje.data_count()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        self.panel


    def Courses(self):
        params = Courses_param_taker(self.param_taker_func , self.domain_setter_func)
        count_of_course = course_count(param_taker=self.param_taker_func)
        
        obje = courses_api(params=params,course_count=count_of_course)
        obje.url_maker()
        obje.data_taker()
        obje.count_controller()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        
        self.panel

x = main(param_taker_func=param_taker , domain_setter_func= domain_setter , data_writter_func= data_writer)


