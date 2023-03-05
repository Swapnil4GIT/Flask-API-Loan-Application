import pickle
import flask

from flask import Flask, request

app = Flask(__name__)

#loading the ML model
model_pickle = open("./classifier.pkl","rb")
clf = pickle.load(model_pickle)

@app.route("/ping", methods=["GET"])
def ping():
    return {
        "message": "Pinging the model successful!!"
}

@app.route("/predict", methods=["POST"])
def predictions():
    loan_req = request.get_json()

    if loan_req["Gender"] == "Male":
        gender = 0
    else:
        gender = 1

    if loan_req["Married"] == "Unmarried":
        marital_status = 0
    else:
        marital_status = 1

    if loan_req["Credit_History"] == "Uncleared Debts":
        credit_history = 0
    else:
        credit_history = 1

    applicant_income = loan_req["ApplicantIncome"]
    loan_amt = loan_req["LoanAmount"]/1000