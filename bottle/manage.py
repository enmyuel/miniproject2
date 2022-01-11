from bottle import route, run, static_file

@route('/hello')
def hello():
    return "Hello World!"

@route('/front-end/<filename>')
def index(filename):
    return static_file(filename, root='/data/project/front-end')

@route('/front-end/static/css/<filename>')
def send_css(filename):
    return static_file(filename, root='/data/project/front-end/static/css')

@route('/front-end/static/js/<filename>')
def send_js(filename):
    return static_file(filename, root='/data/project/front-end/static/js')

@route('/front-end/static/assets/<filepath:path>')
def send_img(filepath):
    return static_file(filepath, root='/data/project/front-end/static/assets')

run(host='0.0.0.0', port=8080, debug=True)
