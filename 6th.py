# logical operators

has_good_income=True
has_bad_income=False
has_good_credit=True

if has_good_income and has_good_credit :
    print("eligible for loan")

if has_bad_income or has_good_credit:
    print("not eligible for loan")

if has_good_income or  not has_good_credit: # true or false=true  ;  true and false=false
    print("you even not ask for  loan")

print("********************************************************************************************")

weight=int(input('enter weight :'))
unit=input('in pounds(L) or kilos(kg)')

if unit.upper()=="L":
    convert=0.45*weight
    print(f'{weight} pounds = {convert}kg')
else:
    convert=weight/0.45
    print(f'{weight} kg = {convert}pounds')
