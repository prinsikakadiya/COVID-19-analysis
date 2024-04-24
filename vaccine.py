import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd


def app():

    st.subheader("COVID-19 vaccine")
    st.write("A COVID‑19 vaccine is a vaccine intended to provide acquired immunity against severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), the virus that causes coronavirus disease 2019 (COVID‑19).")
    st.write("The COVID‑19 vaccines are widely credited for their role in reducing the spread of COVID‑19 and reducing the severity and death caused by COVID‑19. According to a June 2022 study, COVID‑19 vaccines prevented an additional 14.4 to 19.8 million deaths in 185 countries and territories from 8 December 2020 to 8 December 2021. Many countries implemented phased distribution plans that prioritized those at highest risk of complications, such as the elderly, and those at high risk of exposure and transmission, such as healthcare workers.")
    img = Image.open('./static/vaccine_photo.jpg')
    st.image(img,use_column_width=True)
    st.write("Common side effects of COVID‑19 vaccines include soreness, redness, rash, inflammation at the injection site, fatigue, headache, myalgia (muscle pain), and arthralgia (joint pain), which resolve without medical treatment within a few days. COVID‑19 vaccination is safe for people who are pregnant or are breastfeeding")
    st.write("")
    st.write("")
    st.write("")
    df2= pd.read_csv('covid.csv')

    st.subheader("COVID-19 vaccine total dose")
    states = df2['state']
    total_doses = df2['total_doses']

    fig, ax = plt.subplots(figsize=(15, 10))
    bars = ax.bar(states, total_doses, color='skyblue')

        # Add count labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, '{:,}'.format(int(yval)), va='bottom', ha='center')

    ax.set_xlabel('States')
    ax.set_ylabel('vaccine total_doses')
    ax.set_title('COVID-19 vaccine total dos')
    ax.set_xticklabels(states, rotation=45, ha='right')  # Rotate x-axis labels for better readability
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) # Formatting y-axis labels with commas
    plt.tight_layout()  # Adjust layout to prevent clipping of labels

    st.pyplot(fig)