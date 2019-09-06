def str_camelcase(sentence):
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ', '')
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def display_banner():
    print('Awesome camelCase program \n')
    print('Enter a sentence to convert to camelCase')

def main():
    display_banner()
    sentence = input('Enter your sentence: ')
    output = str_camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()