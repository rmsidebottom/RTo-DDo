#!flask/bin/python

from flask import Flask, jsonify, make_response, abort
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)

assignments = [
	{
		'id': 1,
		'source': 'mechanics',
		'details': 'homework 7',
		'start': '7/7',
		'end': '7/11',
		'done': False
	},
	{
		'id': 2,
		'source': 'mechanics',
		'details': 'project',
		'start': '7/7',
		'end': '7/20',
		'done': False
	},
	{
		'id': 3,
		'source': 'math',
		'details': 'problems 2,3,4 p 390',
		'start': '7/7',
		'end': '7/9',
		'done': False
	}
]

################################################################################
""" Error handling """
@app.errorhandler(404)
def not_found(error):
	return "404: No assignment(s) found."

@app.errorhandler(403)
def forbidden(error):
	return "403: Access forbidden."

################################################################################
""" Authentication code """
auth = HTTPBasicAuth()

""" Password checking """
@auth.get_password
def get_password( username ):
	if username == "test":
		return "flask_agenda"
	return None

@auth.error_handler
def unauthorized():
	return make_response("Unauthorized user", 403)

################################################################################
""" Get all of the assignments """
@app.route('/', methods=['GET'])
@auth.login_required
def index():
	return jsonify({'assignments': assignments})

""" This allows you to search for all assignments from a specific source """
@app.route('/<string:assign_id>', methods=['GET'])
def get_assigns(assign_id):
	count = 0
	assign = {}
	for i in range(0, len(assignments) ):
		if assignments[i]['source'] == assign_id:
			assign[count] = assignments[i]
			count += 1
	if count == 0:
		abort(404)
	return jsonify( {'assignment': assign} )


if __name__ == '__main__':
	app.run(debug=True)
