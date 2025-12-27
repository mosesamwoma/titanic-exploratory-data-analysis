import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_all(df):
    """Generates and saves visual reports."""
    sns.set_theme(style="whitegrid")
    
    out_dir = Path(__file__).parent.parent / "reports" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Correlation Matrix
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig(out_dir / "correlation.png")
    plt.close()
    
    # 2. Survival by Class
    if 'survived' in df.columns:
        plt.figure(figsize=(8, 6))
        sns.barplot(data=df, x='pclass', y='survived', hue='sex')
        plt.title("Survival Rates by Class & Gender")
        plt.savefig(out_dir / "survival_analysis.png")
        plt.close()