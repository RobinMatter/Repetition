from typing import Dict, Any

from DataStore import DataStore
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def welcome_user():
    return "Welcome to your budget_tracker: track your personal finance for your financial success"


income = DataStore()
#income.add_income_to_account_balance("salary", 2)
#income.add_income_to_account_balance("salary", 9)
#income.add_income_to_account_balance("rent", 8)


@app.route('/incomes', methods=['GET'])
def get_posted_incomes_of_account_balance():
    return jsonify(income.get_account_balance_data())


@app.route('/incomes', methods=['POST'])
def add_posted_income_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    income.add_income_to_account_balance(key, value)
    return '', 204