
# 🛍️ Customer Purchase Analysis

This project analyzes customer purchase behavior across different regions using Python, Pandas, and Seaborn. It provides insights into total and average purchases by region, top customers, common customer names, and outlier detection.

---

## 📁 Dataset

The dataset used is an Excel file named `customer_data.xlsx`, which includes fields like:

- Name
- Email
- Region
- Purchase Amount

---

## 📊 Key Analyses

1. **Regional Purchase Analysis**
   - Compares total and average purchase amounts by region.
   - Visualized using bar plots and pie charts.

2. **Top Customers**
   - Identifies the top 10 customers based on purchase amount.
   - Visualized using a line plot.

3. **Common Customer Names**
   - Analyzes frequently occurring names.
   - Visualized using a scatter plot.

4. **Region-wise Purchase Distribution**
   - Detailed analysis of purchase amounts across regions.
   - Histogram visualization with KDE.

5. **Outlier Detection**
   - Detects outliers in purchase data using the Interquartile Range (IQR) method.

---

## 📦 Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib
- openpyxl (for reading Excel files)

Install dependencies using:

```bash
pip install pandas numpy seaborn matplotlib openpyxl
```

---

## ▶️ How to Run

1. Place the `customer_data.xlsx` file in the specified directory.
2. Run the Python script:

```bash
python customer_analysis.py
```

---

## 📌 Notes

- Ensure the Excel file has no formatting issues (extra spaces in column names).
- Modify the file path if the dataset is in a different location.
- The script includes multiple visualization techniques to aid understanding.

---

## 📈 Sample Visuals

- Bar Plot: Total purchase amount by region  
- Line Plot: Top 10 customer purchase amounts  
- Scatter Plot: Most common customer names  
- Pie Chart: Regional share of total purchases  
- Histogram: Region-wise distribution of purchase amounts

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Contributions

Feel free to fork this repo and open pull requests for improvements or additional features!
