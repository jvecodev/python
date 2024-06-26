

# from kivy.app import App
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):
#         return Label(text='To chegando seus bunda suja ')

# if __name__ == '__main__':
#     MyApp().run()
# from kivy.app import App
# from kivy.uix.label import Label

# class MainApp(App):
#     def build(self):
#         return Label (text='To chegando seus bunda suja')

# if __name__ == '__main__':
#     MainApp().run()

#com img

from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        # return Image(source='logo.png')
        return AsyncImage(source='https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')

if __name__ == '__main__':
    MainApp().run()
    
