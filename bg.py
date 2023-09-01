import cv2
import json
from datetime import datetime


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        item['price'] = float(item['price'])
        date_obj = datetime.strptime(item['date'], '%Y-%m-%d')
        item['date'] = datetime.strftime(date_obj, '%d/%m/%Y')

    return data

def create_background()
    # Load background image
    background = cv2.imread('background/background.jpg')

    # Define screen dimensions
    screen_width = 1280
    screen_height = 720

    # Resize background to fit screen
    background = cv2.resize(background, (screen_width, screen_height))

    # Create window
    cv2.namedWindow('Background', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Background', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Display background
    cv2.imshow('Background', background)
    cv2.waitKey(0)

    # Release resources
    cv2.destroyAllWindows()
