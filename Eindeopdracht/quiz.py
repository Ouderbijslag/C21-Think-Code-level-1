name = input('Wat is je naam? ')
print("Welkom bij de quiz " + name)
print("Succes met de quiz!")


def stelvraag(vraag, answer, ):
    user_answer = input(vraag)
    if answer == user_answer:
        print("De antwoord is juist!")
    else:
        print("Antwoord is onjuist!")
print("De eerste vraag...")
stelvraag("Wat is 4 x 8? ", "32")


def stelvraag(vraag, answer):
    user_answer = input(vraag)
    if answer == user_answer:
        print("De antwoord is juist!")
    else:
        print("Antwoord is onjuist!")
print("Volgende vraag!")
stelvraag("Wat is 12 : 3? ", "4")


def stelvraag(vraag, answer):
    user_answer = input(vraag)
    if answer == user_answer:
        print("De antwoord is juist!")
    else:
        print("Antwoord is onjuist!")
print("Volgende vraag!")
stelvraag("Wat is 74 - 62? ", "12")


def stelvraag(vraag, answer):
    user_answer = input(vraag)
    if answer == user_answer:
        print("De antwoord is juist!")
    else:
        print("Antwoord is onjuist!")
print("Volgende vraag!")
stelvraag("Yassin gaat op school knikkeren. Hij neemt 30 knikkers mee. Hij wint er 15 knikkers maar verliest er ook 20. Hoeveel knikkers houdt hij over? ", "25")


def stelvraag(vraag, answer):
    user_answer = input(vraag)
    if answer == user_answer:
        print("De antwoord is juist!")
    else:
        print("Antwoord is onjuist!")
print("Laatste vraag!")
stelvraag("Er is uitverkoop vandaag in de Albert Heijn. De wasmiddel is van 22,00 euro naar 14,00 euro. Hoeveel euro korting? ", "8")

print("Bedankt voor het meespelen met de quiz.")
