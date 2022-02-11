from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def symbol():
    return "Testing route"

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=3000)