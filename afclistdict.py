list1=["Harry potter","Wimpy kid","Percy Jackson","Matilda"]
print(list1)
list1.append("Book2")
print("Added: ", list1)
list1.remove("Book2")
print("Removed: ",list1)
list1.sort()
print("Sorted: ",list1)
list1.reverse()
print("Reversed: ",list1)
print("Indexed Matilda: ",list1.index("Matilda"))
print("Sliced: ",list1[:2])
lib={"name":"Mr Librarian","subject":"books","experience":5}
print("Name: ",lib["name"])
lib.pop("experience")
lib["Library"]="Super library"
print("Final: ",lib)
conv=list(zip(lib))
print("ABSOLUTE FINAL: ",conv)
