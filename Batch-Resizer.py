#imports
from pathlib import Path
from PIL import Image

#directory strings
image_directory = 'source'
result_directory = 'result'

#convert PNGs to JPGs
image_paths = Path(image_directory).glob('*.png')
image_paths_list = list(image_paths)

for image_path in image_paths_list:
    image = Image.open(image_path)
    image1 = image.convert('RGB')
    
    #change extension to JPG
    image_name = image_path.name
    image_name1 = image_name.replace("png","jpg")
    output_path = Path(image_directory).joinpath(image_name1)
    image2 = image1.save(output_path, compression='group4')

#resize JPEGs
image_paths = Path(image_directory).glob('*.jpg')
image_paths_list = list(image_paths)

for image_path in image_paths_list:
    image = Image.open(image_path)
    im1 = image.resize((852,480))
    image_name = image_path.name
    output_path = Path(result_directory).joinpath(image_name)
    im2 = im1.save(output_path, compression='group4')
