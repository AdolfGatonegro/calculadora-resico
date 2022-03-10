from __future__ import division
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
    comp_value = 1.001667416

    def __init__(self):
        super(CalcAppRoot, self).__init__()

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

    def calc_field_clear(self):
        self.calc_field.text = ""

    def calc_eval_net(self):
        if self.calc_field.text != "":
            input_amount = float(self.calc_field.text)
            calc_result = input_amount + (input_amount * self.iva_value) - (input_amount * self.iva_ret) - (input_amount * self.isr_ret)
            self.calc_field.text = str(round(calc_result, 2))
        else:
            self.calc_field.text = ""
        
    def calc_eval_gross(self):
        if self.calc_field.text != "":
            input_amount = float(self.calc_field.text)
            calc_result = (input_amount - (input_amount * self.iva_value) + (input_amount * self.iva_ret) + (input_amount * self.isr_ret)) * self.comp_value
            self.calc_field.text = str(round(calc_result, 2))
        else:
            self.calc_field.text = ""

class CalcRESICO(App):
    def build(self):
        return CalcAppRoot()

calcresico = CalcRESICO()
calcresico.run()
