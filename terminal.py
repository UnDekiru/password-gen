import passwordGenerator as pg
import os
import subprocess

class Terminal:
    def __init__(self):
        self.on = True
        self.generator = pg.PasswordGenerator()
        self.generatedPsw = ''
        
        self.turnOff = False
        self.mode = 'menu'
        self.clear = lambda: os.system('cls')

    def manager(self):
        self.launch()
        while not self.turnOff:

            if self.mode == 'menu': self.menu()

            elif self.mode == 'length': self.changeLength()

            elif self.mode == 'generated': self.generated()

    def launch(self):
        print('Password generator 2021.')

    def exit(self):
        self.turnOff = True
        print('Shutting down...')

    def onOff(self, dane):
        if dane: return 'on'
        return 'off'

    def generated(self):
        self.clear()
        print(f'''Generated password is:
        {self.generatedPsw}
What would you like to do?
[M] Back to menu
[G] Generate new password
[X] Close''')
        x = input()
        if x == 'x' or x == 'X':
            self.exit()
            self.mode = 'menu'
        elif x == 'g' or x == 'G':
            self.generatedPsw = self.generator.generate()
            self.generated()
        elif x == 'm' or x == 'M': self.mode = 'menu'
    
    def changeLength(self):
        while(True):
            print('Set password length - between 8 and 10,000 signs. To cancel input non digit.')
            length = input()
            if not length.isdigit(): return False
            length = int(length)
            if length > 10000 or length < 8: continue
            self.generator.setLength(length)
            break
    
    def menu(self, wrongPsw = False):
        self.clear()
        tmp = ''
        if wrongPsw: tmp = 'Generator cannot meet requirements. Change password length or other settings and try again.\n'
        print(f'''{tmp}What would you like to do?
[G] Generate password
[L] Change password length - {self.generator.length}
[1] Lower case - {self.onOff(self.generator.char_lower)}
[2] Upper case - {self.onOff(self.generator.char_upper)}
[3] Digits - {self.onOff(self.generator.digits)}
[4] Signs - {self.onOff(self.generator.symbols)}
[5] Punctuation signs - {self.onOff(self.generator.symbols_special)}
[6] Repeat sign - {self.onOff(self.generator.repeat_character)}
[X] Close.''')
        keystroke = input()
        if keystroke == 'g' or keystroke == 'G':
            self.generatedPsw = self.generator.generate()
            if self.generatedPsw:
                self.mode = 'generated'
            else:
                self.menu(True)
        if keystroke == 'l' or keystroke == 'L':
            self.changeLength()
        if keystroke == 'x' or keystroke == 'X':
            self.exit()
        if keystroke == '1':
            self.generator.switch_char_lower()
        if keystroke == '2':
            self.generator.switch_char_upper()
        if keystroke == '3':
            self.generator.switch_digits()
        if keystroke == '4':
            self.generator.switch_symbols()
        if keystroke == '5':
            self.generator.switch_symbols_special()
        if keystroke == '6':
            self.generator.switch_similiar_chars()
    