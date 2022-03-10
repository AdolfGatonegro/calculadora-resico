'''
    Project: Calculadora RESICO
    Version: 0.1 
    Date: 2022-03-09
    License: MIT
    Author: Gatonegro <adolf@gatoneg.ro>
    URL: github.com/AdolfGatonegro/calculadora-resico
    -----------------------
    An incredibly simple tax calculator app for Android,
    built as a learning experience, a proper programming challenge
    and also because I don't have it in me to use spreadsheets any
    longer.

    The code is about as crude as it can be while still working, so 
    apologies in advance for that. It's literally the first programming thing 
    I've done beyond basic shell and Python scripts. I found out Kivy is a 
    thing only when I started looking into building this. So, yeah. It's 
    not pretty. 
'''
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')
Window.size = (360, 740)

class CalcAppRoot(BoxLayout):

    # Tax and retention values 
    iva_value = 0.16
    isr_value = 0.0125
    iva_ret = 0.1067
    isr_ret = isr_value
    # Compensate for the mismatch when calculating and re-calculating IVA retention
    comp_value = 1.001667416

    def __init__(self):
        super(CalcAppRoot, self).__init__()

    # Input function, with validation to avoid stupid situations 
    def calc_input_symbol(self, symbol):
        if self.calc_field.text == "" and symbol == "0":
            return
        elif self.calc_field.text == "" and symbol == ".":
            self.calc_field.text += "0" + symbol
        elif symbol == "." and symbol in self.calc_field.text:
            return
        elif len(self.calc_field.text) >= 10:
            return
        else:
            self.calc_field.text += symbol

    # Clear the calculation field
    def calc_field_clear(self):
        self.calc_field.text = ""

    '''
    The main calculation functions are rather stupid, because
    it's essentially duplicating code to perform a slightly different
    operation. Might refactor it later, if I'm bored enough.
    '''
    # Calculate the net sum 
    def calc_eval_net(self):
        # If field isn't empty, convert to float and do the calculation
        if self.calc_field.text != "":
            input_amount = float(self.calc_field.text)
            calc_result = input_amount + \
                (input_amount * self.iva_value) - \
                (input_amount * self.iva_ret) - \
                (input_amount * self.isr_ret)
            # round to 2 decimal places, convert to string, update
            self.calc_field.text = str(round(calc_result, 2))
        # If field is empty, just return
        else:
            self.calc_field.text = ""
        
    # Calculate gross sum
    def calc_eval_gross(self):
        # If field isn't empty, convert to float and do the calculation
        if self.calc_field.text != "":
            input_amount = float(self.calc_field.text)
            calc_result = (input_amount - (input_amount * self.iva_value) + \
                (input_amount * self.iva_ret) + (input_amount * self.isr_ret)) * \
                self.comp_value
            # round to 2 decimal places, convert to string, update
            self.calc_field.text = str(round(calc_result, 2))
        # If field is empty, just return
        else:
            self.calc_field.text = ""

class CalcRESICO(App):
    def build(self):
        return CalcAppRoot()

calcresico = CalcRESICO()
calcresico.run()
