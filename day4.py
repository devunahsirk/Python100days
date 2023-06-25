print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

total = name1+name2
#print(total)

t=total.count('t')
r=total.count('r')
u=total.count('u')
e=total.count('e')

fir =t+r+u+e
l=total.count('l')
o=total.count('o')
v=total.count('v')
e=total.count('e')
sec = l+o+v+e
#print(f"TOTAL={fir}{sec}")
com = fir * 10 + sec
#print(com)
if com < 10 :
    print(f"Your score is {com}, you go together like coke and mentos.")
elif com > 90 and com < 99:
    print(f"Your score is {com}, true love is yours.")    
elif com>=100:
    print("Your score is 100 , you are truly made for each other")
elif 75<com<90:
    print(f"Your score is {com},this relationship will be everlasting")        
elif 40 < com < 50:
    print(f"Your score is {com}, you are alright together.")
else:
    print(f"Your score is {com},ok ok ru")
