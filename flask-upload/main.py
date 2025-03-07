from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(f'upload/{file.filename}')
            return 'success'
    return '''
        <!doctype html>
        <form method="POST" enctype='multipart/form-data'>
            <input type='file' name='file'>
            <button type='submit'>Отправить</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)