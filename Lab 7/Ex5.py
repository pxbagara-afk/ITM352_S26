celbs = ("Taylor Swift", "Lionel Messi", "The weeknd", "Keanu Reeves", "Angelina Jolie")
ages=  (36,38,36,61,50)

celbes_list = []
ages_list = []

for celeb in celbs:
    celbes_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"celebrities": celbes_list, "ages": ages_list}   
print(celebs_dict)