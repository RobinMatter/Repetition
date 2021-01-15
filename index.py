from typing import Dict, Any

from DataStore import DataStore
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to your budget_tracker: track your personal finance for your financial success"


income = DataStore()
income.add_income_to_account_balance("salary", 2)
income.add_income_to_account_balance("salary", 6)
income.add_income_to_account_balance("flat", 800)


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


expense = DataStore()
expense.add_expense_to_account_balance("flat", 200)
expense.add_expense_to_account_balance("food", 6)


@app.route('/expenses')
def get_posted_expense_of_account_balance():
    return jsonify(expense.get_account_balance_data())


@app.route('/expenses', methods=['POST'])
def add_posted_expense_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    expense.add_expense_to_account_balance(key, value)

    return '', 204


ROI = DataStore()
ROI.add_ROI_to_account_balance("flat", 2000)
ROI.add_ROI_to_account_balance("flat", 100000)


@app.route('/ROI')
def get_posted_ROI_of_account_balance():
    return jsonify(ROI.get_account_balance_data())


@app.route('/ROI', methods=['POST'])
def add_posted_ROI_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    ROI.add_ROI_to_account_balance(key, value)

    return '', 204


asset_value = DataStore()
asset_value.add_value_to_account_balance("gold", 1500)
asset_value.add_value_to_account_balance("gold", 1.2)


@app.route('/value')
def get_posted_value_of_account_balance():
    return jsonify(asset_value.get_account_balance_data())


@app.route('/value', methods=['POST'])
def add_posted_value_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    asset_value.add_value_to_account_balance(key, value)

    return '', 204



spread_sheet = DataStore
list_spread_sheet = income.get_account_balance_data() + expense.get_account_balance_data()


@app.route('/spread-sheet')
def get_spread_sheet():
    dictionary = {}
    for element in list_spread_sheet:
        key = list(element)[0]
        if key in dictionary:
            dictionary[key] += element[key]
        else:
            dictionary[key] = element[key]
    return jsonify(dictionary)
    #spread_sheet.append({key: dictionary[key]})
    #spread_sheet.make_spread_sheet(list_spread_sheet)