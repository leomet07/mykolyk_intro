print("CW19 by Lenny Metlitsky PD9 3/8/2023")

def FacesOnMoney():
    denomination = int(input("Enter the bank note denomination: "))

    induvidual = ""

    if denomination == 100:
        induvidual = "Benjamin Franklin"
    elif denomination == 50:
        induvidual = "Ulysses S. Grant"
    elif denomination == 20:
        induvidual = "Andrew Jackson"
    elif denomination == 10:
        induvidual = "Alexander Hamlton"
    elif denomination == 5:
        induvidual = "Abraham Lincoln"
    elif denomination == 2:
        induvidual = "Thomas Jefferson"
    elif denomination == 1:
        induvidual = "George Washington"
    else: 
        induvidual = "Nobody! That denomination doesn't exist"

    print("The face on your banknote is: " + induvidual + ".")

FacesOnMoney()
