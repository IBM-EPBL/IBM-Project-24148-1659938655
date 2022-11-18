from flask import Flask,render_template, request, redirect, url_for, session

import requests
app = Flask(__name__)


API_KEY = "UFiKYlV2AoWKo8kRnD98FYnw1kbFf1pjM9tjqIRhQplY"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

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
	#Smodel=joblib.load('dt.pkl')
	#amt=model.predict(x)[0]

	payload_scoring = {"input_data": [{"field": [['dep','apin','coap','la','lat','ch','emi','0','1','0','1','0','1','1','0']], "values":x}]}

	response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/53c0255e-5264-4c30-8c99-7d4f79629557/predictions?version=2022-11-16', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
	print(response_scoring)
	predictions = response_scoring.json()
	predict = predictions['predictions'][0]['values'][0][0]
	print("Final prediction :",predict)
	return render_template('predict.html',predict=predict)


if __name__ == "__main__":
    app.run(debug=True)
