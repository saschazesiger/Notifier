from flask import Flask, render_template, flash, request, url_for, redirect, jsonify, session, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = "094JH094I8OTHJ038I94H0PW3HJ4P0OIJHW3P09OHJZ"

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 