word=input("enter your word: ")
vomels='a,e,u,i,o'
new_word=" "
for letter in word:
    if letter in vomels:
        new_word+="!"
    else:
        new_word+=letter
print(new_word)
