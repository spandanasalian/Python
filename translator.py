d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    return d[word]
 
word = input("Enter word: ")
print(vocabulary(word))