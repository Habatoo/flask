from app import app

@app.route('/')
@app.route('/index')
def index():
    #return "������, ���!"
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)