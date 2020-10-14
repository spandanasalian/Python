def reverse_check_number(number):
    print("original number",number)
    originalNum=number
    reverseNum=0
    while(number>0):
        reminder=number%10
        reverseNum=(reverseNum*10)+reminder
        number=number//10
    if(originalNum==reverseNum):
        return True
    else:
        return False
number=int(input("Enter the number:"))
    
print("The original and reverse number is the same:",reverse_check_number(number))