import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://odmyqxza:QBXiWB5oehN0PzjCAYU2-Ucj1WW36i7f@salt.db.elephantsql.com:5432/odmyqxza")

app = Flask(__name__)
@app.route("/")
def welcome():
    """List all available api routes."""
    return "/api/v1.0/"

# first der.
@app.route("/balance")
def balance():
    print("Session created")
    """display balance sheet"""
    results = pd.read_sql("select * from balance_sheet", engine)
    return jsonify(results.to_dict(orient="records"))
  
@app.route("/income")
def income():
    print("Session created")
    """display income statement"""
    results_1 = pd.read_sql("select * from income_statement", engine)
    return jsonify(results_1.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)