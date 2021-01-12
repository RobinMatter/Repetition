from typing import Dict, Any

from DataStore import DataStore
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to your budget_tracker: track your personal finance for your financial success"


income = DataStore()
income.add_two_values_together("result1", 2, 3)
income.add_two_values_together("result2", 6, 5)
income.add_two_values_together("result1", 8, 5)


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
expense.subtract_first_value_with_second_value("result1", 8, 3)
expense.subtract_first_value_with_second_value("result2", 6, 20)


@app.route('/expenses')
def get_posted_expense_to_account_balance():
    return jsonify(expense.get_account_balance_data())


@app.route('/expenses', methods=['POST'])
def add_posted_expense_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    expense.add_expense_to_account_balance(key, value)

    return '', 204


asset_value = DataStore()
asset_value.add_values_for_ROI("result1", 9, 3)
asset_value.add_values_for_ROI("result2", 8, 2)


@app.route('/ROI')
def get_posted_ROI_to_account_balance():
    return jsonify(asset_value.get_account_balance_data())


@app.route('/ROI', methods=['POST'])
def add_posted_ROI_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    asset_value.add_ROI_to_account_balance(key, value)


    return '', 204


asset_value = DataStore()
asset_value.add_values_to_estimate_asset_value_to_account_balance("result1", 8, 3)
asset_value.add_values_to_estimate_asset_value_to_account_balance("result2", 6, 5)


@app.route('/value')
def get_posted_value_to_account_balance():
    return jsonify(asset_value.get_account_balance_data())


@app.route('/value', methods=['POST'])
def add_posted_value_to_account_balance():
    element = request.get_json()
    key = list(element)[0]
    value = element[key]

    asset_value.add_value_to_account_balance(key, value)

    return '', 204



#
# list_main = income.get_account_balance_data() + expense.get_account_balance_data()
#
# income.add_two_values_together("result2", 6, 5)
# income.add_two_values_together("result1", 8, 5)
#
#
# # list_main = bank_data + post_data
# @app.route('/spread-sheet')
# def get_main():
#     global key, element
#     dic: Dict[Any, Any] = {}
#     for element in list_main:
#             key = list(element)[0]
#         if key not in dic:
#             dic[key] = element[key]
#         else:
#             dic[key] = dic[key] + element[key]
#     return jsonify(dic)