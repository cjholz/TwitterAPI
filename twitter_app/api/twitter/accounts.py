from flask import Blueprint, request, render_template
import psycopg2

accounts = Blueprint('accounts', __name__)

@accounts.route('/sign_in/', methods=['GET'])
def sign_in():
	return render_template('twitter/accounts/sign_in.html')

@accounts.route('/sign_up/', methods=['GET'])
def sign_in():
	return render_template('twitter/accounts/index.html')

@accounts.route('/new/', methods=['POST'])
def create_user():
	form = request.form.to_dict()
	user_name = form.get('user_name')
	email = form.get('email')
	password = form.get('password')
	
	# check email unique

	# need to actually instantiate first
	account_manager.create_user(user_name, email, password)

	# actually use user info
	return "New User"

@accounts.route('/get/', methods=['GET'])
def get_user():
	form = request.form.to_dict()
	conn = psycopg2.connect("dbname=gsl_twitter")
	cur = conn.cursor()

	#check password

	sql_get = """
		SELECT * FROM accounts
		WHERE user_name='%s';
		"""%(form.get('user_name'))
	cur.execute(sql_get)
	conn.commit()
	# actually use user info
	return "User Found"

@accounts.route('/delete/<user_name>/', methods=['DELETE', 'GET'])
def delete_user(user_name):
	# try:
		# user = manager.delete_user(user_name)
	# except:
		# return {'error': 'something went wrong'}, 500
	# return {'doc': 'user_name': user.name}, 200
	return "User Deleted"

@accounts.route('/edit/<user_name>/<email>/<password>/', methods=['POST', 'GET'])
def edit_user(user_name, email=None, password=None):
	# try:
		# user = manager.edit_user(user_name, email, password)
	# except:
		# return {'error': 'something went wrong'}, 500
	# return {'doc': 'user_name': user.name}, 200
	return "User Edited"

@accounts.route('/follow/<user_name>/<other_user>/', methods=['POST', 'GET'])
def follow_user(user_name, other_user):
	# try:
		# user = manager.follow_user(user_name, other_user)
	# except:
		# return {'error': 'something went wrong'}, 500
	# return {'doc': 'user_name': user.name}, 200
	return "User Followed"

@accounts.route('/unfollow/<user_name>/<other_user>/', methods=['POST', 'GET'])
def unfollow_user(user_name, other_user):
	# try:
		# user = manager.unfollow_user(user_name, other_user)
	# except:
		# return {'error': 'something went wrong'}, 500
	# return {'doc': 'user_name': user.name}, 200
	return "User Followed"
