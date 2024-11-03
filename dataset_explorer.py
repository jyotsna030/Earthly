import streamlit as st
from api import fetch_datasets

def display_datasets():
    """Display the dataset exploration interface."""
    st.header("Explore Environmental Datasets")
    page_number = st.number_input("Page Number", min_value=1, value=1, step=1)
    page_size = st.slider("Page Size", min_value=5, max_value=25, value=5)

    datasets = fetch_datasets(page_number, page_size)
    if datasets:
        st.write(f"Displaying page {page_number} with {page_size} datasets per page.")
        for idx, dataset in enumerate(datasets, start=1):
            with st.expander(f"Dataset {idx}: {dataset.get('metadata', {}).get('title', 'Untitled')}"):
                metadata = dataset.get('metadata', {})
                st.write("Overview:", metadata.get("overview", "No overview available"))
                st.write("Source:", metadata.get("source", "No source provided"))
                st.write("Geographic Coverage:", metadata.get("geographic_coverage", "Global"))
                st.write("License:", metadata.get("license", "No license information"))

                tags = metadata.get("tags")
                st.write("Tags:", ", ".join(tags) if isinstance(tags, list) and tags else "No tags available")

                st.write("Citation:", metadata.get("citation", "No citation provided"))
                if dataset.get("is_downloadable"):
                    st.success("This dataset is available for download.")
                else:
                    st.warning("This dataset is not available for download.")
                
                versions = dataset.get("versions", [])
                st.write("Available Versions:", ", ".join(versions) if versions else "No versions available.")
    else:
        st.write("No datasets found or unable to retrieve data.")
