from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Local AutoDeploy App</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #0f172a; color: white; margin: 0; }
            .card { background: #1e293b; padding: 2rem 3rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); text-align: center; border: 1px solid #334155; }
            .badge { background: #22c55e; color: #022c22; padding: 6px 16px; border-radius: 20px; font-weight: bold; font-size: 0.9rem; text-transform: uppercase; }
            h1 { margin-top: 1rem; color: #f8fafc; }
            p { color: #94a3b8; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">Status: Live & Automated</span>
            <h1>Local AutoDeploy Web App</h1>
            <p><strong>App Version:</strong> v3.0.0</p>
            <p>Built by GitHub Actions & Auto-Updated locally</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)