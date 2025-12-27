# Titanic Exploratory Data Analysis

A comprehensive exploratory data analysis of the Titanic dataset, uncovering insights about passenger survival rates, demographics, and socioeconomic factors that influenced survival during the tragic 1912 disaster.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This project performs an in-depth exploratory data analysis (EDA) on the famous Titanic dataset from Kaggle. The analysis investigates various factors that influenced passenger survival rates, including:

- **Socioeconomic status** (passenger class)
- **Demographics** (age, gender)
- **Family relationships** (siblings, parents, children)
- **Fare prices** and embarkation points
- **Cabin locations** and ticket information

The goal is to extract meaningful insights through statistical analysis and data visualization, providing a foundation for predictive modeling.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/mosesamwoma/titanic-exploratory-data-analysis.git
cd titanic-exploratory-data-analysis
```

2. **Create a virtual environment** (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Launch Jupyter Notebook**
```bash
jupyter notebook
```

5. **Open the analysis notebook**
Navigate to `titanic_eda.ipynb` in your browser

## Analysis Workflow

### 1. Data Loading and Initial Exploration
- Load the dataset using pandas
- Display basic information (shape, data types, memory usage)
- Generate descriptive statistics

### 2. Data Cleaning
- **Handle missing values**
  - Age: Impute with median or mean by passenger class
  - Cabin: Analyze patterns or create indicator variable
  - Embarked: Fill with mode
- **Remove duplicates** (if any)
- **Feature engineering**
  - Extract titles from names (Mr., Mrs., Miss, etc.)
  - Create family size feature (SibSp + Parch + 1)
  - Categorize age groups
  - Extract cabin deck information

### 3. Exploratory Data Analysis
- **Univariate analysis**
  - Distribution of individual features
  - Survival rate overview
- **Bivariate analysis**
  - Survival rate by gender
  - Survival rate by passenger class
  - Survival rate by age groups
  - Survival rate by embarkation point
- **Multivariate analysis**
  - Interaction between multiple features
  - Correlation analysis

### 4. Data Visualization
- Bar plots, histograms, and count plots
- Box plots for outlier detection
- Heatmaps for correlation matrices
- Violin plots for distribution comparisons

### 5. Statistical Testing
- Chi-square tests for categorical relationships
- T-tests for comparing means
- ANOVA for multiple group comparisons

## Key Findings

### Survival Statistics
- **Overall survival rate**: ~38%
- **Female survival rate**: ~74%
- **Male survival rate**: ~19%

### Class-Based Insights
- **1st Class**: Highest survival rate (~63%)
- **2nd Class**: Moderate survival rate (~47%)
- **3rd Class**: Lowest survival rate (~24%)

### Age Patterns
- Children (age < 10) had higher survival rates
- Elderly passengers had lower survival rates
- Most passengers were between 20-40 years old

### Family Dynamics
- Passengers with 1-3 family members had better survival rates
- Solo travelers and large families had lower survival rates

### Economic Factors
- Higher fare prices correlated with better survival rates
- Fare varied significantly by passenger class

## Visualizations

Key visualizations included in this analysis:

1. **Survival Rate by Gender** - Bar chart showing dramatic difference
2. **Age Distribution** - Histogram with survival overlay
3. **Passenger Class Distribution** - Count plot with survival rates
4. **Correlation Heatmap** - Feature relationships
5. **Fare vs Survival** - Box plot comparison
6. **Family Size Impact** - Grouped bar chart
7. **Embarkation Analysis** - Stacked bar chart
8. **Age vs Fare Scatter Plot** - Colored by survival status

## Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Programming language | 3.8+ |
| **Pandas** | Data manipulation and analysis | 2.0+ |
| **NumPy** | Numerical computing | 1.24+ |
| **Matplotlib** | Data visualization | 3.7+ |
| **Seaborn** | Statistical visualization | 0.12+ |
| **Jupyter** | Interactive notebooks | 1.0+ |
| **SciPy** | Statistical testing | 1.10+ |

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

Please ensure your code follows Python best practices and includes appropriate documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Moses Amwoma**

- GitHub: [@mosesamwoma](https://github.com/mosesamwoma)
- Project Link: [https://github.com/mosesamwoma/titanic-exploratory-data-analysis](https://github.com/mosesamwoma/titanic-exploratory-data-analysis)

## Acknowledgments

- [Kaggle](https://www.kaggle.com) for providing the Titanic dataset
- The data science community for tutorials and inspiration
- Encyclopedia Titanica for historical context

## Future Improvements

**Machine Learning Models**
- Build predictive models using Logistic Regression and Random Forest
- Compare model performance and accuracy
- Implement feature engineering for better predictions

**Enhanced Visualizations**
- Add interactive plots with Plotly
- Create survival probability heatmaps
- Develop family group survival analysis

**Code Quality**
- Refactor code into reusable functions
- Add unit tests for data cleaning functions
- Create automated data validation pipeline

**Documentation**
- Write detailed analysis report with findings
- Add code comments and docstrings
- Create step-by-step tutorial for beginners

---

**⭐ If you found this project helpful, please consider giving it a star!**

*Last Updated: December 2025*
