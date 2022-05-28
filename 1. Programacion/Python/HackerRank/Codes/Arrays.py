#n = int(input("Iteractions: "))

x = []
y = [1,2,4,2]

for i in range(len(y)):
    a = (i + 1)* -1
    x.append(y[a])

print(x)
