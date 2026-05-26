# Insurance Risk Analytics & Predictive Modeling

AlphaCare Insurance Solutions (ACIS) – End-to-end insurance risk analytics, hypothesis testing, and machine learning for optimized premium pricing.

## Project Overview

This project analyzes 18 months of car insurance claim data (Feb 2014 – Aug 2015) to:
- Discover low‑risk segments for premium reduction
- Statistically validate risk drivers (province, zip code, gender)
- Build predictive models for claim severity and pricing


## Reproducing the Data Pipeline (DVC)

This project uses DVC (Data Version Control) to track the dataset. To reproduce:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bitan/insurance-risk-analytics.git
   cd insurance-risk-analytics

pip install -r requirements.txt
pip install dvc

dvc pull

Run the notebooks in order:

notebooks/01_eda.ipynb

notebooks/02_hypothesis_testing.ipynb

notebooks/03_modeling.ipynb

Key Findings
Loss ratio varies by province (p < 0.05) → regional premium adjustment recommended

Women have lower claim frequency → targeted discount opportunity

XGBoost outperforms Linear Regression and Random Forest for claim severity prediction (RMSE: [your value], R²: [your value])

Top risk drivers: vehicle age, CustomValueEstimate, province, gender, kilowatts

Technologies Used
Python 3.9+

Pandas, NumPy, Matplotlib, Seaborn

Scikit-learn (Linear Regression, Random Forest)

XGBoost

SHAP for model interpretability

DVC for data versioning

GitHub Actions for CI/CD

Submission Details
Challenge: 10 Academy – Artificial Intelligence Mastery (Week 3)

Date: 20–26 May 2026

Author:BITANYA DEREJE

License
This project is for educational purposes as part of the 10 Academy program.

text

**Note:** Replace `[your value]` and `[Your Name]` with your actual numbers and name (optional).

---

## Save, commit, and push

After creating the file, run:

```bash
git add README.md
git commit -m "Add README with DVC reproduction steps"
git push origin master
Final submission check:
README.md exists with DVC instructions

All notebooks committed

All report images committed

reports/final_report.md committed

CI is green on GitHub

DVC files (.dvc, .dvc/config) committed

Now you're fully ready. Submit your GitHub URL. Great work! 🚀


