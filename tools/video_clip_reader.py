import os 
import os.path as osp
import math 

import decord
from decord import VideoReader
from decord import cpu 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid  # (ref) https://matplotlib.org/2.1.2/mpl_toolkits/index.html

from tkinter import Tk
import tkinter as tk


class VideoClipReader(Tk):

    def __init__(self, path):
        super(VideoClipReader, self).__init__()

        self.video_path = path 
        self.NUM_SEGMENTS = None
        self.frames = None


        # == Tkinter 루트 윈도우 생성 == # 
        # ------------------------
        W, H = 800, 600 
        self.title("Show video segments") # 윈도우 이름 
        self.geometry(f"{W}x{H}")  # 윈도우 크기 

        self.label = tk.Label(master=self, text="NUM_SEGMENTS", width=15, font=("Arial", 15))
        self.num_seg_entry = tk.Entry( master=self, width=10, justify="center", font=("Arial", 15) )



        # == Run 버튼 만들기 == # 
        # ----------------------
        """ 입력된 옵션에 따라 Matplotlib가 실행됨. 
        """ 
        self.run_button = tk.Button( master=self, text="Run",  width = 12, height= 3, font=("Arial", 15), command= self.run_pressed)


        # == 위젯 배치 == # 
        # ---------------
        self.label.pack()
        self.num_seg_entry.pack()
        self.run_button.pack()


    def run_pressed(self):
        self.NUM_SEGMENTS = int(self.num_seg_entry.get())
        print(f"NUM_SEGMENTS: {self.NUM_SEGMENTS}")


        self.frames = self.load_video_array(self.video_path, self.NUM_SEGMENTS)
        print(len(self.frames))

        self.plot_video(plot_width=20., plot_height=4., title='Evenly Sampled Frame Clip, No Video Transform')



    def load_video_array(self, path, NUM_SEGMENTS = 8):

        with open(path, 'rb') as f: 
            vr = VideoReader(f, ctx=cpu(0))

        # -----------------------------------
        print(f"Video frames: {len(vr)}")
    #    print(f"type: {type(vr[0])}")
    #    print(f"frame shape: {vr[0].shape}")

        # == frame sampling == # 
        num_seg = NUM_SEGMENTS
        step = int(len(vr)//num_seg)
        indices = [idx for idx in range(0, len(vr), step)] # evenly sampling frames 

        print(f"step_size:{step}")
        print(f"selected frames: {indices}")

        # To get multiple frames at once, use get_batch
        # this is the efficient way to obtain a long list of frames
        frames = vr.get_batch(indices).asnumpy()

        # ---------------- 
        print(f"frame batch: {frames.shape}")
        return frames        



    def plot_video(self, plot_width, plot_height, title: str):
        frame_list = self.frames 
        n_frame = len(frame_list)
        col_size = 8 # column size 

        # design grid size 
        # ---------------
        if n_frame > col_size:
            cols = col_size
            rows = math.ceil(n_frame / col_size)
        else:             
            rows = 1 
            cols = n_frame

        # plots 
        # ---------------            
        fig = plt.figure(figsize=(plot_width, plot_height))
        grid = ImageGrid(fig, 111,  # similar to subplot(111)
                         nrows_ncols=(rows, cols),  # creates 2x2 grid of axes
                         axes_pad=0.3,  # pad between axes in inch.
                         )

        for index, (ax, im) in enumerate(zip(grid, frame_list)):
            # Iterating over the grid returns the Axes.
            ax.imshow(im)
            ax.set_title(index)
        plt.suptitle(title)
        plt.show()