from tkinter import filedialog 


def open_pressed(): 
    print("Open filename")
    filedialog.askopenfilename()  # 파일 불러오기는 버튼을 눌렀을 때 실행되게 



def run_pressed(): 
    print("Run pressed") 