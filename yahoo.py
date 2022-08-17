import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

def web_content_div(web_content):   
    
    try:
        #web_content_div = web_content.find_all("div")
        f_stramers = web_content.find_all('fin-streamer')
        streamers_list = [element.get_text() for element in f_stramers]
        
    except IndexError:
        streamers_list = []
    
    return streamers_list
        



def real_time_price(stock_code):
    HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    url = f'https://finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=fin-srch'
    
    try:
        result = requests.get(url,headers=HEADERS).text
        web_content = BeautifulSoup(result,'html.parser')
        texts = web_content_div(web_content)
        
        if texts != []:
            price, change = texts[0:2]
        else:
            price, change = [], []
    except ConnectionError:
        price, change =[],[]
    
    return price, change

Stock = ['BKR-B']
print(real_time_price(Stock[0]))