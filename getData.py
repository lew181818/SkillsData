import requests
from requests.auth import HTTPBasicAuth
import json, pprint
import shutil

path="/Users/kon9654/Documents/sei_data/resumes/"
start = 0
count = 100
while start < 300:
    print start
    resp = requests.get('https://sysev.jiveon.com/api/core/v3/places/19568/contents?count='+str(count)+'&startIndex='+str(start), \
        auth=HTTPBasicAuth('lmcdonald@sysev.com', 'Password01'))
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    item = resp.json()
    for r in item['list']:
        filename = r['subject']+"_"+r['name']
        print filename
        url = r['binaryURL']
        r = requests.get(url, auth=HTTPBasicAuth('lmcdonald@sysev.com', 'Password01'), stream=True)
        if r.status_code == 200:
            with open(path+filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        del r
    start = start + 100
    print(start)
