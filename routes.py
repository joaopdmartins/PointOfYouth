import random
import time
import copy
import operator

from flask import Request, jsonify

categories = [
    { 'category': 'Covid-19' },
    { 'category': 'Digital Civility' },
    { 'category': "Human Rights" },
    { 'category': 'Education' },
    { 'category': 'Culture' },
    { 'category': 'Work Policies' },
    { 'category': 'Crime' },
    { 'category': 'Finance' },
    { 'category': 'Social Skills' },
    { 'category': 'Web Skills' },
    { 'category': 'Politics' },
    { 'category': '' },
]

user_results = {}
''' dicionários de userid => category => results
'''

random.seed(time.time())

def trendsForUser(userid :int):
    ''' returns list of trends tailored to userid
    '''

    trends = copy.deepcopy(categories)

    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for c in trends:
        pos = random.randint(0, len(positions) - 1)
        c['position'] = positions[pos]
        del positions[pos]

        if len(positions) == 0:
            break


    trends = trends[:10]
    trends.sort(key=operator.itemgetter('position'))

    return jsonify(trends)


def saveCategoryResult(request :Request, userid :int, category :str):
    ''' save response to user questionary
    '''
    user_results[userid] = {}
    user_results[userid][category] = request.get_json(force=True)

    return jsonify({ 'error': None, 'result': 'Saved' })

def getCategoryResult(userid :int, category :str):
    ''' returns user's response to category
    '''

    if userid in user_results and category in user_results[userid]:
        return jsonify(user_results[userid][category])
    else:
        return jsonify({ "error": 'Not yet completed' })


def getUserCategories(userid :int):
    ''' returns user tailored categories
    '''
    user_categories = copy.deepcopy(categories)

    for c in user_categories:
        if userid in user_results and c['category'] in user_results[userid]:
            c['status'] = 'Complete'
        else:
            c['status'] = 'New'

    return jsonify(user_categories)
