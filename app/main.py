import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Solar Energy Data Comparison")

country = st.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
file_map = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_leone_clean.csv",
    "Togo": "data/togo_clean.csv"
}
df = pd.read_csv(file_map[country])

st.write(f"Summary Statistics for {country}")
st.dataframe(df.describe())

fig, ax = plt.subplots()
sns.histplot(df['GHI'], kde=True, ax=ax)
ax.set_title(f"GHI Distribution in {country}")
st.pyplot(fig)

