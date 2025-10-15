import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
# Add your model import here
# from model import your_prediction_model

def load_image(image_file):
    img = Image.open(image_file)
    return img

def prediction(image_file):
    model = YOLO('./runs/classify/train2/weights/last.pt')
    results = model(image_file)
    names_dict = results[0].names
    probs = results[0].probs.top1
    return names_dict[probs]

def main():
    st.set_page_config(
        page_title="Animal Classifier",
        page_icon="🐾",
        layout="wide"
    )

    # Header
    st.title("🦁 Animal Classification System")
    st.markdown("---")

    # Create two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Upload Animal Image")
        st.write("Please upload a JPG image of an animal for classification")
        
        # File uploader
        image_file = st.file_uploader("", type=["jpg"])
        
        if image_file is not None:
            # Display image
            image = load_image(image_file)
            st.image(image, caption='Uploaded Image')
            
            # Add prediction button
            if st.button('Classify Animal'):
                try:
                    # Add your model prediction code here
                    animalName = prediction(image)
                    # For now, using placeholder
                    st.success(f"Predicted Animal: {animalName}")
                except Exception as e:
                    st.error("An error occurred during classification. Please try again.")


    with col2:
        st.subheader("About the Model")
        st.markdown("""
        ### Model Architecture
        This model uses YOLOv8, a state-of-the-art deep learning model for image classification.
        
        ### Training Details:
        - Epochs: 20
        - Image Size: 64x64
        - Training Framework: Ultralytics YOLO
        
        ### Supported Animals:
        1. Bear
        2. Bird
        3. Cat
        4. Cow
        5. Deer
        6. Dog
        7. Dolphin
        8. Elephant
        9. Giraffe
        10. Horse
        11. Kangaroo
        12. Lion
        13. Panda
        14. Tiger
        15. Zebra
        """)
        
    # Display metrics plots
    st.markdown("### Model Performance")
    st.subheader("Training Metrics")
    col_metrics1, col_metrics2 = st.columns(2)
    
    with col_metrics1:
        st.image("runs/classify/train2/results.png", caption="Training Results")
    with col_metrics2:
        st.image("runs/classify/train2/confusion_matrix.png", caption="Confusion Matrix")
    
    st.markdown("""
        ### Key Performance Indicators:
        - Top-1 Accuracy: ~98%
        - Excellent classification across all animal categories
        - Minimal confusion between classes
        - Robust performance on validation set
        
        ### Technologies Used:
        - YOLOv8 Architecture
        - PyTorch Backend
        - Ultralytics Framework
        """)

    # Footer
    st.markdown("---")
    st.markdown("Created with ❤️ by Shaurya Srivastava")

if __name__ == '__main__':
    main()