from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests


Builder.load_file('frontend.kv')

class FirstScreen(Screen):
   def search_image(self):
      #TODO: create a function that search image on web   

      image_prompt = self.manager.current_screen.ids.prompt.text
      image_output = None 

      print(image_prompt)

      r = requests.post('https://clipdrop-api.co/text-to-image/v1',
      files = {
         'prompt': (None,  str(image_prompt), 'text/plain')
      },
      headers = { 'x-api-key': '7ac8f650829f27963b2e9bb26eb6446e1d56d743c7dbfa5aac578738f96a33085aa44d3ed00e9a543efe4abace39dc7b'}
      )
      if (r.ok):
         # r.content contains the bytes of the returned image
         image_output = r.content
         
         with open("files/autoImage.png", "wb") as file:
            file.write(r.content)

      else:
         r.raise_for_status()


      self.manager.current_screen.ids.img.source = 'files/autoImage.png'
      pass


class RootWidget(ScreenManager):
   pass

class MainApp(App):

   def build(self):
      return RootWidget()
   
MainApp().run()

