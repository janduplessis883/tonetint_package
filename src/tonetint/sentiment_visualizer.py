import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from transformers import pipeline
from IPython.display import HTML, display
import streamlit as st


class ToneTint:
    def __init__(
        self,
        model_name="finiteautomata/bertweet-base-sentiment-analysis",
        chunk_size=8,
        colors=None,
    ):
        """
        Initialize the ToneTint visualizer with a specified model, chunk size, and colors.
        """
        self.chunk_size = chunk_size
        self.model = pipeline("sentiment-analysis", model=model_name)
        nltk.download("punkt", quiet=True)

        # Default colors if not provided
        default_colors = {
            "POS": "#aec867",  # Green
            "NEG": "#e8a56c",  # Red
            "NEU": "#f0e8d2",  # Yellow
        }
        self.colors = colors if colors else default_colors

    def split_text(self, text):
        """
        Split text into sentences and further into chunks of specified size.
        """
        sentences = sent_tokenize(text)
        chunks = []
        for sentence in sentences:
            words = word_tokenize(sentence)
            for i in range(0, len(words), self.chunk_size):
                chunk = " ".join(words[i : i + self.chunk_size])
                chunks.append(chunk)
        return chunks

    def analyze_chunks(self, chunks):
        """
        Perform sentiment analysis on each text chunk.
        """
        return self.model(chunks)

    def generate_html(self, chunks, sentiments):
        """
        Generate HTML with background colors based on sentiment and display tooltips.
        """
        html_output = ""
        for chunk, sentiment in zip(chunks, sentiments):
            label = sentiment["label"]
            score = sentiment["score"]
            color = self.get_color(label, score)
            tooltip = f"Label: {label}, Score: {score:.2f}"
            html_output += f"<span style='background-color:{color};' title='{tooltip}'>{chunk} </span>"
        return html_output

    def hex_to_rgba(self, hex_color, alpha):
        """
        Convert hex color code to RGBA string with given alpha (opacity).
        """
        hex_color = hex_color.lstrip("#")
        r, g, b = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
        return f"rgba({r}, {g}, {b}, {alpha})"

    def get_color(self, label, score):
        """
        Determine background color based on sentiment label and score.
        """
        label_upper = label.upper()
        if label_upper in ["POSITIVE", "POS"]:
            color_hex = self.colors.get("POS", "#aec867")  # Default to green
        elif label_upper in ["NEGATIVE", "NEG"]:
            color_hex = self.colors.get("NEG", "#e8a56c")  # Default to red
        elif label_upper in ["NEUTRAL", "NEU"]:
            color_hex = self.colors.get("NEU", "#f0e8d2")  # Default to yellow
        else:
            color_hex = "#d3d3d3"  # LightGray
        return self.hex_to_rgba(color_hex, score)

    def visualize(self, text):
        """
        Full pipeline: split text, analyze sentiments, and generate HTML.
        """
        chunks = self.split_text(text)
        sentiments = self.analyze_chunks(chunks)
        html_output = self.generate_html(chunks, sentiments)
        return html_output

    def display(self, text):
        """
        Display the HTML output in a Jupyter notebook or Streamlit app.
        """
        html_output = self.visualize(text)
        display(HTML(html_output))

    def display_streamlit(self, text):
        """
        Display the HTML output in a Jupyter notebook or Streamlit app.
        """
        html_output = self.visualize(text)
        st.markdown(html_output, unsafe_allow_html=True)  # Display the HTML content
