def is_even(num):
  return num % 2 == 0

def is_zero(num):
  return num == 0

def custom_message(num):
  if is_zero(num):
      return "The number is zero."
  elif is_even(num):
      return "The number is even."
  else:
      return "The number is odd."

number = 3
print(custom_message(number))
# The number is odd.


# 
def is_positive(num):
  return num > 0

def is_negative(num):
  return num < 0

def detailed_message(num):
  if is_zero(num):
      return "The number is zero."
  elif is_positive(num):
      return "The number is positive."
  elif is_negative(num):
      return "The number is negative."
  elif is_even(num):
      return "The number is even."
  else:
      return "The number is odd."

number = -4
print(detailed_message(number))
# The number is negative.