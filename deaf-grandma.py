# Write a program which can imitate a Grandma who's hard of hearing and follows these constraints:

# If you don't input anything (just hit enter) she responds with WHAT?!

# If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!

# If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!

# The first time you say GOODBYE! she says LEAVING SO SOON?

# The second time you say GOODBYE! she says LATER, SKATER! and the program exits.

def deafGrandma():
  answer = input("WHAT DID YOU WANT?: ")
  answer2 = None
  if len(answer) == 0:
    return "WHAT?!"
  elif answer == "GOODBYE!":
    answer2 = input("LEAVING SO SOON?: ")
  elif answer.isupper():
    return "NO, NOT SINCE 1946!"
  elif not answer.islower():
    return "SPEAK UP, KID!?!"
  
  if answer2 == "GOODBYE!":
    return ("LATER, SKATER!")
    
print(deafGrandma())