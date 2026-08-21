print("Welcome to Grammic!")
print("Your writing assistant is starting...")

# TEXT & #ANALYZING TEXT :    
text = input("enter or paste your text :")
if text.strip() == "" :
    print("Error")
else :
    print("===========ANALYZING THE TEXT===========")
    print(text)
    characters = len(text)
    print("Characters In Your Text:",characters)
    words = text.split()
    print("Words In Your Text :",len(words))
    count = 0
    for i in text :
        if i == "?" or i == "!" or i == "." :
            count+=1 
    print("Punctuations In Your Text :",count)    
    paragraphs = text.split("\n\n")
    paragraphs_count = len(paragraphs)
    print("Paragrahs In Your Text:",paragraphs_count)


