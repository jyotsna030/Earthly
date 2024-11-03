import streamlit as st
from config import openai_api_key, gfw_api_key
from art_generator import display_art_generator
from dataset_explorer import display_datasets
from visualizations import display_visualizations

def main():
    st.title("Eco-Art Generator 🌍🎨")
    st.write("Create environmentally inspired artwork based on your prompts or uploaded files, and explore environmental data.")

    display_art_generator()
    display_datasets()
    display_visualizations()

if __name__ == "__main__":
    main()
