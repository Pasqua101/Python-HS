password = input("Enter your new password: ")

numbers = ["0","1","2","3","4","5","6","7","8","9","0"]
caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]

numbercheck = 0
capscheck = 0

for n in password:
    if n in numbers:
        numbercheck +=1
    if n in caps:
        capscheck +=1
    if n not in lower and n not in numbers and n not in caps:
        print ("This is an invalid password. You must use speacial charcaters like _")
        exit()