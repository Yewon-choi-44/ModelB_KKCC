from PIL import Image, ImageOps
import os 


def letter_padding_1024(raw_data_dir,
                     output_dir,
                     target_size = 1024):
    for img_name in os.listdir(raw_data_dir):
        if not img_name.endswith('.png'): continue
        
        img_path = os.path.join(raw_data_dir, img_name)
        img = Image.open(img_path)

        # 비율 유지하며 리사이즈
        img.thumbnail((target_size, target_size))

        # 중앙 정렬 후 패딩 처리
        delta_w = target_size - img.width
        delta_h = target_size - img.height
        padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
        padded_img = ImageOps.expand(img, padding, fill='black')
        padded_img.save(os.path.join(output_dir, img_name))



"""
* PIL 머하는 놈인지 찾기
* Image, ImageOps 머하는 놈인지, 역할 뭐가 다른지
* os.listdir() < 어떤 메서드인지
* os.path.join() < "
* img.thumbnail() < 처음 보므로 검색
* img.width, img.height < 신기하므로 찾아보기
* ImageOps.expand() < 의미 찾기
 
"""

"""
* raw_data_dir > 어떤 폴더인지 설명 적기
* out_dir > "
* img_name, img_path > "
"""