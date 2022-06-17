import tkinter as tk

from tools.utils import open_pressed, run_pressed



# == 루트 윈도우 생성 == # 
# ----------------------
root = tk.Tk()  #Tk 객체 생성. 기본 윈도우 객체
root.title("Show video segments") # 윈도우 이름 
root.geometry("800x600")  # 윈도우 크기 



# == 버튼 만들기 (Master 설정 필요) == # 
# ----------------------------------
button = tk.Button(
    master=root, 
    text="Open video",  
#    bg="black", 
#    fg="white", 
    width = 12, 
    height= 3, 
    font=("Modern", 10),
    command= open_pressed, # 이벤트 입력 
    )

# 버튼 배치 
button.pack(side="right", anchor="n") # LEFT, RIGHT, TOP, BOTTOM



# == Entry로 텍스트 입력받기 == # 
# ----------------------------
label = tk.Label(master=root, text="NUM_SEGMENTS", width=30, font=("Arial", 10))

entry = tk.Entry(
    master=root,
#    bg="black",
#    fg="white",
    width=10,

    justify="center",
    font=("Arial", 10)
)
entry.icursor("end")

# entry 배치 
entry.pack(side="right", anchor="e")
label.pack(side="right", anchor="ne")


# == Run 버튼 만들기 == # 
run_button = tk.Button(
    master=root, 
    text="Run",  
#    bg="black", 
#    fg="white", 
    width = 12, 
    height= 3, 
    font=("Modern", 10),
    command= run_pressed, # 이벤트 입력 
    )

run_button.pack(side="bottom", anchor="center")



# 메인 루프 실행 
root.mainloop()