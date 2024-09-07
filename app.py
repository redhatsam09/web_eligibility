from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# User credentials (username: password)
users = {
    "rasm": "233",
    "sam": "100",
    "pam": "345"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Invalid username or password")

@app.route('/welcome.html')
def welcome():
    return send_from_directory('', 'welcome.html')

@app.route('/')
def index():
    return send_from_directory('', 'login.html')

if __name__ == '__main__':
    app.run(debug=True)
