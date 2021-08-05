#Basic print all intergers from 0 to 150
for x in range(151):
    print(x)
#Print all multiples of 5 between 5 and 1,000
for number in range (5, 1001):
        if number%5==0:
            print (number)


#second attempt: Print multiples of 5 between 5 & 1,000
number=5
while number<=1000:
    if number%5==0:
        print (number)
        number+=5


#Counting the dojo way: print intergers 1 to 100
#if divisible by 5 print"coding"; if divisible by 10 print "coding dojo"
for num in range (1,101):
    if num%5==0:
        print ("coding")

    if num%10==0:
        print("coding dojo")

    else:
        print (num)

#add odd intergers from 0 to 500,000 & print the final sum
#Python program to calculate sum of odd and even numbers using for loop
max=50000
odd_Sum=0
for num in range(1,max+1):
    if (num%2==1):
        odd_Sum=odd_Sum+num

print("The sum of odd numbers 0 to {} = {}".format(num,odd_Sum))

#Add odd intergers from 0 to 50,000 second attempt
n=50000
sum=0
for i in range(1,n+1,2):
    sum+=i
print("The sum of odd integers from 0 to ",n,"=",sum)


#countdown by 4: print positive numbers starting at 2018, counting down by 4

for countdown in range (2018,0,-4):
    print(countdown)
    
    
