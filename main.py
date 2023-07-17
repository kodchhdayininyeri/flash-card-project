BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
current_card={}
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")





def next_card():
    global current_card

    current_card=random.choice(to_learn)
    title=current_card["French"]

    my_canvas.itemconfig(card_word,text=title,fill="black")
    my_canvas.itemconfig(card_title, text="French",fill="black")
    my_canvas.itemconfig(card_background,image=card_font_img)
    window.after(3000,flip_card)

def flip_card():
    my_canvas.itemconfig(card_title,text="English",fill="white")
    my_canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    my_canvas.itemconfig(card_background,image=card_back_image)

def is_known():
    to_learn.remove(current_card)

    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()




window=Tk()
window.title("Flashy")
window.size()
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
window.after(3000,func=flip_card)


my_canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back_image=PhotoImage(file="images/card_back.png")
card_font_img=PhotoImage(file="images/card_front.png")
card_background=my_canvas.create_image(400,263,image=card_font_img)
card_title=my_canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=my_canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
my_canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="images/right.png",)
known_button=Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)
next_card()


window.mainloop()

