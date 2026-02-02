#Create the list of responses from Exercise 2 (values 5, 7, 3, 8). Next add the response “0” to the end of the list using the .append() method. Next add the response “6” to the list between the values 7 and 3 (in what will be the third position in the list) using the .insert() method. Print out the list to verify that you made the changes 
#correctly.
#Name: Paul Bagara
#Date: February 2, 2026
responses = [5, 7, 3, 8]
responses.append(0)
responses.insert(2, 6)
print(responses)

# Alternative: do the same using list slicing and the + operator (no .insert)
responses2 = [5, 7, 3, 8]
responses2 = responses2[:2] + [6] + responses2[2:]
responses2.append(0)
print(responses2)

# Explanation of '+':
# - For lists, '+' concatenates two lists, producing a new list (it does not modify in-place).
#   Example: [1, 2] + [3] -> [1, 2, 3]
# - For strings, '+' concatenates strings ("a" + "b" -> "ab").
# - For numbers, '+' performs numeric addition (1 + 2 -> 3).
# Note: because list '+' creates a new list, using it repeatedly can allocate extra memory;
# for in-place insertion, methods like .insert() or slicing assignment can be preferable.

