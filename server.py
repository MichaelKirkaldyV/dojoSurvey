from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                                                             
def index():
  return render_template('index.html')  

#sets method to POST
@app.route('/survey', methods=['POST']) 
def survey():
	#sets variable equal to form request in html attribute, i.e <div name="name"></div>
	name = request.form['name']
	locations = request.form['locations']
	languages = request.form['languages']
	comments = request.form['comments']
	#returns .html and the variables that were assigned to values to make page, dynamic
	return render_template('survey.html', name=name, locations=locations, languages=languages, comments=comments) 


app.run(debug=True) 