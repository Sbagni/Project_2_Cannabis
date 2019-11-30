import os
import pandas as pd
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from sqlalchemy import create_engine
import json

basedir = os.path.abspath(os.path.dirname(__file__))


engine = create_engine("postgresql://odmyqxza:QBXiWB5oehN0PzjCAYU2-Ucj1WW36i7f@salt.db.elephantsql.com:5432/odmyqxza")

app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    # return "/api/v1.0/"
    bs_results = pd.read_sql("select * from balance_sheet", engine)
    bs_results.assets = bs_results.current_assets + bs_results.noncurrent_assets
    bs_data = bs_results.to_dict(orient="records")
    return render_template(os.path.join('home.html'), bs_data=bs_data)

@app.route('/<ticker>')
def company_page(ticker):
    bs_results = pd.read_sql("select * from balance_sheet", engine)
    bs_data = jsonify(bs_results.to_dict(orient="records"))
    is_results = pd.read_sql("select * from income_statement", engine)
    is_data = jsonify(is_results.to_dict(orient="records"))
    return render_template(os.path.join(ticker+'.html'), bs_data=bs_data, is_data=is_data, ticker=ticker)

# @app.route('/test/<ticker>')
# def raw_data(ticker):
#     bs_results = pd.read_sql("select * from balance_sheet", engine)
#     bs_data = jsonify(bs_results.to_dict(orient="records"))
#     is_results = pd.read_sql("select * from income_statement", engine)
#     is_data = jsonify(is_results.to_dict(orient="records"))
#     return jsonify([bs_data, is_data])

@app.route('/team')
def team_page():
    return render_template(os.path.join('team.html'))


# first der.
@app.route("/balance")
def balance():
    print("Session created")
    """display balance sheet"""
    bs_results = pd.read_sql("select * from balance_sheet", engine)
    bs_data = jsonify(bs_results.to_dict(orient="split"))
    return bs_data
  
@app.route("/income")
def income():
    print("Session created")
    """display income statement"""
    is_results = pd.read_sql("select * from income_statement", engine)
    # is_tickers = list(is_results.ticker)
    is_data = jsonify(is_results.to_dict(orient="records"))
    return is_data

@app.route("/test")
def test():
    # data = jsonify(pd.read_sql("SELECT ticker FROM income_statement", engine).to_dict(orient="records"))
    is_results = pd.read_sql("SELECT * FROM income_statement", engine)
    tickers = is_results.ticker
    dates = is_results.date
    sales = is_results.sales
    cogs = is_results.cogs
    sga = is_results.sga
    # tickers = pd.read_sql("SELECT ticker FROM income_statement", engine)
    return render_template(os.path.join("test1.html"), tickers=tickers, dates=dates, sales=sales, cogs=cogs, sga=sga)

@app.route("/test/<ticker>")
def testTicker(ticker):
    is_df = pd.read_sql("SELECT * FROM income_statement", engine)
    filtered_is_df = is_df.loc[is_df.ticker==ticker]
    is_tickers = filtered_is_df.ticker
    is_dates = filtered_is_df.date
    is_sales = filtered_is_df.sales
    is_cogs = filtered_is_df.cogs
    is_sga = filtered_is_df.sga

    bs_df = pd.read_sql("select * from balance_sheet", engine)
    # bs_df.total_assets = bs_df.current_assets + bs_df.noncurrent_assets
    # bs_df.total_liabilities = bs_df.current_liabilities + bs_df.noncurrent_liabilities
    filtered_bs_df = bs_df.loc[bs_df.ticker==ticker]
    bs_tickers = filtered_bs_df.ticker
    bs_dates = filtered_bs_df.date
    # bs_total_assets = filtered_bs_df.total_assets
    # bs_total_liabilities = filtered_bs_df.total_liabilities
    bs_equity = filtered_bs_df.equity
    bs_goodwill = filtered_bs_df.goodwill
    bs_ev = filtered_bs_df.ev
    bs_inventory = filtered_bs_df.inventory
    return render_template(os.path.join("test1.html"), is_tickers=is_tickers,
                                                       is_dates=is_dates,
                                                       is_sales=is_sales,
                                                       is_cogs=is_cogs,
                                                       is_sga=is_sga, 
                                                       bs_tickers=bs_tickers,
                                                       bs_dates=bs_dates,
                                                    #    bs_total_assets=bs_total_assets,
                                                    #    bs_total_liabilities=bs_total_liabilities,
                                                       bs_equity=bs_equity,
                                                       bs_goodwill=bs_goodwill,
                                                       bs_ev=bs_ev,
                                                       bs_inventory=bs_inventory)

if __name__ == '__main__':
    app.run(debug=True)