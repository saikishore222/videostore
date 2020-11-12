from flask import Flask,render_template,request,send_file,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
app=Flask(__name__)
ALLOWED_EXTENSIONS = {'mp4', 'mkv'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filestorage.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class videocontents(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        name=db.Column(db.String(100),nullable=False)
        videofile=db.Column(db.LargeBinary)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/upload',methods=['POST'])
def upload():
	file=request.files['inputfile']
	newfile=videocontents(name=file.filename,videofile=file.read())
	db.session.add(newfile)
	db.session.commit()
	return redirect(url_for('Download'))
@app.route('/Download')
def Download():
    file_data=videocontents.query.all()
    return  render_template('home.html',users=file_data)                                      
if __name__=='__main__':
    app.run()
