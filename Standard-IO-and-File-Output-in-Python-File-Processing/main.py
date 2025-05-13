with open("names.txt", "r") as infile:
    names = infile.readlines()

names = [name.strip() for name in names]
names.sort(key=lambda name: name.split()[0])  # Sort by first name

with open("output_by_firstname.txt", "w") as outfile:
    for name in names:
        outfile.write(name + "\n")

print("Names sorted by first name and saved to output_by_firstname.txt!")
