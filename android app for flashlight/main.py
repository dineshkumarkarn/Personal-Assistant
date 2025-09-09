from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import flashlight
import socket
import threading

class HomeAssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.flashlight_button = Button(text="Toggle Flashlight", font_size=32)
        self.flashlight_button.bind(on_press=self.toggle_flashlight)
        layout.add_widget(self.flashlight_button)
        
        threading.Thread(target=self.start_server).start()
        return layout

    def toggle_flashlight(self, instance):
        if not hasattr(self, 'flashlight_on'):
            self.flashlight_on = False
        if self.flashlight_on:
            flashlight.off()
            self.flashlight_on = False
            self.flashlight_button.text = "Turn On Flashlight"
        else:
            flashlight.on()
            self.flashlight_on = True
            self.flashlight_button.text = "Turn Off Flashlight"

    def handle_command(self, command):
        if "flashlight on" in command:
            flashlight.on()
            self.flashlight_button.text = "Turn Off Flashlight"
            self.flashlight_on = True
        elif "flashlight off" in command:
            flashlight.off()
            self.flashlight_button.text = "Turn On Flashlight"
            self.flashlight_on = False

    def start_server(self):
        host = "0.0.0.0"
        port = 12345
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with conn:
                    command = conn.recv(1024).decode()
                    self.handle_command(command)

if __name__ == '__main__':
    HomeAssistantApp().run()
