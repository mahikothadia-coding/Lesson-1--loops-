num=int(input("Enter a number to see if it is an armstrong number."))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
    