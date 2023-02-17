#Write a code that gives following as an output.```iNeuroniNeuroniNeuroniNeuron```

i = 'iNeuron'
print(i*4)


#Write a code to take a number as an input from the user and check if the number is odd or even.

n=int(input("Please enter any number : "))
if n%2 ==0:
    print(n,"is Even")
else:
    print(n,"is odd")


#Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

age=int(input("Please enter your age : "))
if age>=18:
    print("I can vote")
else:
    print("I can't vote")


#Write a code that displays the sum of all the even numbers from the given list.```numbers = [12, 75, 150, 180, 145, 525, 50]```

numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for i in numbers:
    sum += i
print(sum)


#Write a code to take 3 numbers as an input from the user and display the greatest no as output.

a,b,c = input("Please enter any three numbers : ").split()
if int(a)>=int(b) and int(a)>=int(c):
    print(a,"is gretest number")
elif int(b)>=int(a) and int(b)>=int(c):
    print(b,"is gretest number")
else:
    print(c,"is gretest number")


"""Write a program to display only those numbers from a list that satisfy the following conditions
- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop```numbers = [12, 75, 150, 180, 145, 525, 50]```"""

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i>500:
        break
    if (i%5==0) and (i <=150):
        print(i)
