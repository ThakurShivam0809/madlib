from re import A


char1 = input("First character: ")
char2 = input("Second character: ")
verb1 = input("Verb1: ")
verb2 = input("Verb1 in third form: ")

madlib = (f"Once upon a time {char1} and {char2} had an argument about who was better.\
They decided to settle the argument with a {verb1}. They started off the {verb1}.\
 {char1} shot ahead and {verb2} briskly for some time. \
Then seeing that he was far ahead of the {char2}, he thought he'd sit under \
a tree for some time and rest before continuing the {verb1}. He sat under the tree \
and soon fell asleep. {char2} plodding on overtook him and soon finished the \
{verb1}, emerging as the champ. {char1} woke up and realized that he'd lost the challange.")

print(madlib)