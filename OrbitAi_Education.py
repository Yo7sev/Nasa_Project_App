import streamlit as st
from streamlit_option_menu import option_menu

# Import your pages
from pages import home, edu2, edu3, edu4, edu5

# Page configuration
st.set_page_config(page_title="OrbitAI Education", layout="wide")

# Hide Streamlit’s default sidebar navigation
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


# MultiApp class
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            # Custom sidebar header (centered with emoji)
            st.markdown("<h2 style='text-align: center;'>🚀 OrbitAI Education</h2>", unsafe_allow_html=True)

            # Custom option menu (no default title)
            selected = option_menu(
                menu_title=None,  # no title, we already have our custom one
                options=[app["title"] for app in self.apps],
                icons=["house", "globe", "globe2", "robot", "star"],  # one icon per page
                default_index=0
            )

        # Run the selected app
        for app in self.apps:
            if app["title"] == selected:
                app["function"]()
                break


# Create the app object
app = MultiApp()

# Add your pages (include Home FIRST)
app.add_app("🏠 Home", home.app)
app.add_app("The Solar System", edu2.app)
app.add_app("Exploring Exoplanets", edu3.app)
app.add_app("AI & Machine Learning in Exoplanet", edu4.app)
app.add_app("Stars in an Exoplanet World", edu5.app)

# Run the app
app.run()
