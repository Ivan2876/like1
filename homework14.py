import requests
import json

url = 'https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf'
save_path = 'need_document.pdf'
response = requests.get(url)
content = response.content


with open(save_path, mode='wb') as image_file:
     image_file.write(content)

url_2 = 'http://api.open-notify.org/astros.json'
params = {
    "skip": 0,
    "limit": 1000,
}
response = requests.get(url=url_2 ,params=params)
response_json = response.json()

save_path_2 = 'need_file.json'
with open(save_path_2, mode='w', encoding='utf-8') as file:
     json.dump(response_json, fp=file,ensure_ascii=False, indent=4)



