import tkinter as tk
from pynput import keyboard
import file_management.file_manager as file_manager
import image_management.screen_manager as screen
from tkinter import filedialog

class OverlayWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.attributes("-transparentcolor", "white")
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.geometry('+0+0')

        self.panel = tk.Frame(self, bg='white')
        self.panel.grid(row=0, column=0, sticky='ew')

        menuconverter = self.create_menubutton("Converter", [("To_CSV", file_manager.to_csv), ("To_PDF", file_manager.to_pdf)])
        menuconverter.grid(row=0, column=0)

        menubutton2 = self.create_menubutton("Screen", [("Capture", screen.capture_screen), ("Option", self.option1)])
        menubutton2.grid(row=0, column=1)

        self.buttons = [menuconverter, menubutton2]

        self.panel_visible = True

        self.listener = keyboard.Listener(on_release=self.on_key_release)
        self.listener.start()

    def create_menubutton(self, text, options):
            menubutton = tk.Menubutton(self.panel, text=text, bg='#f8f8f8')
            menu = tk.Menu(menubutton, tearoff=False)
            menubutton.configure(menu=menu)
            for option, command in options:
                menu.add_command(label=option, command=command)
            return menubutton

    def option1(self):
        print("Option 1 selected")

    def on_key_release(self, key):
        if key == keyboard.Key.esc:
            self.toggle_panel()

    def toggle_panel(self):
        if self.panel_visible:
            for button in self.buttons:
                button.grid_remove()
        else:
            for button in self.buttons:
                button.grid()
        self.panel_visible = not self.panel_visible

if __name__ == "__main__":
    app = OverlayWindow()
    app.mainloop()