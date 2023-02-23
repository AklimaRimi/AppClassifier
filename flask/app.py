from flask import Flask, render_template,request
import requests


app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def home():
    
    if request.method == 'POST':
        text = request.form['text']
        output = classifyer(text)['confidences']
        print(output)
        labels = [x['label'] for x in output if x['confidence'] > .05]
        
        return render_template('home.html',text=text,labels=labels)
    else:
        return render_template('home.html',text='',labels='')

def classifyer(text):

    response = requests.post("https://rimi98-appclassifier.hf.space/run/predict", json={
        "data": [
            text
        ]
    }).json()

    data = response["data"]
    
    return data[0]


if __name__ == '__main__':
    app.run()