string_input = '''GeeksforGeeks is a Computer Science portal for geeks.
  It contains well written, well thought and well explained
  computer science and programming articles, quizzes etc.'''


words = string_input.split()


dictionary = {}

for word in words:


  if (word[0] not in dictionary.keys()):

    dictionary[word[0]] = []
    dictionary[word[0]].append(word)

  else:

    if (word not in dictionary[word[0]]):
      dictionary[word[0]].append(word)


print(dictionary)
