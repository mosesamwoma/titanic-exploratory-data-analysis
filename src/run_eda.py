import sys
import pandas as pd
from pathlib import Path

# 1. SETUP PATHS (The "Smart" Way)
# This finds the 'EDA' folder no matter how you run the script
ROOT_DIR = Path(__file__).resolve().parent.parent

# Update these to match exactly where your file is right now
INPUT_FILE = ROOT_DIR / "data" / "titanic_cleaned.csv" 
OUTPUT_DIR = ROOT_DIR / "reports" / "figures"

# Add 'src' to system path for imports
sys.path.append(str(ROOT_DIR / "src"))

from data_cleaning import clean_data
from feature_engineering import add_features
from visualization import plot_all

def main():
    print(f"🚀 Project Root: {ROOT_DIR}")
    
    if not INPUT_FILE.exists():
        print(f"❌ Still can't find the file at: {INPUT_FILE}")
        print("Please check if the filename is 'titanic_cleaned.csv' inside the 'data' folder.")
        return

    try:
        # Load
        df = pd.read_csv(INPUT_FILE)
        print(f"✅ Loaded {INPUT_FILE.name}")

        # Process
        df = clean_data(df)
        df = add_features(df)
        
        # Visualize
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        plot_all(df)
        print(f"✅ Visuals generated in: {OUTPUT_DIR}")
        
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    main()