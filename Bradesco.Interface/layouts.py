from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Determinado as cores
#      R  G  B  A / red green blue alpha → Opacidade 
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]
yellow = [1, 1, 0, 1]

# class MainAppExample(App):
#     def build(self):
#         layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
#         colors = [red, green, blue, purple, yellow]

#         for i in range(5):
#             btn = Button(text=f'Button {i+1}', background_color = colors[i])
            
#             layout.add_widget(btn)  # Adicionamos o botão ao layout

#         return layout
    
# if __name__ == '__main__':
#     MainAppExample().run()

#acrescentando um BTN 

class MainAppExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
        colors = [red, green, blue, purple, yellow]
        for i in range(5):
            btn = Button(text=f'Button {i+1}', background_color = colors[i])
            
            layout.add_widget(btn)  # Adicionamos o botão ao layout


            # mostra no terminal qual botão foi pressionado
            btn.bind(on_press=self.on_press_button)

        return layout
    
    def on_press_button(self, instance):
        print(f'Button {instance.text} was pressed')      #Mostra qual botão foi pressionado

if __name__ == '__main__':
    MainAppExample().run()




