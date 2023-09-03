from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Set the theme to dark
        return Builder.load_file("main-ui.kv")

    # def build_card(drink_data):
    #       MDCard:
    #             id: 1
    #             orientation: "vertical"
    #             size_hint: None, None
    #             size: "200dp", "200dp"
    #             pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    #             BoxLayout:
    #                 orientation: "vertical"

    #                 MDLabel:
    #                     text: "Tile 1"
    #                     theme_text_color: "Primary"
    #                     font_size: "20sp"
    #                     halign: "center"
    #                     valign: "middle"


if __name__ == "__main__":
    MainApp().run()
