# new-project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

# Soil Nutrient Gap Prediction
## Overview

This project aims to predict soil nutrient levels (in ppm) to eventually estimate the nutrient gap for African farms, helping optimize fertilizer application for maize production. The nutrient gap is the difference between the required nutrients for a target maize yield and the nutrients available in the soil.
---

## Dataset

The dataset was obtained from the **[Amini Soil Prediction Challengeon Zindi]([https://zindi.africa/](https://zindi.africa/competitions/amini-soil-prediction-challenge))** and contains:

- Measured **soil chemical properties** (in ppm)
- **Environmental and spatial features**
- **Bulk density** and other agronomic indicators

 Soil samples reflect conditions at **20 cm depth**, which is standard for assessing nutrient availability for crops like maize.

---
## Problem Statement

Farmers need accurate information on soil nutrient deficiencies to apply the right amount of fertilizer. Over- or under-application can lead to wasted resources or poor crop yields.

This project focuses on predicting nutrient concentrations (in ppm) based on soil and environmental features. The predicted values can then be used to calculate the nutrient gap (kg/ha) by applying agronomic formulas, helping farmers make data-driven fertilization decisions.
---


## Nutrient Gap Formula(Background)

Although this project focuses on **predicting nutrients in ppm**, the values can later be converted into the nutrient gap using:

```python
# Convert ppm to kg/ha
Available_kg_per_ha = ppm * soil_depth_cm * bulk_density_g_per_cm3 * 0.1

# Calculate requirement
Required_kg_per_ha = nutrient_uptake_per_ton * target_yield_t_per_ha

# Compute gap
Gap = Required_kg_per_ha - Available_kg_per_ha
```

🔸 A **positive gap** means more nutrients are needed.  
🔸 A **negative gap** means the soil already contains more than enough of that nutrient.

---

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         gap_prediction and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── gap_prediction   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes gap_prediction a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------



## Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/soil-nutrient-gap.git
cd soil-nutrient-gap
```

2. **Create and activate virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

##  Current Progress

- ✅ EDA and data cleaning
- ✅ Feature engineering
- ✅ Built modular code structure in `src/`
- ✅ Trained models to **predict nutrients in ppm**
- ❌ Yet to apply nutrient gap formula to predictions

---

##  Next Steps

- [ ] Apply nutrient gap formula to model predictions
- [ ] Visualize gaps across regions
- [ ] Evaluate using agronomic thresholds
- [ ] Consider spatial interpolation techniques

---

## 🤝 Acknowledgements

- [Zindi Africa](https://zindi.africa/) for the dataset and challenge
- Agronomists and researchers whose work informed the nutrient gap formula

-


