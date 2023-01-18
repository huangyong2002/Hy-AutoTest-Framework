# @Time:2023/1/18 8:53
# @Author:Henry
import ddddocr

class OcrIdentify:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def identify(self, pic_path):
        with open(pic_path, 'rb') as f:
            image = f.read()
        res = self.ocr.classification(image)
        return res


if __name__ == '__main__':
    print(OcrIdentify().identify("test.png"))
