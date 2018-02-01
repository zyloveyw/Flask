import os
from flask import Flask,render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, path_request
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECREY_KEY'] = 'Hello World'
app.config['UPLOADED_PHOTOS_DEST'] = os.getwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  

class UploadForm(FlaskForm):
    photo = FileField(validators = [FileAllowed(photos, u'only upload picture'),FileRequired(u'not choose files')])
    submit = SubmitField(u'submit')

@app.route('/', methods = ['GET','POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
	file_url = photos.url(filename)
    else:
	file_url = None
    return render_template('index.html', form=form, file_url=file_url)

if __name__ == '__mian__':
    app.run()
