from bottle import route, run, request, static_file, redirect, template
from pymongo import MongoClient
import sys, os
sys.path.append("/data/project/front-end")
import map

@route('/front-end/<filename>')
def index(filename):
    return static_file(filename, root='/data/project/front-end')


@route('/front-end/rent.html')
def rent():
    map.getMap()
    return static_file("rent.html", root='/data/project/front-end')


# 로그인 처리
@route('/front-end/login.html', method='POST')
def login():
    client = MongoClient(host='localhost', port=27017)
    db = client.member

    id = request.forms.get("id")
    password = request.forms.get("password")

    user = db.member.find_one({'id':id, 'password':password})
    print("id = " + id, "password = " + password)

    client.close()

    if user != None:
        print("welcome! "+ user['name'])
        return "<script>alert('로그인에 성공하였습니다'); window.location.href='index.html';</script>"
    else:
        print("authentication failed")
        return "<script>alert('다시 시도해주세요'); window.location.href='login.html';</script>"

# 회원가입 처리
@route('/front-end/signup.html', method='POST')
def signup():

    name = request.forms.get("name")
    id = request.forms.get("id")
    password = request.forms.get("password")

    data = {"name":name, "id":id, "password":password}

    client = MongoClient(host='localhost', port=27017)
    db = client.member
    db.member.insert_one(data)
    # a = db.member.find_one({'id':'1111', 'password':'2222'})
    client.close()
    return static_file("signup.html", root='/data/project/front-end')


@route('/front-end/static/css/<filename>')
def send_css(filename):
    return static_file(filename, root='/data/project/front-end/static/css')

@route('/front-end/static/js/<filename>')
def send_js(filename):
    return static_file(filename, root='/data/project/front-end/static/js')

@route('/front-end/static/assets/<filepath:path>')
def send_img(filepath):
    return static_file(filepath, root='/data/project/front-end/static/assets')

run(host='0.0.0.0', port=80, debug=True, reloader=True)
