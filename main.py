from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

openai.api_key = 'your-openai-key'

@app.route('/', methods=['GET', 'POST'])
def summarize_text():
    if request.method == 'POST':
        text = request.form['text']
        
    
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Please provide a brief and concise SUMMARY of the following text, ensuring that all crucial information is retained."},
                {"role": "user", "content": text}
            ],
            max_tokens=150  
        )
        
        assistant_reply = response['choices'][0]['message']['content']
        
        return render_template('result.html', original_text=text, result=assistant_reply)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)



