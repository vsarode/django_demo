from flask import Flask, request, jsonify

from quora.db.quora.models import User

app = Flask(__name__)


@app.route("/user")
def create_user():
    import django
    django.setup()
    request_data = request.args
    print request_data
    try:
        user_object = User.objects.create(username=request_data['username'], password=request_data['password'],
                                          mobile_number=int(request_data['mobileNumber']))
    except Exception as e:
        print e
    response_dict = {"username": user_object.username,
                     "password": user_object.password,
                     "mobileNumber": user_object.mobile_number}
    return jsonify(response_dict)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2004, debug=True)
