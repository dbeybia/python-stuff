from flask import Flask,request, render_template
from jinja2 import Template
import praw

app = Flask(__name__)


@app.route('/',  methods=['GET'])
def reddit():
	SUBREDDIT = raw_input("Please enter the name of the subreddit: ")
	USERAGENT = 'Web image browser by @meddbeibia'
	r = praw.Reddit(USERAGENT)
	submissions = r.get_subreddit(SUBREDDIT).get_hot(limit=20)
	return (render_template('index.html', submissions=submissions, len=len))


if __name__ == '__main__':
    app.run(debug=True)