from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder 

Builder.load_file('cameraCaptureApp.kv')

from filesharer import FileSharer 

class CameraScreen(Screen):
   
   def start(self):
      self.ids.camera.play = True

   def stop(self):
      self.ids.camera.play = False

   def capture(self):
      pass

class ImageScreen(Screen):
   pass

class RootWidget(ScreenManager):
   pass

class MainApp(App):

   def build(self):
      return RootWidget()
   
MainApp().run()

