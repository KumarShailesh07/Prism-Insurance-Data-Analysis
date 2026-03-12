# ================================================
# Prism Insurance - Customer Feedback Word Cloud
# Tool: Python
# Author: Shailesh Kumar
# Description: Generates a word cloud from customer
#              feedback data for sentiment visualization
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ── Load Data ──────────────────────────────────
# Replace with your actual CSV file path
df = pd.read_csv('customer_feedback.csv')

# ── Generate Word Cloud ────────────────────────
text = " ".join(df['Feedback'].astype(str))

wordcloud = WordCloud(
    width=1200,
    height=1600,
    background_color='black',
    max_words=150,
    max_font_size=250,
    min_font_size=20,
    prefer_horizontal=0.9
).generate(text)

# ── Plot & Save ────────────────────────────────
plt.figure(figsize=(12, 16))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()
plt.savefig('wordcloud_output.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ Word cloud saved as 'wordcloud_output.png'")
