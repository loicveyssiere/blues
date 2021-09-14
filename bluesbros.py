from flask import Flask, request, jsonify, make_response, abort
from functools import wraps

app = Flask(__name__)

allowed_ip = '10.0.0.'

@app.before_request
def limit_remote_addr():
        client_ip = str(request.remote_addr)
        if not client_ip.startswith(allowed_ip):
                abort(403)

def auth_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if auth and auth.username == 'Edwood' and auth.password == 'Edwood':
			return f(*args, **kwargs)
		
		return make_response('There is a problem with your username or password !', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
	return decorated

@app.route("/simu", methods=["POST"])
@auth_required
def simu():
        if request.is_json :
                json_obj = request.get_json()
                dict = {
                        "nb_musicians": json_obj.get("nb_musicians"),
                        "theta": json_obj.get("theta")
                }
                s = 0
                for i in range(dict["nb_musicians"]):
                        s = s + dict["theta"][i]
                x = 1/dict["nb_musicians"]*s
                result = {
                        "mean" : 1/(1-x),
                        "variance" : x/(1-x)**2
                }
                result = make_response(jsonify(result), 200) #status code 200 means everything's fine
                return result
        else:
                dict = { "message": "You did not send a JSON object !"}
                result = make_response(jsonify(dict), 400) #status code 400 means error
                return  result

@app.route("/ping", methods=["GET"])
def ping():
    return make_response(jsonify({"message": "pong"}), 200)


# Entrypoint for development only
if __name__ == "__main__":
    app.run(port=8080)

