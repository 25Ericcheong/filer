import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

class App:
  def __init__(self, root):
    self.root = root    
    self.root.title("Filer processing application")
    self.root.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    # frame/container creation
    self.main_frame = tk.Frame(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='white')
    
    # widgets creation
    self.descriptive_label = tk.Label(self.main_frame, text="Ensure selected file is a .csv file")
    self.process_button = tk.Button(self.main_frame, text="Process file", command=self.close_window)
    self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.close_window)
    
    # widgets pack
    self.descriptive_label.pack()
    self.process_button.pack()
    self.quit_button.pack()
    
    # widgets placement
    
    # pack frames
    self.main_frame.pack(side="left", expand=1)
    
  def close_window(self):
    self.root.destroy()

def main():
  root = tk.Tk()
  app = App(root)
  root.mainloop()

if __name__ == "__main__":  
  main()
