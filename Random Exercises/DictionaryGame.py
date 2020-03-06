import random

dict = {'Data':'Sample', 'Lens':'Vision', 'Battle':'Champion', 'Inmate':'Parole', 'Pitbull': 'Ferocious'}
word = random.choice(list(dict))
maxAttempt = 0
while True and maxAttempt <= 4:
    guess = input("Guess the word __")

    if guess == word:
        print('That\'s ' 'correct!')
        break
    maxAttempt += 1
    if guess != word:
        print({guess}, 'is wrong')
        maxAttempt += 1

print ("Random key value pair from dictonary is ", word, " - ", dict[word])
print('Game over!')
