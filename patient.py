import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
from streamlit_option_menu import option_menu 

def app():
        st.title('COVID-19 ANALYSIS')
        img = Image.open('./static/covid.jpg')
        st.image(img,use_column_width=True)

        col1, col2, col3 = st.columns(3)
    
        col1.error('Active - 3552')
        col2.success('Discharged - 44143665')
        col3.warning('Deaths - 530698')

        df= pd.read_csv('weekly_data.csv')
        df2= pd.read_csv('covid.csv')


        # -----------------------1st chart-------------------------------
        st.subheader("Weekly COVID-19 Cases Across India by Date")
        # Create the line plot
        end_dates = df['enddate']
        total_cases = df['total']
        fig, ax = plt.subplots(figsize=(18, 9))
        ax.plot(end_dates, total_cases, marker='o', color='blue', linestyle='-')
        ax.set_xlabel('End Date')
        ax.set_ylabel('Total COVID-19 Cases')
        ax.set_title('Distribution of Total COVID-19 Cases by End Date')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        ax.grid(True)  # Add grid lines

        # Format y-axis labels to display in millions
        formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
        ax.yaxis.set_major_formatter(formatter)

        # Add annotations
        for date, cases in zip(end_dates, total_cases):
            ax.annotate(f'{cases:,.0f}', (date, cases), textcoords="offset points", xytext=(0,10), ha='center')

        # Adjust layout to prevent clipping of labels
        plt.tight_layout()

        # Display the plot in Streamlit
        st.pyplot(fig)

        # -----------------------2nd chart-------------------------------
        st.subheader("Confirmed COVID-19 Cases by State")
        states = df2['state']
        confirmed_cases = df2['confirmed']

        fig, ax = plt.subplots(figsize=(15, 10))
        bars = ax.bar(states, confirmed_cases, color='skyblue')

        # Add count labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, '{:,}'.format(int(yval)), va='bottom', ha='center')

        ax.set_xlabel('States')
        ax.set_ylabel('Confirmed Cases')
        ax.set_title('Confirmed COVID-19 Cases by State')
        ax.set_xticklabels(states, rotation=45, ha='right')  # Rotate x-axis labels for better readability
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) # Formatting y-axis labels with commas
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        st.pyplot(fig)

        # -----------------------3rd chart-------------------------------
        st.subheader("active COVID-19 Cases by State")
        states = df2['state']
        active_cases = df2['active']

        fig, ax = plt.subplots(figsize=(15, 10))
        bars = ax.bar(states, active_cases, color='skyblue')

        # Add count labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, '{:,}'.format(int(yval)), va='bottom', ha='center')

        ax.set_xlabel('States')
        ax.set_ylabel('active Cases')
        ax.set_title('active COVID-19 Cases by State')
        ax.set_xticklabels(states, rotation=45, ha='right')  # Rotate x-axis labels for better readability
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) # Formatting y-axis labels with commas
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        st.pyplot(fig)

        # -----------------------4th chart-------------------------------
        st.subheader("COVID-19 Recovered Cases by State")
        states = df2['state']
        passive_cases = df2['passive']

        fig, ax = plt.subplots(figsize=(15, 10))
        bars = ax.bar(states, passive_cases, color='skyblue')

        # Add count labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, '{:,}'.format(int(yval)), va='bottom', ha='center')

        ax.set_xlabel('States')
        ax.set_ylabel('Discharged Cases')
        ax.set_title('Discharged COVID-19 Cases by State')
        ax.set_xticklabels(states, rotation=45, ha='right')  # Rotate x-axis labels for better readability
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) # Formatting y-axis labels with commas
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        st.pyplot(fig)

        # -----------------------5th chart-------------------------------
        st.subheader("COVID-19 Deaths by State")
        states = df2['state']
        deaths_cases = df2['deaths']

        fig, ax = plt.subplots(figsize=(15, 10))
        bars = ax.bar(states, deaths_cases, color='skyblue')

        # Add count labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, '{:,}'.format(int(yval)), va='bottom', ha='center')

        ax.set_xlabel('States')
        ax.set_ylabel('deaths Cases')
        ax.set_title('deaths COVID-19 Cases by State')
        ax.set_xticklabels(states, rotation=45, ha='right')  # Rotate x-axis labels for better readability
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) # Formatting y-axis labels with commas
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        st.pyplot(fig)


        #---------------------------------------------------------------
        st.subheader("Population by State")
        states = df2['state']
        deaths_cases = df2['population']

        fig, ax = plt.subplots(figsize=(15, 10))
        bars = ax.bar(states, deaths_cases, color='skyblue')

        # Add count labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, '{:,}'.format(int(yval)), va='bottom', ha='center')

        ax.set_xlabel('States')
        ax.set_ylabel('population')
        ax.set_title('population by State')
        ax.set_xticklabels(states, rotation=45, ha='right')  # Rotate x-axis labels for better readability
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) # Formatting y-axis labels with commas
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        st.pyplot(fig)
       