speed={"jan":47,"feb":52,"march":47,"april":44,"may":52,"june":53,"july":54,"aug":44,"sept":54}

values=speed.values()
print("Dictionarys values:",values)

speedlist=[]
for item in values:
    if item not in speedlist:
        speedlist.append(item)

print("Unique list:",speedlist)