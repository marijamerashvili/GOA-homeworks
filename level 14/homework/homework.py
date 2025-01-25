"""2) დაწერე პროგრამა, რომელიც ამოწმებს, შეყვანილი რიცხვი 5-სა და 15-ს შორის არის, მაგრამ არა 10-ის ტოლი.
3) მომხმარებელმა უნდა შეიყვანოს თავისი ასაკი და სახელი. პროგრამამ უნდა შეამოწმოს, რომ ასაკი 18-ზე მეტია და სახელი იწყება "A"-ზე.
4) დაწერე პროგრამა, რომელიც ამოწმებს, რიცხვი ლუწია ან 3-ის გამყოფი.
5) პროგრამამ უნდა გამოიანგარიშოს, მოცემული ორი რიცხვიდან რომელიმე 100-ის ტოლი ან მასზე მეტია თუ არა."""

print("chose number bitwen 5-15: ")
x = input()

x= int(x)

if 5<= x <= 15 or x==10 :
    if x==10:
        print("you failed")
        exit()

    if 5<= x <=15 :
        print("you won")


print("enter your name: ")
x = input()

if x[0]!= "a" :
    print("you cant continue...")
    exit()

print("enter your age: ")
x= input()

if int(x)>18 :
    print("you passed")
else:
    print("you did not passed")
    






