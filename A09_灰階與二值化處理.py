import cv2 as cv
import glob

# 讀取圖片
image_path = glob.glob('./*/*.png')[0]
image = cv.imread(image_path)

# 建立視窗
window_name = 'Binary Threshold'
cv.namedWindow(window_name)

# 全域變數
current_threshold = 127
current_channel = 0  # 0: gray, 1: B, 2: G, 3: R
invert_mode = 0     # 0: THRESH_BINARY, 1: THRESH_BINARY_INV

# 通道名稱對應
channel_names = ['Gray', 'Blue', 'Green', 'Red']

# 取得單通道影像
def get_selected_channel(img, channel_type):
    if channel_type == 0:
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elif channel_type == 1:
        return img[:, :, 0]
    elif channel_type == 2:
        return img[:, :, 1]
    elif channel_type == 3:
        return img[:, :, 2]

# 更新顯示
def update_display(*args):
    global current_threshold, current_channel, invert_mode

    # 取得選擇的通道影像
    channel_img = get_selected_channel(image, current_channel)

    # 決定使用哪種閾值方法
    thresh_type = cv.THRESH_BINARY_INV if invert_mode == 1 else cv.THRESH_BINARY

    # 執行二值化
    _, binary = cv.threshold(channel_img, current_threshold, 255, thresh_type)

    # 設定視窗標題
    title_text = f'{channel_names[current_channel]} | Threshold={current_threshold} | Invert={invert_mode}'
    cv.setWindowTitle(window_name, title_text)

    # 顯示影像
    cv.imshow(window_name, binary)

# 閾值滑桿回調
def on_thresh_trackbar(val):
    global current_threshold
    current_threshold = val
    update_display()

# 通道滑桿回調
def on_channel_trackbar(val):
    global current_channel
    current_channel = val
    update_display()

# 反向滑桿回調
def on_invert_trackbar(val):
    global invert_mode
    invert_mode = val
    update_display()

# 建立滑桿
cv.createTrackbar('Threshold', window_name, current_threshold, 255, on_thresh_trackbar)
cv.createTrackbar('Channel: 0-G 1-B 2-G 3-R', window_name, current_channel, 3, on_channel_trackbar)
cv.createTrackbar('Invert: 0-Off 1-On', window_name, invert_mode, 1, on_invert_trackbar)

# 顯示初始畫面
update_display()

# 等待關閉
cv.waitKey(0)
cv.destroyAllWindows()
