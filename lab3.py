def cipher(inputText, password, n, d):
    inputText = inputText[::-1]
    password = password[::-1] 
    str1 = ""
    str2 = ""
    
    for i in inputText:
        if i.isspace():
            str1 += " "
        elif int(d) == 1: #if positive d
            str1 += (chr(ord(i)+int(n)))
        else: #if negative d
            str1 += (chr(ord(i)-int(n)))
            
    for x in password:
        if x.isspace():
            str2 += " "
        elif int(d) == 1: # if positive
            str2 += (chr(ord(x)+int(n)))
        else: #if negative d
            str2 += (chr(ord(x)-int(n)))
        password = password[::-1] #original password
        inputText = inputText[::-1] #originaluserID
        print("encrypted userid: " + str1)
        print("encrypted password: " + str2)
        print("original userid: " + str(inputText))
        print("original password: " + password)
        
def testCustomEncrypt():
    inputText = input("Enter user ID as text: ")
    password = input("Enter password as text: ")
    n = input("Enter value of n: ")
    d = input("Enter value of d: ")
    return cipher(inputText, password, n, d)

if __name__=="__main__": 
    testCustomEncrypt()