![github](https://github.com/user-attachments/assets/058bc49e-008a-4121-95db-9fd3284cddb8)

## 🧪 Artificial Enzymes Assistant

Artificial Enzymes Assistant (AE-A) is an AI-driven framework for large-scale AE discovery, integrating data construction, model prediction, and automated screening into a unified pipeline.

This project aims to accelerate AE design by reducing reliance on manual trial-and-error and enabling efficient exploration of massive material spaces.

## 🚀 Overview

AEs have emerged as promising candidates in catalysis, biomedicine, and environmental applications. However, discovering high-performance AEs remains challenging due to the vast search space.

AE-A provides an end-to-end solution:

- 📊 Constructing large-scale AE candidate databases  
- 🤖 Training AI models to predict catalytic activity  
- 🔍 Automatically screening high-potential materials  

## 🧠 Framework
AE-A establishes an end-to-end screening pipeline for three representative AE activities:

- Peroxidase-like (POD)
- Oxidase-like (OXD)
- Catalase-like (CAT)

Each activity is implemented as an independent module and corresponds to a dedicated folder in this repository, enabling flexible experimentation and extension.

## 📁 Project Components

To illustrate the project structure, we take the **Peroxidase-like (POD)** task as an example. The directory structure for POD is organized as follows:

### 1. 🧪 Code Pipeline

The complete workflow of AE-A is implemented through a series of Jupyter notebooks:

- **Database Construction**
  - `1 download_pubmed.ipynb`  
    Build the AE database using LLM-assisted literature mining.
  - `2 database_overview.ipynb`  
    Perform statistical analysis and visualization of the constructed database.

- **Data Preprocessing**
  - `3 process_peroxidase.ipynb`  
    Preprocess the AE dataset (e.g., cleaning, filtering, feature preparation).
  - `4 process_materials_project.ipynb`  
    Preprocess data from the Materials Project database.
  - `5 process_data.ipynb`  
    Integrate the AE database with Materials Project data to construct the final training dataset.

- **Model Training**
  - `6 model.ipynb`  
    Train the machine learning model for AE activity prediction.
  - `7 model_year.ipynb`  
    Evaluate model performance (e.g., temporal generalization).

- **Large-scale Screening**
  - `8 predict_materials_project.ipynb`  
    Predict potential AEs from the Materials Project database.
  - `9 predict_aflow.ipynb`  
    Predict potential AEs from the AFLOW database.

### 2. 📊 Database

Due to GitHub storage limitations, some large files are hosted externally on [Google Drive](https://drive.google.com/drive/folders/1hx0y6aLQ8fMEHXUdqUtIi06uDkwt3osO?usp=sharing). 

The datasets used in this project are organized as follows:

- **Database**
  - `./data/peroxidase.xlsx`  
    Curated AE dataset collected from literature.

  - `./data/peroxidase_feature.csv`  
    Feature-engineered AE dataset for model training.

- **Integrated Dataset**
  - `./data/data.csv`  
    Final integrated dataset used for model training, constructed by combining AE data with Materials Project features. Storaged in [Google Drive](https://drive.google.com/drive/folders/1hx0y6aLQ8fMEHXUdqUtIi06uDkwt3osO?usp=sharing). 

- **Materials Project**
  - `./data/materials_project.xlsx`  
    Raw materials data obtained from the Materials Project database.

  - `./data/materials_project_features.csv`
    Feature-engineered Materials Project dataset.

  - `./data/theoretical.csv`  
    Subset of Materials Project materials that are theoretically synthesizable.

  - `./data/predict_materials_project.csv`  
    Predicted AE activity scores for all Materials Project materials. Storaged in [Google Drive](https://drive.google.com/drive/folders/1hx0y6aLQ8fMEHXUdqUtIi06uDkwt3osO?usp=sharing). 

  - `./data/predict_pod.csv`  
    Final screened AE candidates with high predicted activity.

- **AFLOW**
  - `./data/aflow_features.csv`  
    Feature-engineered dataset derived from the AFLOW database. Storaged in [Google Drive](https://drive.google.com/drive/folders/1hx0y6aLQ8fMEHXUdqUtIi06uDkwt3osO?usp=sharing). 

  - `./data/predict_aflow.csv`  
    Predicted AE activity scores for AFLOW materials. Storaged in [Google Drive](https://drive.google.com/drive/folders/1hx0y6aLQ8fMEHXUdqUtIi06uDkwt3osO?usp=sharing). 


### 3. 🤖 Model

The trained models used for AE discovery are provided via [Google Drive](https://drive.google.com/drive/folders/1hx0y6aLQ8fMEHXUdqUtIi06uDkwt3osO?usp=sharing) in `.cbm` format .

Please download the models and place them in the `model/` directory before running the code.

### 4. ⚙️ Environment

The environment dependencies are provided in the `environment.yml` file.

To reproduce the environment, run:

```bash
conda env create -f environment.yml
conda activate nanozyme
