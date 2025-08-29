from Immersive_Products import *
from Jobs_API import *
from file_funcs import *
from parameter_bringer import *
from News_api_service import *
from Popular_Destinations_api_service import *


# params = Immersive_Products_parameters(param_taker=param_taker , domain_setter= domain_setter)
# obje = Immersive_Products(parameters=params) 
# obje.url_maker()
# obje.data_taker()
# datas = obje.clear_data_maker()
# data_writer(datas=datas)

# params = Jobs_parameters(param_taker=param_taker,domain_setter=domain_setter)
# job_count = job_count(param_taker=param_taker)
# obje = Jobs_apı(params=params,job_count=job_count)
# obje.url_maker()
# obje.data_taker()
# obje.data_count_controller()
# datas = obje.clear_data_maker()
# data_writer(datas=datas)
# print(obje.job_count)

# params = News_parameters(param_taker=param_taker,domain_setter=domain_setter)
# obje = news_api(params=params)
# obje.url_maker()
# obje.data_taker()
# datas = obje.clear_data_maker()
# data_writer(datas=datas)
# print(obje.url)




params = Popular_Destinations_parameters(param_taker=param_taker,domain_setter=domain_setter)
obje = Popular_Destinations_api(params=params)
obje.url_maker()


print(obje.url)




