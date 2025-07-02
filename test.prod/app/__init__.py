from flask import Flask, render_template
from flask import request, abort

def create_app():
    app = Flask(__name__)
    TRUSTED_IP = '49.36.189.9'
    TRUSTED_LOCAL_IPS = ['127.0.0.1', 'localhost']

    @app.before_request
    def restrict_access():
        client_ip = request.remote_addr
        if client_ip in TRUSTED_LOCAL_IPS or client_ip == TRUSTED_IP:
            return  # Trusted IP, skip token check
        allowed_tokens = ['secret123', 'token456', 'token789']
        if request.endpoint != 'static' and request.args.get('token') not in allowed_tokens:
            abort(403)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    @app.route('/do1')
    def do1():
        return 'hi, World!'

    @app.route('/do2')
    def do2():
        return 'hi, World!'
    @app.route('/env')
    def show_env():
        import os
        env_info = [f"{k} = {v}" for k, v in os.environ.items()]
        return "<br>".join(env_info)
    @app.route('/vars')
    def show_vars():
        import sys
        vars_info = [f"{k} = {v}" for k, v in vars(sys).items()]
        return "<br>".join(vars_info)
    @app.route('/hvars')
    def show_httpvars():
        from flask import request
        http_vars = [f"{k} = {v}" for k, v in request.environ.items()]
        cookies = [f"Cookie: {k} = {v}" for k, v in request.cookies.items()]
        return "<br>".join(http_vars + cookies)

    return app

