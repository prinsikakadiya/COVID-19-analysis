import streamlit as st

from streamlit_option_menu import option_menu 
import vaccine, overview, patient, patient2

def main():
        
        with st.sidebar:
            choice= option_menu(
                 menu_title = None,
                 options = ["Patient(india)","Patient(statewise)","Vaccine","Overview"]
            )
      
        if choice =='Patient(india)':
            patient.app()
            
        elif choice =='Vaccine':
            vaccine.app()

        elif choice =='Overview':
            overview.app()  

        elif choice =='Patient(statewise)':
            patient2.app()  
    

if __name__ == '__main__':
      main()          

 




