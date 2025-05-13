with open("names.txt", "r") as infile:
    names = infile.readlines()

names = [name.strip().title() for name in names]
names.sort(key=lambda name: name.split()[1])  # Sort by last name

with open("output_by_lastname.txt", "w") as outfile:
    for name in names:
        outfile.write(name + "\n")

print("Names capitalized and sorted by last name. Saved to output_by_lastname.txt!")