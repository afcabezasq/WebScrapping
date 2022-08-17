from unittest import result
from bs4 import BeautifulSoup
import requests

# with open('index.html', 'r') as file:
#    doc = BeautifulSoup(file, 'html.parser')

#print(doc.prettify())

# tag = doc.title

#print(tag)
#tag.string = 'hello'
#print(tag.string)
#print(doc)

# p_tags = doc.find_all('p')
# p_tag_list = [element.string for element in p_tags]

# print(p_tag_list)


# url = 'https://www.newegg.com/Yeston-GeForce-GTX-1050-Ti-GTX1050Ti-4G/p/27N-0042-00041?cm_sp=SH-_-946256-_-8-_-1-_-9SIAZUEEV65926-_-gpu-_-gpu-_-1&Item=9SIAZUEEV65926'
# result = requests.get(url)

# document = BeautifulSoup(result.text,'html.parser')

# prices = document.find_all(text="$")

# parent = prices[0].parent

# strong_tag = parent.find('strong')

# print(strong_tag.string)

#print(document)

url = "https://coinmarketcap.com/"
result = requests.get(url).text

document = BeautifulSoup(result, 'html.parser')

table_content = document.tbody

table_rows = table_content.contents

print(list(table_rows[0].descendants)[2])

print(table_rows)
prices = {}
for row  in table_rows:
    try:
        name, price = row.contents[2], row.contents[3]
        print(name.p,price.p)
        asset_name = name.p.string
        asset_price = price.a.string
        
        prices[asset_name] = asset_price
    except:
        pass
    
print(prices)
    
