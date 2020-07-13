from flask import Flask, render_template,url_for
import os

app = Flask(__name__)

picFolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolder

@app.route('/')
def home():
    return '''<h1>Wanna catch a flag...</h1>
    <p>Are u ready for the challenge..</p>
    <p>Then , Wake up your cryptography and steganography skills..</p>
    <h3>Move to the challenge page to start your task</h3>'''
 
@app.route('/home')
def flag():
 	return render_template("home.html")


@app.route('/challenge')
def source():
	pic1=os.path.join(app.config['UPLOAD_FOLDER'],'puppys.jpeg')
	return render_template("image.html",user_image=pic1)

@app.route('/hint')
def hint():
	return '''<h1>Hint:</h1><p>First,check out the image thoroughly and then start your task..<p>'''	

if (__name__ == '__main__'):
    app.run()
