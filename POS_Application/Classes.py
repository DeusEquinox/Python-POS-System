class tables:
    def __init__(self, tableNo):
        self.tableNo = int(tableNo)
        self.waiter = "None"
        self.assignment = "unassigned"
        self.customers = 0
        self.order = []
        self.billPrepared = False

    def assign(self, username):
        self.waiter = username
        self.assignment = "assigned"

    def unassign(self):
        self.waiter = "None"
        self.assignment = "unassigned"
        self.customers = 0
        self.order = []
        self.billPrepared = False

    def add_customers(self, amount):
        self.customers = int(amount)

    def add_order(self, item, quantity, price):
        order = [item, quantity, price]
        self.order.append(order)

    def calc_total(self):
        total = 0
        for order in self.order:
            quantity = order[1]
            price = order[2]
            total += price * quantity
        self.billPrepared = True
        return total


table1 = tables(1)
table2 = tables(2)
table3 = tables(3)
table4 = tables(4)
table5 = tables(5)
table6 = tables(6)

tableList = [table1, table2, table3, table4, table5, table6]
