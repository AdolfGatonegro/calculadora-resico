from __future__ import division
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

class CalcAppRoot(BoxLayout):

   # Tax and retention values 
    iva_value = 0.16
    isr_value = 0.0125
    iva_ret = 0.1067
    isr_ret = isr_value
    comp_value = 1.001667416

    def __init__(self):
        super(CalcAppRoot, self).__init__()

    def calc_eval_net(self):
        input_amount = float(self.calc_field.text)
        calc_result = input_amount + (input_amount * self.iva_value) - (input_amount * self.iva_ret) - (input_amount * self.isr_ret)
        self.calc_field.text = str(round(calc_result, 2))
        
    def calc_eval_gross(self):
        input_amount = float(self.calc_field.text)
        calc_result = (input_amount - (input_amount * self.iva_value) + (input_amount * self.iva_ret) + (input_amount * self.isr_ret)) * self.comp_value
        self.calc_field.text = str(round(calc_result, 2))
class CalcRESICO(App):
    def build(self):
        return CalcAppRoot()

calcresico = CalcRESICO()
calcresico.run()
