# 🚗 Bangla License Plate Detection System  

A comprehensive **Computer Vision** project to detect Bangla number plates from images, videos, or live webcam feeds using a YOLOv8 model. This repository provides an interactive system that enables users to:  
1. Upload an image for detection.  
2. Process a video file for inference.  
3. Detect in real-time using a webcam feed.  

![Project Demo](https://www.canva.com/design/DAGa9PPsxtg/7uTMFpPdD8j871Zr5vbltw/view?utm_content=DAGa9PPsxtg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=ha8da6c8072)  

---

## ✨ Features  
- **High Accuracy**: Trained on a robust Bangla number plate dataset.  
- **Real-Time Detection**: Efficient detection with YOLOv8 on webcam feeds.  
- **Versatile Input Options**: Supports image, video, and webcam inputs.  
- **User-Friendly Interface**: Easy-to-use menu-based system.  

---

## 💁️ Project Structure  

```plaintext
├── main.py               # The main interactive script
├── best.pt               # Trained YOLOv8 model weights
├── requirements.txt      # Required Python dependencies
├── sample_images/        # Sample test images
├── sample_videos/        # Sample test videos
└── README.md             # Project documentation
```  

---

## 🛠️ Setup and Installation  

### Prerequisites  
- Python 3.8 or higher  
- pip (Python package manager)  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/shakauthossain/Begali_Car_Number_Plate_Detection.git  
cd bangla-license-plate-detection  
```  

### Step 2: Install Dependencies  
Install all required Python packages using:  
```bash  
pip install -r requirements.txt  
```  

### Step 3: Download the YOLOv8 Model  
- Place your trained YOLOv8 model (e.g., `best.pt`) in the root directory.  

---

## 🚀 Usage  

Run the main script to start the system:  
```bash  
python main.py  
```  

### Options in the Menu:  
1. **Detect from an Image**: Upload an image file and see the detection results.  
2. **Detect from a Video**: Upload a video file to process it frame by frame.  
3. **Detect using Webcam**: Perform real-time detection using your webcam.  

---

## 📊 Model Performance  

- **Model**: YOLOv8  
- **Dataset**: Bangla number plate dataset from [Roboflow] 
- **mAP (Mean Average Precision)**: `95.6%`  

![Performance Metrics](https://via.placeholder.com/800x400.png?text=Performance+Metrics+Placeholder)  

---

## 🖼 Example Results  

### Image Detection  
![Image Detection](https://via.placeholder.com/400x200.png?text=Image+Placeholder)  

### Video Detection  
![Video Detection](https://via.placeholder.com/400x200.png?text=Video+Placeholder)  

### Real-Time Detection  
![Real-Time Detection](https://via.placeholder.com/400x200.png?text=Real-Time+Placeholder)  

---

## 🖍️ To-Do List  
- [ ] Add deployment instructions for mobile and cloud-based systems.  
- [ ] Improve real-time inference speed for edge devices.  
- [ ] Explore multi-language license plate detection.  

---

## 🤝 Contribution  

Contributions are welcome!  
1. Fork the repository.  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).  
4. Push to the branch (`git push origin feature/AmazingFeature`).  
5. Open a pull request.  


---

## 🧑‍💻 Author  

**Shakaut Hossain**  
- 💼 [Portfolio](#)  
- 📧 shakauthossain0@gmail.com  

Feel free to reach out for collaborations or inquiries about AI, computer vision, or embedded systems!  

---

## ⭐ Acknowledgments  

- Dataset provided by [Roboflow](https://roboflow.com/).  
- Powered by the ultralytics YOLO framework.
