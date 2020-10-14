# string=input("Enter the string:")
# substring=input("Enter the word to search:")
# count=string.count(substring)
# print(string)
# print(substring)
# print("the count:",count)

string=input("Enter a sentence:")
word=input("Enter a word:")

def count_word(string,word):
    count=0
    str_list=string.split()
    
    for i in str_list:
        if i==word:
            count+=1
    return count

count=count_word(string, word)
print(word,"appeared",count,"timeshi")
