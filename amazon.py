from bs4 import BeautifulSoup 
import requests

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

url = "https://www.amazon.com/deal/8b009a43?showVariations=true&pf_rd_r=9H6NGP74DKN530Y0QAFQ&pf_rd_p=4854a263-9793-4a61-a077-e933fd65736e&pd_rd_r=fe413489-83c6-4974-9b46-b4b37e7da5bc&pd_rd_w=3U1PU&pd_rd_wg=RkfcF&ref_=pd_gw_unk"
result = requests.get(url, headers=HEADERS).text
doc = BeautifulSoup(result)
print(doc)