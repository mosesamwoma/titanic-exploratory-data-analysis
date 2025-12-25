# Data Cleaning and Visualization

A collection of hands-on projects for learning data cleaning, analysis, and visualization with Python.

## Prerequisites

- Python 3.8+
- Git
- pip

## Quick Start

```bash
# Clone repository
git clone https://github.com/mosesamwoma/data-cleaning-and-visualization.git
cd data-cleaning-and-visualization

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter (optional)
jupyter notebook
```

## What You'll Learn

- Clean messy datasets (missing values, duplicates, outliers)
- Transform and reshape data
- Perform exploratory data analysis
- Create meaningful visualizations
- Build automated data workflows

```

## Key Technologies

- **Pandas** - Data manipulation
- **Matplotlib/Seaborn** - Visualization
- **NumPy** - Numerical computing
- **Jupyter** - Interactive notebooks

## Quick Example

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('data.csv')
df.dropna(inplace=True)

# Visualize
df['sales'].plot(kind='bar')
plt.show()
```

## Resources

- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Matplotlib Docs](https://matplotlib.org/)
- [Seaborn Docs](https://seaborn.pydata.org/)

## License

MIT License - Personal learning project

---

**Moses Amwoma** - [GitHub](https://github.com/mosesamwoma)
