print("Перша константа", None)
a1 = 2
print(a1.__eq__(2))
print("a1 equale {a}".format(a=a1))

a1 = 3
a2 = 6
if a1 == a2:
    print("{}={}".format(a1,a2))
elif a1 > a2:
    print("{}>{}".format(a1,a2))
else:
    print("{}<{}".format(a1,a2))
a = [9,8,7,6,5,4,3,2,1,0]
for i in a:
    print(-i)


try:
    print("Що буде якщо (list(a)*(-1))", -a, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")


with open("new_file.md", "w") as f:
    f.write("ljdasdjaslkdjsal")


a3 = lambda x: x**2-1
print(a3(4))
