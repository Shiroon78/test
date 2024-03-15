question = "Does she have a boy friend?"
print(question)

answer = input("")

if(len(answer)>3 or len(answer)<2):
    raise SyntaxError("Answer should be with yes or no only")

if (len(answer)==3):
    print("Time to move on.. I give up ahhhhhhhhhhhh")
if (len(answer)==2):
    print("Happy, Happy , Happy")
else: 
    print("My life is beautiful")

