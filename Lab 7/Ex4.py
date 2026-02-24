recent_purchae=[36.13,23.07,103.35,22.93,11.62]

budget = 150
total_spent = 0

for purchase in recent_purchae:
    total_spent += purchase 
if total_spent > budget:
    print("This purchase is over budget", purchase)
else:       print("This purchase is within budget", purchase)



#On your own
def check_budget (purchase,limit):
    if purchase > limit:
        print("This purchase is over budget", purchase)
    else:       print("This purchase is within budget", purchase)

print(check_budget(200, 150))   # Expected: Over budget
print(check_budget(100, 150))   # Expected: Within budget
print(check_budget(150, 150))   # Expected: Within budget
print(check_budget(0, 150))     # Expected: Within budget
print(check_budget(1000, 500))  # Expected: Over budget