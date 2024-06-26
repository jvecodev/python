from kivy.app import App
from kivy.uix.button import Button

class MainAppExample(App):
    def build(self):
        button =  Button(text='Hello World')
        size_hint = (0.5, 0.5)
        pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        button.bind(on_press=self.on_press_button)  # Evento de clique

        return button

    def on_press_button(self, instance):
        print(f'Button  was pressed')


if __name__ == '__main__':
    MainAppExample().run()