from bottle import route, run, request, static_file
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


    a = db.member.find_one({'id':id, 'password':password})
    if a != None:
        print("welcome! "+ a['name'])
    else:
        print("authentication failed")
    client.close()
    return static_file("signup.html", root='/data/project/front-end')

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
    ## a = db.member.find_one({'id':'1111', 'password':'2222'})
    # db.member.delete_one({'name':'abcd'})
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

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
