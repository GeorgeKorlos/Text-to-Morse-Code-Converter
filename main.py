# Text to morse code converter

alphabet = {
    "A": ".-",     "B": "-...",   "C": "-.-.",   "D": "-..",    "E": ".",
    "F": "..-.",   "G": "--.",    "H": "....",   "I": "..",     "J": ".---",
    "K": "-.-",    "L": ".-..",   "M": "--",     "N": "-.",     "O": "---",
    "P": ".--.",   "Q": "--.-",   "R": ".-.",    "S": "...",    "T": "-",
    "U": "..-",    "V": "...-",   "W": ".--",    "X": "-..-",   "Y": "-.--",
    "Z": "--..",

    "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--",  "4": "....-",
    "5": ".....",   "6": "-....",  "7": "--...",  "8": "---..",  "9": "----.",
    
    " ": "/"
}

def get_key_by_value(dictionary, value):
    reverse_dict = {v: k for k, v in dictionary.items()}
    return reverse_dict.get(value, None) 

def to_and_from_morse(coding, text):
    new_text = ''
    
    if coding == 'encode':
        for char in text:
            morse_char = alphabet.get(char)
            if morse_char:  
                new_text += morse_char + ' '
            else:
                new_text += '?' + ' ' 

    elif coding == 'decode':
        words = text.split('/')  
        for word in words:
            morse_symbols = word.strip().split(' ')  
            for symbol in morse_symbols:
                key = get_key_by_value(alphabet, symbol.strip()) 
                if key:
                    new_text += key  
                else:
                    new_text += '?'  
            new_text += ' '  


    
    return new_text.strip()


def restart_program():
    while True:
        coding = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
        text = input("Type your message:\n").upper()

        result = to_and_from_morse(coding=coding, text=text)

        print("Result:", result)

        reset = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if reset == 'no':
            print("Goodbye")
            break

restart_program()