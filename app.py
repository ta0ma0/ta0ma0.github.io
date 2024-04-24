from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages(app)

def pages_key(page):
    # Sort by 'date' metadata, descending order (newest first)
    return page.meta.get('date', 0) 

@app.route('/')
def index():
    posts = sorted(flatpages, key=pages_key, reverse=True)  # Sort on template call
    return render_template('index.html', posts=posts)

@app.route('/<path:path>/')
def post(path):
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
