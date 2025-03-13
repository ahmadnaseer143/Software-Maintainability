# Empirical Study on Module Size and Software Maintainability

## 📌 Project Overview
This project investigates the **effect of module size on software maintainability in Python projects**. The study analyzes **Lines of Code (LOC), Cyclomatic Complexity (CC), Maintainability Index (MI), and Code Quality Metrics** using **Radon** and **Pylint**.

## 📂 Repository Contents
- `data_extraction.py` – Extracts LOC and CC from Python repositories using Radon.
- `analysis.py` – Performs correlation and regression analysis.
- `visualization.py` – Generates scatter plots and box plots.
- `raw_data.csv` – Extracted data from open-source Python projects.
- `processed_data.csv` – Processed dataset with maintainability metrics.
- `metrics_results.csv` – Results from Radon and Pylint.
- `README.md` – Project documentation (this file).

## 🔧 How to Use the Scripts

### 1️⃣ **Install Dependencies**
Ensure you have Python and the required libraries installed:
```bash
pip install radon pylint pandas seaborn matplotlib statsmodels
```

### 2️⃣ **Extract Data from Python Projects**
Run `data_extraction.py` to analyze a local Python repository:
```bash
python data_extraction.py
```
It will generate `raw_data.csv` containing **LOC and Cyclomatic Complexity**.

### 3️⃣ **Perform Statistical Analysis**
Run `analysis.py` to compute **correlations and regression models**:
```bash
python analysis.py
```
Results will be saved in `correlation_results.csv`.

### 4️⃣ **Generate Visualizations**
Run `visualization.py` to create scatter and box plots:
```bash
python visualization.py
```
Plots will be saved as `scatter_loc_mi.png` and `boxplot_cc.png`.

## 📊 Example Results
- **Higher LOC correlates with lower Maintainability Index.**
- **Modules exceeding 500 LOC show increased complexity and bug density.**
- **Optimal module size for maintainability: 200-500 LOC.**

## 📎 Repository Link
📌 **[GitHub Repository](https://github.com/your-repo-link)**  
_(Replace with your actual repository link)_

## 🔗 References
- [Radon Documentation](https://radon.readthedocs.io/)
- [Pylint Documentation](https://pylint.pycqa.org/)
