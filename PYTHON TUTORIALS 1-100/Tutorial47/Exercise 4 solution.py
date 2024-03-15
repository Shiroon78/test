# Solution to exercise 4 by code with harry

st = input("enter message... \n") # Taking user input
words = st.split(" ") # It split the input from st
coding = True
if(coding):
    nwords = [] 
    for word in words:
        if(len(word)>=3):
            r1 = "dsf" # Three random characters
            r2 = "lca" # Three random characters
            stnew = r1 + word[1:]+word[0]+ r2 # (word[1:]+ word[0]) removing the first letter  and appending it to the end
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if(len(word)>= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)