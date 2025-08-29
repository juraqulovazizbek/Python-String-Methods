matn = input("matn: ")
uzunlik = int(input("uzunlik: "))

result = matn.rjust(uzunlik, "0")
print(result)
