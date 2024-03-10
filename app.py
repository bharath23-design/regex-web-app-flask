import re
from flask import Flask, request, render_template

app = Flask(__name__)

def validate_email(email):
    # Add your email validation logic here
    # For simplicity, this example uses a basic regex pattern
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pattern = request.form.get('pattern', '')
        data = request.form.get('data', '')
        email = request.form.get('email', '')

        if pattern and data:  # Pattern matching
            matches = re.findall(pattern, data, re.IGNORECASE)
            return render_template('index.html', pattern=pattern, data=data, matches=matches, email=email)

        elif email:  # Email validation
            is_valid_email = validate_email(email)
            return render_template('index.html', email=email, is_valid_email=is_valid_email)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
