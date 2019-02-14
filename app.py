# coding:utf-8
#!bin/python3.6
from flask import Flask
from flask_apscheduler import APScheduler
import redis
from instance import create_newpoj

app = Flask(__name__)
scheduler = APScheduler()
task = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

'''

def get_task():
    print(task.keys())

scheduler.add_job(func=get_task, id="0", trigger='interval', seconds=5)
scheduler.start()

'''

list = {
    'id': '000',
    'templet': 0,
    'data': {
        'text': [
            {
                'title': '我的妈'
            },
            {
                'title2': 'title2'
            }
        ],
        'material': [
            {
                'name': '1.jpg',
                'key': 'xxx.jpg'
            },
            {
                'name': '2.jpg',
                'key': 'xxx2.jpg'
            }
        ]
    }
}
create_newpoj(list)

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
