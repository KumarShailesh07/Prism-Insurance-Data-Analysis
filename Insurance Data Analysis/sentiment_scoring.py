# ================================================
# Prism Insurance - Customer Sentiment Scoring
# Tool: Python + TextBlob
# Author: Shailesh Kumar
# Description: Calculates sentiment polarity scores
#              from customer feedback using TextBlob
# ================================================

import pandas as pd
from textblob import TextBlob

# ── Load Data ──────────────────────────────────
df = pd.read_csv('customer_feedback.csv')

# ── Sentiment Scoring ──────────────────────────
text_column = "Feedback"

df['Sentiment_Score'] = df[text_column].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

# ── Categorize Sentiment ───────────────────────
def categorize(score):
    if score >= 0.5:
        return 'Excellent'
    elif score >= 0.1:
        return 'Good'
    else:
        return 'Needs Improvement'

df['Sentiment_Category'] = df['Sentiment_Score'].apply(categorize)

# ── Save Output ────────────────────────────────
df.to_csv('sentiment_output.csv', index=False)

print("✅ Sentiment scoring complete!")
print(df[['Feedback', 'Sentiment_Score', 'Sentiment_Category']].head(10))