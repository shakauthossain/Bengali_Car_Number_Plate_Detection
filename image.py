import cv2
import os

def detect_from_image(model):
    """Detect objects in an uploaded image."""
    image_path = input("Enter the path to the image file: ").strip()
    if not os.path.exists(image_path):
        print("Invalid image path!")
        return

    # Load and process the image
    image = cv2.imread(image_path)
    results = model.predict(source=image, conf=0.8)

    # Draw bounding boxes
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f"Class {cls} ({conf:.2f})"

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Detected Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
