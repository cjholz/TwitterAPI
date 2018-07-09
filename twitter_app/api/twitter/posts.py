from flask import Blueprint, request

posts = Blueprint('posts', __name__)


@posts.route('/new/<user_name>/<message>/', methods=['POST', 'GET'])
def create_post(user_name, message):
    # post = manager.create_post(user_name, message)
	# if not post:
		# return {'error': 'post creation failed'}, 500
	# else:
		# return {'post_id': post.post_id}, 200
    return "New Post"

@posts.route('/edit/<user_name>/<post_id>/<message>/', methods=['POST', 'GET'])
def edit_post(user_name, post_id, message):
    # try:
    	# manager.edit_post(user_name, post_id, message)
    	# return {}, 200
	# except:
		# return {'error': 'post edit failed'}, 500
    return "Post Edited"

@posts.route('/delete/<user_name>/<post_id>/', methods=['DELETE', 'GET'])
def delete_post(user_name, post_id):
    # try:
    	# manager.delete_post(user_name, post_id)
    	# return {}, 200
	# except:
		# return {'error': 'post edit failed'}, 500
    return "Post Deleted"

@posts.route('/retweet/<user_name>/<post_id>/', methods=['POST', 'GET'])
def retweet_post(user_name, post_id):
    # try:
    	# manager.retweet_post(user_name, post_id)
    	# return {}, 200
	# except:
		# return {'error': 'post edit failed'}, 500
    return "Post Retweeted"

@posts.route('/get_all/<user_name>/', methods=['GET'])
def get_all_posts(user_name=None):
    # posts = manager.get_all_posts(user_name)
    	# return {'doc': {'posts': posts}}, 200
	# if not posts:
		# return {'error': 'post edit failed'}, 500
    return "All Posts"

@posts.route('/get_one/<post_id>/', methods=['GET'])
def get_one_post(post_id):
    # post = manager.get_all_posts(user_name)
    	# return {'doc': {'post': post}}, 200
	# if not post:
		# return {'error': 'post edit failed'}, 500
    return "Requested Post"
