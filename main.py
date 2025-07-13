import turtle
import random
import tkinter as tk

# ====DEĞİŞKENLER====
time = 20
Score = 0
time_d = 20.0
game_active = True
difficulty_map = {"easy": 1,"normal": 0.8,"hard": 0.5}
X = 0
difficulty_name = ""

# ====EKRAN====
my_screen = turtle.Screen()
my_screen.title("Catch_The_Turtle")
my_screen.bgcolor("light blue")
my_screen.setup(width=700,height=600)

FONT = ("Arial", 30, "normal")

# ====KAPLUMBAĞA NESNELERİ====
turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.speed(0)
turtle_instance.shapesize(1.5)
turtle_instance.penup()
turtle_instance.shape("turtle")

turtle_score = turtle.Turtle()
turtle_score.hideturtle()
turtle_score.penup()
turtle_score.speed(0)
turtle_score.goto(0,220)
turtle_score.color("yellow")

turtle_time = turtle.Turtle()
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.speed(0)
turtle_time.goto(0,250)
turtle_time.color("yellow")

turtle_finish = turtle.Turtle()
turtle_finish.hideturtle()
turtle_finish.penup()
turtle_finish.speed(0)
turtle_finish.goto(0,15)
turtle_finish.color("red")

turtle_final_score = turtle.Turtle()
turtle_final_score.hideturtle()
turtle_final_score.penup()
turtle_final_score.speed(0)
turtle_final_score.goto(0,-15)
turtle_final_score.color("green")

# ====OYUN FONKSİYONLARI====
def time_and_writings():
    global time, game_active
    if time > 0 and game_active:
        turtle_time.clear()
        turtle_time.write(f"Time:{time}", align="center", font=FONT)
        turtle_score.clear()
        turtle_score.write(f"Score:{Score}", align="center", font=FONT)
        time -= 1
        my_screen.ontimer(time_and_writings, 1000)
    else:
        game_active = False
        turtle_time.clear()
        turtle_score.clear()
        turtle_instance.hideturtle()
        turtle_finish.write("Time Finish", align= "center", font=FONT)
        turtle_final_score.write(f"Your Score:{Score}",align= "center", font=FONT)

def turtle_apper():
    global time_d
    if game_active:
        numX = random.randint(-325, 325)
        numY = random.randint(-275, 215)
        num = random.randint(1, 36)
        turtle_instance.right(10 * num)
        turtle_instance.goto(numX, numY)

        time_d -= X
        my_screen.ontimer(turtle_apper, int(X * 1000))

def click_turtle(x,y):
    global Score
    if game_active:
        Score += 1

# ====ZORLUK GİRİŞ PENCERESİ====

# NOT=> Bu kısımda ihtiyaç olduğundan "tkinter" kullanıldı

def get_difficulty():
    def submit():
        global X, difficulty_name
        diff = entry.get().lower() # ".get" ile entrydeki yazılacak yazı alınılır. ".lower" ile de yazılan yazı küçük formata dönüştürülür
        if diff in difficulty_map:
            X = difficulty_map[diff]
            difficulty_name = diff
            root.destroy()  # pencereyi kapat
            start_game()
        else:
            label_error.config(text="Please type: easy, normal or hard") #.config() metodu ile widget özellikleri sonradan değiştirilebilir.

    root = tk.Tk() # Bir pencere oluştururuz
    root.title("Choose Difficulty")
    root.geometry("300x150")

    label = tk.Label(root, text="Enter difficulty (easy, normal, hard):") # ".Label" belirtilen yazıyı gösteren bir "widget" yapar.
    label.pack(pady=10) # "pack" eklenilmesi istenilen şeyleri ekleme sırasına göre ekler.
                        # "pady" yazının üstünde ve altında belli bir piksel boşluk bırakır.

    entry = tk.Entry(root) # ".Entry" içine yazı yazılabilen bir "widget" yapar.
    entry.pack()
    entry.focus() # Bu satır, program pencere açılır açılmaz giriş kutusunun aktif (odaklanmış) olmasını sağlar.

    label_error = tk.Label(root, text="", fg="red")
    label_error.pack()

    send_button = tk.Button(root, text="Send", command=submit) # "command=submit" ile butona tıklanınca submit() fonksiyonu çalışacak.
    send_button.pack(pady=10)

    root.bind('<Return>', lambda event: submit())  # Enter tuşuna basınca da çalışır
    # "bind", Tkinter’da bir klavye ya da fare olayını (event) bir fonksiyona bağlamak demektir.
    # <Return> demek Enter
    # "lambda event: submit()" event parametresi gelse bile ben onu kullanmayacağım, sadece submit() fonksiyonunu çalıştıracağım anlamına gelir.

    root.mainloop() # Bu satır "tkinter" penceresini açar ve kullanıcı etkileşimlerini beklemeye başlar. Pencere kapatılana kadar kod buradan ilerlemez.

# ====OYUN BAŞLAT====
def start_game():
    turtle_instance.onclick(click_turtle)
    time_and_writings()
    turtle_apper()

# ====PROGRAM BAŞLAT====
get_difficulty()
my_screen.listen()
my_screen.mainloop()