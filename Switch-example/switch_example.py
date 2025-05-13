'''
Following code only work in python 3.10
'''
def switch(lang):
  lang = lang.lower()
  match lang:
      case "javascript":
          return "You can become a web developer."
      case "python":
          return "You can become a Data Scientist"
      case "php":
          return "You can become a backend developer"
      case "solidity":
          return "You can become a Blockchain developer"
      case "java":
          return "You can become a mobile app developer"
      case _:
          return "The language doesn't matter, what matters is solving problems."