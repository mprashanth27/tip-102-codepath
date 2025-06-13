'''
U:
i/p= ticket_sales: dict
o/p= total_sales: int

#edge cases
1. non-int val in ticket_sales dict
2. empty ticket_sales dict {}

P:
return sum(dict.values)
'''
def total_sales(ticket_sales):
    return sum(ticket_sales.values())

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))