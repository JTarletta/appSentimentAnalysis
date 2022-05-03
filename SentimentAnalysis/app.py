from flask import Flask, render_template, request
from clasificador import clasificador
#print(Flask)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def principal():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def logica():
 
    text = request.form.get("texto")
    classification = clasificador(text)
    return render_template('index.html', clasificador=classification) 


@app.route('/cls', methods=['GET'])
def cls():
    return render_template('indexcls.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)