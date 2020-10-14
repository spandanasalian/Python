r=input("Eneter the string:")
n=int(input("Enter the number:"))

def removeChars(str, n):
  return str[n:]

new_str = removeChars(r, n)
print("Result:", new_str)