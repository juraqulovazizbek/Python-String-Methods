usurname = input("usurname: ")

if usurname.replace('-', '').isalnum():
    print (True)
else:
    print( "usernames faqat a-z, A-Z, 0-9, - dan iborat bo‘lishi kerak")