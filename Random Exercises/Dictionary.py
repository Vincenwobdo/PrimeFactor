import random

dictionary = {'Data': 'Sample', 'Lens': 'Vision', 'Battle': 'Champion', 'Inmate' : 'Parole', 'Pitbull' : 'Ferocious'}
word = random.choice(list(dictionary))
maxAttempt = 0
print(word)

while word and maxAttempt <= 4:
    user_input = input('Guess the key-word in the dictionary: ')
    print(user_input)

    if user_input == word:
        print('That\'s ' 'correct')
        break
    maxAttempt += 1
    if user_input != word:
        print('Your guess is wrong')
    maxAttempt += 1

print(f'The matching key pair value from dictionary is {word}  :  {dictionary[word]}')
print('You exhausted all your attempts. Game over !!')