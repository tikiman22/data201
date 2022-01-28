from signal import Signals
from tokenize import Name
from unittest.util import strclass

#There was a strange sound that came from the guest bedroom, I was scared, but my wife told me to check on it
#This is when I saw them for the first time, small, brave, sleep obssessed creatures they were.

print ("Hello there sleepy earthling, what is your call sign and recognition code?")
firstname = input("enter call sign:"" ")
lastname = input("enter recognition code:"" ")
fullname = firstname + " " + lastname
print("Salutations", fullname)
print("we are troglodytes, cave dwellers from a different world")
print(fullname ,"are you sleepy, yes or no?")
answer = input()
if answer == "yes":
    print("so sorry, wa,wa,wa, let us help you...beeeeebooop") 
    answer_1 = input( "do you sleep 8 hours per night, yes or no?"" ")
elif answer == "no":
    print("oooo lala lucky you, bye bye and sweet dreams, muah!")
if answer_1 == "yes":
    print("mhmmmm, we troglodytes would like to learn your ways, say your goodbyes to this cruel world and come with us!")
elif answer_1 == "no":
    print("this is unacceptable, we will now begin data collection to analyze your sleep deficits...beeeboopboopbeeeeeep")
    print("Earthling! Tell us how many times have you spun around the orange hot shadow maker in the sky?")
    age = input()
    print("Your species has a prosperous lifespan, much to learn...mhmmmm")

#Permission to proceed with questions

answer_2 = input("do you agree to further questioning?"" ")
if answer_2 == "yes":
    
#Data collection 
# using the float function the user input data for each day can be stored as an integer

    print("Please tell us how many hours you sleep on each of the following nights:")   
    Mervsday = float(input("Mervsday:"" "))
    Tervsday = float(input("Tervsday:"" "))
    Wodnozday = float(input("Wodnozday:"" "))
    Threeorsday = float(input("Threeorsday:"" "))
    Freeorsday = float(input("Freeorsday:"" "))
    Slaseursday = float(input("Slaseursday:"" "))
    Sewnsday = float(input("Sewnsday:"" "))

    print("DAILY DREAMING DEFICIT:")
    #display sleep deficit calculations
    print("Mervsday:", 8 - Mervsday) 
    print("Tervsday:", 8 - Tervsday)
    print("Wodnozday:", 8 - Wodnozday) 
    print("Threeorsday:",8 - Threeorsday)
    print("Freeorsday:", 8 - Freeorsday)
    print("Slaseursday:",8 - Slaseursday)
    print("Sewnsday:", 8 - Sewnsday)
elif answer_2 == "no":
    print("You may face great difficulty dreaming without us, buh bhyeee...")    
print("OMG, it seems like you sleep like crap, let us aggregate your sleep data...beeebooobeeeeebooop")
input("HIT ENTER TO AGGREGATE DATA")
print("BEEBOPBAAAABEEEBOOP***ANALYZING DATA*** BEEEEEEPBOPBEEEEBOOOP")
input("Press ENTER to see results")
recsleepaverage = 56
indvsleepaverage = (Mervsday + Tervsday + Wodnozday + Threeorsday + Freeorsday + Slaseursday + Sewnsday/7)
print("*SLEEP SUMMARY*")
print("name:", fullname)
print ("age:",age)
print("weekly sleep average:", indvsleepaverage, "hrs per week")
print("daily sleep average", indvsleepaverage/7, "hrs per night")

