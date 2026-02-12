def analyze_list(lst):
	n = len(lst)
	print(f"List: {lst}")
	if n < 5:
		print(f"Result: fewer than 5 elements ({n})")
	elif 5 <= n <= 10:
		print(f"Result: between 5 and 10 elements (inclusive) ({n})")
	else:
		print(f"Result: more than 10 elements ({n})")
	print("---")


# Test cases with various lengths and value types
# A list-of-lists covering each condition:
list_of_tests = [
	[1, 'a', 3.14],           # 3 elements -> fewer than 5
	[1, 2, 3, 4],             # 4 elements -> fewer than 5
	[0, 1, 2, 3, 4],          # 5 elements -> between 5 and 10
	['x'] * 7,                # 7 elements -> between 5 and 10
	list(range(10)),          # 10 elements -> between 5 and 10
	list(range(11)),          # 11 elements -> more than 10
	list(range(15)),          # 15 elements -> more than 10
]

for test_case in list_of_tests:
	analyze_list(test_case)

