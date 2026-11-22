
first_name = input("Wat is je voornaam? ").strip().title()      #Deze functies gevonden in de lesstof BONUS onder werken met tekst
infix = input("Wat is het tussenvoegsel? (laat leeg als je er geen hebt) ").strip().lower()
last_name = input("Wat is je achternaam? ").strip().title()

while True:     #zorgen dat de invoer klopt (while)
    gender = input("Wat is je geslacht? (man/vrouw/anders): ").strip().lower()

    if gender == "man":
        salutation = "meneer"
        break
    elif gender == "vrouw":
        salutation = "mevrouw"
        break
    elif gender == "anders":
        salutation = ""
        break
    else:
        print("Ongeldige invoer, kies uit man, vrouw of anders")
#inspringen toegevoegd omdat deze code zonder niet functioneert.
#break toevoegd omdat hij bleef rekenen. Zie hoofdstuk 5 (deze had ik al gelezen)


birthday = input("Wat je geboortedatum? (dd-mm-yyyy) ").strip()

if infix:
    full_name = f"{first_name} {infix} {last_name}"
else:
    full_name = f"{first_name} {last_name}"


initial_budget = float(input("Wat is je startbudget?: "))

ENTRANCE_FEE = 10.00
MANDATORY_DRINK= 5.00
GAMBLING_TAX= 2.00
#de punt geeft een float waarde

fixed_costs = ENTRANCE_FEE + MANDATORY_DRINK + GAMBLING_TAX
balance = initial_budget - fixed_costs

print("Casino de Gouden Driehoek")
print("-" * 25)

if salutation:
    print(f"Welkom, {salutation} {full_name}")
else:
    print(f"Welkom, {full_name}")
#gender aangepast naar salutation omdat hij anders man of vrouw toont

print ("")
print (f"{'Startbudget:':<15}€ {initial_budget:>4.2f} ")
print (f"{'Vaste kosten:':<15}€ {fixed_costs:>4.2f} ")
print (f"{'Saldo:':<15}€ {balance:>4.2f} ")
#.2 Notatie gebruikt om twee decimalen achter de punt te laten zien (google is your best friend)

print ("")
if balance > 0:
    print("Je hebt nog genoeg budget voor toegang tot het casino")
else:
    print ("Je hebt niet voldoende budget voor toegang tot het casino")


###CasinoWeek 2###

