import os
import pandas as pd
from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))


engine = create_engine(
    "postgresql://odmyqxza:QBXiWB5oehN0PzjCAYU2-Ucj1WW36i7f@salt.db.elephantsql.com:5432/odmyqxza")

app = Flask(__name__)
@app.route("/")
def home():
    """List all available api routes."""
    # return "/api/v1.0/"
    return render_template(os.path.join(basedir, 'templates', 'P3_HOME.html'))



@app.route('/<ticker>')
def company_page(ticker):
    bs_results = pd.read_sql("select * from balance_sheet", engine)
    bs_data = jsonify(bs_results.to_dict(orient="records"))
    is_results = pd.read_sql("select * from income_statement", engine)
    is_data = jsonify(is_results.to_dict(orient="records"))
    return render_template(os.path.join(ticker+'.html'), bs_data=bs_data, is_data=is_data, ticker=ticker)

# @app.route('/test')
# def test_page():
#     bs_results = pd.read_sql("select * from balance_sheet", engine)
#     bs_data = jsonify(bs_results.to_dict(orient="records"))
#     is_results = pd.read_sql("select * from income_statement", engine)
#     is_data = jsonify(is_results.to_dict(orient="records"))
#     return bs_data
#     return is_data
    # return render_template(os.path.join(ticker+'.html'), bs_data=bs_data, is_data=is_data)

# @app.route('/acb')
# def acb():
#     return render_template(os.path.join('templates', 'acb.html'))

# @app.route('/apha')
# def apha():
#     return render_template(os.path.join('templates', 'acb.html'))    

# @app.route('/fire')
#     return render_template(os.path.join('templates', 'fire.html'))

# @app.route('/hexo')
#     return render_template(os.path.join('templates', 'hexo.html'))

# @app.route('/ogi')
#     return render_template(os.path.join('templates', 'ogi.html'))

# @app.route('/oh')
#     return render_template(os.path.join('templates', 'oh.html'))

# @app.route('/ter')
#     return render_template(os.path.join('templates', 'ter.html'))

# @app.route('/weed')
#     return render_template(os.path.join('templates', 'weed.html'))

# @app.route('/wmd')
#     return render_template(os.path.join('templates', 'wmd.html'))


# first der.
# @app.route("/balance")
# def balance():
#     print("Session created")
#     """display balance sheet"""
#     bs_results = pd.read_sql("select * from balance_sheet", engine)
#     bs_data = jsonify(results.to_dict(orient="records"))
  
# @app.route("/income")
# def income():
#     print("Session created")
#     """display income statement"""
#     is_results = pd.read_sql("select * from income_statement", engine)
#     is_data = jsonify(is_results.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)