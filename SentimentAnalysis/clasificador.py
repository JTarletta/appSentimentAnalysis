import flair

texto = "Hello World!"
model = flair.models.TextClassifier.load('en-sentiment')
def clasificador(text=texto):
    
    
    text = flair.data.Sentence(text)
    model.predict(text)
    
    clasificado = text.labels[0].value
    porcentaje = text.labels[0].score

    print(texto, clasificado, porcentaje)
    
    return clasificado, porcentaje
clasificador(texto)