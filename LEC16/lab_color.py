from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
import viewer

cat_img = Image.open('zophie.png')
bright = ImageEnhance.Brightness(cat_img)

# bright_cat_img = bright.enhance(1.5)
# viewer.show_img(cat_img, bright_cat_img)

# colored_cat_img = ImageEnhance.Color(cat_img).enhance(5.5)
# viewer.show_img(cat_img, colored_cat_img)

# colored_cat_img = ImageEnhance.Color(cat_img).enhance(0)
# viewer.show_img(cat_img, colored_cat_img)

# contrasted_cat_img = ImageEnhance.Contrast(cat_img).enhance(1.5)
# viewer.show_img(cat_img, contrasted_cat_img)

# sharpened_cat_img = ImageEnhance.Sharpness(cat_img).enhance(3.0)
# viewer.show_img(cat_img, sharpened_cat_img)

# new_img = cat_img.filter(ImageFilter.GaussianBlur(radius=20))
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.FIND_EDGES)
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.CONTOUR)
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.DETAIL)
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.SMOOTH)
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.SMOOTH_MORE)
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.EMBOSS)
# viewer.show_img(cat_img, new_img)

# new_img = cat_img.filter(ImageFilter.SHARPEN)
# viewer.show_img(cat_img, new_img)

red_card = Image.new('RGBA', (200, 200), 'red')
# red_card.save('red.png')
# viewer.show_img2(red_card, cat_img)
#
# face = cat_img.crop((335, 345, 565, 560))
# viewer.show_img1(face)

# target_img = cat_img.copy()
# mask_logo_img = Image.open('catlogo.png').resize(red_card.size)
# target_img.paste(red_card, (100,100), mask_logo_img)
# viewer.show_img1(target_img)

# new_img = cat_img.rotate(45, expand=True)
# new_img = cat_img.transpose(Image.FLIP_TOP_BOTTOM)
# viewer.show_img1(new_img)

# cat_img.getpixel((120, 120))
# cat_img.putpixel((100,102), ImageColor.getcolor('red', 'RGBA'))

# im = Image.new('RGBA', (200,200), 'white')
# draw = ImageDraw.Draw(im)
# draw.point([(0,0), (199,0), (199, 199), (0, 199), (0,0)], fill='black')
# draw.line([(0,0), (199,0), (199, 199), (0, 199), (0,0)], fill='black')
# draw.line([(0,0), (199,0), (199, 199), (0, 199), (0,0)], fill='black', width=5)
#
# draw.rectangle((20,30,60,60), fill='blue')
# draw.rectangle((20,30,60,60), fill='blue', outline='red')
# draw.ellipse((120,30,160,60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i-100)], fill='green')
#
# viewer.show_img1(im)

im = Image.new('RGBA', (400, 400), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
arialFont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 32)
#nanumFont = ImageFont.truetype(r'C:\Windows\Fonts\NanumGothic.ttf', 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
#draw.text((100, 150), 'Hello', fill='red', font=nanumFont)
viewer.show_img1(im)
