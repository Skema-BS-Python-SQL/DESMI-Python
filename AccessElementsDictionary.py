# Both methods will work the same, but the former 
# will return a KeyError while the latter returns None 
# if the element is not available. 

dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}

#print(dict)

print(dict['Student Name']) # Berry
print(dict['Roll No.'])     # 12
print(dict['Subject'])      # English

# Append Elements to Dictionary
#dict_append = {"lang2" : "Python", "lang3" : "Java"}

#dict_append["lang1"] = "CSharp"
#print(dict_append)

#dict_append["waoo"] = "C++"

#print(dict_append)
#print(dict_append['waoo'])

#Update Method to Append Elements
#dict_append.update({"4" : "JavaScript"})
#print(dict_append)
# now {‘1': 'Python', '3': 'CSharp', '2': 'Java', '4': 'JavaScript'}

#Use Assignment
#dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
#  The student who left: Berry
#print("The student who left:", dict.get('Student Name')) 
                                        
#dict['Student Name'] = 'Larry'
#print("The student who replaced: [Update]", dict.get('Student Name')) # The student who replaced: [Update] Larry
#dict['Student Name'] = 'Jarry'
#print("The student who joined: [Addition]", dict.get('Student Name’)) # The student who joined: [Addition] Jarry

# Remove Elements from Dictionary
#sixMonths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}
#print(sixMonths)
#sixMonths.pop(1) # delete 30
#print(sixMonths)

#Carstest = {'Car':'Chevrolet Chevelle Malibu','MPG': 18.0 }
#use key to call the variable
#print(Carstest['Car'])
#print(Carstest['MPG'])
