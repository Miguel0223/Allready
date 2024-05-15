from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class AllreadyLoginLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(AllreadyLoginLayout, self).__init__(**kwargs)
        
        # minimum window size
        Window.minimum_height = 768
        Window.minimum_width = 1024

        # Username label and input
        self.add_widget(Label(text='Username:', size_hint = (None, None), size = (100, 30)))
        self.username_input = TextInput(size_hint = (None, None), size = (200, 30))
        self.add_widget(self.username_input)

        # Password label and input
        self.add_widget(Label(text = 'Password:', size_hint=(None, None), size = (100, 30)))
        self.password_input = TextInput(password=True, size_hint = (None, None), size = (200, 30))
        self.add_widget(self.password_input)

        # Login button
        self.login_button = Button(text = 'Login', size_hint=(None, None), size=(80, 40), on_press = self.login)
        self.add_widget(self.login_button)

        # Create account button
        self.create_account_button = Button(text = 'Create Account', size_hint = (None, None), size = (120, 40), on_press = self.create_account)
        self.add_widget(self.create_account_button)

        # Forgot password button
        self.forgot_password_button = Button(text = 'Forgot Password', size_hint=(None, None), size =(180, 40), on_press = self.forgot_password)
        self.add_widget(self.forgot_password_button)

        # Calculate the center point based on the window size
        self.update_positions()

        # Bind the update_positions method to be called whenever the window is resized
        Window.bind(on_resize=self.update_positions)

    def update_positions(self, *args):
        # Update the center point and reposition the widgets when the window is resized
        self.center_x = Window.width / 2
        self.center_y = Window.height / 2

        self.username_input.pos = (self.center_x, self.center_y)
        self.password_input.pos = (self.center_x, self.center_y - 50)
        self.login_button.pos = (self.center_x - 80, self.center_y - 100)
        self.create_account_button.pos = (self.center_x + 40, self.center_y - 100)
        self.forgot_password_button.pos = (self.center_x - 60, self.center_y - 150)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        #login logic

    def create_account(self, instance):
        #create account logic
        print("Create Account clicked")

    def forgot_password(self, instance):
        #forgot password logic
        print("Forgot Password clicked")

class AllreadyLoginApp(App):
    def build(self):
        return AllreadyLoginLayout()

if __name__ == '__main__':
    AllreadyLoginApp().run()

