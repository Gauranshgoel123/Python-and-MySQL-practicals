fin=open("book.txt","r")
fout=open("empty.txt","w")
s=fin.readlines()
for j in s:
    if 'a' in j:
        fout.write(j)
fout.close()
fin.close()
