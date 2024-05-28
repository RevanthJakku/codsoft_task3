import random
def generate():
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="?@!$%^&*_+*#"
    all=lower+upper+numbers+symbols
    length = int(input("Enter length of password: "))
    n = int(input("Enter number of passwords to be generated: "))
    for i in range(n):
        password="".join(random.sample(all,length)) 
        print(password)
    
    regenerate = input("Do you want to regenrate new passwords?(Yes/No): ")
    if regenerate.lower() == "yes":
        generate()
    else:
        print("Good Bye")

generate()