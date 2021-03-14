# RetrO_13th (Sadra Ghoalmi)

from MorseTranslator import Eng_to_Morse
from MorseTranslator import Morse_to_ENG

print('''
RetrO_13th

For using the translator select:
1. English to Morse Code
2. Morse Code to English
3. Exit
''')

while True:
    try:
        # selection input
        selected_inp = input('Type number or text of selection: ').lower()

        # English to Morse Code
        if selected_inp in ['1', 'english to morse code']:
            E_text = Eng_to_Morse().get_eng_sentence()
            print(f'Morse Code Text: {Eng_to_Morse().eng_to_morse(E_text)}\n')

        # Morse Code to English 
        elif selected_inp in ['2', 'morse code to english']:
            M_text = Morse_to_ENG().get_morse_sentence()
            print(f'English Text: {Morse_to_ENG().morse_to_eng(M_text)}\n')

        # Exit from the program(break)
        elif selected_inp in ['3', 'exit']:
            print('\nThanks!')
            break
        
        else:
            print('Invalid Input!\nThanks')
            break

    except EOFError:
        print('Invalid Input!\nThanks')
        break