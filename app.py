import streamlit as st

current_page=st.navigation([st.Page("Home.py"),st.Page("Preprocess.py", title="Image Preprocessing"),
                            st.Page("Detect.py",title="Image Detection")])

current_page.run()