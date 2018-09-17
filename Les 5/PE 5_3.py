leeftijd = int(input("Hou oud ben je? : "))
Nederlandspaspoort= input("Heeft u een nederlands paspoort? : ")
if leeftijd >= 18 and Nederlandspaspoort == 'ja':
    tekst = 'gefeliciteerd u mag stemmen'
else:
    tekst = 'helaas u mag niet stemmen'

print(tekst)