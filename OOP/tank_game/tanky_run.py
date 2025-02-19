import tkinter

window = tkinter.Tk()

window.config(bg='white')
window.title("Clock")
window.geometry('1430x900')
window.resizable(0, 1)


tkinter.Label(window, text="Time For War !", font=("Arial", 40), fg='black').pack()


class destroyer_tank:
    def __init__(self,name,hp,ammo):
        self.name = name
        self.hp = hp
        self.ammo = ammo
    def fire(self):
        print(f"{self.name} fired")
    def move_up(self):
        pass
    def move_down(self):
        pass
    def move_left(self):
        pass
    def move_right(self):
        pass
class target:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def position(self):
        pass
window.mainloop()