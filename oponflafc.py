spn=["IMPORTANT: Complete Python homework\n","TODO: Revise file handling concepts\n","NOTE:read(n) previews characters\n","IMPORTANT: Submit assignment today\n","SKIP:This line is not needed\n","NOTE:readlines() stores lines in a list\n","TODO:Practise loops with files\n"]
file=open("oponflafc.txt","w")
file.writelines(spn)
file.close()
print("FILE CREATED.")
file=open("oponflafc.txt","r")
print("First 40 characters of file: ",file.read(40))
file.close()
file=open("oponflafc.txt","r")
lines=file.readlines()
print(f"You have {len(lines)} in this file.")
for i in range(len(lines)):
    print(i+1,">>",lines[i].strip())
file.close()
file=open("oponflafc.txt","r")
lines=file.readlines()
for i in range(len(lines)):
    print("READING: ", lines[i].strip())
file.close()
file=open("oponflafc.txt","r")
word=input("SKIP LINES STARTING WITH: ")
if word:
    for line in lines:
        if line.startswith(word):
            print("SKIPPED: ",line.strip())
        else:
            print("KEPT: ",line.strip())
file.close()
file=open("oponflafc.txt","w")
wordt=input("WRITE LINES STARTING WITH: ")
if word:
    for line in lines:
        if line.startswith(wordt):
            file.write(line)
            print("WRITTEN: ",line.strip())
        else:
            print("NOT WRITTEN: ",line.strip())
file.close()
print("FINAL SUMMARY: ")
file=open("oponflafc.txt","r")
lines=file.readlines()
for i in range(len(lines)):
    print("LINES: ",lines[i].strip())
file.close()