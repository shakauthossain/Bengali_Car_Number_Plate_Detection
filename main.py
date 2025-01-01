from ultralytics import YOLO
from image import detect_from_image 
from video import detect_from_video
from webcam import detect_from_webcam 
import os

if __name__ == "__main__":
    # Load the YOLO model
    # model_path = input("Enter the path to your YOLO model (e.g., best.pt): ").strip()
    model_path = 'best.pt'
    if not os.path.exists(model_path):
        print("Invalid model path!")
        exit()

    model = YOLO(model_path)

    # Main menu
    while True:
        print("\nChoose an option:")
        print("1. Detect from an image")
        print("2. Detect from a video file")
        print("3. Detect using the webcam")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            detect_from_image(model)
        elif choice == "2":
            detect_from_video(model)
        elif choice == "3":
            detect_from_webcam(model)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")
