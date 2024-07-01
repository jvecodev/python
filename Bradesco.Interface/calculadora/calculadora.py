from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from math import sqrt

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculadora, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.solucao = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.add_widget(self.solucao)
        
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '√']
        ]
        
        for linha in botoes:
            h_layout = BoxLayout()
            for label in linha:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)
    
    def on_button_press(self, instance):
        current = self.solucao.text
        button_text = instance.text
        
        if button_text == 'C':
            self.solucao.text = ''
        elif button_text == '=':
            try:
                self.solucao.text = str(eval(self.solucao.text))
            except:
                self.solucao.text = 'Erro'
        elif button_text == '√':
            if current:
                try:
                    num = float(current)
                    if num >= 0:
                        self.solucao.text = str(sqrt(num))
                    else:
                        self.solucao.text = 'Erro'
                except ValueError:
                    self.solucao.text = 'Erro'
        else:
            self.solucao.text += button_text

class CalculadoraApp(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    CalculadoraApp().run()
