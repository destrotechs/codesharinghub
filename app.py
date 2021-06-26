from flask import Flask,render_template,redirect,url_for,request,flash
import flask
import os
from random import randint
app = flask.Flask(__name__)
UPLOAD_FOLDER = '/snippets'

app.secret_key = "ABC"


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':

        # os.system('cmd /k "python app.py"')
        return render_template('index.html')
    elif request.method == 'POST':
        language = request.form.get('language')

        code = request.form.get('code')

        description = request.form.get('description')

        
        if language == 'python':
            filename = randint(1,1000000)
            file = open("snippets/python/"+str(filename)+".txt","w")
            file.write(str(code)+"\n")
            file.write("desk"+str(description))
            file.close()
            flash("success")
            return redirect(url_for('index'))
        if language == 'php':
            filename = randint(1,1000000)
            file = open("snippets/php/"+str(filename)+".txt","w")
            file.write(str(code)+"\n")
            file.write("desk"+str(description))
            file.close()
            flash("success")
            return redirect(url_for('index'))
        if language == 'java':
            filename = randint(1,1000000)
            file = open("snippets/java/"+str(filename)+".txt","w")
            file.write(str(code)+"\n")
            file.write("desk"+str(description))
            file.close()
            flash("success")
            return redirect(url_for('index'))               
       


@app.route('/snippets/view/<language>',methods=['GET'])
def snippet_view(language):
    if language == 'python':
        arr_txt = [x for x in os.listdir('snippets/python/') if x.endswith(".txt")]
        content = list()
        for snippet in arr_txt:
            file = open("snippets/python/"+snippet,'r')
            filecontent = file.read()
            code = filecontent.split("desk")
            content.append(code)
        length = len(arr_txt)
        return render_template("languages.html",snippets = arr_txt,content=content,length=length,language=language)
    if language == 'php':
        arr_txt = [x for x in os.listdir('snippets/php/') if x.endswith(".txt")]
        content = list()
        for snippet in arr_txt:
            file = open("snippets/php/"+snippet,'r')
            filecontent = file.read()
            code = filecontent.split("desk")
            content.append(code)
        length = len(arr_txt)
        return render_template("languages.html",snippets = arr_txt,content=content,length=length,language=language)
    if language == 'java':
        arr_txt = [x for x in os.listdir('snippets/java/') if x.endswith(".txt")]
        content = list()
        for snippet in arr_txt:
            file = open("snippets/java/"+snippet,'r')
            filecontent = file.read()
            code = filecontent.split("desk")
            content.append(code)
        length = len(arr_txt)
        return render_template("languages.html",snippets = arr_txt,content=content,length=length,language=language)



app.run(debug=False)
