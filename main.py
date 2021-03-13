import routes

from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/trending', methods=['GET'])
def trending():
    # cookies = request.cookies()
    # userid = get identifier from cookies
    userid = 0

    return routes.trendsForUser(userid)


@app.route('/category/<category_name>/results', methods=['POST'])
def saveCategoryResult(category_name):
    # cookies = request.cookies()
    # userid = get identifier from cookies
    userid = 0

    return routes.saveCategoryResult(request, userid, category_name)


@app.route('/category/<category_name>/results', methods=['GET'])
def getCategoryResult(category_name):
    # cookies = request.cookies()
    # userid = get identifier from cookies
    userid = 0

    return routes.getCategoryResult(userid, category_name)

@app.route('/user/categories', methods=['GET'])
def getUserCategories():
    # cookies = request.cookies()
    # userid = get identifier from cookies
    userid = 0

    return routes.getUserCategories(userid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
