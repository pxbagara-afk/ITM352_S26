def is_leap(year):
	"""Return True if year is a leap year.

	Uses the grouped form (A and B) or C where:
	  A = year % 4 == 0
	  B = year % 100 != 0
	  C = year % 400 == 0

	Parentheses are required: `(A and B) or C` mirrors the flow-chart.
	"""
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def find_closest_leap(year):
	"""Return the closest leap year to `year` (search up to 4 years each way)."""
	if is_leap(year):
		return year
	for d in range(1, 5):
		if is_leap(year - d):
			return year - d
		if is_leap(year + d):
			return year + d
	return None


if __name__ == "__main__":
	# Change this to your birth year for quick testing
	birth = 2005

	if is_leap(birth):
		# per instruction, if birth is leap, also test birth+1 as a non-leap
		tests = [birth, birth + 1]
	else:
		closest = find_closest_leap(birth)
		tests = [birth, closest]

	for y in tests:
		# boolean check
		print(f"{y}: leap -> {is_leap(y)}")
		# string-returning function using if-statements
		print(f"{y}: isLeapYear -> {isLeapYear(y)}")


def isLeapYear(year):
	"""Return 'Leap year' or 'Not a leap year' using if-statements.

	Implementation details:
	  - check divisible by 400 first -> leap
	  - then divisible by 100 -> not leap
	  - then divisible by 4 -> leap
	  - otherwise not leap

	Uses early returns for clarity and to avoid nested ifs.
	"""
	if year % 400 == 0:
		return "Leap year"
	if year % 100 == 0:
		return "Not a leap year"
	if year % 4 == 0:
		return "Leap year"
	return "Not a leap year"


