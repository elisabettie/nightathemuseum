# -*-coding: utf-8 -*-
#spelet visar ett scenario
print (chr(27) + "[2J")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Äntligen, du har kommit. Jag måste erkänna, jag var osäker om du skulle dyka upp..")

#spelet frågar vad du heter
person = raw_input("Vad heter du? ")
print ("Nåväl, det är inte ditt fel. ")

answer = raw_input("Jag antar att du vet varför du är här? ")
if answer.lower() == "ja":
	print ("Bra. Då struntar jag i att gå igenom detaljerna. Allt du behöver göra är att hämta blodsafiren och ge den till mig. Jag betalar såklart.")
else:
	print person + (", varför får du betalt egentligen? Nåja, vi tar det igen.")
	print ("Blodsafiren är en juvel - varför den är viktig för mig behöver du inte veta. Jag vill att du hämtar den, jag kommer självklart att betala dig. Om du lyckas, så att säga.")

print

options = ["skryt","fegis"]

for i, val in enumerate(options):
	print i+1, '::', val 

print

answer = raw_input("Vad väljer du? ")
if answer == "1":
	print "Cool."

elif answer == "2":
	print "nooo"

else:
	print "vad menar du? 1 eller 2?"

#print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
