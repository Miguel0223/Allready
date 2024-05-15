
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from Auth.LoginLogic import authenticate_user
from Auth.EmailLogic import send_email_with_otp, generate_otp, verify_otp
import smtplib
import random
import time
from kivy.clock import Clock
from kivy.core.window import Window



Window.minimum_width = 725
Window.minimum_height = 600
Window.resizable = False
    


   



"""-Notes:
| 1. Make email auth to send you to a one time page to create username and password and then send you to the main page                            |
| 2. Make the login screen a float layout to make it easier to center the widgets and make it responsive to window resizing.                      |
|
|
|
|
|
|
|
"""





class LoginScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

       
        
        
        
        with self.canvas.before:
            Color(0.07, 0.07, 0.07, 1)  # RGBA values
            # Create a RoundedRectangle that covers the entire window
            self.background = RoundedRectangle(pos=self.pos, size=(1920, 1080), radius=[0])
        
        with self.canvas.before:
            self.color = Color(0.14, 0.14, 0.14, 1)  # Grey color
           
            self.rect = RoundedRectangle(pos=(0, 0), radius=[10], size=(300, 600))
            
            self.bind(pos=self.update_rect, size=self.update_rect)

        # Schedule update_rect after the layout is initialized
        Clock.schedule_once(self.update_rect)

        # Sign In label
        self.add_widget(MDLabel(text='Sign In or Sign Up', theme_text_color="Custom", size_hint=(None, None),
                                text_color=(1, 1, 1, 1), font_style='H5',
                                size=(200, 30), pos_hint={'center_x': 0.5, 'top': 0.65}, ))

        
        
        # Username label and input
        self.username_input = MDTextField(size_hint=(None, None), size=(200, 70),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          helper_text="exmaple@gmail.com", helper_text_mode="on_focus",
                                          mode = "rectangle",
                                          width = 200,
                                          icon_right="account",  # Light grey icon color  
                                          hint_text="Username", 
                                          line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                          line_color_focus=(1, 1, 1, 1), 
                                          text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                          text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                          
                                          )   # Transparent line color in focus state
        
        self.add_widget(self.username_input)
        

       

    
        
        # Password label and input
        self.password_input = MDTextField(multiline=False, password=True, size_hint=(None, None), 
                                            helper_text="Password", helper_text_mode="on_focus",
                                            mode = "rectangle",
                                            icon_right="eye-off",  # Light grey icon color
                                            line_color_normal=((0.6, 0.6, 0.6, 1)), line_color_focus=(1, 1, 1, 1), # Transparent line color in normal 
                                            size=(200, 70), pos_hint={'center_x': 0.5, 'center_y': 0.35},
                                            hint_text_color=(0.5, 0.5, 0.5, 1),  # Light grey hint text color
                                            hint_text="Password")
        self.add_widget(self.password_input)

        # Login button
        self.login_button = MDRoundFlatButton(text='Login', size_hint=(None, None), size=(80, 40),
                                         pos_hint={'center_x': 0.43, 'center_y': 0.2}, on_press=self.handle_login,
                                            theme_text_color="Custom",
                                            line_color=(1, 1, 1, 1),  # White line color
                                              
                                         text_color=(1, 1, 1, 1))  # White text color
        self.add_widget(self.login_button)
    
        # Sign Up button
        self.signup_button = MDRoundFlatButton(text='Sign Up', size_hint=(None, None), size=(80, 40),
                                         pos_hint={'center_x': 0.57, 'center_y': 0.2},
                                         theme_text_color="Custom",
                                         line_color=(1, 1, 1, 1),  # White line color
                                         text_color=(1, 1, 1, 1))
        self.signup_button.bind(on_press=self.switch_to_signup)
        self.add_widget(self.signup_button)
    def switch_to_signup(self, instance):
        self.clear_widgets()
        signupScreen = SignUpScreen()
        self.add_widget(signupScreen)

    def handle_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if authenticate_user(username, password):
            print("Login successful!")
        else:
            print("Login failed. Invalid username or password.")
    
    def update_rect(self, *args):
        # Update position of the RoundedRectangle to keep it centered
        self.rect.pos = (self.center_x - self.rect.size[0] / 2, self.center_y - self.rect.size[1] / 2)
        # Update size of the RoundedRectangle to be a small square
        min_dimension = min(Window.width, Window.height)
        self.rect.size = (min_dimension * 0.6, min_dimension * 0.9) # 60% of the smallest dimension
        Clock.schedule_once(self.update_rect)

class SignUpScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)

        self.add_widget(MDLabel(text='-----------------Sign Up-----------------', theme_text_color="Custom", size_hint=(None, None),
                                text_color=(1, 1, 1, 1), font_style='Body1',
                                size=(200, 30), pos_hint={'center_x': 0.51, 'top': 0.65}, ))
        
        

        self.email_input = MDTextField(size_hint=(None, None), size=(200, 70),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.52},
                                          helper_text="exmaple@gmail.com", helper_text_mode="on_focus",
                                          mode = "rectangle",
                                          width = 200,
                                          icon_right="account",  # Light grey icon color  
                                          hint_text="Email", 
                                          line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                          line_color_focus=(1, 1, 1, 1), 
                                          text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                          text_color_focus=(1, 1, 1, 1), # White text color in focus state
                                          ) 
        self.add_widget(self.email_input)
    
        email = self.email_input.text

        


        

        self.continue_button = MDRoundFlatButton(text='Continue', size_hint=(None, None), size=(80, 40),
                                         pos_hint={'center_x': 0.57, 'center_y': 0.18}, 
                                            theme_text_color="Custom",
                                            line_color=(1, 1, 1, 1),  # White line color
                                            
                                         text_color=(1, 1, 1, 1))
        self.add_widget(self.continue_button)
        self.continue_button.bind(on_press=self.send_otp)
        self.continue_button.bind(on_press=self.switch_to_otp)
    
        
        

        



        self.back_button = MDRoundFlatButton(text='Back', size_hint=(None, None), size=(80, 40),
                                         pos_hint={'center_x': 0.43, 'center_y': 0.18}, 
                                            theme_text_color="Custom",
                                            line_color=(1, 1, 1, 1),  # White line color
                                              
                                         text_color=(1, 1, 1, 1))
        self.back_button.bind(on_press=self.switch_to_login)
        self.add_widget(self.back_button)


    
    
    
    def switch_to_login(self, instance):
        self.clear_widgets()
        backScreen = LoginScreen()
        self.add_widget(backScreen)
    
    def switch_to_otp(self, instance):
        self.clear_widgets()
        otp_Screen = otpScreen()
        self.add_widget(otp_Screen)

    def send_otp(self, instance):

        email = self.email_input.text

        otp = generate_otp()

        send_email_with_otp(email, otp)

class otpScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(otpScreen, self).__init__(**kwargs)
        self.add_widget(MDLabel(text='-----------------Enter OTP-----------------', theme_text_color="Custom", size_hint=(None, None),
                                text_color=(1, 1, 1, 1), font_style='Body1',
                                size=(200, 30), pos_hint={'center_x': 0.51, 'top': 0.65}, ))
        


        self.otp_digit_one = MDTextField(size_hint=(None, None), size=(40, 70),
                                            
                                            id="digit1",
                                            input_filter="int",
                                            max_text_length=1,
                                            
                                            pos_hint={'center_x': 0.36, 'center_y': 0.36},
                                            mode = "rectangle",
                                             # Light grey icon color
                                            line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                            line_color_focus=(1, 1, 1, 1),  # Transparent line color in focus state
                                            text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                            text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                            
                                             )
        self.add_widget(self.otp_digit_one)



        self.otp_digit_two = MDTextField(size_hint=(None, None), size=(40, 70),
                                            
                                            id="digit2",
                                            input_filter="int",
                                            max_text_length=1,
                                            
                                            pos_hint={'center_x': 0.42, 'center_y': 0.36},
                                            mode = "rectangle",
                                             # Light grey icon color
                                            line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                            line_color_focus=(1, 1, 1, 1),  # Transparent line color in focus state
                                            text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                            text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                             )
        self.add_widget(self.otp_digit_two)


        self.otp_digit_three = MDTextField(size_hint=(None, None), size=(40, 70),
                                            
                                            id="digit3",
                                            input_filter="int",
                                            max_text_length=1,
                                            
                                            pos_hint={'center_x': 0.48, 'center_y': 0.36},
                                            mode = "rectangle",
                                             # Light grey icon color
                                            line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                            line_color_focus=(1, 1, 1, 1),  # Transparent line color in focus state
                                            text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                            text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                             )
        self.add_widget(self.otp_digit_three)

        self.otp_digit_four = MDTextField(size_hint=(None, None), size=(40, 70),
                                            
                                            id="digit4",
                                            input_filter="int",
                                            max_text_length=1,
                                            
                                            pos_hint={'center_x': 0.54, 'center_y': 0.36},
                                            mode = "rectangle",
                                             # Light grey icon color
                                            line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                            line_color_focus=(1, 1, 1, 1),  # Transparent line color in focus state
                                            text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                            text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                             )
        self.add_widget(self.otp_digit_four)

        self.otp_digit_five = MDTextField(size_hint=(None, None), size=(40, 70),
                                            
                                            id="digit5",
                                            input_filter="int",
                                            max_text_length=1,
                                            
                                            pos_hint={'center_x': 0.60, 'center_y': 0.36},
                                            mode = "rectangle",
                                             # Light grey icon color
                                            line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                            line_color_focus=(1, 1, 1, 1),  # Transparent line color in focus state
                                            text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                            text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                             )
        self.add_widget(self.otp_digit_five)

        self.otp_digit_six = MDTextField(size_hint=(None, None), size=(40, 70),
                                            
                                            id="digit6",
                                            input_filter="int",
                                            max_text_length=1,
                                            
                                            pos_hint={'center_x': 0.66, 'center_y': 0.36},
                                            mode = "rectangle",
                                             # Light grey icon color
                                            line_color_normal=(0.6, 0.6, 0.6, 1),  # Transparent line color in normal state
                                            line_color_focus=(1, 1, 1, 1),  # Transparent line color in focus state
                                            text_color_normal=(0.6, 0.6, 0.6, 1),  # White text color in normal state
                                            text_color_focus=(1, 1, 1, 1),  # White text color in focus state
                                            
                                        

                                             )
        self.add_widget(self.otp_digit_six)
        
        opt_user_input = self.otp_digit_one.text + self.otp_digit_two.text + self.otp_digit_three.text + self.otp_digit_four.text + self.otp_digit_five.text + self.otp_digit_six.text

        if opt_user_input:
            if verify_otp(opt_user_input):
                print("OTP verified!")
            else:
                print("Invalid OTP. Please try again.")

        self.verify_button = MDRoundFlatButton(text='Verify', size_hint=(None, None), size=(80, 40),
                                         pos_hint={'center_x': 0.57, 'center_y': 0.18}, 
                                            theme_text_color="Custom",
                                            line_color=(1, 1, 1, 1),  # White line color
                                            
                                         text_color=(1, 1, 1, 1))
        self.add_widget(self.verify_button)
        verify_otp()
        self.verify_button.bind(on_press=self.verify_otp)

        


        
    
    
    

        
        
        

