from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate_progress():
    for i in range(101):
        time.sleep(.1)
        yield f"data: {i}\n\n"

@app.route('/progress')
def progress():
    return Response (
        generate_progress(),
        mimetype = 'text/event-stream'
    )

if __name__ == '__main__':
    app.run(debug=True)