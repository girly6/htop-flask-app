from flask import Flask, render_template_string
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Tejaswi"
    
    username = os.getenv('USER') or os.getenv('USERNAME') or 'Unknown'
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], timeout=5).decode('utf-8')
    except (subprocess.SubprocessError, OSError):
        top_output = "Unable to retrieve top output on this system."

    html_template = """
    <html>
        <head>
            <title>MorphLe Labs Online Test</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                pre { background-color: #f0f0f0; padding: 10px; border-radius: 5px; overflow-x: auto; }
            </style>
        </head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {{ name }}</p>
            <p><strong>Username:</strong> {{ username }}</p>
            <p><strong>Server Time (IST):</strong> {{ server_time }}</p>
            <h2>Top Output:</h2>
            <pre>{{ top_output }}</pre>
        </body>
    </html>
    """
    
    return render_template_string(html_template, name=name, username=username, 
                                  server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)