from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class RootElement(BoxLayout):
	pass

class MyNavBar(BoxLayout):
	pass

class MyNavigator(ScreenManager):
	pass

class Home(Screen):
	pass


class Video_player_screen(Screen):
	pass


class Config(Screen):
	pass

class Reports(Screen):
	pass
	
class MainApp(App):
	def build(self):
		self.icon = 'logo.png'
		return RootElement()

MainApp().run()
# Button:
#
#             # text which will appear on button
#             text:"Watch online videos"
#             on_release:
#                 # importing webbrowser module
#                 import webbrowser
#                 # it will open google window in your browser
#                 webbrowser.open('https://www.youtube.com/watch?v=5KJH5fuF9zc')