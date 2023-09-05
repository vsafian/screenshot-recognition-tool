# Screenshot Recognition Tool

This app captures screenshots, recognizes text from the images, and places the text in the operating system's clipboard.

## Before You Start

1. Download version 5.3.1 of the Tesseract OCR engine. You can find installation instructions for your operating system here: [Tesseract Installation](https://tesseract-ocr.github.io/tessdoc/Installation.html).

2. After installing, specify the path to `tesseract.exe`. Your path should resemble this: `"Tesseract-OCR/tesseract.exe"`. To do this, I have created a function. Open the `tesseract_processor` package and locate `tess_cmd.py`. Edit the path there as follows: `"your tesseract directory, Tesseract-OCR, tesseract.exe"`.

3. The next step is to open `tesseract_train_data` and move all files to your Tesseract storage directory in `tessdata`.

4. Once you've completed these steps, you can run `activator.py` and access the App's GUI Interface.

## About Work Modes

The default work mode is "Single." It captures a single fragment and immediately sends it to the clipboard.

The "Combine" mode allows you to capture multiple screenshots and combine them into a single text fragment. There is an "End" button 
on the same level as "Extract" to finalize your work.

Feel free to reach out if you have any questions.

# Languages

Currently, the app supports the following languages:

- Ukrainian + English
- Russian + English
- English
