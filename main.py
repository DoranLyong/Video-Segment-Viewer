import os 
import os.path as osp


from tools.video_clip_reader import VideoClipReader


def get_video_files(data_dir, sub_dir): 
    VIDEO_FORMAT = ["avi", "mp4"]

    video_list = []
    video_dir = osp.join(data_dir, sub_dir)

    video_list = [file for file in os.listdir(video_dir) 
                        if file.split('.')[-1] in VIDEO_FORMAT]
    return video_list 




# ---------------------------------------
def main():
    data_dir = osp.join("data") 
    sub_dir = "falling"
    video_list = get_video_files(data_dir, sub_dir)

    print(video_list)

    idx = 1
    video_path = osp.join(data_dir, sub_dir, video_list[idx])


    # == 루트 윈도우 생성 == # 
    # ----------------------
    vcr = VideoClipReader(video_path)
    vcr.mainloop()



if __name__ == '__main__':
    main()