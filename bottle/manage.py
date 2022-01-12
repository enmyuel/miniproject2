from bottle import route, run, request, static_file
from pymongo import MongoClient

@route('/front-end/<filename>', method='GET')
def index(filename):
    print("GET")
    return static_file(filename, root='/data/project/front-end')

@route('/front-end/signup.html')
def test():
    print("hello")
    return static_file("signup.html", root='/data/project/front-end')

# 회원가입 처리
@route('/front-end/signup.html', method='POST')
def post_test():
    print("hello post")
    name = request.forms.get("name")
    id = request.forms.get("id")
    password = request.forms.get("password")

    data = {"name":name, "id":id, "password":password}

    client = MongoClient(host='localhost', port=27017)

    db = client.member
    db.member.insert_one(data)
    # db.member.delete_one({'name':'abcd'})
    # user = db.member.find_one({'name' : 'abcd'})
    # print(user)
    #db = client.station
    #user = db.data.find_one({'rackTotCnt':'22'})

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
