import os
from PIL import Image

input_folder = "jacket_200"       # 元の画像が入っているフォルダ
output_folder = "jacket_50"     # 出力フォルダ名

new_size = (50, 50)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)  
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)
        print(f"{filename} をリサイズして保存しました")