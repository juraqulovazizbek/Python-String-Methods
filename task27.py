fayl = input("fayl name: ")

if fayl.lower().endswith((".pdf" , ".docx" , ".text")):
    print (True)
else:
    print(False)