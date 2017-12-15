from flask import Flask
from flask import render_template
from flask_assets import Environment, Bundle
from livereload import Server

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path

js = Bundle(
        'js/base.js',
        filters='rjsmin',
        output='public/js/witches.js')
assets.register('js_all', js)

css = Bundle(
        'scss/application.scss',
        filters='pyscss',
        output='public/css/style.css')
assets.register('css_all', css)

@app.route('/')
def hello():
    return render_template('home.html')

if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  server = Server(app.wsgi_app)
  server.serve()
