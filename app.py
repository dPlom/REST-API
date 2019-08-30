from flask import Flask, request, jsonify, abort
import urllib.request
import json



app = Flask(__name__)


@app.route("/user", methods=["POST"])
def add_user():
    """POST /user
    
    {
    "user_id": "username3"
    }
    
    """
    if 'user_id' not in request.json:
         abort(400)   
         
    user_id = request.json['user_id']
    url = 'https://randomuser.me/api/?ud={}'.format(str(user_id))
    req = urllib.request.Request(url)    
    r = urllib.request.urlopen(req).read()
    r_user = json.loads(r.decode('utf-8'))
    random_result=r_user['results'][0]
    final_result=    {'user':{
        'lastname': random_result['name']['last'],
        'firstname': random_result['name']['first'],
        'image': random_result['picture']['medium'],
        'Address':{
            'street':random_result['location']['street'],
            'city':'{} - {}'.format(random_result['location']['city'],random_result['location']['state'])
        }}
        }    
    
    

    return jsonify(final_result)


if __name__ == '__main__':
    app.run(debug=True)