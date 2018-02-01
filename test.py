from flask import Flask, url_for,render_template,request,redirect,abort,make_response,session,escape
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/shiyanlou')
def hello_world():
    return 'Yang'

@app.route('/user/<username>')
def showname(username):
    return 'Your name is : %s' % username

@app.route('/postid/<int:id>')
def showid(id):
    return 'your id is: %s' %id


@app.route('/sum/<int:a>/<int:b>')
def return_sum(a,b):
    return 'sum is: %d' %(a+b) 

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/mystyle/')
@app.route('/mystyle/<name>')
def mystyle(name=None):
    return render_template('mystyle.css',name=name)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath,'/home/shiyanlou/Desktop/Flask/uploads/',secure_filename(f.filename))

        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

@app.route('/')
def indedx():
    #return redirect(url_for('test'))
    if 'username' in session:
	return 'Logged in as %s' %escape(session['username'])
    return 'You are not logged in'  

@app.route('/login', methods=['GET','POST'])
def login():
    #if request.method =='GET':
       # show_the_login()
       # return render_template('hello.html')
    if request.method =='POST':
       # do_the_login()
        session['username'] = request.form['username']
	return redirect(url_for('index'))
    return ''' <form action="" method="post">
	        <p><input type=text name=username>
		<p><input type=submit value=Login>
	      </form>  ''' 
    
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
app.config['SECRET_KEY'] = 'yaowan is a good girl'
app.secrect_key = 'yaowan is a good girl'
app.config.update(SECRET_KEY='yaowan is a good girl')

@app.route('/test')
def test():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('upload.html'),404)
    resp.headers['X-Something'] = 'A value'
    return resp
   #return render_template('page_not_found.html'),404


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')


