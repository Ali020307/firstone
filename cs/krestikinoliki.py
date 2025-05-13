import tkinter

def set_tile(row, column):
  global tekush_oyinchi
  if (game_over):
    return
  
  if doska[row][column]["text"] != "":
     #Already taken spot
    return

  doska[row][column]["text"] = tekush_oyinchi#
  
  if tekush_oyinchi ==  oyinchi0: #solishtruv
    tekush_oyinchi = oyinchiX
  else:
    tekush_oyinchi =oyinchi0

  lable["text"] = tekush_oyinchi+" navbati"
 
  #check winner

  check_winner()
def check_winner():
  global navbat, game_over
  navbat += 1

  #Gorizontal, check 3 rows

  for row in range(3):
    if (doska[row][0]["text"] == doska[row][1]["text"] == doska[row][2]["text"]
      and doska[row][0]["text"] !=""):
      lable.config(text=doska[row][0]["text"] +" G'olib boldi! ", foreground = rang_sariq)
      for column in range(3):
        doska[row][column].config(foreground = rang_sariq, background = rang_tyomniy_seriy)
      game_over = True
      return

  #Vertikal, check 3 columns
  for column in range(3):
    if (doska[0][column]["text"] == doska[1][column]["text"] == doska[2][column]["text"]
      and doska[0][column]["text"] != ""):
      lable.config(text=doska[0][column]["text"] + " G'olib boldi! ", foreground = rang_sariq)
      for row in range(3):
                doska[row][column].config(foreground = rang_sariq, background = rang_tyomniy_seriy)
      game_over = True
      return
  #Dioganal
  if (doska[0][0]["text"] == doska[1][1]["text"] == doska[2][2]["text"]
    and doska[0][0]["text"] != ""):
    lable.config(text=doska[0][0]["text"] + " G'olib boldi! ", foreground = rang_sariq)
    for i in range(3):
      doska[i][i].config(foreground = rang_sariq, background = rang_tyomniy_seriy)
    game_over = True
    return
  #anti-deoganal
  if (doska[0][2]["text"] == doska[1][1]["text"] == doska[2][0]["text"]
    and doska[0][2]["text"] != ""):
    lable.config(text=doska[0][2]["text"] + " G'olib boldi! ", foreground = rang_sariq)
    doska[0][2].config(foreground = rang_sariq, background = rang_tyomniy_seriy)
    doska[1][1].config(foreground = rang_sariq, background = rang_tyomniy_seriy)
    doska[2][0].config(foreground = rang_sariq, background = rang_tyomniy_seriy)
    game_over = True
    return

  #tie condition
  if (navbat == 9):
    game_over = True
    lable.config(text=" Durang ", foreground = rang_sariq)


def yangi_oyin():
  global navbat, game_over

  navbat = 0
  game_over = False

  lable["text"] = tekush_oyinchi +" navbati"
  
  for row in range(3):
    for column in range(3):
      doska[row][column].config(text = "", foreground = rang_kok,background = bgrang_seriy)



#game setup
oyinchiX = "x"
oyinchi0 = "0"
tekush_oyinchi = oyinchiX
doska = [[0,0,0],
         [0,0,0],
         [0,0,0]]

rang_kok = "#4584b6"
rang_sariq = "#ffde57"
bgrang_seriy = "#343434"
rang_tyomniy_seriy = "#646464"

navbat = 0
game_over = False

#window setup

window = tkinter.Tk()# oyin oynasini yaratish
window.title("Krestiki Noliki")
window.resizable(False, False)

frame = tkinter.Frame(window)
lable = tkinter.Label(frame, text = tekush_oyinchi+" navbati ", font=("Consolas", 20), background=bgrang_seriy,
            foreground="white")
lable.grid(row=0, column=0, columnspan=3,sticky="we")

for row in range(3):
  for column in range(3):
    doska[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                      background=bgrang_seriy, foreground = rang_kok, width = 4, height = 1,
                      command = lambda row=row, column=column: set_tile(row, column))
    doska[row][column].grid(row=row+1, column=column)                  
frame.pack()

knopka = tkinter.Button(frame, text="Takrorlash", font=("Consolas", 20), background=bgrang_seriy,
            foreground="white", command=yangi_oyin)
knopka.grid(row=4, column=0,columnspan=3, sticky="we")

#window the window
window.update
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (screen_height/2))

window.mainloop()