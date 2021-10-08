import string
import random
class PasswordGenerator:
    def __init__(self):
        self.symbols = True
        self.symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

        self.digits = True
        self.digits_list = list(string.digits)

        self.char_lower = True
        self.char_lower_list = list(string.ascii_lowercase)

        self.char_upper = True
        self.char_upper_list = list(string.ascii_uppercase)

        self.repeat_character = True

        self.symbols_special = True
        self.symbols_special_list = list(string.punctuation)
        for item in self.symbols_list:
            x = self.symbols_special_list.index(item)
            self.symbols_special_list.pop(x)

        self.length = 12
        self.password = ''
        self.allowed_characters = []


    def switch_symbols(self):
        self.symbols = not self.symbols
    def switch_digits(self):
        self.digits = not self.digits
    def switch_char_lower(self):
        self.char_lower = not self.char_lower
    def switch_char_upper(self):
        self.char_upper = not self.char_upper
    def switch_similiar_chars(self):
        self.repeat_character = not self.repeat_character
    def switch_symbols_special(self):
        self.symbols_special = not self.symbols_special
    
    def resetPassword(self):
        self.password = ''

    def setLength(self, length):
        self.length = length
    
    def setAllowedCharacters(self):
        self.allowed_characters = []
        if self.symbols: self.allowed_characters += self.symbols_list
        if self.digits: self.allowed_characters += self.digits_list
        if self.char_lower: self.allowed_characters += self.char_lower_list
        if self.char_upper: self.allowed_characters += self.char_upper_list
        if self.symbols_special: self.allowed_characters += self.symbols_special_list

    def generate(self):
        if not self.symbols and not self.digits and not self.char_lower and not self.char_upper and not self.symbols_special:
            print('Choose any set of signs.')
            return False

        self.resetPassword()
        self.setAllowedCharacters()

        if len(self.allowed_characters) < self.length and not self.repeat_character: return False

        while len(self.password) < self.length:
            tmp = random.randrange(len(self.allowed_characters))
            self.password += self.allowed_characters[tmp]

            if not self.repeat_character: self.allowed_characters[tmp] = ''
        return self.password