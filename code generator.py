import random
name = input('Enter your name: \n')
print(f"{name} let's start the game")
print('You have 10 words to decode, create your high-score,\nGOOD LUCK')
point = 0
attemts = 0

while True: 
    animalNames = ['dog', 'cat', 'hen', 'rat', 'bat', 'horse', 'cow', 'peacock', 'lion', 'tiger']

    # now we can create an array from which we will get the words randomly from
    # now we will take the text(word random from the animalNames)

    text = random.choice(animalNames)
    # print(text)
    # convert text to an array/list
    arr = list(text)
    random.shuffle(arr)
    newStr = ''.join(arr)
    print(f'Encoded word: {newStr}')
    decode = input('Decode the word: \n')
    if(decode==text):
        point+=1
        attemts+=1
        print('Correct!')
    else:
        point+=0
        attemts+=1
        print('Wrong!')       
    if(attemts==10):
        break
    print(f'Points: {point}')
print(f'Game over your points are {point}')
    

