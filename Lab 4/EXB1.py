url=input("Enter a full URL")
cleaned_url=url.replace("http://","").replace("https://","").replace("www.","")

printt ("cleaned URL is: " + cleaned_url)


parts=cleaned_url.split(".")

domain=parts[0]
print("Domain name is: " + domain)


#We might get a trailing / character, so we need to remove it.
TLD=parts[2]
print("Top level domain is: " + TLD)
TLD_clean=TLD.split("/")
TLD_clean=TLD.replace("/","")
print("Cleaned TLD is: " + TLD_clean[0])
