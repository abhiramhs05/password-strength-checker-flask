from flask import Flask, render_template, request

import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        remarks.append("Add numbers.")

    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        remarks.append("Add special characters.")

    common_passwords = ["password", "123456", "qwerty", "admin"]
    if password.lower() in common_passwords:
        remarks.append("This password is too common!")

    if score <= 2:
        strength = "Weak ❌"
    elif score == 3 or score == 4:
        strength = "Moderate ⚠️"
    else:
        strength = "Strong ✅"

    return strength, remarks

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    remarks = []
    if request.method == 'POST':
        password = request.form['password']
        strength, remarks = check_password_strength(password)
    return render_template('index.html', strength=strength, remarks=remarks)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
