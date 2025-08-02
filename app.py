import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# --- Setup Streamlit UI ---
st.set_page_config(page_title="Conscious Cart AI", layout="centered")
st.title("Conscious Cart AI Agent 🛒")

# --- Input: Product Name or URL ---
product_input = st.text_input("Enter a Product NAME or URL:")

# --- Store API key persistently in session_state ---
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key = st.text_input("Enter your Gemini API Key:", type="password", value=st.session_state.api_key)
if api_key:
    st.session_state.api_key = api_key

# --- Initialize LLM (only once using cache_resource) ---
@st.cache_resource(show_spinner=False)
def load_llm(api_key):
    return ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash-latest",
        temperature=0,
        google_api_key=api_key,
    )

llm = None
if st.session_state.api_key:
    try:
        llm = load_llm(st.session_state.api_key)
    except Exception as e:
        st.error(f"Error initializing Gemini model: {e}")
        st.stop()
else:
    st.info("Please enter your Gemini API key to continue.")

# --- Function: Scrape Product Details ---
def scrape_product_details(url):
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "Unknown Product"
        return title
    except Exception as e:
        return f"Error scraping: {e}"

# --- Function: Generate Product Description ---
def generate_details_from_name(name):
    try:
        response = llm.invoke([HumanMessage(content=f"Describe the product: {name}")])
        return response.content
    except Exception as e:
        return f"Error generating details: {e}"

# --- Function: Analyze Environmental Impact ---
def analyze_environmental_impact(details):
    try:
        response = llm.invoke([HumanMessage(content=f"Analyze the environmental impact of this product: {details}")])
        return response.content
    except Exception as e:
        return f"Error analyzing impact: {e}"

# --- Function: Generate Recommendation ---
def generate_recommendation(impact):
    try:
        response = llm.invoke([HumanMessage(content=f"Based on this environmental impact, what would you recommend?: {impact}")])
        return response.content
    except Exception as e:
        return f"Error generating recommendation: {e}"

# --- Analyze Button ---
if st.button("Analyze"):
    if not llm:
        st.warning("LLM is not initialized. Please enter your Gemini API key.")
    elif not product_input:
        st.warning("Please enter a product URL or name.")
    else:
        if product_input.lower().startswith("http"):
            details = scrape_product_details(product_input)
        else:
            details = generate_details_from_name(product_input)

        st.markdown("### 📦 Product Description")
        st.markdown(details)

        impact = analyze_environmental_impact(details)
        st.markdown("### 🌍 Environmental Impact")
        st.markdown(impact)

        recommendation = generate_recommendation(impact)
        st.markdown("### 📝 Final Recommendation")
        st.markdown(recommendation)

