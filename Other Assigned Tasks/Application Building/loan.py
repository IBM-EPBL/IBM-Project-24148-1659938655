from flask import Flask,render_template, request, redirect, url_for, session
import joblib
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('loan.html')

@app.route('/predict',methods =['GET', 'POST'])
def predict():
	name=request.form['name']
	dep=int(request.form['dep'])
	apin=int(request.form['appin'])
	coap=int(request.form['coappin'])
	la=int(request.form['lamt'])
	lat=int(request.form['lamttrm'])
	ch=int(request.form['ch'])
	emi=int(request.form['emi'])
	x=[[dep,apin,coap,la,lat,ch,emi,0,1,0,1,0,1,1,0]]
	model=joblib.load('dt.pkl')
	#amt=model.predict(x)[0]
	return render_template('predict.html',predict=1000000)


if __name__ == "__main__":
    app.run(debug=True)
