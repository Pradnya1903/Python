i=1
while i<=5:
    print("*" * i)
    i=i+1

print("******************************************************************")

L=""" preparing a number guessing game in which user will get 3 chances  and if he/she 
able to guess the number right then he win and remaining turns will get finish and if he loose print as you loose """
print(L)
guess_num=9
limit=3
guess_count=0

while guess_count<limit:
    guess=int(input('guess : '))
    guess_count+=1
    if guess==guess_num:
        print("you won !")
        break
else:
    print("you loose")

