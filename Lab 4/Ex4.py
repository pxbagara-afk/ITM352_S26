# Exercise 4 of Lab 4
# Name: Paul Bagara
# Date: February 2, 2026
# Create the tuple of respondent IDs and attempt to append to it.
respondent_ids = (1012, 1035, 1021, 1053)
print("Original tuple:", respondent_ids)

respondent_ids.append(1011)
print(respondent_ids)


# Correction: use concatenation with a one-element tuple (note the trailing comma):
respondent_ids = respondent_ids + (1011,)
print( respondent_ids)

