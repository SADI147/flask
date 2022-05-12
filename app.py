from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('content.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      print(str(f.filename))
      print(os.path.abspath(str(f.filename)))
      f.save(secure_filename(f.filename))
      return "file uploaded"
		
if __name__ == '__main__':
   app.run(debug = True)