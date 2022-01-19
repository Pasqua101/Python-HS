name = raw_input("User please enter your name")
space = name.find(' ')
firstname = name[0:space]
lastname = name[space:-1]
print lastname+name[-1],",", firstname