# 👁️ Diabetic Retinopathy Detection using Deep Learning

> An AI-powered web application that detects diabetic retinopathy from retinal fundus images using a deep learning model, enabling early screening and assisting healthcare professionals in diagnosis.

---

## 📌 Overview

Diabetic Retinopathy Detection is a Deep Learning-based medical imaging project that classifies retinal fundus images to identify signs of diabetic retinopathy. The system leverages Convolutional Neural Networks (CNNs) to analyze retinal images and predict disease severity with high accuracy.

A Flask-based web interface allows users to upload retinal images and receive instant predictions, making the solution suitable for early screening and educational purposes.

---

## 🚀 Features

- 👁️ Upload retinal fundus images
- 🤖 Deep Learning-based disease detection
- ⚡ Real-time image prediction
- 🌐 Interactive Flask web application
- 📊 Automated image preprocessing
- 🩺 Supports early diabetic retinopathy screening
- 📈 High-performance CNN model
- 💻 Simple and user-friendly interface

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Deep Learning
- TensorFlow
- Keras

### Image Processing
- OpenCV
- NumPy

### Data Analysis
- Pandas
- Matplotlib

### Web Framework
- Flask

### Frontend
- HTML
- CSS

---

## 📂 Project Structure

```
Diabetic-Retinopathy/
│
├── app.py                     # Flask application
├── inference.py               # Prediction script
├── coat-net-on-aptos.ipynb    # Model training notebook
├── index.html                 # Frontend
├── style.css                  # Styling
├── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Diabetic-Retinopathy.git
```

### Navigate to the Project

```bash
cd Diabetic-Retinopathy
```

### Create a Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Model Workflow

1. Collect retinal fundus image dataset
2. Image preprocessing and augmentation
3. CNN/CoAtNet model training
4. Model evaluation
5. Save trained model
6. Upload retinal image
7. Predict diabetic retinopathy stage
8. Display prediction result

---

## 📷 Input

The system accepts:

- Retinal Fundus Images
- JPG / JPEG / PNG formats

---

## 📊 Output

The model predicts whether the retinal image indicates:

- ✅ No Diabetic Retinopathy
- Mild Diabetic Retinopathy
- Moderate Diabetic Retinopathy
- Severe Diabetic Retinopathy
- Proliferative Diabetic Retinopathy

*(Modify these classes according to your trained model.)*

---

## 🎯 Applications

- Medical image analysis
- Early diabetic retinopathy screening
- Clinical decision support
- Healthcare AI research
- Educational demonstrations
- Deep learning image classification

---

## 📸 Screenshots

Include screenshots of:

- Home Page
- Image Upload Interface
- Prediction Result
- Model Output

---

## 📈 Future Enhancements

- Multi-class severity classification
- Confidence score visualization
- Explainable AI using Grad-CAM
- Cloud deployment
- Mobile-friendly interface
- Patient report generation
- REST API support
- Batch image prediction

---

## 📚 Libraries Used

- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Flask

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Preetham Patel**

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## ⭐ Support

If you like this project:

- ⭐ Star this repository
- 🍴 Fork the project
- 💡 Suggest improvements
- 🤝 Contribute

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis or clinical decision-making. Always consult a qualified healthcare professional for medical advice.

---

> **"Artificial Intelligence has the potential to transform healthcare by enabling faster, more accurate, and accessible disease detection."**
