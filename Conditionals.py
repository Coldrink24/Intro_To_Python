#Conditionals

is_hungry = False
is_out = False
if is_hungry:
    print("go eat")
elif is_out and is_hungry:
    print("Order food")
elif not (is_out) or is_hungry:
    print("Let's cook")
else:
    print("5las ma4y")

agetest1 = 19
# You Can Type A Short If Condithon ( Ternary If ) Like This ..


# Another Shape For Ternary If

print ("Your Age Is 19, Good You Will Have Some Good Advantages in This Script") if agetest1 == 19 else print ("f Your Age Is {agetest1}, You Won't Have All Advantages in This Script")

print("Let's cook") if (is_hungry == True) else print("5las ma4y")
