samplelist=[10,10,20,40,50,60,70]
print("original list:" ,samplelist)

samplelist=list(set(samplelist))
print("Unique list:", samplelist)

tuple=tuple(samplelist)
print("Tuple:",tuple)

print("Minimum number:",min(tuple))
print("Maximum number",max(tuple))