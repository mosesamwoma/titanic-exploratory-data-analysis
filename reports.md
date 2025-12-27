# Titanic Dataset – Explanatory Data Analysis (EDA)

## 1. Introduction
The sinking of the RMS Titanic is one of the most well-known maritime disasters in history.  
This project performs **Explanatory Data Analysis (EDA)** on the Titanic dataset to identify
key factors that influenced passenger survival.

The primary objective of this analysis is to understand patterns, relationships, and trends
in the data rather than to build predictive models.

---

## 2. Dataset Overview
- **Source:** Titanic passenger dataset
- **Number of records:** 891 passengers
- **Target variable:** `Survived`
  - `0` → Did not survive
  - `1` → Survived

### Key Features
- `Sex` – Passenger gender
- `Age` – Passenger age
- `Pclass` – Passenger class (1st, 2nd, 3rd)
- `Fare` – Ticket fare
- `SibSp` / `Parch` – Family relations onboard
- `Embarked` – Port of embarkation

---

## 3. Data Cleaning Summary
The following preprocessing steps were applied:
- Removed high-cardinality and non-informative columns (`Name`, `Ticket`, `Cabin`)
- Filled missing `Age` values with the median
- Filled missing `Fare` values with the median
- Filled missing `Embarked` values with the mode
- Created a new feature `FamilySize`

These steps ensured consistency while preserving interpretability.

---

## 4. Target Variable Analysis
### Survival Distribution
The dataset is **imbalanced**, with significantly more passengers not surviving than surviving.
This reflects the severity of the disaster and provides an important baseline for analysis.

**Insight:**
> Survival was the exception rather than the norm.

---

## 5. Survival by Gender
Female passengers had a **much higher survival rate** compared to male passengers.

**Insight:**
> Gender was one of the strongest determinants of survival, supporting the historical
“women and children first” evacuation policy.

---

## 6. Survival by Passenger Class
Survival rates varied significantly across passenger classes:
- 1st Class: Highest survival rate
- 2nd Class: Moderate survival rate
- 3rd Class: Lowest survival rate

**Insight:**
> Socioeconomic status played a critical role in survival outcomes.

---

## 7. Age and Survival
Age distributions show that:
- Children had higher survival rates
- Older passengers were less likely to survive

**Insight:**
> Younger passengers were prioritized during evacuation, while age reduced survival chances.

---

## 8. Fare and Survival
Passengers who survived generally paid higher fares.

**Insight:**
> Higher fares, which correlate with better accommodation and class, increased survival probability.

---

## 9. Family Size and Survival
Family size was engineered as:

Findings:
- Small families (2–4 members) had the highest survival rates
- Solo travelers and very large families had lower survival rates

**Insight:**
> Moderate family size provided support without creating evacuation difficulties.

---

## 10. Embarkation Port Analysis
Survival rates differed across embarkation ports.

**Insight:**
> Differences likely reflect variations in passenger class and demographics at each port.

---

## 11. Key Findings
- Gender and passenger class are the most influential survival factors
- Age and fare provide secondary explanatory power
- Family structure impacts survival non-linearly
- Survival was not random; it followed social and economic patterns

---

## 12. Conclusion
This EDA demonstrates that survival aboard the Titanic was strongly influenced by
social structure, gender norms, and economic status rather than chance alone.

The insights gained from this analysis provide a strong foundation for future
predictive modeling or historical interpretation.

---

## 13. Future Work
- Apply machine learning models for survival prediction
- Perform feature importance analysis
- Compare classical ML vs modern techniques
