from twitter_app.app import app

app.run(
    host="0.0.0.0",
    port=8888,
    use_reloader=True,
    use_debugger=True,
    threaded=False
)