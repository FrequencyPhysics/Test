#25/07/2021

# Program to Remove duplicates from a list

mylist = ["a", "a", "d", "f", "f","e","r","r","e","a"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
