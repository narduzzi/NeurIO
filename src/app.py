from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
@app.route('/')
def index():
    return render_template('indexv3.html')

@app.route('/v2')
def index2():
    return render_template('indexv2.html')

if __name__ == '__main__':
    app.run(debug=True)
