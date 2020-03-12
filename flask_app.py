from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def render_static(page_name):
    return render_template('%.html' % page_name)

if __name__ == '__main__':
    app.run()