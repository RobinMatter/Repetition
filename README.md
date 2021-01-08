## Budget Tracker
### Introduction
This program gives you a good overview of your finances. You can give the program an input which includes an income or expense from you. The program will calculate
it together with other incomes or expenses in the same category. The program shows you all your expenses and incomes in two
different files and under another incomes and expenses from the same category are combined, so you can see the true income
or expenses of a category for example a real estate you are renting.
This program was written during an internship at TimeElement to repeat the things I’ve learned in the first 2 months.

### How to install
Copy this into your terminal
```bash
git clone https://github.com/RobinMatter/budget_tracker.git
```
### How to start it
The program is started by running the bootstrap.sh file.
``` bash
./bootstrap.sh
``` 
In the terminal, you find this link http://0.0.0.0:5000/. Open this link and you can use the program on there.

### How to use it
On the first page, you will be welcomed by the budget tracker. When you change the URL to calculator/income you can see all your given incomes under their categories. The same is true under calculator/expense just for the expenses. Under calculator/multiply and calculator/divide you can look up the results generated with these operators under the different categories. When you switch to calculator/main you can see your different categories from calculator\incomes and calculator\expenses. If there is the same category in incomes as in expanses they will be calculated into one. The result is your profit or your loss from something.
To post something on these pages use this command customized to your problem.

```bash
curl -X POST -H "Content-Type: application/json" -d '{ "name": Betrag.0 }' http://localhost:5000/calculator/?
```



### Technologies used
listed in requirements.txt
