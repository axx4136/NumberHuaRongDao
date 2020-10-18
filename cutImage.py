import os

from PIL import Image
#import getproblem as URL
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):  # 两重循环，生成9张图片基于原图的位置
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
def save_images(image_list):
    index = 1
    for image in image_list:
        if not os.path.exists('./QuestionCut'):
            os.mkdir('./QuestionCut')#创建存储题目图片的切片
        image.save('./QuestionCut/'+str(index) + '.jpg')#保存图片
        index += 1
img=Image.open('./photo.jpg')
save_images(cut_image(img))