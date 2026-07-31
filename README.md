# Concrete Crack Detection Module - Group CO3


This is a machine learning application designed to automatically inspect concrete structures. By analyzing close-up images of concrete surfaces, the module can accurately determine if the concrete has visible structural cracks or if it is clean and undamaged.

##  Dataset Used
To train the module, we used the **[Surface Crack Detection](https://www.kaggle.com/datasets/arunrk7/surface-crack-detection)** dataset. This dataset consists of high-resolution, closely cropped images of real concrete textures, categorized into two distinct classes:
*   **Cracked (Positive):** Images showing distinct fractures and lines in the concrete.
*   **Clean (Negative):** Images of smooth, unblemished concrete surfaces.

---

**Participants:**
  
| Name | Reg. No. |
|---|---|
| OKPATA, DANIE LAZ | 22/EG/CO/1741 |
| JOE-UNDIE GODFREY ADAMBE | 22/EG/CO/1791 |
| AKPABIO, AKANINYENE ANIEKAN | 22/EG/CO/1811 |
| NATHANS CHIDERA DANIELLA | 22/EG/CO/1631 |
| OLADELE, OLUWATEMIDARA DAVID | 22/EG/CO/1771 | 
| STEPHEN DAVID ETOROABASI | 22/EG/CO/1731 |
| EDET, UNWANA MICHAEL | 22/EG/CO/1711 |
| NYONG,EMMANUEL IMOH | 22/EG/CO/1801 |
| Omale EmmanuelMary Omale | 22/EG/CO/1661 |
| Ekott, Anietie Aniedi | 22/EG/CO/1761 |

*   **ROLES:**

i. OKPATA DANIEL LAZ &
JOE-UNDIE Godfrey Adambe - Dataset preparation and preprocessing

ii. Edet, Unwana Michael &
Nathans Chidera Daniella - Model development and training

iii. Edet, Unwana Michael &
Nathans Chidera Daniella - Model evaluation

iv. Nathans Chidera Daniella - Application development

v. Divine Innocent Udoka - Cloud deployment

vi. Akaninyene Akpabio &
Nyong Emmanuel Imoh - Documentation and report writing

*   **Project Details:**

The app is an image-classification machine-learning system. Its main job is to receive a close-up image of concrete and classify it into one of two categories:

	•	Cracked (Positive): a visible crack is detected.
	•	Clean (Negative): no visible crack is detected.

The core logic is:

Concrete image → image preprocessing → trained model → prediction probabilities → final result
# CPE 324: Concrete Bridge Deck Crack Detection (Cracked vs. Non-Cracked)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%20%2F%20PyTorch-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Course](https://img.shields.io/badge/Course-CPE%20324-lightgrey)

**Group:** Group C03  
**Department:** Computer Engineering  

---

## 📌 Project Overview
Automated structural health monitoring is vital for civil infrastructure maintenance. Manual inspection of concrete bridge decks is time-consuming, subjective, and hazardous. 

This project develops a deep learning image classification model to automatically identify surface cracks on concrete bridge decks, classifying images into two distinct classes:
- **Cracked**
- **Non-Cracked (Uncracked)**

---

## 📁 Repository Structure
```text
├── data/                  # Instructions or scripts for dataset download
├── notebooks/             # Jupyter notebooks for EDA and model training
├── src/                   # Python modules (preprocessing, model, train, evaluate)
│   ├── preprocess.py
│   ├── model.py
│   ├── train.py
│   └── predict.py
├── saved_models/          # Trained weights (.h5, .keras, or .pt)
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
