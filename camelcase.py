#inputing the sentence from the user
sentence = input("Please enter a sentence: ")

#convert the first letter to uppercase from the sentence
upper_words = sentence.title()

#not adding space in the result sentence
no_spaces = upper_words.replace(' ', '')
joined = ''.join(no_spaces)
camelcase = joined[0].lower() + joined[1:]

#Display the result
print(camelcase)

def display_banner():
    print('Awesome camelCase program')