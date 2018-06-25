from flask import Flask
from flask import render_template
from flask import request
import json
from examples.im_spider import spider

app = Flask(__name__)
@app.route('/')
def shouye():
    return render_template("index.html")

@app.route('/s',methods=['POST'])
def search():
    userName=request.form['userName']
    kind=request.form['postclass']
    json_str=spider(kind,userName)
    return json_str

    #data = [{'TiteName': '第一个标题'},{ 'TiteName': '第二个标题'},{'TiteName': '第三个标题'}]
   # json_str = json.dumps(data)
    #print(json_str)
   # print(userName,kind)
   # return json_str


if __name__ == '__main__':
    app.run(debug=True, port=8000)