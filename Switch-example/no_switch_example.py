def switch(lang):
  lang = lang.lower()
  print(lang)
  if lang == "javascript":
      return "You can become a web developer."
  elif lang == "php":
      return "You can become a backend developer."
  elif lang == "python":
      return "You can become a Data Scientist"
  elif lang == "solidity":
      return "You can become a Blockchain developer."
  elif lang == "java":
      return "You can become a mobile app developer"
  else:
      return "The language doesn't matter, what matters is solving problems."