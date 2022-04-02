import random
import time

#magic 8 ball
print("Welcome to the Magic 8 Ball!")

#input a question
input("Ask a question: ")

#random list of words
words = ("Yes","No","Maybe","Try Again","You're Funny! LOL")


print("Thinking...")

#delay answer for 3 secs
time.sleep(2.0)


#prints random words
print(random.choice(words))