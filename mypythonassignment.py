#!/usr/bin/env python
# coding: utf-8


# In[30]:


import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.png")
image=image.convert('RGB')
txt_color = 'rgb(255,255,255)'
images= []
rgb = 0,1,2
intensity = [(0.1),(0.5),(0.9)]
font = ImageFont.truetype(r"readonly/fanwood-webfont.ttf", 50)
for color in rgb:
    for i in intensity:
        black_addition = PIL.Image.new("RGB",(image.width,image.height//8))
        text = "channel {} intensity {}".format(color,i)
        draw = ImageDraw.Draw(black_addition)
        draw.text((15,15), text, font = font, align ="left",fill=txt_color)  
        total_image =  PIL.Image.new("RGB",(image.width,image.height+black_addition.height))
        total_image.paste(image,(0,0))
        total_image.paste(black_addition,(0,image.height))
        for x in range(total_image.width):
            for y in range(total_image.height):
                rgb_pixels = total_image.getpixel((x,y))
                if color == 0:
                    total_image.putpixel((x,y),(int(rgb_pixels[0]*i),rgb_pixels[1],rgb_pixels[2]))
                elif color == 1:
                    total_image.putpixel((x,y),(rgb_pixels[0],int(rgb_pixels[1]*i),rgb_pixels[2]))
                else:
                    total_image.putpixel((x,y),(rgb_pixels[0],rgb_pixels[1],int(rgb_pixels[2]*i)))
        images.append(total_image)

    
    
   

# create a contact sheet from different intensity manipulations
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()
contact_sheet.save("assignment.pdf")



