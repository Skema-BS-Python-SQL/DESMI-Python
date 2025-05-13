#Single quotes and double quotes function identically
num = "10" 
printer = "HP"
print("I just printed %s pages to the printer %s" % (num, printer))
print("I just printed {0} pages to the printer {1}".format(num, printer))
print("I just printed " + num + " pages to the printer " + printer)
