import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.header('COVID-19 State wise Status')
    select = st.selectbox('Please select one',['Andman and Nicobar',
                                               'Andhra Pradesh',
                                               'Arunachal Pradesh',
                                               'Assam',
                                               'Bihar',
                                               'Chandigarh',
                                               'Chhattisgarh',
                                               'Daman and Diu',
                                               'Delhi',
                                               'Goa',
                                               'Gujarat',
                                               'Haryana',
                                               'Himachal Pradesh',
                                               'Jammu and Kashmir',
                                               'Jharkhand',
                                               'Karnataka',
                                               'Kerala',
                                               'Ladakh',
                                               'Lakshadweep',
                                               'Madhya Pradesh',
                                               'Maharashtra',
                                               'Manipur',
                                               'Meghalaya',
                                               'Mizoram',
                                               'Nagaland',
                                               'Odisha',
                                               'Puducherry',
                                               'Punjab',
                                               'Rajasthan',
                                               'Rajasthan',
                                               'Tamil Nadu',
                                               'Telengana',
                                               'Tripura',
                                               'Uttar Pradesh',
                                               'Uttarakhand',
                                               'West Bengal'])

    if select == 'Andman and Nicobar':
        Andman_and_Nicobar()

    if select == 'Andhra Pradesh':
        Andhra_Pradesh()    

    if select == 'Arunachal Pradesh':
        Arunachal_Pradesh()

    if select == 'Assam':
        Assam()

    if select == 'Bihar':
        Bihar()

    if select == 'Chandigarh':
        Chandigarh()    

    if select == 'Chhattisgarh':
        Chhattisgarh()

    if select == 'Daman and Diu':
        Daman_Diu()    

    if select == 'Delhi':
        Delhi()

    if select == 'Goa':
        Goa()

    if select == 'Gujarat':
        Gujarat()

    if select == 'Haryana':
        Haryana()   

    if select == 'Himachal Pradesh':
        Himachal_Pradesh()

    if select == 'Jammu and Kashmir':
        Jammu_Kashmir()    

    if select == 'Jharkhand':
        Jharkhand()

    if select == 'Karnataka':
        Karnataka()
    
    if select == 'Kerala':
        Kerala()

    if select == 'Ladakh':
        Ladakh()
    
    if select == 'Lakshadweep':
        Lakshadweep()

    if select == 'Madhya Pradesh':
        Madhya_Pradesh()
    
    if select == 'Maharashtra':
        Maharashtra()

    if select =='Manipur':
        Manipur()
    
    if select =='Meghalaya':
       Meghalaya()

    if select =='Mizoram':
        Mizoram()
    
    if select =='Nagaland':
        Nagaland()
    
    if select =='Odisha':
        Odisha()

    if select =='Puducherry':
        Puducherry()
    
    if select =='Punjab':
        Punjab()
    
    if select =='Rajasthan':
        Rajasthan()
    
    if select =='Sikkim':
        Sikkim()
    
    if select =='Tamil Nadu':
        Tamil_Nadu()

    if select =='Telengana':
        Telengana()

    if select =='Tripura':
        Tripura()

    if select =='Uttar Pradesh':
        Uttar_Pradesh()

    if select =='Uttarakhand':
        Uttarakhand()

    if select =='West Bengal':
        West_Bengal()

    
    
    
def Andman_and_Nicobar():
    st.subheader('COVID-19 pandemic in Andman and Nicobar')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the union territory of Andaman and Nicobar Islands. The first case was recorded in this region on 26 March 2020. The islands have pursued a strategy of zero COVID-19 transmission, which, except for three flareups in August 2020, May 2021, and January 2022, which were swiftly contained, have resulted in no community outbreaks. The islands have successfully managed the outbreaks, and the union territory has the lowest case count of any region of India, both in total cases and infection rate')
    st.write('In 2021 during the 2nd Wave of COVID-19 Pandemic the Colleges & educational Institutions of Andaman & Nicobar Islands was still continued follow the offline mode of teaching. Siddhanth Rai Sharma a Students Leader of ABVP demanded to close all the colleges of Andaman & Nicobar Islands for the safety of the Students community of Islands.')
    st.write('total population: 426251')
    st.write('total confirmed case: 10742')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [1, 10612, 129]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Andman and Nicobar')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Andman and Nicobar')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)



def Andhra_Pradesh():
    st.subheader('COVID-19 pandemic in Andhra Pradesh')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Andhra Pradesh was reported in Nellore on 12 March 2020. A 24-year-old who was confirmed positive for coronavirus. He had travel history to Italy.The Andhra Pradesh Health department has confirmed a total of 5,37,687 cases, including 4,702 deaths and 4,35,467 recoveries, as of 10 September.The virus has spread in 13 districts of the state, of which East Godavari has the highest number of cases.')
    st.write('total population: 52883163')
    st.write('total confirmed case: 2339067')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [3, 2324331, 14733]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Andhra Pradesh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Andhra Pradesh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Arunachal_Pradesh():
    st.subheader('COVID-19 pandemic in Arunachal Pradesh')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the state of Arunachal Pradesh. The first case was recorded in this region on 2 April 2020')
    st.write('As of February 2, 2022, more than 1.26million cases of COVID-19 have been confirmed in Arunachal Pradesh')  
    st.write('total population: 1528296')
    st.write('total confirmed case: 66890')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 66594, 296]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Arunachal Pradesh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Arunachal Pradesh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)      

def Assam():
    st.subheader('COVID-19 pandemic in Assam')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Assam was reported on 31 March 2020.As of 12 April 2024, the Government of Assam has confirmed a total of 89,468positive cases of COVID-19 including 67,641 recoveries, three migrations and 234 deaths in the state.The state as well as northeast largest city, Guwahati, has been worst affected by coronavirus')
    st.write('The COVID-19 outbreak in Assam has been traced to persons who attended the conference of the Tablighi Jamaat religious organisation at Nizamuddin Markaz (Delhi) and did not report to the authorities after their return to Assam. Out of the total patients of COVID-19 in Assam – 37 are either attendees or contacts of Tablighi Jamaat. The COVID-19 tally in Assam also shoots up due to some pilgrims of Ajmer Sharif Dargah (Rajasthan), who arrived in the Silchar city of Cachar district by bus on 6 May. Later on, 10 pilgrims tested positive for coronavirus and the others were sent to quarantine as per guidelines')
    st.write('total population: 34586234')
    st.write('total confirmed case: 746100')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 738065, 8035]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Assam')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Assam')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

#****
def Bihar():
    st.subheader('COVID-19 pandemic in Bihar')
    st.write('The first COVID-19 case in the Indian state of Bihar was reported in Munger on 22 March 2020, a 38-year-old tested positive for COVID-19, he was also the first victim. He had travel history to Qatar. The Ministry of Health and Family Welfare has confirmed a total of 62,031 cases as of 4 August 2020, including 20,922 active cases, 349 deaths and 40,760 recoveries. The virus has spread in 38 districts of the state, of which Patna district has the highest number of cases.')
    st.write('The state has been under lockdown since 25 March 2020. The state government has responded to the outbreak by following a contact-tracing, testing, and home-to-home surveillance model.')
    st.write('total population: 119461013')
    st.write('total confirmed case: 851379')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [15, 839062, 12302]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Bihar')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Bihar')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Chandigarh():
    st.subheader('COVID-19 pandemic in Chandigarh')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the union territory of Chandigarh. The first case was recorded in this region on 19 March 2020. As on 24 May, total number of cases in Chandigarh was 225. This contains 43 active cases as 179 successfully recovered from it and three died from the virus.')
    st.write('On 19 March, first confirmed case was reported in the union territory as a 23-year-old woman who had travel history to London tested positive.')
    st.write('total population: 1182104')
    st.write('total confirmed case: 99348')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [6, 98161, 1181]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Chandigarh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Chandigarh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Chhattisgarh():
    st.subheader('COVID-19 pandemic in Chhattisgarh')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the state of Chhattisgarh. The first case was recorded in this region on 19 March 2020.')
    st.write('The first confirmed case of coronavirus in Chhattisgarh was reported on 19 March 2020 in Raipur, where a woman returning from London via Mumbai Airport was tested positive.')
    st.write('total population: 28566990')
    st.write('total confirmed case: 1177749')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [6, 1163597, 14146]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Chhattisgarh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Chhattisgarh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Daman_Diu():
    st.subheader('COVID-19 pandemic in Daman and Diu')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the union territory of Dadra and Nagar Haveli and Daman and Diu. The first case was recorded in this region on 10 April 2020.')
    st.write('As of december, 2022, the total number of cases in Dadra & Nagar Haveli and Daman & Diu was 11591, including 11587 cures and 4 deaths. There wasn not any active case in the UT.')
    st.write('total population: 657391')
    st.write('total confirmed case: 11591')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 11587, 4]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Daman and Diu')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Daman and Diu')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Delhi():
    st.subheader('COVID-19 pandemic in Delhi')
    st.write('The first case of the COVID-19 pandemic in the Indian capital of Delhi was reported on 2 March 2020. Delhi has the seventh-highest number of confirmed cases of COVID-19 in India. On 22 March, Delhi observed a 14-hour voluntary public curfew (the Janata curfew) along with 75 districts in India, at the directive of the Prime Minister. A nationwide lockdown was later issued for 21 days from 24 March.[')
    st.write('It was reported that air quality index of Delhi improved on 28 March 2020, after the lockdown had reduced traffic. In April 2021, with cases increasing daily, CM Arvind Kejriwal announced a weekend curfew in Delhi every weekend. Notably, the traffic in the capital city decreased by a large amount. On 19 April 2021, Delhi turned the weekend curfew to a week-long lockdown. The lockdown was extended several times - on April 25, May 2, May 9, May 15 until May 24 (as updated on May 19). Now lockdown is unlocked on 8 June.')
    st.write('total population: 18802494')
    st.write('total confirmed case: 2007188')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [35, 1980632, 26521]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Delhi')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Delhi')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Goa():
    st.subheader('COVID-19 pandemic in Goa')
    st.write('First case relating to the COVID-19 pandemic was confirmed in Goa on 25 March 2020. The state was COVID-19 free for 23 days until the disease resurfaced on 14 May when a family returning from the neighbouring state of Maharashtra tested positive. The worst impact was felt around September–October 2020, while as of April–May 2021, a second wave of COVID-19 was also felt strongly across the small State.')
    st.write('On 14 March 2020, the government of Goa announced that the schools and colleges in the state would remain closed until 1 April 2020. 2 more positive cases were announced as being positive on 29 March 2020. One person had returned from the Bahamas, while the other had been in contact with one of the first three positive patients. Both were Goans, and were already under quarantine.')
    st.write('total population: 1542750')
    st.write('total confirmed case: 259079')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [26, 255040, 4013]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Goa')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Goa')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Gujarat():
    st.subheader('COVID-19 pandemic in Gujarat')
    st.write('In Gujarat, the first two cases of the COVID-19 pandemic were confirmed on 19 March 2020 in Rajkot and Surat.')
    st.write('On 15 March 2020, Anil Mukim, Chief Secretary of Gujarat, announced the closure of schools, colleges, educational institutes, malls, multiplexes, and swimming pools across the state until March 29 as a precaution against COVID-19. However, the ongoing board examinations for class X and XII were allowed to be conducted.[3] Also, fine of ₹500 was imposed on public spitting in Gujarat.')
    st.write('total population: 63907200')
    st.write('total confirmed case: 1277557')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [41, 1266473, 11043]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Gujarat')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Gujarat')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Haryana():
    st.subheader('COVID-19 pandemic in Haryana')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Haryana was reported on 4 March 2020.')
    st.write('As of december,2022, the total number of cases in Haryana was 1056602, including 1045845 cures and 10714 deaths. There was 43 active case in the Haryana. The recovery rate in Haryana is 98.9%.')
    st.write('total population: 27388008')
    st.write('total confirmed case: 1056602')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [43, 1045845, 10714]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Haryana')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Haryana')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Himachal_Pradesh():
    st.subheader('COVID-19 pandemic in Himachal Pradesh')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the state of Himachal Pradesh. The first case was recorded in this region on 20 March 2020.')
    st.write('As of december,2022, the total number of cases in Himachal Pradesh was 312644, including 308408 cures and 4213 deaths. There was 23 active case in the Haryana. The recovery rate in Himachal Pradesh is 98.6%.')
    st.write('total population: 7316708')
    st.write('total confirmed case: 312644')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [23, 308408, 4213]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Himachal Pradesh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Himachal Pradesh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Jammu_Kashmir():
    st.subheader('COVID-19 pandemic in Jammu and Kashmir')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the Indian-administered union territory of Jammu and Kashmir. Two suspected cases with high virus load were detected and isolated on 4 March in Government Medical College, Jammu. One of them became the first confirmed positive case on 9 March 2020. Both individuals had a travel history to Iran.')
    st.write('As of december,2022, the total number of cases in Jammu Kashmir Pradesh was 479410, including 474608 cures and 4785 deaths. There was 17 active case in the Haryana. The recovery rate in Jammu and Kashmir is 99%.')
    st.write('total population: 14046258')
    st.write('total confirmed case: 479410')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [17, 474608, 4785]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Jammu and Kashmir')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Jammu and Kashmir')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 

def Jharkhand():
    st.subheader('COVID-19 pandemic in Jharkhand')
    st.write('The first case of the COVID-19 pandemic was confirmed in the Indian state of Jharkhand on 31 March 2020 as a Malaysian women came positive on the test. The state has confirmed a total of 1,11,366 cases, including 995 deaths and 1,08,761 recoveries, as of 12 December.')
    st.write('Chaibasa district headquarters of West Singhbhum launched coronavirus swab collection booth which is Indias first of the kind.[3] Chaibasa also launched remote-controlled robot called co-bot for providing medicines and food and minimize the contact between the staff and the patients. After MGM Medical College in Jamshedpur and RIMS in Ranchi, ICMR gave approval for 2 more testing facilities in the state namely, Patliputra Medical College in Dhanbad and TB Sanitorium Hospital in Itki, Ranchi. So, the total testing facility in the state stands at 4.')
    st.write('total population: 37329128')
    st.write('total confirmed case: 442570')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [3, 437236, 5331]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Jharkhand')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Jharkhand')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig) 


#******

def Karnataka():
    st.subheader('COVID-19 pandemic in Karnataka')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Karnataka was confirmed on 8 March 2020. Two days later, the state became the first in India to invoke the provisions of the Epidemic Diseases Act, 1897, which was set to last for a year, to curb the spread of the disease.As of 25 October 2022, Karnataka has 40,01,655 confirmed cases and 40,097 deaths with 39,52,381 recoveries and 9,135 active cases.')
    st.write('Total population: 66165886')
    st.write('Total confirmed case: 4071893')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [1275, 4030311, 40307]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Karnataka')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Karnataka')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Kerala():
    st.subheader('COVID-19 pandemic in Kerala')
    st.write('The first case of the COVID-19 pandemic in Kerala (which was also the first reported case in all of India) was confirmed in Thrissur on 30 January 2020.As of 5 April 2022, there have been 65,34,352 confirmed cases, test positivity rate is at 2.04% (13.96% cumulative), with 64,62,811 (98.91%) recoveries and 68,197 (1.04%) deaths in the state.')
    st.write('Total population:35330888 ')
    st.write('Total confirmed case:6828245 ')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [1389, 6755304, 71552 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Kerala')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Kerala')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)
    
def Ladakh():
    st.subheader('COVID-19 pandemic in Ladakh')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China.Slowly, the pandemic spread to various states and union territories of India including the union territory of Ladakh.The first case was recorded in this region on 18 March.')
    st.write('Total population:307204 ')
    st.write('Total confirmed case:29412 ')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [3, 29178, 231 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Ladakh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Ladakh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Lakshadweep():
    st.subheader('COVID-19 pandemic in Lakshadweep')
    st.write('The first case of COVID-19 on the Union Territory of Lakshadweep was recorded on 18 January 2021.[1] Lakshadweep Islands, until then, was India''s only COVID-free territory (state/UT), and life was fairly normal for the residents of the UT.As of 13 September 2021, there were 10,297 confirmed cases (5 active) and 51 deaths.')
    st.write('Total population:72210 ')
    st.write('Total confirmed case:11415 ')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 11363, 52 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Lakshadweep')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Lakshadweep')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Madhya_Pradesh():
    st.subheader('COVID-19 pandemic in Madhya_Pradesh')
    st.write('The first four cases of the COVID-19 pandemic in Jabalpur, Madhya Pradesh were confirmed on March 20, 2020.As of August 14, 2021, Madhya Pradesh has confirmed a total of 791,998 cases, and has recorded 10,514 deaths.')
    st.write('As of August 13, 2021, COVID-19 vaccines have been administered to 36,739,380 people in Madhya Pradesh.')
    st.write('Total population:82342793')
    st.write('Total confirmed case:1054918')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [4, 1044138, 10776 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Madhya_Pradesh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Madhya_Pradesh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Maharashtra():
    st.subheader('COVID-19 pandemic in Maharashtra')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Maharashtra was confirmed on 9 March 2020.The largest single day spike (68,631 cases), highest peak in all of India was reported on 18 April 2021.Maharashtra is a hotspot that accounts for nearly 22.35% of the total cases in India as well as about 30.55% of all deaths As of 10 May 2021, the states case fatality rate is nearly 1.49%.Pune is the worst-affected city in Maharashtra, with about 930,809 cases as of 10 May 2021.About half of the cases in the state emerged from the Mumbai Metropolitan Region (MMR).The total number of cases in Maharashtra reported as of May 2022, is 78,87,086 consisting of 1,47,860 deaths and 77,35,751 who have recovered.')
    st.write('As of 6 June 2022, there are 7,429 active COVID-19 cases in the state, the health minister warns that the cases are likely to increase in June and July.')
    st.write('Total population:120837347')
    st.write('Total confirmed case:8136588')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [164, 7988008, 148416 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Maharashtra')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Maharashtra')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Manipur():
    st.subheader('COVID-19 pandemic in Manipur')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China.Slowly, the pandemic spread to various states and union territories including the state of Manipur.The first case was recorded in this region on 24 March 2020.')
    st.write('Total population:3008546')
    st.write('Total confirmed case:139922')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 137773, 2149 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Manipur')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Manipur')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Meghalaya():
    st.subheader('COVID-19 pandemic in Meghalaya')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the state of Meghalaya.The first case was recorded in this region on 14 April')
    st.write('Total population:3276323')
    st.write('Total confirmed case:96783')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [1, 95158, 1624 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Meghalaya')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Meghalaya')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Mizoram():
    st.subheader('COVID-19 pandemic in Mizoram')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China.Slowly, the pandemic spread to various states and union territories including the state of Mizoram.The first case was recorded in this region on 24 March 2020,and the first death was recorded on 28 October 2020.')
    st.write('Total population:1205974')
    st.write('Total confirmed case:238964')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 238238, 726 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Mizoram')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Mizoram')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Nagaland():
    st.subheader('COVID-19 pandemic in Nagaland')
    st.write('The COVID-19 pandemic reached the state of Nagaland on 22 May 2020, with its first case confirmed on 25 May 2020.Officially, Nagaland is the last of the northeastern states after Sikkim to report COVID-19 positive cases.')
    st.write('Total population:2189297')
    st.write('Total confirmed case:35986')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 35204, 782 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Nagaland')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Nagaland')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Odisha():
    st.subheader('COVID-19 pandemic in Odisha')
    st.write('The first case of the COVID-19 pandemic was confirmed in the Indian state of Odisha on 16 March 2020.The state has confirmed 10,00,084 cases, including 9,497 active cases, 9,83,245 recoveries, and 7,289 deaths as of 21 August 2021.')
    st.write('Total population:45429399')
    st.write('Total confirmed case:1336552')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [91, 1327256, 9205 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Odisha')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Odisha')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Puducherry():
    st.subheader('COVID-19 pandemic in Puducherry')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the union territory of Puducherry. The first case was recorded in this region on 17 March.')
    st.write('Total population:1397707')
    st.write('Total confirmed case:175508')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [5, 175508, 1975 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Puducherry')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Puducherry')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Punjab():
    st.subheader('COVID-19 pandemic in Punjab')
    st.write('The COVID-19 pandemic was confirmed to have spread to the Indian state Punjab on 9 March 2020, when an Indian man returning from Italy was tested positive. As of 31 March 2021, the Ministry of Health and Family Welfare has confirmed a total of 2,39,734 cases, including 6,868 deaths and 2,09,034 recoveries in Punjab.')
    st.write('Total population:29611935')
    st.write('Total confirmed case:784205')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [49, 764867, 19289 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Punjab')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Punjab')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)
 
def Rajasthan():
    st.subheader('COVID-19 pandemic in Rajasthan')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Rajasthan was reported on 2 March 2020 in Jaipur.The Rajasthan Health Department has confirmed a total of 29,835 cases, including 563 deaths and 21866 recoveries as of 20 July 2020.All districts in the state have reported confirmed cases of which, Jaipur is the worst-affected.')
    st.write('Total population:78230816')
    st.write('Total confirmed case:1315455')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [88, 1305714, 9653 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Rajasthan')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Rajasthan')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Sikkim():
    st.subheader('COVID-19 pandemic in Sikkim')
    st.write('The first case was recorded in this region on 23 May 2020.')
    st.write('Total population:671720')
    st.write('Total confirmed case:44319')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [1, 43819, 499 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Sikkim')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Sikkim')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Tamil_Nadu():
    st.subheader('COVID-19 pandemic in Tamil_Nadu')
    st.write('The first case of the COVID-19 pandemic in the Indian state of Tamil Nadu was reported on 7 March 2020.The largest single-day spike (36,987 cases) was reported on 13 May 2021 and Tamil Nadu now has the fourth highest number of confirmed cases in India after Maharashtra, Kerala and Karnataka. All 38 districts of the state are affected by the pandemic, with capital district Chennai being the worst affected.')
    st.write('As per the Health Department, 88% of the patients are asymptomatic while 84% of deaths were among those with co-morbidities.In June, the state saw a surge in deaths with 209 deaths (36% of the states recorded deaths) occurring between 11 and 16 June 2020.Another large local cluster in Koyambedu of Chennai was identified in May 2020.')
    st.write('Total population:76481545')
    st.write('Total confirmed case:3594388')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [60, 3556279, 38049 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Tamil_Nadu')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Tamil_Nadu')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Telengana():
    st.subheader('COVID-19 pandemic in Telengana')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the state of Telangana. The first case was recorded in this region on 2 March from a man who had travel history with the UAE.')
    st.write('As per the health bulletin issued by Government of Telangana on June 30, Telangana state claims to have conducted a cumulative number of 88563 tests of which, 16339 tested positive. The overall positivity rate comes to 18.44% (applicable for up to June 30). It needs to be noted that for a long time, the Telangana state did not publicly disclose the daily number of tests it was conducting daily that drew the ire of the High Court.[10] Hence, the cumulative number of tests cannot be corroborated.The daily positivity rate for number of tests conducted by Telangana state on June 30 comes to 27.33%. On 30 June, the Telangana state conducted 3457 tests, out of which the positive cases were 945.')
    st.write('Total population:38472769')
    st.write('Total confirmed case:841324')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [71, 837142, 4111 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Telengana')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Telengana')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Tripura():
    st.subheader('COVID-19 pandemic in Tripura')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020, originating from China. Slowly, the pandemic spread to various states and union territories including the state of Tripura. The first case was recorded in this region on 6 April.As on 23 May, total number of cases in Tripura was 191, including 39 active cases and 152 recoveries')
    st.write('Total population:4057847')
    st.write('Total confirmed case:108034')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [0, 107094, 940 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Tripura')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Tripura')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Uttar_Pradesh():
    st.subheader('COVID-19 pandemic in Uttar_Pradesh')
    st.write('COVID-19 Pandemic spread to Uttar Pradesh in March 2020. While the World Health Organization praised the UP government for its contact tracing efforts, there were several other issues in its management of the pandemic, including under reportage of cases by the government,vaccine shortages and dismal conditions of COVID-19 hospitals.')
    st.write('On 19 June 2020, the Uttar Pradesh government announced that it has fixed the maximum price for COVID-19 tests at ₹2,500. "The price has been fixed in two categories. The first one relates to the corona testing at private or corporate hospitals. In this case, the charges will not be more than ₹2,000 per person. The same applies to a situation where these hospitals tie up with private labs. The second category is that of private pathology or diagnostic labs where the rate cannot exceed ₹2,500," a government spokesperson said.Currently there are 121 government laboratories conducting COVID-19 Testing.Government has also permitted testing in 44 privately operated labs.')
    st.write('Total population:228959599')
    st.write('Total confirmed case:2128103')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [46, 2104424, 23633 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Uttar_Pradesh')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Uttar_Pradesh')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def Uttarakhand():
    st.subheader('COVID-19 pandemic in Uttarakhand')
    st.write('The first case of the COVID-19 pandemic in India was reported on 30 January 2020. Slowly, the pandemic spread to various states and union territories including the state of Uttarakhand. The first case was recorded in this region on 15 March.As on 24 May, the total number of confirmed cases in Uttarakhand was 244, including 188 active cases, 55 recoveries, and one death. As of 5 June, this number has risen to 1,153 cases, of which 842 are active, and there have been 297 recoveries and 10 deaths.Newly sworn Uttarakhand Chief Minister Tirath Singh Rawat has been criticised for placing faith before the pandemic and accused of double standards on restrictions of gatherings of different religions.')
    st.write('On 19 June 2020, the Uttar Pradesh government announced that it has fixed the maximum price for COVID-19 tests at ₹2,500. "The price has been fixed in two categories. The first one relates to the corona testing at private or corporate hospitals. In this case, the charges will not be more than ₹2,000 per person. The same applies to a situation where these hospitals tie up with private labs. The second category is that of private pathology or diagnostic labs where the rate cannot exceed ₹2,500," a government spokesperson said.Currently there are 121 government laboratories conducting COVID-19 Testing.Government has also permitted testing in 44 privately operated labs.')
    st.write('Total population:11090425')
    st.write('Total confirmed case:449379')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [28, 441600, 7751 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in Uttarakhand')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in Uttarakhand')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)

def West_Bengal():
    st.subheader('COVID-19 pandemic in West_Bengal')
    st.write('The COVID-19 pandemic was first confirmed in the Indian state of West Bengal on 17 March 2020 in Kolkata.The Health and Family Welfare department of Government of West Bengal has confirmed a total of 13,43,442 COVID-19 positive cases, including 1,09,806 active cases, 15,120 deaths and 12,18,516 recoveries, as of 28 May 2021.Districts of West Bengal were classified as red, orange, or green zones, with red zones having the strictest regulations and green zones having the least strict regulations.')
    st.write('Total population:97694960')
    st.write('Total confirmed case:2118606')

    cases_data = {
    'Category': ['Active', 'Discharged', 'Deaths'],
    'Count': [58, 2097016, 21532 ]
    }

    # Create a DataFrame with the data
    cases_df = pd.DataFrame(cases_data)

    # Calculate percentages
    total_cases = cases_df['Count'].sum()
    cases_df['Percentage'] = (cases_df['Count'] / total_cases) * 100

    # Plotting
    st.subheader('COVID-19 Cases Summary in West_Bengal')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(cases_df['Category'], cases_df['Count'], color=['blue', 'green', 'red'])
    ax.set_title('Total Confirmed Cases in West_Bengal')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    for i, count in enumerate(cases_df['Count']):
        ax.text(i, count + 10000, f"{count} ({cases_df['Percentage'][i]:.2f}%)", ha='center')
    st.pyplot(fig)