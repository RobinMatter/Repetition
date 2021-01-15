## Budget Tracker
### Table of contents
1. [ Introduction. ](#intro)
2. [ How to install. ](#install)
3. [ How to start it. ](#start)
4. [ How to use it. ](#use)
5. [ Technologies used. ](#tec)


<a name="intro"></a>
### 1. Introduction
This program gives you a broad overview of your finances. The program generates 5 webpages telling you different things about your financial situation. One shows all your different expenses and their amount, another shows you all your different incomes and also their amount. Then there is a webpage called main, where you can see the difference between your incomes and expenses listed by their category. For example, it shows you how much your rental property brings you in. Another webpage can be used to calculate a return on your investments. The fifth webpage multiply and can be used to calculate your assets values. To all these webpages you can send an input to add a new income, expense, or when you want to calculate an ROI (return on investment) or need to calculate the value of your assets.
This program was written during an internship at TimeElement to repeat the things I’ve learned in the first 2 months.

<a name="install"></a>
### 2. How to install
Create directory budget_tracker and change in to it. Then copy command below into your terminal.
```bash
git pull https://github.com/RobinMatter/budget_tracker.git
```

<a name="start"></a>
### 3. How to start it
The program is started by running the bootstrap.sh file.
``` bash
./bootstrap.sh
``` 
In the terminal, you find this link http://0.0.0.0:5000/. Open this link and you can use the program on there. If http://0.0.0.0:5000/ is already used on your computer you need to change it in the bootstrap.sh source code. Under this text, you can see the source code from bootstrap.sh. 
```bash
#!/bin/bash

export FLASK_APP=index.py
export FLASK_ENV=development
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
```

<a name="use"></a>
### 4. How to use it
On the first webpage, you will be welcomed by the budget tracker. When you change the URL to `/incomes` you can see all your given incomes under their categories. The same is true under `/expenses` just for the expenses. Under `/value` and `/ROI` you can look up the value or the ROI of an asset. So that the program can show you your financial situation, you first need to give it the right information’s for the program understandable way. It is not thought to list assets like currencies as an income or in spread-sheet. You just give the program the information about the gains or losses an asset made.
#### /incomes
To give the program a new income you post it as an input into the terminal. This should look like this: Attention that everything is customized right to your example. You print the name of the income source at the space wherein the example the salary is placed. Where the 5500 is written you print in your earned money. At the end of the post, it is written `/incomes` for adding an income you use this ending. Change it for posting to other webpages like `/expenses`.
```bash
curl -X POST -H "Content-Type: application/json" -d '{ "salary": 5500 }' http://localhost:5000/incomes
```
#### /expenses
It works the same as `/incomes` just that you post your expenses and not your incomes.
Here an example:
 ```bash
curl -X POST -H "Content-Type: application/json" -d '{ "car": 120}' http://localhost:5000/expenses
```

#### /value
For using ‘/value` you need to look up if the category you want to get the value of is already listed under `/value`. If it is so, your next input will be multiplied with the listed value. Because of that you should give de percentage increase or decrease as a number. For example “1.2” for a 20% price increase. 
```bash
curl -X POST -H "Content-Type: application/json" -d '{ "Tesla Stock": 1.2}' http://localhost:5000/value
```
But if the category does not already exist, it must be added first with an input. In this input, you put the value the asset had before the price change. After you have done this you can post increase or decrease as I described above.
```bash
curl -X POST -H "Content-Type: application/json" -d '{ "Tesla Stock": 880}' http://localhost:5000/value
```
#### /ROI
The “ROI” stands for return on investment and can be calculated by dividing the income after the expenses with the invested capital.
%
To use this feature make an input, in which you give a new category and as a number you give (income generated of the asset) – (expenses which the asset produce).
Then you do a second input where you use the same category as before, but as a number, you give the invested Money.
To clarify things I make an example:
The cash flow (money coming in after expenses) in a year of a flat in Zürich is 4800 and you would pay a down payment of 70’000. The result the program gives will be 0.068 so you get 6.8% of your down payment. Shure, you also need to see that the bank loan is not too high.
```bash
curl -X POST -H "Content-Type: application/json" -d '{ "flat, Zürich, Höngenberg": 4800}' http://localhost:5000/value
```
```bash
curl -X POST -H "Content-Type: application/json" -d '{ "flat, Zürich, Höngenberg": 70000}' http://localhost:5000/value
```



Lookup the results generated with these operators under the different categories. When you switch to calculator/spread-sheet you can see your different categories from calculator/incomes and calculator/expenses. If there is the same category in incomes as in expenses they will be calculated into one. The result is your profit or your loss from something.
To post something on these pages use this command customized to your problem.

```bash
curl -X POST -H "Content-Type: application/json" -d '{ "name": Betrag.0 }' http://localhost:5000/calculator/?
```


<a name="tec"></a>
### 5. Technologies used
python 3.81
pip3
pipenv
flask

#### Install python 3.81
Linux, Mac:
`sudo apt-get install python3.81`
Windows:

Further information about python3.8:
https://docs.python.org/3/whatsnew/3.8.html

#### Install pip3
Linux, Mac:
`sudo apt-get install python3-pip3`
Windows:
`Python get-pip3.py`

Further information about pip:
https://realpython.com/what-is-pip/

#### Install pipenv
`pip install pipenv`

Further information about pipenv:
https://realpython.com/pipenv-guide/


#### Install flask
`pip3 install flask`

Further information about flask:
https://palletsprojects.com/p/flask/