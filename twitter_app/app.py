from flask import Flask

def create_app():
    # Create the flask app
    twitter_app = Flask('twitter')
    register_blueprints(twitter_app)
    return twitter_app

def register_blueprints(twitter_app):
    from twitter_app.api.twitter.accounts import accounts
    twitter_app.register_blueprint(accounts, url_prefix='/accounts')
    from twitter_app.api.twitter.posts import posts
    twitter_app.register_blueprint(posts, url_prefix='/posts')

app = create_app()
