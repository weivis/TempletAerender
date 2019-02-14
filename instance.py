def create_newpoj(data):
    #{'id': '000', 'templet': 0, 'data': {'text': [{'title': '内容'}], 'material': [{'name': '1.jpg', 'key': 'xxx.jpg'}]}}
    if data['templet'] == 0:
        from mould.templet1.templet_1 import delete_oldmaterial, download_newmaterial, upload_templetjson
        delete_oldmaterial()
        download_newmaterial(data['data']['material'])
        upload_templetjson(data['data']['text'])