from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Set the theme to dark
        return Builder.load_file("main-ui.kv")

if __name__ == "__main__":
    MainApp().run()
