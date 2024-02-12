import tkinter as tk
from tkinter import filedialog
import pyautogui

def capture_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    root.wait_visibility(root)
    root.wm_attributes('-alpha',0.3)  
    canvas = tk.Canvas(root, cursor="cross", bg="grey75")
    canvas.pack(fill=tk.BOTH, expand=True)

    def on_mouse_press(event):
        global start_x, start_y
        start_x = event.x
        start_y = event.y
        canvas.delete("rect")
        canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", tag="rect")

    def on_mouse_drag(event):
        global start_x, start_y
        end_x = event.x
        end_y = event.y
        canvas.coords("rect", start_x, start_y, end_x, end_y)

    def on_mouse_release(event):
        global start_x, start_y
        end_x = event.x
        end_y = event.y
        canvas.delete("rect")
        left = min(start_x, end_x)
        top = min(start_y, end_y)
        width = abs(start_x - end_x)
        height = abs(start_y - end_y)
        region = (left, top, left + width, top + height)

        output_file = filedialog.asksaveasfilename(defaultextension=".png")
        if not output_file:
            return
        
        root.destroy()

        screenshot = pyautogui.screenshot(region=region)

        screenshot.save(output_file)

    canvas.bind("<ButtonPress-1>", on_mouse_press)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_release)

    root.mainloop()