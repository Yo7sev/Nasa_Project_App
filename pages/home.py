import streamlit as st
from PIL import Image

import streamlit as st
from PIL import Image

# 🌍 Translations Dictionary
translations = {
    "en": {
        "title": "🪐 OrbitAI Education",
        "caption": "Developed for the NASA Space Apps Challenge 🌍",
        "quote": "“Exploring the Wonders of the Solar System and Beyond”",
        "what_is": "🌌 What is OrbitAI Education?",
        "what_is_text": """
        **OrbitAI Education** is an interactive learning platform that combines **astronomy, data visualization, and artificial intelligence**
        to make space exploration accessible and exciting for everyone.  
        It was proudly developed as part of the **NASA Space Apps Challenge**, where creativity meets real science.
        """,
        "purpose": "🧠 Our Purpose",
        "purpose_text": """
        Our goal is to make **space education engaging, interactive, and data-driven**.  
        OrbitAI helps you discover:
        - 🌞 The fascinating structure of our **Solar System**
        - 🪐 The diversity of **planets and moons**
        - 🌠 The discovery of **exoplanets** and how scientists detect them
        - 🤖 The role of **AI and data science** in space research
        """,
        "why": "🚀 Why We Built This",
        "why_text": """
        Space exploration connects humanity — it inspires innovation, curiosity, and a sense of wonder.  
        **OrbitAI Education** bridges **science and technology**, empowering learners to:
        - Visualize complex space data through interactive tools  
        - Understand planetary systems in a fun and intuitive way  
        - Explore real NASA datasets and simulations
        """,
        "features": "🌟 What You’ll Find Inside",
        "lessons": "📘 Lessons",
        "lessons_text": "Learn about each planet, moon, and exoplanet through structured lessons and visuals.",
        "interactive": "🧩 Interactive Learning",
        "interactive_text": "Explore quizzes, simulations, and dynamic visualizations that make astronomy hands-on.",
        "ai": "🤖 AI Insights",
        "ai_text": "Discover how artificial intelligence helps astronomers detect exoplanets and study cosmic patterns.",
        "tip": "✨ Tip: Use the **sidebar** to navigate through lessons and activities.",
        "footer": "👨‍🚀 <b>Developed with passion for the NASA Space Apps Challenge — because space belongs to everyone.</b>",
    },
    "ar": {
        "title": "🪐 تعليم OrbitAI",
        "caption": "تم تطويره لمسابقة NASA Space Apps 🌍",
        "quote": "“استكشاف عجائب النظام الشمسي وما بعده”",
        "what_is": "🌌 ما هو OrbitAI Education؟",
        "what_is_text": """
        **OrbitAI Education** هي منصة تعليمية تفاعلية تجمع بين **علم الفلك، وتصوير البيانات، والذكاء الاصطناعي**
        لجعل استكشاف الفضاء ممتعًا وسهل الوصول للجميع.  
        تم تطويرها بفخر ضمن **تحدي NASA Space Apps** حيث يلتقي الإبداع بالعلم الحقيقي.
        """,
        "purpose": "🧠 هدفنا",
        "purpose_text": """
        هدفنا هو جعل **تعليم الفضاء تفاعليًا ومبنيًا على البيانات**.  
        يساعدك OrbitAI على اكتشاف:
        - 🌞 الهيكل المذهل للنظام الشمسي  
        - 🪐 تنوع الكواكب والأقمار  
        - 🌠 اكتشاف الكواكب الخارجية وكيفية رصدها  
        - 🤖 دور الذكاء الاصطناعي وعلوم البيانات في أبحاث الفضاء
        """,
        "why": "🚀 لماذا أنشأنا هذا المشروع",
        "why_text": """
        استكشاف الفضاء يوحّد البشرية — فهو مصدر إلهام للابتكار والفضول والإعجاب.  
        **OrbitAI Education** يربط **العلم والتكنولوجيا**، لتمكين المتعلمين من:
        - تصور بيانات الفضاء المعقدة عبر أدوات تفاعلية  
        - فهم الأنظمة الكوكبية بطريقة ممتعة وبديهية  
        - استكشاف مجموعات بيانات ومحاكاة حقيقية من NASA
        """,
        "features": "🌟 ما الذي ستجده هنا",
        "lessons": "📘 الدروس",
        "lessons_text": "تعلّم عن كل كوكب وقمر وكوكب خارجي من خلال دروس وصور منظمة.",
        "interactive": "🧩 تعلم تفاعلي",
        "interactive_text": "استكشف الاختبارات والمحاكاة والعروض التفاعلية التي تجعل علم الفلك ممتعًا.",
        "ai": "🤖 رؤى الذكاء الاصطناعي",
        "ai_text": "اكتشف كيف يساعد الذكاء الاصطناعي العلماء في اكتشاف الكواكب الخارجية ودراسة الأنماط الكونية.",
        "tip": "✨ تلميح: استخدم **الشريط الجانبي** للتنقل بين الدروس والأنشطة.",
        "footer": "👨‍🚀 <b>تم تطويره بشغف لمسابقة NASA Space Apps — لأن الفضاء ملك للجميع.</b>",
    }
}

# 🌐 Main App
def app():
    st.set_page_config(page_title="OrbitAI Education", layout="wide")

    # Sidebar language selector
    st.sidebar.markdown("### 🌍 Language / اللغة")
    lang = st.sidebar.selectbox("Select Language", ["English", "العربية"])
    lang_code = "ar" if lang == "العربية" else "en"

    t = translations[lang_code]

    # Right-to-left fix for Arabic
    if lang_code == "ar":
        st.markdown("""
            <style>
                body, div, p, h1, h2, h3, h4, h5, h6 {
                    direction: rtl;
                    text-align: right;
                }
            </style>
        """, unsafe_allow_html=True)

    # Main Content
    st.title(t["title"])
    st.caption(t["caption"])
    st.markdown("---")

    st.image("assets/logos/solar_system_Cover_rev_40-3_1600.jpg", use_container_width=True)

    st.markdown(f"""
    <div style="text-align: center; font-size: 22px; font-weight: 600;">
        <em>{t["quote"]}</em>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.header(t["what_is"])
    st.write(t["what_is_text"])

    st.header(t["purpose"])
    st.write(t["purpose_text"])

    st.header(t["why"])
    st.write(t["why_text"])

    st.markdown("---")
    st.subheader(t["features"])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/logos/machine-learning.png", width=80)
        st.markdown(f"### {t['lessons']}")
        st.write(t["lessons_text"])

    with col2:
        st.image("assets/logos/saturn.png", width=80)
        st.markdown(f"### {t['interactive']}")
        st.write(t["interactive_text"])

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)
        st.markdown(f"### {t['ai']}")
        st.write(t["ai_text"])

    st.markdown("---")
    st.success(t["tip"])

    st.markdown(f"""
    <div style="text-align: center; margin-top: 30px; font-size: 18px;">
        {t["footer"]}
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
