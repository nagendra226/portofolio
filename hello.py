from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None,post_id=2):
	#return render_template('index.html',name=username,id=post_id)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
	return render_template(page_name)

def write_file(data):
	with open('database.csv','a',newline='\n') as db:
		email = data['email']
		subject = data['subject']
		message = data['message']
		spamwriter = csv.writer(db,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			write_file(data)
			return redirect('/thankyou.html')
		except:
			return "did not save to database"
	else:
		return "something went wrong."
