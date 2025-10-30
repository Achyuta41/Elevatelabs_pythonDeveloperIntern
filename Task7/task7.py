import os
from PIL import Image

input_folder=input("Enter the folder name of your image files:").strip()
parent_dir=os.path.dirname(input_folder.rstrip('/\\'))
output_folder=os.path.join(parent_dir,"output_images")
os.makedirs(output_folder,exist_ok=True)

width=int(input("Enter new width(i.e.800)"))
height=int(input("Enter new height(i.e.800)"))
resize=(width,height)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg",".png",".jpeg")):
        img_path=os.path.join(input_folder,filename)
        img=Image.open(img_path)
        img_resized=img.resize(resize)
        ori_format=img.format if img.format else ".png"

        base_name=os.path.split(filename)[0]
        extension=os.path.split(filename)[1]

        output_path=os.path.join(output_folder,f"{base_name}{extension}")
        img_resized.save(output_path,format=ori_format)
        print(f"{filename} is resized and saved to the {output_path}")

print(f"All images have been resized successfully and saved in the output folder")
