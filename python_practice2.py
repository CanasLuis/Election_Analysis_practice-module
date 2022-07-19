# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election?" ))
# print(f"I received {my_votes / total_votes * 100}% of the total votoes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters .")