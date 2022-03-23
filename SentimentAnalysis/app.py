from distutils.log import debug
from flask import Flask, render_template, request, url_for, redirect
from clasificador import clasificador
#print(Flask)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def principal():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def logica():
    #textFile = request.files.get('texto', None) 
    req = request.get_json() 
    textFile = req['text']
    text_path = "./texto/" + textFile.filename
    textFile.save(text_path)

    #text = "texto"
    classification = clasificador(text_path)


    return render_template('index.html', clasificador=classification) 


if __name__ == '__main__':
    app.run(port=5000, debug=True)