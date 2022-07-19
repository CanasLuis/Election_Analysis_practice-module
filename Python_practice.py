counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso iis not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties.")



x = 0
while x <= 5:
    print(x)
    x= x + 1

for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)


for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for key,value in dictionary_name.items()
    print(key,value)


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my votes / total_votes ) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
