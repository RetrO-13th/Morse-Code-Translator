class Morse_to_ENG:

    def morse_to_eng(self,sentence):
        translated_sentence = []

        for letter in sentence:
            # Space
            if letter == '^': 
                translated_sentence.append(' ')
            # Alphabet
            elif letter == '.-':
                translated_sentence.append('a')
            elif letter == '-...':
                translated_sentence.append('b')
            elif letter == '-.-.':
                translated_sentence.append('c')
            elif letter == '-..':
                translated_sentence.append('d')
            elif letter == '.':
                translated_sentence.append('e')
            elif letter == '..-.':
                translated_sentence.append('f')
            elif letter == '--.':
                translated_sentence.append('g')
            elif letter == '....':
                translated_sentence.append('h')
            elif letter == '..':
                translated_sentence.append('i')
            elif letter == '.---':
                translated_sentence.append('j')
            elif letter == '-.-':
                translated_sentence.append('k')
            elif letter == '.-..':
                translated_sentence.append('l')
            elif letter == '--':
                translated_sentence.append('m')
            elif letter == '-.':
                translated_sentence.append('n')
            elif letter == '---':
                translated_sentence.append('o')
            elif letter == '.--.':
                translated_sentence.append('p')
            elif letter == '--.-':
                translated_sentence.append('q')
            elif letter == '.-.':
                translated_sentence.append('r')
            elif letter == '...':
                translated_sentence.append('s')
            elif letter == '-':
                translated_sentence.append('t')
            elif letter == '..-':
                translated_sentence.append('u')
            elif letter == '...-':
                translated_sentence.append('v')
            elif letter == '.--':
                translated_sentence.append('w')
            elif letter == '-..-':
                translated_sentence.append('x')
            elif letter == '-.--':
                translated_sentence.append('y')
            elif letter == '--..':
                translated_sentence.append('z')
            # Number
            elif letter == '.----':
                translated_sentence.append('1')
            elif letter == '..---':
                translated_sentence.append('2')
            elif letter == '...--':
                translated_sentence.append('3')
            elif letter == '....-':
                translated_sentence.append('4')
            elif letter == '.....':
                translated_sentence.append('5')
            elif letter == '-....':
                translated_sentence.append('6')
            elif letter == '--...':
                translated_sentence.append('7')
            elif letter == '---..':
                translated_sentence.append('8')
            elif letter == '----.':
                translated_sentence.append('9')
            elif letter == '-----':
                translated_sentence.append('0')
            elif letter in ['_', '-', '.' '/', '*']:
                pass


        return ''.join(translated_sentence).capitalize()

    def get_morse_sentence(self):
        print('\nNotice: Type "Space" betweee every morse code and "^" between every word. You are not allow to use underline, dot, slash etc.')
        text = input('Enter your morse code sentence: ').split()

        return text

class Eng_to_Morse:
    def eng_to_morse(self, sentence):
        transelated_sentence = []

        for i in range(len(sentence)):
            word = []

            for letter in sentence[i]:
                    # Alphabet
                    if letter in ['a', 'A']:
                        word.append('.-')
                    elif letter in ['b', 'B']:
                        word.append('-...')
                    elif letter in ['c', 'C']:
                        word.append('-.-.')
                    elif letter in ['d', 'D']:
                        word.append('-..')
                    elif letter in ['e', 'E']:
                        word.append('.')
                    elif letter in ['f', 'F']:
                        word.append('..-.')
                    elif letter in ['g', 'G']:
                        word.append('--.')
                    elif letter in ['h', 'H']:
                        word.append('....')
                    elif letter in ['i', 'I']:
                        word.append('..')
                    elif letter in ['j', 'J']:
                        word.append('.---')
                    elif letter in ['k', 'K']:
                        word.append('-.-')
                    elif letter in ['l', 'L']:
                        word.append('.-..')
                    elif letter in ['m', 'M']:
                        word.append('--')
                    elif letter in ['n', 'N']:
                        word.append('-.')
                    elif letter in ['o', 'O']:
                        word.append('---')
                    elif letter in ['p', 'P']:
                        word.append('.--.')
                    elif letter in ['q', 'Q']:
                        word.append('--.-')
                    elif letter in ['r', 'R']:
                        word.append('.-.')
                    elif letter in ['s', 'S']:
                        word.append('...')
                    elif letter in ['t', 'T']:
                        word.append('-')
                    elif letter in ['u', 'U']:
                        word.append('..-')
                    elif letter in ['v', 'V']:
                        word.append('...-')
                    elif letter in ['w', 'W']:
                        word.append('.--')
                    elif letter in ['x', 'X']:
                        word.append('-..-')
                    elif letter in ['y', 'Y']:
                        word.append('-.--')
                    elif letter in ['z', 'Z']:
                        word.append('--..')
                    # Number
                    elif letter == '1':
                        word.append('.----')
                    elif letter == '2':
                        word.append('..---')
                    elif letter == '3':
                        word.append('...--')
                    elif letter == '4':
                        word.append('....-')
                    elif letter == '5':
                        word.append('.....')
                    elif letter == '6':
                        word.append('.----')
                    elif letter == '7':
                        word.append('--...')
                    elif letter == '8':
                        word.append('---..')
                    elif letter == '9':
                        word.append('----.')
                    elif letter == '0':
                        word.append('-----')
                    elif letter in ['_', '-', '.' '/', '*']:
                        pass

            transelated_sentence.append(' '.join(word))

        return ' ^ '.join(transelated_sentence)

    def get_eng_sentence(self):
        print('\nNotice: Use alphabet and numbers. You are not allow to use underline, dot, slash etc.')
        text = list(map(list, input('Enter your English sentence: ').split()))

        return text

