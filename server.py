from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                                                             
def index():
  return render_template('index.html')  

@app.route('/survey', methods=['POST']) 
def survey():
	print "Summary:"
	name = request.form['name']
	locations = request.form['locations']
	languages = request.form['languages']
	comments = request.form['comments']
	return redirect('/') 


app.run(debug=True) 