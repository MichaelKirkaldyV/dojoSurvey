from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                                                             
def index():
  return render_template('index.html')  

@app.route('/survey', methods=['POST']) 
def survey():
	name = request.form['name']
	locations = request.form['locations']
	languages = request.form['languages']
	comments = request.form['comments']
	return render_template('survey.html', name=name, locations=locations, languages=languages, comments=comments) 


app.run(debug=True) 