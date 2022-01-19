name = raw_input("Please enter the name of your file: ")
file_name = raw_input("Was your doc written on Word, Excel, Power Point, Publisher or Access? ")

if file_name == 'Word':
    print "Your file will be called",name,".doc"
elif file_name == 'Excel':
    print "Your file will be called",name,".xcl"
elif file_name == 'Power Point':
    print "Your file will be called",name,".ppt"
elif file_name == 'Publisher':
    print "Your file will be called",name,".pub"
elif file_name == 'Access':
    print "Your file will be called",name,".accdb"
else:
    print"I'm sorry, I don't know that program name"
    