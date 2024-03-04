import re
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pattern = request.form['pattern']
        data = request.form['data']

        # Perform case-insensitive regex matchings
        matches = re.findall(pattern, data, re.IGNORECASE)

        return render_template('index.html', pattern=pattern, data=data, matches=matches)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
