""" ყველაფერი გააკეთეთ input-ებით 
1) დაწერეთ პროგრამა რომელიც თუ მოქალაქე არის 18 წლის და მას აქვს მართვის მოწმობა შეუშვებს ქვეყანაში
2) მომხმარებელმა ფასდაკლება უნდა მიიღოს თუ 100 ლარზე მეტ რამეს ყიდულობს ან არის vip მომხმარებელი
3) ოთახის გათბობა აქტიურდება თუ ტემპერატურა ან ძალიან დაბალია ან ძალიან მაღალი
4) სკოლაში მხოლოდ ისეთი სტუდენტები შედიან რომლებიც სტუდენტური ბარათბით შედიან ან მასწავლებლის ნებართვა აქვთ """

print('Enter your name:')
x = input()
print('Hello, ' + x)

print('How old are u?')
x = input()

if int(x) < 18:
  print("not allow to go country!!!!!!")
  exit()

print('Have u drive license? yes/no')
x = input()

if x == 'yes' or x == 'no':
  if x == 'no':
    print("not allow to go country")
    exit()
else: 
  print("please write only yes or no")
  x = input()
  

print("allow to go country and safetly")


print("what did you paid for your things?: ")
x = input()

if int(x)<100:
  print("you will not have eny sales!")
  exit()

print("do you have vip?: ")
x= input()

if x == 'yes' or x == 'no':
  if x == 'no':
    print("not allow to have sales")
    exit()

else: 
  print("please write only yes or no")
  x = input()
  

print("congradulations, you can have sales!!")

print("what temperature is your house? (cold/hot/natural): ")
x = input()

if x=="cold" or x=="hot" or x=="natural" :
    if x=="cold":
        print("your room heating will teorn on")
    if x=="hot":
        print("your room heating will teorn on")
else:
   print("your room heating will not teorn on!")


print("do you have a card of school?: (no/yes) ")
x== input()

if x== "no":
 print("you cant go into school")
 exit()

print("do you asked teacher going into school?: ")
x==input()

if x=="no" or x=="yes" :
   if x=="no":
    print("you cant go to school")
    exit()
else:
   print("you can go into school!")
   

