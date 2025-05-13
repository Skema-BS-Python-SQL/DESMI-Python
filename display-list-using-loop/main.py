# Loops are mostly used to access items in a list in order 
# to manipulate the items. So, in case we want to operate 
# on the items of a list, we can use the for loop to access the items
# and pass them over to be operated on. Say, we want to 
# count the number of letters for each item. 
# We can use the for loop to accomplish that.
# 
def count_letters(l):
    count = {}  # define a dict to hold our count
    for i in l: # loop through the list
        # for each item, compute its length and store it in the dict
        count[i] = len(i)
    return count # return the count
 
if __name__ == '__main__':
    colors = ['red', 'blue', 'green', 'yellow', 'black']
    print(count_letters(colors))

def get_number_of_elements(list):
    pos = 0
    for element in list:
        pos += 1
    return pos

display_str = "Number of elements in the list: "
print(display_str , get_number_of_elements(colors))