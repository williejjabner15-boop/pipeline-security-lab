import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    # Deliberately insecure: user input into a shell. SAST should flag this.
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)
