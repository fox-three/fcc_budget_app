### FreeCodeCamp Budget App Project

`budget.py` consists of a `Category` class that creats objects for helping maintain budgets of different categories (i.e., food, clothing, entertainment, business).

Instances of `Category` have methods that include:

* `deposit()` accepts an `amount` and a `description` of the deposit and appends a deposit object to the instance's ledger list

* `withdraw()` is similar to `deposit` but will not work and will return `False` if the withdraw is unsuccessful

* `get_balance()` is used to return the current balance of the instance's ledger

* `transfer()` is used to transfer an `amount` to another instance of `Category`. It returns `False` if unsuccessful

* `check_funds()` accepts an `amount` to see if the `amount` can be withdrawn/transferred. It returns `False` if not. This method is used to error check `withdraw()` and `transfer()`

Here is an example of the output if an instance is printed:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

`budget.py` also consists of the function `create_spend_chart()` that accepts a list of `Category` instances and prints the percentages of total expenses for each or the objects. Here is an example:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
