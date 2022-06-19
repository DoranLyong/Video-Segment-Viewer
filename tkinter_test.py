import tkinter as tk
from tkinter import filedialog 
#from tools.buttons import open_pressed, run_pressed




def open_pressed(): 
    print("Open filename")
    filedialog.askopenfilename()  # 파일 불러오기는 버튼을 눌렀을 때 실행되게 



def run_pressed(): 
    print("Run pressed") 





# == 루트 윈도우 생성 == # 
# ----------------------
W, H = 800, 600 
root = tk.Tk()  #Tk 객체 생성. 기본 윈도우 객체
root.title("Show video segments") # 윈도우 이름 
root.geometry(f"{W}x{H}")  # 윈도우 크기 



# == 버튼 만들기 (Master 설정 필요) == # 
# ----------------------------------
button = tk.Button(
    master=root, 
    text="Open video",  
#    bg="black", 
#    fg="white", 
    width = 12, 
    height= 3, 
    font=("Arial", 15),
    command= open_pressed, # 이벤트 입력 
    )

# 버튼 배치 
button.place(x=0, y=0, width=200, height=50) 



# == NUM_SEGMENTS Entry로 텍스트 입력받기 == # 
# ----------------------------
label = tk.Label(master=root, text="NUM_SEGMENTS", width=15, font=("Arial", 15))

num_seg_entry = tk.Entry(
    master=root,
#    bg="black",
#    fg="white",
    width=10,
    justify="center",
    font=("Arial", 15)
)
num_seg_entry.icursor("end")

# entry 배치 
loc_y = 100
label.place(x=0, y=loc_y)
num_seg_entry.place(x=0, y=loc_y+50)


# == Sampling method 옵션 선택 버튼 == # 
# -----------------------------------
""" 샘플링 옵션 선택 
"""




# == Run 버튼 만들기 == # 
# -----------------------
""" 입력된 옵션에 따라 Matplotlib가 실행됨. 
""" 
run_button = tk.Button(
    master=root, 
    text="Run",  
#    bg="black", 
#    fg="white", 
    width = 12, 
    height= 3, 
    font=("Arial", 15),
    command= run_pressed, # 이벤트 입력 
    )

run_button.place(x=0, y=H-100)



# 메인 루프 실행 
root.mainloop()