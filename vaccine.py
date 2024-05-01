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

#####################3


    st.subheader('COVID-19 Vaccine Doses by State')

    # Line plot for dose1 and dose2
    fig, ax = plt.subplots(figsize=(15, 10))

    # Plot dose1
    ax.plot(df2['state'], df2['dose1'], marker='o', color='blue', label='Dose 1')

    # Plot dose2
    ax.plot(df2['state'], df2['dose2'], marker='o', color='orange', label='Dose 2')

    # Plot dose3
    ax.plot(df2['state'], df2['dose3'], marker='o', color='black', label='Dose 3')

    # Add count labels on top of each data point for dose1
    for i, txt in enumerate(df2['dose1']):
        ax.text(i, txt, f'{txt:,}', ha='center', va='bottom')

    # Add count labels on top of each data point for dose2
    for i, txt in enumerate(df2['dose2']):
        ax.text(i, txt, f'{txt:,}', ha='center', va='bottom')

    # Add count labels on top of each data point for dose3
    for i, txt in enumerate(df2['dose3']):
        ax.text(i, txt, f'{txt:,}', ha='center', va='bottom')    

    ax.set_xlabel('States')
    ax.set_ylabel('Doses Administered')
    ax.set_title('COVID-19 Vaccine Doses by State')
    ax.set_xticklabels(df2['state'], rotation=45, ha='right')  # Rotate x-axis labels for better readability
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))  # Formatting y-axis labels with commas
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)


    

#***********************************************************************


##########################

    st.subheader('COVID-19 Vaccine Distribution by State')

    # Selectbox to choose the state
    selected_state = st.selectbox('Select State', df2['state'])

    if selected_state:
        # Filter data for the selected state
        state_data = df2[df2['state'] == selected_state]

        # Plot the data
        plt.figure(figsize=(10, 6))

        # Bar plot for dose1, dose2, and dose3 distribution
        bars = plt.bar(['Dose 1', 'Dose 2', 'Dose 3'], state_data[['dose1', 'dose2', 'dose3']].iloc[0])
        plt.xlabel('Dose')
        plt.ylabel('Number of Doses')
        plt.title(f'COVID-19 Vaccine Distribution in {selected_state}')
        plt.grid(True)

        # Add total population as text in front of each bar
        for i, bar in enumerate(bars):
            yval = bar.get_height()
            total_population = state_data['population'].iloc[0]
            plt.text(bar.get_x() + bar.get_width()/2, yval + 50, f'Total Population: {total_population:,}\nDoses: {int(yval):,} ({yval / total_population * 100:.2f}%)', va='bottom', ha='center')

        st.pyplot(plt)

    
