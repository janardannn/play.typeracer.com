# ABOUT

The script automates typing in play.typeracer.com using image recognition through pytesseract module.

## Installation

```bash
pip install -r requirements.txt
```
The script also uses the Tesseract-OCR binary, so install it from [here](https://github.com/UB-Mannheim/tesseract/wiki) and add it to PATH as well.

## How to use

```python
python3 playtyperacer.py
```
## Known Issues

The scripts isn't able to identify "" in text and completely ignores them(quotes).
Also, many a times it doesn't recognizes the first character in the text.
