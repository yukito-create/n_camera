import cv2
import os

cap = cv2.VideoCapture(0)

# 保存先フォルダ
save_dir = "photos"

# フォルダがなければ作成
os.makedirs(save_dir, exist_ok=True)

count = 0  # 写真番号

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF
    
    # qで終了
    if key == ord('q'):
        break
    
    # sで撮影して保存
    if key == ord('s'):
        filename = f"{save_dir}/photo_{count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        count += 1

cap.release()
cv2.destroyAllWindows()