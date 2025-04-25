from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    user = request.args.get('user', 'Guest')
    resp = make_response(f"Hello, {user}!")

    # Simulating an insecure cache control header (vulnerable!)
    resp.headers['Cache-Control'] = 'public, max-age=60'

    return resp

if __name__ == '__main__':
    app.run(debug=True)
