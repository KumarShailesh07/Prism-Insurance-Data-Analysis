# 🏢 Prism Insurance Pvt. Ltd. — Data Analysis Dashboard

> An end-to-end Data Analytics project built using SQL Server, Excel, Python, and Power BI
> to analyze insurance business performance and customer sentiment for Prism Insurance Pvt. Ltd.

---

## 📌 Project Overview
This project delivers a complete Business Intelligence solution for Prism Insurance Pvt. Ltd.
It combines insurance operational data from SQL Server with customer feedback from Excel,
processes sentiment using Python NLP, and presents everything through two interactive
Power BI dashboards — one for business KPIs and one for customer sentiment analysis.

---

## 🎯 Objectives
- Monitor key insurance business metrics — premiums, claims, and policies
- Analyze customer sentiment from feedback using Python NLP
- Identify business red flags and service strengths
- Support data-driven decision making for management

---

## 🛠️ Tools & Technologies
| Tool | Purpose |
|------|---------|
| SQL Server | Primary data source for insurance data |
| Excel (.xlsx) | Data source for customer feedback |
| Power BI | Interactive business dashboards |
| Python | Sentiment scoring & word cloud |
| TextBlob | NLP sentiment polarity analysis |
| WordCloud | Visual text frequency mapping |
| Pandas | Data manipulation & processing |
| Matplotlib | Plotting & visualization |

---

## 🗄️ Data Sources

### Source 1 — SQL Server
- **Dataset:** `InsuranceData`
- **Contains:** Policy details, claim amounts, customer demographics, premium data
- **Connection:** Imported into Power BI via SQL Server connector

### Source 2 — Excel Import
- **File:** `Insurance+Customer+Feedback.xlsx`
- **Contains:** Customer names, feedback text, sentiment scores
- **Connection:** Imported into Power BI via Excel connector

### Data Flow
```
SQL Server (Insurance Data)
          +
Excel (Customer Feedback)
          ↓
Power BI (Data Model)
          ↓
Python (Sentiment Scoring + Word Cloud)
          ↓
2 Interactive Dashboards
```

---

## 📁 Project Structure
```
Prism-Insurance-Data-Analytics/
│
├── 📄 README.md
├── 🐍 sentiment_scoring.py            ← Sentiment scoring script
├── 🐍 wordcloud_sentiment.py          ← Word cloud generation script
├── 📊 Insurance Data Analysis.pbix    ← Power BI dashboard file
├── 📁 Data/
│   ├── InsuranceData.xlsx             ← Raw insurance dataset
│   └── Insurance+Customer+Feedback.xlsx  ← Customer feedback dataset
└── 📁 Screenshots/
    ├── Insurance Business Overview.png   ← Dashboard 1
    └── Customer Sentiment Analysis.png  ← Dashboard 2
```

---

## 📊 Dashboard 1 — Insurance Business Overview

<img width="638" height="359" alt="Insurance Business Overview" src="https://github.com/user-attachments/assets/8bb4db77-bbb6-4c3c-a018-bc45434a1257" />

### Key KPIs
| Metric | Value |
|--------|-------|
| Premium Amount | 5.97M |
| Coverage Amount | 600.33M |
| Claim Amount | 16.90M |
| Total Customers | 10,000 |
| Male Customers | 5,000 |
| Female Customers | 5,000 |

### Premium by Policy Type
| Policy Type | Premium Amount | |
|-------------|---------------|-|
| Travel | 2.5M | 🏆 Top Performer |
| Health | 1.2M | |
| Auto | 1.0M | |
| Life | 0.7M | |
| Home | 0.6M | ⚠️ Needs Growth |

### Claims Status
| Status | Count | |
|--------|-------|-|
| Rejected | 4,400 | 🚨 Highest |
| Settled | 3,400 | |
| Pending | 2,300 | |

### Active vs Inactive Policies
| Status | Percentage |
|--------|-----------|
| Active | 58.11% |
| Inactive | 41.89% ⚠️ |

### Claim Amount by Age Group
| Age Group | Claim Amount |
|-----------|-------------|
| Adult | 8.8M |
| Elder | 6.4M |
| Young Adult | 1.7M |

### Claims by Policy Type (Detailed)
| Policy Type | Pending | Rejected | Settled |
|-------------|---------|----------|---------|
| Auto | 20.8M | 40.6M | 32.9M |
| Health | 27.6M | 52.4M | 40.0M |
| Home | 13.0M | 27.4M | 20.6M |
| Life | 17.2M | 33.7M | 23.1M |
| Travel | 57.0M | 107.3M | 86.1M |
| **Total** | **135.8M** | **261.5M** | **202.9M** |

---

## 📊 Dashboard 2 — Customer Sentiment Analysis

<img width="639" height="364" alt="Customer Sentiment Analysis" src="https://github.com/user-attachments/assets/da94ad30-1949-449c-9f02-0c0e9537ca8d" />


### Sentiment Distribution
| Category | Count | Percentage |
|----------|-------|------------|
| Needs Improvement | 140 | 73% 🚨 |
| Good | 32 | 16% |
| Excellent | 22 | 11% |

### Sentiment Score Range
| Category | Score Range |
|----------|------------|
| Excellent | >= 0.50 |
| Good | 0.10 to 0.49 |
| Needs Improvement | Below 0.10 |

### Top Pain Points 🚨
| Issue | Customer Feedback |
|-------|------------------|
| Customer Service | Rude, unhelpful, needs better training |
| Claims Process | Too slow, hassle to get reimbursed |
| Policy Clarity | Terms too confusing for customers |

### Strengths ✅
| Strength | Customer Feedback |
|----------|------------------|
| Mobile App | Excellent, very user-friendly |
| Website Navigation | Easy to use, find information quickly |
| Coverage Options | Customers pleased with policy options |

---

## 🔗 Key Business Findings

### 🚨 Red Flags
- Rejected claims **(4.4K)** exceed settled claims **(2.3K)** — major operational concern
- **41.89%** policies are inactive — serious customer retention issue
- **73%** of all customer feedback needs improvement
- Customer service is the **#1 complaint** area
- Coverage **(600.33M)** vs Premium **(5.97M)** — high financial risk exposure
- Travel policy has highest rejected claims at **107.3M**

### ✅ Positives
- Travel insurance is strongest revenue driver at **2.5M**
- Equal gender distribution (50/50) shows broad market reach
- Mobile app and website navigation rated highly
- Coverage options well received when clearly communicated

### 💡 Business Recommendations
- Improve customer service training urgently
- Simplify claims process to reduce rejection rate
- Focus on reactivating **41.89%** inactive policies
- Clarify policy terms to reduce customer confusion
- Invest more in Health and Home insurance growth

---

## 🔄 Complete Project Workflow
```
SQL Server                    Excel
(InsuranceData)    +    (Customer Feedback)
         ↓
   Power BI Data Model
         ↓
Python — sentiment_scoring.py
(TextBlob NLP Sentiment Scoring)
         ↓
Python — wordcloud_sentiment.py
(Word Cloud Visual in Power BI)
         ↓
Dashboard 1: Insurance Business Overview
Dashboard 2: Customer Sentiment Analysis
```

---

## ⚙️ How to Run

### Install Python Requirements
```bash
pip install pandas textblob wordcloud matplotlib
```

### Run Sentiment Scoring
```bash
python sentiment_scoring.py
```

### Run Word Cloud
```bash
python wordcloud_sentiment.py
```

### View Power BI Dashboard
- Open `Insurance Data Analysis.pbix` in **Power BI Desktop**
- Connect to your **SQL Server** for insurance data
- Import `Insurance+Customer+Feedback.xlsx` for feedback data

---

## 📈 Future Improvements
- Use **BERT/Transformers** for more accurate sentiment detection
- Add **time-series analysis** to track sentiment trends over time
- Build **topic clustering** to group feedback by category
- Add **neutral sentiment** category for borderline scores
- Create **automated data refresh** pipeline in Power BI Service
- Add **drill-through pages** per policy type

---

## 👤 Author
**Shailesh Kumar**
- 🔗 LinkedIn: www.linkedin.com/in/shailesh-kumar7
- 🐙 GitHub: [your github profile]

---

## 📜 License
This project is open source and available under the [MIT License](LICENSE).
