from PIL import Image
import PIL.ImageOps
import pytesseract as tess
from PIL import Image
import PIL.ImageOps
import cv2

# Add your path here
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class GetText:
    def __init__(self, file):
        self.file = file

    def get_code(self):
        if self.check_bb() == 'white':
            img = Image.open(self.file)
            text = tess.image_to_string(img)
            self.save(text)
            return self.format_string(text)
        else:
            InvertImage(self.file).get_invert()
            img = Image.open('snips/invert.png')
            text = tess.image_to_string(img)
            self.save(text)
            return self.format_string(text)

    def format_string(self, txt):
        ch = {'‘': "'", '’': "'", '“': '"'}
        for i in ch:
            if i in txt:
                txt = txt.replace(i, ch[i])
        return self.structure_me(txt)

    @staticmethod
    def structure_me(txt):
        key_line = ['def', 'class']
        keys = ['elif', 'except', 'else:', 'except:', 'finally:', 'finally']
        lines = txt.splitlines()
        new_txt = ''
        tab = 0
        for line in lines:
            if len(line.split()) != 0:
                sp = line.split()[0]
                if sp in key_line:
                    tab = 0
                elif sp in keys:
                    tab -= 4

            new_txt += (' ' * tab) + line + '\n'
            if ':' in line:
                tab += 4

        return new_txt

    def check_bb(self):
        img = Image.open(self.file)
        img = img.convert("RGBA")
        pixdata = img.load()
        item = pixdata[0, 0]
        value_check = 150
        if item[0] >= value_check and item[1] >= value_check and item[2] >= value_check:
            # print('white')
            return 'white'
        else:
            # print(item[0:3])
            # print('black')
            return 'black'

    @staticmethod
    def save(text):
        file = open(r'output/capture.py', 'w')
        file.write(text)
        file.close()


class InvertImage:
    def __init__(self, file):
        self.file = file

    def get_invert(self):
        self._invert()
        # return self._grey_scale()

    def grey(self):
        _img = cv2.imread(self.file, 0)
        cv2.imwrite('snips/output.png', _img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return _img

    def _invert(self):
        image = Image.open(self.file)
        if image.mode == 'RGBA':
            r, g, b, a = image.split()
            rgb_image = Image.merge('RGB', (r, g, b))

            inverted_image = PIL.ImageOps.invert(rgb_image)

            r2, g2, b2 = inverted_image.split()

            final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))

            final_transparent_image.save('snips/invert.png')

        else:
            inverted_image = PIL.ImageOps.invert(image)
            inverted_image.save('snips/invert.png')

    @staticmethod
    def _grey_scale():
        img = Image.open('snips/invert.png')
        thresh = 175
        fn = lambda x: 255 if x > thresh else 0
        return img.convert('L').point(fn, mode='1')

# g = InvertImage('invert.png').grey()
# text = tess.image_to_string(g)
# print(text)
