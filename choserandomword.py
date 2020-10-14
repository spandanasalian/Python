import random
wordlist=[]
with open("wikipidea.txt",'r') as file:
    data=file.readlines()
    for line in data:
       splitt= line.split()
       for item in splitt:
           if len(item)>5:
               wordlist.append(item.capitalize())
               
print(random.choice(wordlist))
      