import os
import requests
import json

DOWNLOAD_PATH = "http://pmwqkhyrx.bkt.clouddn.com/"
TEMPLET_PATH = "mould/templet1/material/"

def delete_oldmaterial():
    data = [{'name':'1.jpg'}]
    for i in data:
        if i['name'] in os.listdir(TEMPLET_PATH):
            os.remove(TEMPLET_PATH + i['name'])
            print("删除旧文件:",i['name'])
            return True

def download_newmaterial(data):
    print('传入的模板素材文件:',data)
    for i in data:
        r = requests.get(DOWNLOAD_PATH + i['key'], timeout=5)
        with open(TEMPLET_PATH + i['name'],'wb') as f:
            f.write(r.content)
            print('成功下载:',i['key'])

def upload_templetjson(data):
    print('传入的模板文字数据:',data)
    for i in data:
        fb = open(TEMPLET_PATH + 'variable.json', 'r', encoding='gbk')
        dicts = json.load(fb)
        fb.close()

        print('未更新之前的json:',dicts)

        key = i.keys()
        key = list(key)
        if 'title' in key:
            dicts["title"] = i["title"]

        if 'title2' in key:
            dicts["title2"] = i["title2"]

        fb = open(TEMPLET_PATH + 'variable.json','w', encoding='gbk')
        fb.write(json.dumps(dicts,indent=2))
        fb.close()

        print('更新后的json:',dicts)