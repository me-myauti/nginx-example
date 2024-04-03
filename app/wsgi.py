from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    #Returns container ID to check if default nginx load balancer is working (round robin)
    return f"Container ID: {socket.gethostname()}"

if __name__ == "__main__":
    app.run(debug=True)