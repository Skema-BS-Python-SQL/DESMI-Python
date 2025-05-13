age = int(input("Enter your age: "))

answer = "You are a minor."

if age > 18:
  answer = "You are an adult."
elif age == 18:
  answer = "happy birthday !"
  
print(answer)
