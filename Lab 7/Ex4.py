recent_purchases = [36.13, 23.07, 103.35, 22.93, 11.62]

def check_budget(purchase, limit):
    """Return a message indicating whether a single purchase is over the limit.

    Args:
        purchase (float): the purchase amount
        limit (float): the budget limit to compare against

    Returns:
        str: message "This purchase is over budget!" if purchase > limit,
             otherwise "This purchase is within budget"
    """
    if purchase > limit:
        return "This purchase is over budget!"
    else:
        return "This purchase is within budget"


if __name__ == '__main__':
    # example usage: iterate the recent purchases and print a message per purchase
    budget = 50
    total_spent = 0
    for purchase in recent_purchases:
        total_spent += purchase
        msg = check_budget(purchase, budget)
        print(msg, purchase)

    # also show total spent vs the same budget
    if total_spent > budget:
        print("Total spent is over budget!", total_spent)
    else:
        print("Total spent is within budget", total_spent)