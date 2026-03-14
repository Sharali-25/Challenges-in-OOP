class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word +'('+self.meaning+')'
flash=[]
print("Welcome to the flashcard application")
while(True):
    word=input("enter the name u want to add to the flashcard: ")
    meaning=input("enter the meaning of the word : ")
    flash.append(flashcard(word,meaning))
    option=int(input("if u wanna add other flashcard,enter 0,otherwise enter 1 :"))
    if(option):
        break
print("\n your flashcards")
for i in flash:
    print(">",i)