import flair
import emoji

texto = "Hello World! 😀"
model = flair.models.TextClassifier.load('en-sentiment')
def clasificador(text=texto):
    
    text = emoji.demojize(text, delimiters=(" ", ""))
    text = flair.data.Sentence(text)
    model.predict(text)
    
    clasificado = text.labels[0].value
    porcentaje = text.labels[0].score

    print(texto, clasificado, porcentaje)
    
    return clasificado, porcentaje
#clasificador(texto)