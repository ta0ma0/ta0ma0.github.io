from flask import Flask, render_template
from flask_flatpages import FlatPages
import pygments.styles

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages(app)

@app.route('/')
def index():
    posts = flatpages
    return render_template('index.html', posts=posts)

@app.route('/<path:path>/')
def post(path):
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
