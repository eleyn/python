from bottle import route, run
a = [1,2,3,4,5]

def find(array, x):
    for i in range(len(a) - 1):
        if a[i] == x:
            return True

    return False 


@route('/hello')
def hello():
    return "Hello World!"

@route('/search/<number>')
def search(number):
    return str(find(a,int(number)))

run(host='localhost', port=8080, debug=True)

