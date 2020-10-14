string="hello my name is spandana"
if "spandana" in string:
    print("found")
    

string="hello my name is spandana"
if "spandanaa" in string:
    print("found")
    


import re
pattern=r"p....n"
string=("I ma learning th epyhton programming Python is a fun language.")
result=re.findall(pattern,string)
print(result)

import re
pattern=r"p....n" #as we add th edots the retriving dat changes
string=("I ma learning the paaaan pyhton programming.python pvrtun is a fun language.")
result=re.findall(pattern,string)
print(result)

import re 
pattern=r"\d+"
string="spandana 12345, samarth 12567, shamitha 908765 ,shisheer 74757656"
result=re.findall(pattern,string)
print(result)

print("--------------------------condition to retrieve the data here it is 6---------------------------------------------")
import re 
pattern=r"\d{6}"
string="spandana 12345, samarth 12567, shamitha 908765 ,shisheer 74757656,sahithya 12"
result=re.findall(pattern,string)
print(result)


#------------------------------to find the methods in regular expression--------------------------------------------------
import re
print(dir(re))


#---------------------------  method 1------------------------------------------------------------

import re
pattern=r"spandana"
string="my name is spandana.my name is spandana"
result=re.findall(pattern,string)
print(result)


#-----------------------------fullmatch() which requires the exact match--------------------------------------------------

import re
pattern=r"my name is spandana.my name is spandana"
string="my name is spandana.my name is spandana"
result=re.fullmatch(pattern,string)
print(result)


#------------------------------search()----------------------------------------------------------------------------------
import re
pattern=r"spandana"
string="my name is spandana.My name is spandana"
result=re.search(pattern,string)
print(result)



import re
pattern=r"spandana"
string="my name is spandana.My name is spandana"
result=re.search(pattern,string)
print(result.end())


import re
pattern=r"spandana"
string="my name is spandana.My name is spandana"
result=re.search(pattern,string)
print(result.span())


import re
pattern=r"spandana"
string="my name is spandana.My name is spandana"
result=re.search(pattern,string)
print(result.start())


import re
pattern=r"spandana"
string="my name is spandana.My name is spandana"
result=re.search(pattern,string)
print(result.group())


#-----------------------------------------------split()-----------------------------------------------------------------
import re
pattern=r"s"
string="my name is spandana.My name is spandana"
result=re.split(pattern,string)
print(result)


import re
pattern=r","
string="my name is spandana.My name is spandana"
result=re.split(pattern,string)
print(result)

import re
pattern=r"!"
string="my name is spandana!My name is spandana"
result=re.split(pattern,string)
print(result)

#----------------------------------------------sub()--------------------------------------------------------------------
#dots cannot be replaced by the comma
import re
pattern=r"."
replace=","
string="my name is spandana.My name is spandana"
result=re.sub(pattern,replace,string)
print(result)

import re
pattern=r","
replace="."
string="my name is spandana,My name is spandana"
result=re.sub(pattern,replace,string)
print(result)



#. dot cannot be used directly because it has different meaning so use escape \ before dot .


