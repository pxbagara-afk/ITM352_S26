#Parse through the protions of an email address

#Method 1: Using split() to separate usner and domain

email=input("Enter your email address: ")
parts=email.split("@")
username=parts[0]
domain=parts[1]

print("Username is: " + username)
print("Domain is: " + domain)

#Method 2 (Using index() and slicing
at_symbol_index=email.index("@")
username_manual=email[:at_symbol_index]
domain_manual=email[at_symbol_index+1:]

print("Username is: " + username_manual)
print("Domain is: " + domain_manual)