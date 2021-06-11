class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for event in self.ledger:
            description = event["description"][0:23].ljust(23)
            amount = "{:.2f}".format((event["amount"]))[0:7].rjust(7)
            output += f"{description}{amount}\n"
        output += f"Total: {self.balance}"
        return output

    def deposit(self, amount, description):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        if amount <= self.balance:
            return True


def create_spend_chart(categories):
    total_spent = 0
    spend_dict = {}
    for cat in categories:
        for event in cat.ledger:
            if event["amount"] < 0:
                if cat.name not in spend_dict.keys():
                    spend_dict[cat.name] = abs(event["amount"])
                else:
                    spend_dict[cat.name] += abs(event["amount"])
                total_spent += abs(event["amount"])
    percentage_dict = {key: (value / total_spent) * 100 for key, value in spend_dict.items()}
    chart_cols = len(percentage_dict.keys())
    chart = "Percentage spent by category\n"
    current_chart_row = 100
    while current_chart_row >= 0:
        row = str(current_chart_row).rjust(3) + "|"
        for cat in percentage_dict.keys():
            if percentage_dict[cat] >= current_chart_row - 5:
                row += " o "
            else:
                row += "   "
        row += " \n"
        chart += row
        current_chart_row -= 10
    longest_cat_name = 0
    for cat in percentage_dict.keys():
        if len(cat) > longest_cat_name: longest_cat_name = len(cat)
    chart += "    " + "---" * len(percentage_dict.keys()) + "-" +"\n"
    for i in range(longest_cat_name):
        row = "    "
        for cat in percentage_dict.keys():
            try:
                row += f" {cat[i]} "
            except:
                row += "   "
        row += " \n"
        chart += row
    return chart
