is_hot=False

if is_hot:
    print("it is really a hot day")# indentation begins
print("it's a cold day")

print("********************************************************************************")

is_hot=True
is_cold=False


if is_cold:
    print("really a hot")
    print("drink water")
else:
    print("it's a cold day")
    print("wear warm clothes")
print("lastly enjoy your day !")


print(" *************************************************************************************")

house_price=100000
has_good_credit=True
has_bad_credit=False


if has_good_credit:
    down_payment=0.3*house_price
else:
    down_payment=0.1*house_price
print(f"down payment : ${down_payment}")