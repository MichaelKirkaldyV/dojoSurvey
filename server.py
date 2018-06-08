from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                                                             
def index():
  return render_template('index.html')  

@app.route('/survey', methods=['POST']) 
def survey():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comments = request.form['comments']
	return render_template('survey.html', name=name, locations=location, languages=language, comments=comments) 


app.run(debug=True) 