import streamlit as st

def education_page():
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h2 style='margin: 0; color: #212529;'>Education</h2>
        </div>
        """
    )
    
    st.markdown(""" 
    <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
        <h3 style='margin: 0; color: #212529;'>Master Degree of Science in Marketing</h3>
    </div>
    **The Chinese University of Hong Kong (CUHK)**  
    **HongKong, China**| *Aug 2024 - July 2025*
    - GPA: 3.6/4.0
    - Course: Marketing Research, Buyer Behavior, Digital Marketing, Customer Analytics, Social Media Analytics, Marketing Analytics
    
    <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
        <h3 style='margin: 0; color: #212529;'>Bachelor of Economics</h3>
    </div>
    **East China Normal University (ECNU)**  
    **Shanghai, China** | *Aug 2020 - July 2024*
    - GPA: 3.5/4.0
    - Course: Mathematical Analysis, Mathematical Statistic, Probability Theory, Linear Algebra, Econometrics, Data Base and Statistical Software, Game Theory
    
    <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
        <h3 style='margin: 0; color: #212529;'>Berkeley International Study Program</h3>
    </div>
    **University of California, Berkeley (UCB)**  
    **California, United States** | *Jan 2023- May 2023*
    - GPA: 4.0/4.0
    - Course: Asset pricing and Portfolio Choice, Financial Accounting, Urban Economics
    """)
    
    st.markdown("---")
    
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h2 style='margin: 0; color: #212529;'>Certifications</h2>
        </div>
        """
    )
    
    cert1, cert2 = st.columns(2)
    
    with cert1:
        st.markdown("""
            <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
                <h3 style='margin: 0; color: #212529;'>Xiaohongshu Marketing Competence Certification：</h3>
            </div>
            #### Primary  
            **Xiaohongshu** | *November 2023*
            """
        )

    with cert2:
        st.markdown("""
            <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
                <h3 style='margin: 0; color: #212529;'>Putonghua Proficiency Test：</h3>
            </div>
            #### Grade 2, Class A  
            **Putonghua Proficiency Test** | *July 2024*
            
            """
        )
    
    st.markdown("---")
    
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h2 style='margin: 0; color: #212529;'>Academic Projects</h2>
        </div>
        """
    )
    
    st.markdown("""
    <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
        <h4 style='margin: 0; color: #212529;'>Successful Overseas Marketing Case of a Domestic Game —— "Black Myth: Wukong"</h4>
    </div>
    Use Python and API crawlers to obtain the data performance of "Black Myth: Wukong" on YouTube, TikTok, and Steam. Then, conduct data analysis and visualization such as traffic analysis, text sentiment analysis, and word cloud charts. Compare the overseas performance of domestic games of the same type. Combine with the 4P theory to summarize the reasons for the successful overseas launch of "Black Myth: Wukong".
    
    <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
        <h4 style='margin: 0; color: #212529;'>Analysis and Suggestions on the Current Situation of Commercial Advertising Revenue on Bilibili</h4>
    </div>
    Conduct a case analysis on the imperfect commercialization system of Bilibili's advertising. First, I collected and sorted out the annual reports of Bilibili over the years, and conducted data analysis using Excel and Stata. By comparing with competing products Based on the successful commercialization cases of the company, combined with the 4P theory and STP strategy, this paper explores Bilibili's market positioning, user profile and potential business opportunities. Personalized commercialization for Bilibili has been formulated
    """)
    
    st.markdown("---") 