'''
10.Build a countdown calculator. Write some code that can take two dates as input, and
then calculate the amount of time between them
'''

from datetime import date

first_date=date(2023,9,17)
Second_date=date(2023,6,10)

difference=first_date - Second_date
print(difference)

"=============================="

'''
11. Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
ways
'''
'1-- first way'
def temp(x,y,z):
    if x=='celisuis':
        y=(z-32)*(5/9)
        print(y)
    else:
        y=(z*(9/5))+32    
        print(y)

c=float(input("whats Temprature = "))
a=str(input("Enter The type = "))
temp(a,0,c)


'2--Second Way'

class convert:
    def __init__(self):
        """
        1-- converting from inches to cm 
        2-- converting from cm to inches
        """
        user_choice=int(input())

        if user_choice==1:
            cm=int(input("How many Centimeters"))
            self.centimeters(cm)

        elif user_choice==2:
            inches=int(input("How Many Inches"))
            self.inches(inches)

        else:
             print("Good Bye")    
                 

    def centimeters(cm,x):
            
            x=str(input())
            if x=='cm':
                cm=cm*2.4

    def inches(inches,y):
            y=str(input())
            if y=='inches':
                inches=inches/2.4


'3--Third Way'

"مش عارف "


'================================'


"""Build an email slicer : create a function that takes an email as input and retrieve the
username and domain of the email"""


email=input("enter your email : ").strip()

at=email.find('@')
after_at=email.find(' ',at)
domain=email[at+1 : after_at]

print(domain)

"================================="

'''
13. Currency converter : create a python script that takes a money with currency sign and
convert it to some other currencies , the code should be like the game we did before
'''
