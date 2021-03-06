#-*- coding: UTF-8 -*-  
 
import imageio
from setting import CURRENT_SETTINGS
from PIL import Image
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
 
    return
 
def main():
    image_list = ['test_gif-1.png', 'test_gif-2.png', 'test_gif-4.png', 
                  'test_gif-6.png', 'test_gif-8.png', 'test_gif-10.png']
    # gif_name = 'created_gif.gif'
    # create_gif(image_list, gif_name)

    im=Image.open("test_gif-0.png")
    images=[]
    for i in image_list:
        images.append(Image.open(i))
    im.save('ccgif.gif', save_all=True, append_images=images,loop=1,duration=100,comment=b"aaabb")
 
if __name__ == "__main__":
    main()
