import random
import string

from PIL import Image, ImageFont, ImageDraw

from database.redis_cli import code_redis
from config import VERIFICATION_CODE_EXPIRE


def random_color():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def gen_text():
    return ''.join(random.sample(string.ascii_letters + string.digits, 4))


def draw_lines(draw, num, width, height):
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)


def gen_verification_code():
    code = gen_text()
    width, height = 120, 46
    im = Image.new('RGB', (width, height), 'white')
    font = ImageFont.truetype("utils/arial.ttf", 40)
    draw = ImageDraw.Draw(im)
    for item in range(4):
        draw.text(
            (5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)), text=code[item], fill=random_color(),
            font=font)
    draw_lines(draw, 4, width, height)
    return im, code


def save_verification_code(sid, code):
    code = code.lower()
    code_redis.setex(sid, VERIFICATION_CODE_EXPIRE, code)


def check_verification_code(sid, code):
    code = code.lower()
    saved_code = code_redis.get(sid)
    if saved_code and str(saved_code, encoding="utf-8") == code:
        code_redis.delete(sid)
        return True, ''
    elif not saved_code:
        return False, '验证码过期'
    return False, '验证码错误'
