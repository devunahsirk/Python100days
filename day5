#Password Generator Project 
# to use easy project comment the hard one and vice versa
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nl= int(input("How many letters would you like in your password?\n")) 
ns = int(input(f"How many symbols would you like?\n"))
nn = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""

for i in range(0,nl+1):
    let=random.choice(letters)
    password = password + let
for i in range(0,ns+1):
    let=random.choice(numbers)
    password = password + let
for i in range(0,nn+1):
    let=random.choice(symbols)
    password = password + let    
print(password)

password=[]
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for i in range(0,nl+1):
    password.append(random.choice(letters))
for i in range(0,ns+1):
    password.append(random.choice(numbers))
for i in range(0,nn+1):
    password.append(random.choice(symbols))   
print(password)  

passw=""
for j in password:
    passw += j
print(passw)    
