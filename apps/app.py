import streamlit as st


def home_page():
    st.title("Welcome to Nutreto.AI! 👋")
    st.success("Select a tool from the sidebar to get started!")

    st.markdown(
        """
            Nutreto.AI is an application suite designed to help you with your nutritional needs.
            
            **👈 Select a tool from the sidebar** to get started.
            
            ### Our Tools:
            - **NutriNet:** Analyze nutritional information.
            - **FoodCraft:** Discover new recipes and meal plans.
        """
    )
    
# Set the page config at the very beginning
st.set_page_config(page_title="Nutreto.AI", page_icon="👩‍🍳")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ("🏠 Home", "🥗 NutriNet", "🍔 FoodCraft") )

# --- Page Display Logic ---
if page == "🏠 Home":
    # Call the function to display the home page content
    home_page()
elif page == "NutriNet":
    # Call the main function from the imported calMate module
    from apps import NutriNet
    NutriNet.main()
elif page == "FoodCraft":
    # Call the main function from the imported dishify module
    from apps import FoodCraft
    FoodCraft.main()