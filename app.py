from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CSI2113 DevOps Application</title>
        </head>
        <body>
            <h1>Welcome to My DevOps Application</h1>
            <p>Containerized Web Application</p>
            <p>Built using Python, Flask and Docker.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)