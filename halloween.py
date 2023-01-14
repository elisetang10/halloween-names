print("happy halloween! before you go trick-or-treating, you need a name.")
print("ms asha is a zombie that will come to get you in your bed tonight.")
import random
adjectives = open("adjective.txt", "r")
nouns = open("noun.txt","r")
adj = []
noun = []
while(adjectives.readline()!=""):
    split = adjectives.readline().split("\n")
    adj.append(split[0])
while(nouns.readline()!=""):
    split = nouns.readline().split("\n")
    noun.append(split[0])
adjectives.close()
nouns.close()
word1 = random.choice(adj)
word2 = random.choice(noun)
print(f"YOUR HALLOWEEN NAME IS: {word1} {word2}")