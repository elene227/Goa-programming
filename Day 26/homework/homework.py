# i already did everything in my classwork btw

names = ["giorgi", "ana", "nika", "marii", "elene"]
names.insert(4, "david")  # adding davit in the fourth index ofc
print(names) #displaying it on the screen


items = [10, 20, 30, 40, 50]
items.pop(0)  # ამოიღებს პირველი ელემენტს (10)
items.pop()   # ამოიღებს ბოლო ელემენტს (50)
print(items)




elements = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
index = int(input("ENTER A NUMBER (0-9): "))
removed_element = elements.pop(index)  # Removes element at the specified index (cuz thats what pop does duhh)
print(str(removed_element))
print(elements)

# hahahha finally 


name = input("enter your name: ")
if len(name) > 5:
    print("Hello")
else:
    print("Bye")
