import json
import urllib.error
import urllib.parse
import urllib.request
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "daple.settings")
import django
django.setup()
import requests
from stores.models import Store

Store.objects.all().delete()

#
# for i in range(1,46):
#     searching = '스타벅스'
#     num = i
#     url = 'https://dapi.kakao.com/v2/local/search/keyword.json?page={}&query={}'.format(i,searching)
#     headers = {
#         "Authorization": "KakaoAK 0f23477b2b3262f820c688ff81fdf916"
#     }
#     print(url)
#     places = requests.get(url, headers=headers).json()
#     places = places['documents']
#     for i in range(len(places)):
#         db_save = Store(store_name=places[i]["place_name"], store_address=places[i]["address_name"], store_x=places[i]["x"],
#                         store_y=places[i]["y"],kakao_id=places[i]["id"])
#         db_save.save()

# client_id = "uCCiykUMH5IF4JADGgWL"
# client_secret = "mD53NEgVgg"
# encText = urllib.parse.quote("우동")
# url = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=10&start=1&sort=random"  # JSON 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id", client_id)
# request.add_header("X-Naver-Client-Secret", client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if rescode == 200:
#     response_body = response.read()
#     response_body = response_body.decode('utf-8')
#     response_body = json.loads(response_body)
#     temp = response_body["items"]
#     print(temp)
