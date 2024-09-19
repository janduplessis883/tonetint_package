import streamlit as st
from tonetint.sentiment_visualizer import ToneTint
import nltk
from io import BytesIO
import pdfkit

# Download the required NLTK resource
nltk.data.path.append('images/')  # Make sure the path exists and is writable
nltk.download('punkt_tab', download_dir='images/')
nltk.download('punkt', download_dir='images/')

st.title("ToneTint Sentiment Visualizer")

# Select model from dropdown
selected_model = st.selectbox(
    "Pick a Text Classification Model",
    options=[
        "finiteautomata/bertweet-base-sentiment-analysis",
        "cardiffnlp/twitter-roberta-base-sentiment-latest"
    ]
)

# Text area for user input with default text
initial_text = """On a bright Sunday morning in London, the city hums with a soft, lazy energy.
The streets, usually packed with hurried commuters, are now filled with leisurely strollers
and families enjoying a slow brunch in trendy cafes. The air is crisp, and the scent of freshly
baked croissants mingles with the rich aroma of brewing coffee. Down by the Thames, joggers
pass by tourists taking in the iconic skyline, their contrasting paces a reflection of the
different ways people unwind. Yet, even amidst the calm, there’s a pulse of vibrancy —
street performers at Covent Garden strumming upbeat tunes, and the chatter of markets,
like Brick Lane, buzzing with life. As the sun starts to set, the quiet anticipation of a new
week begins to settle in, tinged with a hint of nostalgia for the fleeting relaxation that Sundays bring."""
text_area = st.text_area("Paste Text here", value=initial_text)

# Slider for chunk size
chunk_size = st.slider("Select chunk size", min_value=6, max_value=18, value=8)

# Color pickers for sentiment colors
c1, c2, c3 = st.columns(3, gap="large")
with c1:
    red_picker = st.color_picker("NEG Color", value="#e8a56c")
with c2:
    yellow_picker = st.color_picker("NEUT Color", value="#f0e8d2")
with c3:
    green_picker = st.color_picker("POS Color", value="#aec867")

# Button to trigger text analysis
button = st.button("Analyze Text")

def init_model():
    # Initialize ToneTint with selected model and colors
    colors = {"NEG": red_picker, "NEU": yellow_picker, "POS": green_picker}
    visualizer = ToneTint(model_name=selected_model, chunk_size=chunk_size, colors=colors)
    return visualizer

# Generate PDF from HTML
def create_pdf(html_content):
    pdf = pdfkit.from_string(html_content, False)
    return pdf

# When button is clicked, analyze the text and display the result
if button:
    visualizer = init_model()  # Initialize the ToneTint model
    html_content = visualizer.visualize(text_area)  # Generate HTML from analyzed text
    st.markdown(html_content, unsafe_allow_html=True)  # Display the HTML content

    # Convert HTML content to bytes
    html_bytes = html_content.encode('utf-8')

    # Download HTML
    st.download_button(
        label="Download as HTML",
        data=html_bytes,
        file_name="analyzed_text.html",
        mime="text/html"
    )

    # Create PDF and provide as download
    pdf_bytes = create_pdf(html_content)
    st.download_button(
        label="Download as PDF",
        data=pdf_bytes,
        file_name="analyzed_text.pdf",
        mime="application/octet-stream"
    )
