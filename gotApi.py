import requests
from flask import Flask,render_template

app = Flask(__name__)
contentList = []
@app.route("/home",methods=['GET'])#http requests
def kingdom():
    req = requests.get("https://thronesapi.com/api/v2/Characters")
    content = req.json()
    for data in content:
        if data not in contentList:
            contentList.append(data)
    return render_template('index.html',contentList=contentList)#context


if __name__ == '__main__':
    app.run(debug=True)


