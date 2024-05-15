from kivymd.app import MDApp
from GUI.LoginScreen import LoginScreen
from GUI.LoginScreen import SignUpScreen
from GUI.LoginScreen import otpScreen
from Auth.UserDataBase import UserDatabase


class MyApp(MDApp):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()


