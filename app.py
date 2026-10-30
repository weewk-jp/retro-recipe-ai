import streamlit as st
from openai import OpenAI

# 1. Настройка страницы (широкий формат)
st.set_page_config(
    page_title="moonlight's recipes", 
    page_icon="🍀", 
    layout="wide"
)

st.markdown("""
<style>
    
    .header-title {
        text-align: center;
        font-family: 'YujiMai', serif;
        font-size: 42px;
        color: #e882a4;
        margin-bottom: 5px;
    }
    .header-sub {
        text-align: center;
        font-family: 'YujiMai', serif;
        font-size: 18px;
        color: #a87293;
        margin-bottom: 20px;
    }
    /* Карточки виджетов в сайдбарах */
    .widget-box {
        background-color: #ffffff;
        border: 2px solid #f9c5d1;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .stApp {
        background-image: url("Baby Pink Landscape.png");
        background-size: cover;
    }    
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='header-title'>moon lover</div>", unsafe_allow_html=True)
st.markdown("<div class='header-sub'>Cooking Space</div>", unsafe_allow_html=True)

st.divider()


col_left, col_center, col_right = st.columns([1, 2.2, 1])


with col_left:
    st.markdown("#### Moodboard & Key")
    
    # API Ключ помещаем в эстетичный левый блок
    nebius_key = st.text_input("🔑 Nebius API Key:", type="password")
    st.caption("Get your key at tokenfactory.nebius.com")
    
    st.divider()
    
    # Эстетичная картинка/гифка
    st.image("just.jpg", use_container_width=True)
    


    
    st.markdown("### 🎵 Spotify Playlist")
    spotify_embed_code = """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
    st.components.v1.html(spotify_embed_code, height=160)
   
    st.markdown("---")
    st.markdown("### day left")
    st.metric(label="Total Pageviews", value="124")


with col_center:
    st.markdown("## weewkkee page")
    
    tab_recipe, tab_chat = st.tabs(["📖 Recipe Parser AI", "💬 General AI Assistant"])
    
    # Вкладка 1: Парсер рецептов
    with tab_recipe:
        st.subheader("🍳 Smart Recipe Parser")
        recipe_input = st.text_area(
            "Paste Instagram/Tiktok recipe link or raw ingredients:", 
            placeholder="https://instagram.com/p/... or 'Matcha powder, rice flour...'"
        )
        
        cooking_goal = st.selectbox(
            "Select AI Action:",
            [
                "Extract structured recipe & steps",
                "Suggest ingredient substitutes",
                "Calculate macros & calories",
                "Japanese culinary style presentation"
            ]
        )
        
        if st.button("✨ Parse Recipe with AI", type="primary", use_container_width=True):
            if not nebius_key:
                st.error("Please enter your API Key in the left sidebar!")
            elif not recipe_input:
                st.warning("Please paste a link or ingredients!")
            else:
                try:
                    client = OpenAI(
                        base_url="https://api.studio.nebius.ai/v1/",
                        api_key=nebius_key
                    )
                    prompt = f"Parse this recipe: {recipe_input}. Goal: {cooking_goal}. Provide clear steps, ingredients, and pro-tips."
                    
                    with st.spinner("AI Chef is cooking..."):
                        response = client.chat.completions.create(
                            model="meta-llama/Llama-3.3-70B-Instruct",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.6
                        )
                    st.success("Parsed Successfully!")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"API Error: {e}")

    
    with tab_chat:
        st.subheader("💬 Ask AI Anything")
        user_prompt = st.text_area("Your Question:", placeholder="Ask about study plans, code, or daily routine...")
        
        if st.button("Generate Response", use_container_width=True):
            if not nebius_key:
                st.error("Please enter your API Key!")
            elif not user_prompt:
                st.warning("Please enter a prompt!")
            else:
                try:
                    client = OpenAI(
                        base_url="https://api.studio.nebius.ai/v1/",
                        api_key=nebius_key
                    )
                    with st.spinner("Thinking..."):
                        response = client.chat.completions.create(
                            model="meta-llama/Llama-3.3-70B-Instruct",
                            messages=[{"role": "user", "content": user_prompt}],
                            temperature=0.6
                        )
                    st.success("Done!")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"API Error: {e}")

# ==========================================
# ПРАВАЯ КОЛОНКА: Профиль, Факты, Эстетика
# ==========================================
with col_right:
    st.markdown("#### daily reminder")
    st.image("title.jpg", use_container_width=True)
    st.write("there's so much more to live than waiting to be chosen.")
    st.write("create more than you consume. people think about how they can receive love, but we should be thinking about how we can give love. - juhoon cortis")
    
    st.divider()

    st.markdown("#### 🗓️ Month Overview")
    calendar_html = """
    <div style="background-color: #ffffff; border: 2px solid #f9c5d1; border-radius: 12px; padding: 10px; text-align: center; font-family: sans-serif;">
        <h4 style="color: #e882a4; margin: 0 0 10px 0;">October 2026</h4>
        <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
            <tr style="color: #a87293;"><th>Mo</th><th>Tu</th><th>We</th><th>Th</th><th>Fr</th><th>Sa</th><th>Su</th></tr>
            <tr><td></td><td></td><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr>
            <tr><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr>
            <tr><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td></tr>
            <tr><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td></tr>
            <tr><td>26</td><td>27</td><td>28</td><td>29</td><td>30</td><td>31</td><td></td></tr>
        </table>
    </div>
   """
    st.components.v1.html(calendar_html, height=210)


    st.divider()
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjEx.../giphy.gif", caption="Good Luck! ✨", use_container_width=True)