listOne=[3,6,9,12,15,18,21]
listTwo=[4,8,12,16,20,24,28]
listThree=[]

oddElements=listOne[1::2]
print("Elements at odd-index positions from list one:",oddElements)

EvenElement=listTwo[0::2]
print("Elements from odd index positions from list two:",EvenElement)

listThree.extend(oddElements)
listThree.extend(EvenElement)
print("update third list:",listThree)
