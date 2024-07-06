"""add=lambda x,y:x+y
print(add(9,8))

# i am going to print patterns
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
print("\n")

student = {
    "marks":89,
    "age":15
}
print(student["marks"])"""
list = [12,4,5,7,86]
evens = []
for i in list:
    if i%2==0:
        evens.append(i)
print (evens)       