import os

project_dir = os.path.dirname(os.path.abspath(__file__))
import sys

sys.path.append(project_dir)

from qrcode.image.styledpil import StyledPilImage
import qrcode
from qrcode.image.svg import SvgPathImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *

qr = qrcode.QRCode(image_factory=SvgPathImage, error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://bareblackfoot.github.io/TopologicalSemanticGraphMemory')
qr.make(fit=True)

from PIL import Image, ImageDraw


def style_eyes(img):
    img_size = img.size[0]
    eye_size = 70  # default
    quiet_zone = 40  # default
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((40, 40, 110, 110), fill=255)
    draw.rectangle((img_size - 110, 40, img_size - 40, 110), fill=255)
    draw.rectangle((40, img_size - 110, 110, img_size - 40), fill=255)
    return mask


# background_color = (255, 255, 255, 0)
background_color = (255, 255, 255)
qr_img = qr.make_image(image_factory=StyledPilImage,
                       color_mask=SolidFillColorMask(front_color=(118, 138, 178, 255), back_color=background_color),
                       module_drawer=CircleModuleDrawer(),
                       eye_drawer=RoundedModuleDrawer(radius_ratio=1))
qr_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            color_mask=SolidFillColorMask(front_color=(186, 182, 206, 255), back_color=background_color),
                            module_drawer=CircleModuleDrawer(),
                            eye_drawer=RoundedModuleDrawer(radius_ratio=1))
mask = style_eyes(qr_img)
final_img = Image.composite(qr_eyes_img, qr_img, mask)

with open('QR_TSGM_webpage_with_white_background.png', 'wb') as f:
    final_img.save(f)
