# Eco-Art Generator 🌍🎨

The **Eco-Art Generator** allows users to create environmentally inspired artwork based on their unique prompts or uploaded files. It also provides tools to explore environmental data and visualize trends related to ecological impacts. This project aims to inspire awareness through art, utilizing AI and data visualization to highlight pressing environmental issues.

## Features

- **Generate Eco-Art**: Users can create eco-art by inputting custom prompts or uploading text files. Options are available to customize the style, emotional tone, and specific environmental themes of the artwork.
- **Explore Environmental Datasets**: Access and browse various datasets from Global Forest Watch (GFW) to gain insights into environmental impacts, with detailed metadata for each dataset.
- **Data Visualization**: View visual representations of trends in deforestation and CO₂ emissions over the years, helping to illustrate the environmental situation graphically.
- **Feedback System**: Users can rate their experience with the eco-art generation process, allowing continuous improvements based on user feedback.

## Setup

### Prerequisites

To run the Eco-Art Generator, ensure that you have the following installed:

- **Python**: Version 3.7 or higher is required.
- **Streamlit**: A web application framework for Python.
- **OpenAI API key**: Sign up at [OpenAI](https://beta.openai.com/signup/) to get your API key.
- **GFW API key**: Register at [Global Forest Watch](https://data.globalforestwatch.org/) to obtain access to their datasets.

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd eco-art-generator
    ```
   Replace `<repository-url>` with the actual URL of your GitHub repository.

2. **Install Required Packages**:
   Create a virtual environment (recommended) and install the required dependencies:
    ```bash
    python -m venv venv              # Create a virtual environment
    source venv/bin/activate         # Activate the virtual environment (Linux/Mac)
    # OR
    venv\Scripts\activate            # Activate the virtual environment (Windows)

    pip install -r requirements.txt   # Install the required packages
    ```

3. **Add Your API Keys**:
   Open the `main.py` file and replace the placeholder API keys with your actual keys:
   ```python
   openai.api_key = "your-openai-api-key"  # Replace with your actual OpenAI API key
   gfw_api_key = "your-gfw-api-key"        # Replace with your actual GFW API key


### Run the Application

To start the Streamlit app:
```bash
streamlit run main.py
