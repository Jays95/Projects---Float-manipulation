# Importing the random method 
from random import randint
# List of random jokes ,source = google
jokes = ["What did the shark say when he ate the clownfish?: This tastes a little funny",
        "What orange sounds like a carrot?: A parrot","What did the pirate say when he turned 80?: Aye matey",
        "What did the buffalo say when his son left for college?: Bison",
        "What is an astronauts favorite part on a computer?: The space bar",
        "Did you hear about the two people who stole a calendar?: They each got six months",
        "What do cows do on date night?: Go to the moo-vies ","Why didnt the chicken cross the road?: Cause his a chicken :)"]
# Storing the index in magic_num which is going to be an int 
magic_num = randint(0,len(jokes) - 1)
# Printing out the jokes in the list by the index of the int value being held in magic_num variable
print(jokes[magic_num])
  