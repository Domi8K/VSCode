import csv
import numpy as np
from PIL import Image
import sys


def main():
    with open('views.csv', 'r', encoding='utf-8') as views, open('analysis.csv', 'w', encoding='utf-8', newline='') as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ['brightness']) # or manually type in the field names in a list
        writer.writeheader()
        for row in reader:
            if row['id'] == '6':
                sys.exit()
            row['brightness'] = round(calculate_brightness(f'{row["id"]}.jpeg'), 2)
            writer.writerow(row)
            

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert('L'))) / 255
    return brightness




main()