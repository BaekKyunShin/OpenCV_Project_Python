'''
GitHub : https://github.com/dltpdn/book_opencv_prject_using_python
Author : Lee Sewoo(이세우, dltpdn@gmail.com)
'''
import cv2

img_file = "../img/yeosu.jpg" # 표시할 이미지 경로            ---①
img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②

if img is not None:
  cv2.imshow('IMG', img)   # 읽은 이미지를 화면에 표시      --- ③
  cv2.waitKey()           # 키가 입력될 때 까지 대기      --- ④
  cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤
else:
    print('No image file.')
    