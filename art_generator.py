import streamlit as st
from api import generate_art

def display_art_generator():
    """Display the eco-art generation interface."""
    st.header("Generate Eco-Art Based on Your Prompt or File")
    input_option = st.selectbox("Select input type:", ("Type a prompt", "Upload a file"))

    prompt = None
    if input_option == "Type a prompt":
        prompt = st.text_input("Describe the eco-art you want to generate:")
    elif input_option == "Upload a file":
        uploaded_file = st.file_uploader("Upload a text file with your eco-art description:")
        if uploaded_file is not None:
            try:
                prompt = uploaded_file.read().decode("utf-8")
                st.write(f"Summary of uploaded content: {prompt[:150]}...")
            except Exception as e:
                st.error(f"Error reading file: {e}")
                prompt = None

    if prompt:
        style_option = st.selectbox("Choose an art style:", ("None", "Realistic", "Abstract", "Grayscale"))
        emotion_option = st.selectbox("Choose an emotional tone:", ("None", "Urgent", "Hopeful", "Tranquil"))
        category = st.selectbox("Choose an environmental category:", ("None", "Deforestation", "Ocean Pollution", "Air Pollution"))

        keywords = st.multiselect(
            "Add keywords to enrich your prompt:",
            options=["climate crisis", "biodiversity loss", "global warming", "reforestation", "wildlife conservation"],
            default=["climate crisis"]
        )

        keyword_text = " ".join(keywords)
        complete_prompt = f"{emotion_option} {style_option} {category} art: {keyword_text} {prompt}"
        st.write(f"Generated Prompt: {complete_prompt}")

        if st.button("Generate Artwork"):
            st.write(f"Generating artwork for theme: {category}")
            image_url = generate_art(category)
            if image_url:
                st.image(image_url, caption=f"{category} Art", use_column_width=True)
                st.markdown(f"[Share on Twitter](https://twitter.com/intent/tweet?url={image_url}&text=Check out this eco-art on {category})")
