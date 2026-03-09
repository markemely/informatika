pages = 100
lines = 50
symbols = 25
symbolweight = 4
disk = 1.44
book = (pages * lines * symbols * symbolweight) / 1024
content = (disk * 1024) // book
content = int(content)
print("Количество книг, помещающихся на дискету:", content)
