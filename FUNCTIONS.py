#VOID FUNCTIONS
def full_name(name, surname):
    print(f"{name} {surname}")
result1 = full_name("Pule", "Thekiso")
result2 = full_name("Lungile", "Saliwe")

#CHECK IF THE NUMBER IS EVEN(FRUITFUL)
def is_even(number):
    return number % 2 == 0
result3 = is_even(2)
result4 = is_even(4)
print(result3)
print(result4)
fruits = ["banana", "apple"]
fruits.copy()
print(fruits)
#POP
#VOID FUNCTIONS
def full_name(name, surname):
    print(f"{name}{surname}")
result1 = full_name("Pule", "Thekiso")
result2 = full_name("Lungile", "Saliwe")
print(result1)
print(result2)
#POP
names = ["Pule", "Thekiso", "Sabata"]
names.pop(1)
print(names)
#REVERSE
order = ["Pule", "Thekiso", "Sabata"]
order.reverse()
print(order)
#GET METHOD
get_method = {"Name": "Victor"}
x = get_method.get("Name")
print(x)
