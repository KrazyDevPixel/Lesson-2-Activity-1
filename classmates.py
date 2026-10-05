list=["Wania","Aazeen","Johan","Tazwar","Nuraz"]
print(list)
print("Total students: ", len(list))
print("First student: ", list[0])
print("Last student: ", list[-1])
print("First three students: ", list[:3])
list.append("Arham")
print("Added student: ",list)
list.remove("Arham")
print("Removed student: ",list)
list.sort()
print("Sorted: ",list)
list.reverse()
print("Reversed: ",list)
teach={"name":"Ms. Soheni Das","subject":"Coding","experience":8}
print(f"\n Teacher Statistics: {teach}")
print("Subject:", teach["subject"])
print("Experience: ",teach.get("experience", "Not Found"))
teach["experience"]=9
teach["email"]='soheni.jina@gmail.com'
teach.pop("experience")
print("Updated teacher profile: ",teach)
rn=[1,2,3,4]
n=["Johan","Tazwar","Zabeer","Nuraz"]
sd=dict(zip(rn,n))
print("Student Dictionary: ",sd)
print("Student with roll number of 2 is: ",sd[2])
