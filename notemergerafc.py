import os
print("Science notes")
with open("scop.txt", "r") as f:
    for line in f:
        print(line.strip())
print()
print("math notes")
with open("mnop.txt","r") as f:
    for line in f:
        print(line.strip())
print()
with open("cnop.txt","r") as f:
    for line in f:
        print(line.strip())
print()
print("ALLNTOEST TIME")
if os.path.exists("allnotes.txt"):
    print("allnotes.txt EXISTS.")
else:
    print("allnotes.txt DOES NOT EXIST. CREATING FILE.")
content=''
with open("scop.txt", "r") as f:
    content+="---SCIENCE NOTES---\n"
    content+=f.read()+"\n"
with open("mnop.txt","r") as f:
    content+='---MATH NOTES---\n'
    content+=f.read()+"\n"
with open("cnop.txt","r") as f:
    content+='---COMPUTER NOTES---\n'
    content+=f.read()+"\n"
with open("allnotes.txt","w") as out:
    out.write(content)
print("SAVED TO ALLNOTES.TXT")
print()
if os.path.exists("allnotes.txt"):
    os.remove("allnotes.txt")
    print("allnotes.txt DELETED.")
else:
    print("allnotes.txt DOES NOT EXIST. CANNOT DELETE.")