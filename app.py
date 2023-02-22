from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/wx', methods=['GET', 'POST'])
def wechat():
    # 微信公众号的请求处理逻辑
    # 您可以在这里添加您的 ChatGPT 机器人逻辑
    return 'Hello, WeChat!'

if __name__ == '__main__':
    app.run()
