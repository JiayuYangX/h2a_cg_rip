import cv2
import numpy as np

def find_darkest_pixel(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频")
        return

    min_brightness = 255     # 初始设最大亮度（8位）
    darkest_color = None
    darkest_pos = None
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 转为灰度图（亮度：Y = 0.299R + 0.587G + 0.114B）
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 找到当前帧的最小亮度及其位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)

        if min_val < min_brightness:
            min_brightness = min_val
            # 保存该像素的原始BGR颜色（OpenCV默认BGR）
            darkest_color = frame[min_loc[1], min_loc[0]]  # (x,y) -> (y,x)
            darkest_pos = (min_loc[0], min_loc[1], frame_idx)
            print(f"更新最暗像素: 亮度={min_val}, 位置={min_loc}, 帧={frame_idx}")

        frame_idx += 1

    cap.release()

    if darkest_color is not None:
        # 转为RGB顺序显示
        r, g, b = darkest_color[2], darkest_color[1], darkest_color[0]
        print("\n===== 结果 =====")
        print(f"最低亮度值 (0-255): {min_brightness}")
        print(f"对应的RGB颜色: ({r}, {g}, {b})")
        print(f"出现位置: 帧 {darkest_pos[2]}, 坐标 (x={darkest_pos[0]}, y={darkest_pos[1]})")
        # 可选：保存该帧图像用于检查
        # cv2.imwrite("darkest_frame.jpg", frame)
    else:
        print("视频无有效帧")

# 使用示例
find_darkest_pixel("F:\\Videos\\h2a_cg\\Ep_035_Bookend_Outro.mp4")