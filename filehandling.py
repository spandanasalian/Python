fh=open("example.txt","w")
fh.write("The task involve in manupulating the text")
fh.close()

fht=open("example1.txt","w")
for i in range(1,11):
    
    fht.write("%d \n" %i)
fht.close()