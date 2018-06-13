from flask import Flask, render_template, request, redirect, flash, session
                                          
app = Flask(__name__)        
app.secret_key = "9nv2y4r92478tvye2uthgo2ir7894764697sdgr6g6fhf4h6g6"             
                                          
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

	if len(request.form['name']) < 1:
		flash("Invalid. Name is too short")
	else:
		flash("Welcome!")

	if len(request.form['comments']) > 120:
		flash("Comments cannot be greater than 120 characters.")

	#returns .html and the variables that were assigned to values to make page, dynamic
	return render_template('survey.html', name=name, locations=locations, languages=languages, comments=comments) 


app.run(debug=True) 