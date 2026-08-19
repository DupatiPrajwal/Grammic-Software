print("Welcome to Grammic!")
print("Your writing assistant is starting...")

# TEXT :
text = input("enter or paste your text :")
print(text)

# ANALYZING TEXT :
print("================================")
print("GRAMMIC ANALYSIS")
print("================================")
characters = len(text)
print(characters)
words = text.split()
print(len(words))
count = 0
for i in text :
    if i == "?" or i == "!" or i == "." :
        count+=1 
        print(count)
paragraphs = text.split("\n\n")
paragraphs_count = len(paragraphs)
print(paragraphs_count)

