## CODEPY
Copy codes from youtube videos to clipboard

## Accuracy
* The program has a minimum accuracy level of 80%
* May need to eyeball and adjust code

## REQUIREMENTS
1. __Python Requirements__
    * clipboard
    * pyautogui
    * tkinter
    * opencv-python (see `windows_install`)
    * pytesseract
    * pillow
2. __System Requirements__
    * _Tesseract-OCR_: (see `windows_install`) To install, download from <https://github.com/tesseract-ocr/tesseract/wiki>. Then add path in `bb.py`
    * [installation video link](https://www.youtube.com/watch?v=4DrCIVS5U3Y&t=138s)
 ```python
# Add your path here
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## DEMO
[YouTube Link](https://youtu.be/bFv0ZPqCIDI)

![](output/demo.gif)