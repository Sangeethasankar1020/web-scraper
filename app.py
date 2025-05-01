import streamlit as st
import requests

st.set_page_config(
    page_title="Image Scraper 🔍",
    page_icon="🖼️",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto"
)

st.title("Unsplash Image Search & Download")

ACCESS_KEY = st.secrets["unsplash"]["access_key"]

# with st.form("Search"):
#     keyword = st.text_input("Enter keyword")
#     search = st.form_submit_button("Search")

#     if search and keyword:
#         url = "https://api.unsplash.com/search/photos"
#         params = {
#             "query": keyword,
#             "client_id": ACCESS_KEY,
#             "per_page": 6,
#         }

#         response = requests.get(url, params=params)

#         if response.status_code == 200:
#             data = response.json()
#             st.subheader(f"Results for: {keyword}")
#             for i, result in enumerate(data["results"]):
#                 image_url = result["urls"]["regular"]
#                 alt = result["alt_description"] or "Image"

#                 # Display image
#                 st.image(image_url, caption=alt)

#                 # Download logic
#                 img_data = requests.get(image_url).content
#                 st.download_button(
#                     label="Download Image",
#                     data=img_data,
#                     file_name=f"{keyword}_{i+1}.jpg",
#                     mime="image/jpeg"
#                 )
#         else:
#             st.error("Failed to fetch images. Check your API key or usage limit.")
# --- Form for user input ---



with st.form("Search"):
    keyword = st.text_input("Enter keyword")
    search = st.form_submit_button("Search")

# --- Fetch and display results outside the form ---
if search and keyword:
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": keyword,
        "client_id": ACCESS_KEY,
        "per_page": 6,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Results for: {keyword}")

        for i, result in enumerate(data["results"]):
            image_url = result["urls"]["regular"]
            alt = result["alt_description"] or "Image"

            # Display image
            st.image(image_url, caption=alt)

            # Download logic (now outside form)
            img_data = requests.get(image_url).content
            st.download_button(
                label="Download Image",
                data=img_data,
                file_name=f"{keyword}_{i+1}.jpg",
                mime="image/jpeg"
            )
    else:
        st.error("Failed to fetch images. Check your API key or usage limit.")