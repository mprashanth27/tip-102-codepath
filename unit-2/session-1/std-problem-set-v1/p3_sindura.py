#U:
# input: dict
#output: sum of values (total number of tickets)

#edge cases:
#empty dict


def total_sales(ticket_sales):
    return sum(ticket_sales.values())


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))