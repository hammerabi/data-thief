import requests
import json
import os

rekt = requests.get('http://yourendpoint.com', auth=('user', 'password')).json()
#All the datas
i = 0
for prepay in rekt:
    payload = dict()
    #assign key, value to temp dict
    for key, value in prepay.iteritems():
        payload['video_id'] = prepay['video_id']
        payload['name'] = prepay['name']
        payload['email'] = prepay['email']
        payload['video_name'] = prepay['video_name']
        payload['phone'] = prepay['phone']
        payload['institution'] = prepay['institution']
        payload['categoryId'] = prepay['categoryId']
        payload['city'] = prepay['city']
        payload['provinceId'] = prepay['provinceId']
        payload['age'] = prepay['age']
        payload['language'] = prepay['language']
    #Post each payload here
    files = {'file': ('blah.m4v', open('blah.m4v', 'rb'))}
    r = requests.post("http://yourotherendpoint.com", files=files, auth=('admin','password'), data=payload)
    print str(r.status_code) + ": for video " + str(i)
    i = i + 1
