#CALCULATOR
a=int(input("Select operators from 1,2,3,4,5:"));
num1=int(input("Enter the value of first number="));
num2=int(input("Enter the value of second number="));
if a==1:
    print("1 is used for find the addition of two numbers=",num1+num2);
elif a==2:
    print("2 is used for find the substraction of two numbers=",num1-num2);
elif a==3:
    print("3 is used for find the multipliction of two numbers=",num1*num2);
elif a==4:
    print("4 is used for find the division of two numbers=",num1/num2);
elif a==5:
    print("5 is used for find the squareroot of any number=",(num1)**2,",",(num2)**2);

else:
    print("Invalid Inputs")
