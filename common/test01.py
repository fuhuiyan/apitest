
# dict1 = {"a":1,"a1":"hh"}
#
#
# for i,j in dict1.items():
#     print(i,j)

import json

# data ='{"shopId":2512,"hqId":496,"name":"兰兰","gender":"1","phone":13588888888,"nfcCardNo":"","status":"1","idcard":"","income":"","industry":"","habit":"","educationBackground":"","levelId":1819,"birthDay":"2021-10-28","integralTime":"9999-12-31","email":"","address":"","remarks":"","isHq":false}'
#
#
#
# y = json.loads(data)
#
# s = json.dumps(y)
#
# print(type(s),s)

# case = '{"shopId":2512,"hqId":496,"name":"兰兰","gender":"1","phone":13588888888,"nfcCardNo":"","status":"1","idcard":"","income":"","industry":"","habit":"","educationBackground":"","levelId":1819,"birthDay":"2021-10-28","integralTime":"9999-12-31","email":"","address":"","remarks":"","isHq":false}'
# if 1==1:
#     # headers["accessToken"] = CaseData.accessToken
#     js = json.loads(case)
#     case = json.dumps(js)
#     # case = str(case)
#     print(type(case))

# data = eval(replace_data(case["data"]))
import requests
import json

url= "https://pos-sit.yingeo.com/api/es-server/shop/member/register"

headers = {"Content-Type": "application/json",
    "access-token":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNjg5IiwiaWF0IjoxNjM1NDcwMTI5LCJzdWIiOiJhbGwiLCJpc3MiOiJ3ZXRvb2wiLCJleHAiOjE2MzU0OTg5Mjl9.jDy5TzfEYsfYz3gowKWHuGq77BY8B-6dEzyiSwRGPY8"}

str1 = {"shopId":2512,"hqId":496,"name":"1","gender":"1","phone":222222,"nfcCardNo":"","status":"1","idcard":"","income":"","industry":"","habit":"","educationBackground":"","levelId":1819,"birthDay":"2021-10-29","integralTime":"9999-12-31","email":"","address":"","remarks":"","isHq":False}

# print(str1)

# str2 = json.loads(str1)
#
# data = json.dumps(str2)

# print(type(data), data)

res = requests.post(url=url, headers=headers, json=str1)

print(res.json())


import requests

# url = "https://pos-sit.yingeo.com/api/es-server/shop/member/register"
#
# payload="" \
#         "{\n    \"shopId\": 2512,\n    \"hqId\": 496,\n    \"name\": \"1\",\n    \"gender\": \"1\",\n    \"phone\": 222221,\n    \"nfcCardNo\": \"\",\n    \"status\": \"1\",\n    \"idcard\": \"\",\n    \"income\": \"\",\n    \"industry\": \"\",\n    \"habit\": \"\",\n    \"educationBackground\": \"\",\n    \"levelId\": 1819,\n    \"birthDay\": \"2021-10-29\",\n    \"integralTime\": \"9999-12-31\",\n    \"email\": \"\",\n    \"address\": \"\",\n    \"remarks\": \"\",\n    \"isHq\": false\n}"
# headers = {
#   'access-token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNjg5IiwiaWF0IjoxNjM1NDcwMTI5LCJzdWIiOiJhbGwiLCJpc3MiOiJ3ZXRvb2wiLCJleHAiOjE2MzU0OTg5Mjl9.jDy5TzfEYsfYz3gowKWHuGq77BY8B-6dEzyiSwRGPY8',
#   'Content-Type': 'application/json'
# }
# print(payload)
#
# # response = requests.post(url, headers=headers, data=payload)
# #
# # print(response.text)
