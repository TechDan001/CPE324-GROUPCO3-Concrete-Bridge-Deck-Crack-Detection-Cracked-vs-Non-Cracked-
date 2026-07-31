# Concrete Crack Detection Module - Group CO3


This is a machine learning application designed to automatically inspect concrete structures. By analyzing close-up images of concrete surfaces, the module can accurately determine if the concrete has visible structural cracks or if it is clean and undamaged.

##  Dataset Used
To train the module, we used the **[Surface Crack Detection](https://www.kaggle.com/datasets/arunrk7/surface-crack-detection)** dataset. This dataset consists of high-resolution, closely cropped images of real concrete textures, categorized into two distinct classes:
*   **Cracked (Positive):** Images showing distinct fractures and lines in the concrete.
*   **Clean (Negative):** Images of smooth, unblemished concrete surfaces.

___

*   **participants:**

OKPATA, DANIE LAZ - 22/EG/CO/1741
AKPABIO, AKANINYENE - ANIEKAN	22/EG/CO/1811
NATHANS CHIDERA DANIELLA - 22/EG/CO/1631
OLADELE, OLUWATEMIDARA DAVID - 22/EG/CO/1771	
STEPHEN DAVID ETOROABASI - 22/EG/CO/1731
*   **ROLES:**

i. OKPATA DANIEL LAZ
JOE-UNDIE Godfrey Adambe - Dataset preparation and preprocessing

ii. Edet, Unwana Michael
Nathans Chidera Daniella - Model development and training

iii. Edet, Unwana Michael
Nathans Chidera Daniella - Model evaluation

iv. Nathans Chidera Daniella - Application development
v. Divine Innocent Udoka - Cloud deployment
vi. Akaninyene Akpabio
Emmanuel Imoh - Documentation and report writing

*   **Project Details:**

The app is an image-classification machine-learning system. Its main job is to receive a close-up image of concrete and classify it into one of two categories:

	•	Cracked (Positive): a visible crack is detected.
	•	Clean (Negative): no visible crack is detected.

The core logic is:

Concrete image → image preprocessing → trained model → prediction probabilities → final result
