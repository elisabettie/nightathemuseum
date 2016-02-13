# -*-coding: utf-8 -*-
# Utf-8 gör det möjligt för mig att använda svenska bokstäver utan att det krashar något.



# Hej! Welcome to "Night at the museum"
# Bli inte förkräckt av alla kodrader, jag har lagt in kommentarer som förklarar hur programmet/spelet fungerar.
# Testa gärna spelet en gång, det kan underlätta att följa vad som händer i koden.

# Det första spelet gör är att rensa din historik i terminalen, 
# så att du startar spelet utan att bli distraherad från en massa text.

# För att spelet ska kännas mer som en dialog, har vi importerat tid, 
# så att vi kan ha några sekunders väntetid tills nästa mening skrivs ut.
import time

print (chr(27) + "[2J")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~Night at the museum~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Det första vi möter är en dialog mellan dig och den mystiska personen som har ett uppdrag till dig.
print ("Well hello, princess. How nice of you to finally show up!")

# Här ser vi att det kommer dröja 2 sek innan nästa print visas.
time.sleep(2)

print ("I took the liberty of ordering a beer for you. Wouldn't be surpriced if its flat now though.")

# Den mystiska personen frågar vad du heter
# person = raw_input indikerar att inkommande text (svaret som spelaren ger), 
# kommer att användas som värde till ordet/variabeln "person". 
# Att lägga in tomma print kommandon skapar ett radavstånd
print

person = raw_input("What's your name? ")
print ("Well, that's not your fault. ")

print

# På nästa fråga ska det gå att välja mellan två svar - 'yes' eller 'no'
# beroende på om spelaren skriver 'yes' eller 'no' kommer den mystiska personen att ge olika respons.

# Metoden som vi använder här kallas för if-sats på svenska.
# Det betyder att programmet följer regeln: 
# Om (if) svaret är 'yes' > skriv ut "svarsalternativ 1", om svarät är något annat (else) > skriv ut "svarsalternativ 2".

# --- Några detaljer:
# Precis som i scenariot innan så kommer raw_input att vara något som spelaren svarat,
# och kommer att användas som värde till ordet/variabeln 'answer'.
# answer.lowercase betyder att programmet alltid kommer tolka svaret som spelaren ger som små bokstäver 
# det underlättar så att vi inte behöver skriva in alla olika versioner man kan skriva yes på. Tex YeS, yeS osv.

answer = raw_input("I assume that you know why you are here? ")
print

if answer.lower() == "yes":
	print ("Good. Then we don't have to get into details.")
	print ("All you need to do is retrieve the Bloodsaphire to its rightful owner, which is me.")
	print ("I will pay for your work of course.")

# Här ser vi att namnet som spelaren angett i början kommer att skrivas ut, innan dialogen fortsätter.

else:
	print person + (", why do you get paid? Let's go through the job again -")

	time.sleep(2)

	print (" The Bloodsaphire is an artifact currently at the National Gem Museum.")

	time.sleep(2)
	
	print (" I want you to hand it to me.")

	time.sleep(2)
	
	print (" I will pay you for your work of course. If you succeed.")

	time.sleep(2)
print

# I detta parti kommer spelaren att få två svarsalternativ att välja mellan 
# (till skillnad från raw_input, där man kunde svara vad som helst)
# Svarsalternativen presenteras i en numrerad lista.
# Spelaren väljer vilket svarsalternativ som passar bäst.

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
print person + (" slowly takes a sip of the beer while thinking about what to answer..")
print

# Värdet till ordet/variabeln "options" består i detta fall av två svarsalternativ.

options = ["Don't you worry old man. Consider the job done.","Wait a minuite! Stealing from an museum?! Hell no, I'm not doing that without a pre-payment. "]

# --- var händer här ----

for i, val in enumerate(options):
	print i+1, '::', val 

print

answer = raw_input("What will you answer? ")
print 

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if answer == "1":
	print "You seem to be sure about yourself. I hope that won't bite you in the end. The stranger replies."

	time.sleep(4)

elif answer == "2":
	print "Well, I guess you're right. I can't give you the money right now, but I have a name. Kaylei Schassy. She works at the local electric shop. Tell her that you want to change your light. She might be able to help you out."

	time.sleep(4)

else:
	print "You know, I'm putting a lot of trust in you right now. Don't screw it up!"

# Kapitell 1 avslutas med att karaktären lämnar den mystiska peronen.
print

print ("On the way out of the bar you notice a poster on the wall.")
print

print ("     The poster says:")
print ("     Young and old! Big and Small!")
print ("     Don't miss the grand opening of the amazing National Gem Museum exhibition - chrystals beyond imagination, tomorrow at 8 pm.")

print
print ("This means the job needs to be done tonight..")
print

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~End of chapter 1~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
