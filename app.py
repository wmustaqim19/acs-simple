from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import socket

app = Flask(__name__)

counter = 0
started_at = datetime.utcnow()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>ACS Simple App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e5e7eb;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .card {
            background: #020617;
            padding: 30px;
            border-radius: 12px;
            width: 420px;
            box-shadow: 0 20px 40px rgba(0,0,0,.4);
        }
        h1 { color: #38bdf8; }
        button {
            background: #38bdf8;
            border: none;
            padding: 10px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #0ea5e9;
        }
        input {
            padding: 8px;
            width: 100%;
            border-radius: 6px;
            border: none;
            margin-top: 8px;
        }
        .box {
            background: #020617;
            border: 1px solid #1e293b;
            padding: 10px;
            border-radius: 8px;
            margin-top: 12px;
        }
    </style>
</head>
<body>
<div class="card">
    <h1>🚀 ACS Simple App</h1>

    <div class="box">
        <b>Server:</b> {{ host }}<br>
        <b>Started at:</b> {{ started }}<br>
        <b>Uptime:</b> {{ uptime }} sec
    </div>

    <div class="box">
        <p>Counter: <b id="counter">{{ counter }}</b></p>
        <button onclick="increment()">+ Increment</button>
    </div>

    <div class="box">
        <form onsubmit="sendMessage(event)">
            <label>Send message:</label>
            <input id="msg" placeholder="type something..." />
        </form>
        <p id="response"></p>
    </div>
</div>

<script>
function increment() {
    fetch('/api/increment', { method: 'POST' })
        .then(res => res.json())
        .then(data => {
            document.getElementById('counter').innerText = data.counter
        })
}

function sendMessage(e) {
    e.preventDefault()
    fetch('/api/message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: document.getElementById('msg').value })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('response').innerText = data.reply
    })
}
</script>
</body>
</html>
"""

@app.route("/")
def index():
    uptime = int((datetime.utcnow() - started_at).total_seconds())
    return render_template_string(
        HTML,
        counter=counter,
        host=socket.gethostname(),
        started=started_at.strftime("%Y-%m-%d %H:%M:%S UTC"),
        uptime=uptime
    )

@app.route("/api/increment", methods=["POST"])
def increment():
    global counter
    counter += 1
    return jsonify(counter=counter)

@app.route("/api/message", methods=["POST"])
def message():
    data = request.get_json()
    text = data.get("mes

