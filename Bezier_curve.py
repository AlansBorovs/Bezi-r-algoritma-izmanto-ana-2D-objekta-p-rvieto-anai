import tkinter as tk
from tkinter import Canvas, Scale, HORIZONTAL, Frame

# Bezier līknes funkcija
def bezier(t, points):
    A, B, C = points
    x = (1 - t)**2 * A[0] + 2 * (1 - t) * t * B[0] + t**2 * C[0]
    y = (1 - t)**2 * A[1] + 2 * (1 - t) * t * B[1] + t**2 * C[1]
    return x, y

# Izveido galveno logu
root = tk.Tk()
canvas = Canvas(root, width=500, height=500, bg='white')  # Izveido audeklu
canvas.pack()

# Inicializē vadības punktus
control_points = []

# Funkcija, lai pievienotu vadības punktus
def add_point(event):
    if len(control_points) < 3:
        control_points.append((event.x, event.y))
        canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='red')  # Palielina punkta izmēru
        if len(control_points) == 1:
            canvas.create_text(event.x, event.y+10, text="A", fill="black")  # Pievieno tekstu "A"
        elif len(control_points) == 3:
            canvas.create_text(event.x, event.y+10, text="B", fill="black")  # Pievieno tekstu "B"
            draw_curve()  # Zīmē līkni

# Funkcija, lai zīmētu Bezier līkni
def draw_curve():
    points = []
    for t in range(0, 101):
        x, y = bezier(t/100, control_points)
        points.append(x)
        points.append(y)
    canvas.create_line(points, fill='black', width=2)  # Palielina līnijas biezumu

# Funkcija, lai atiestatītu vadības punktus
def reset_points(event):
    global control_points
    control_points = []
    canvas.delete('all')  # Dzēš visu audekla saturu

# Funkcija, lai animētu objektu
def animate_object(t=0, obj=None):
    global animating
    if len(control_points) >= 3:
        if obj is not None:
            canvas.delete(obj)  # Dzēš iepriekšējo objektu
        if t <= 1:
            x, y = bezier(t, control_points)
            obj = canvas.create_oval(x-10, y-10, x+10, y+10, fill='blue')  # Palielina aplīša izmēru
            root.after(int(speed_scale.get()), animate_object, t+0.01, obj)  # Regulē ātrumu
        else:
            animating = False
            start_button.config(state="normal")  # Iespējo sākuma pogu

# Saista funkcijas ar audeklu
canvas.bind('<Button-1>', add_point)  # Saista kreisās peles pogas klikšķi ar add_point funkciju
canvas.bind_all('r', reset_points)  # Saista "r" taustiņu ar reset_points funkciju

# Pievieno sākuma pogu
animating = False
def start_animation():
    global animating
    if not animating and len(control_points) >= 3:
        animating = True
        start_button.config(state="disabled")  # Atspējo sākuma pogu
        animate_object()  # Sāk animāciju

start_button = tk.Button(root, text='Start', command=start_animation)  # Izveido sākuma pogu
start_button.pack(side='left')

# Pievieno ātruma slīdni
speed_scale = Scale(root, from_=1, to=100, orient=HORIZONTAL, label='Ātrums')  # Izveido ātruma slīdni
speed_scale.set(50)  # Noklusējuma ātrums
speed_scale.pack(side='left')

# Pievieno + un - pogas, lai regulētu ātrumu
def increase_speed():
    speed_scale.set(min(speed_scale.get() + 1, 100))  # Palielina ātrumu

def decrease_speed():
    speed_scale.set(max(speed_scale.get() - 1, 1))  # Samazina ātrumu

button_frame = Frame(root)  # Izveido pogu rāmi
button_frame.pack(side='left')

plus_button = tk.Button(button_frame, text='+', command=increase_speed)  # Izveido + pogu
plus_button.pack(side='left')

minus_button = tk.Button(button_frame, text='-', command=decrease_speed)  # Izveido - pogu
minus_button.pack(side='left')

root.mainloop()  # Sāk galvenā loga cilpu
