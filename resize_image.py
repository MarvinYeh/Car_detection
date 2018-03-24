import cv2
import os
cwd = os.getcwd()
print(cwd)
image_path = os.path.join(cwd,'test_images')

print(image_path)
image_list = os.listdir(image_path)

for i in range(len(image_list)):
    img = cv2.imread(os.path.join(image_path,image_list[i]))
    # cv2.imshow('test',img)
    # cv2.waitKey()
    resized_img = cv2.resize(img,(800,600),interpolation=cv2.INTER_CUBIC)
    # cv2.imshow('test2',resized_img)
    # cv2.waitKey()
    cv2.imwrite(os.path.join(cwd,'processed_test_image',image_list[i]),resized_img)
    print(image_list[i],' done')