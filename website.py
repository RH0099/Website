from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Anonymous 18 Hosting Service</title>
    <style>
        body {
            font-family: 'JetBrains Mono', monospace;
            background: linear-gradient(135deg, #000000, #1a1a1a);
            color: #00ff41;
            text-align: center;
            padding: 50px;
        }
        .logo img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
        }
        h1 {
            text-shadow: 0 0 20px #00ff41;
        }
        form {
            margin-top: 20px;
        }
        input[type="file"], input[type="submit"] {
            padding: 10px;
            margin: 10px;
            border: 2px solid #00ff41;
            background: #000;
            color: #00ff41;
            border-radius: 5px;
        }
        .links a {
            color: #00ff41;
            text-decoration: none;
        }
        .disclaimer {
            margin-top: 20px;
            color: red;
        }
    </style>
</head>
<body>
    <div class="logo">
        <img src="https://via.placeholder.com/120" alt="Logo">
    </div>
    <h1>The Anonymous 18 Hosting Service</h1>
    <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="submit" value="Upload File">
    </form>
    <div class="links">
        <a href="https://t.me/TheAnonymous18R" target="_blank">Join My Group</a>
    </div>
    <div class="disclaimer">
        <p>Disclaimer: You are responsible for your uploaded files. Backup your files.</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return f"File {file.filename} uploaded successfully."
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
