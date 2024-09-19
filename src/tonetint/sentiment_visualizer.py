import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from transformers import pipeline
from IPython.display import HTML, display
import streamlit as st
from colorama import Fore, Style, init
import os
import webbrowser

# Initialize colorama
init(autoreset=True)

class ToneTint:
    def __init__(
        self,
        model_name="finiteautomata/bertweet-base-sentiment-analysis",
        chunk_size=8,
        colors=None,
        font="Arial",               # New argument for font
        font_size="14px",           # New argument for font size
    ):
        """
        Initializes the ToneTint class with a sentiment analysis model, chunk size, optional color, font, and font size settings.

        Args:
            model_name (str): The name of the sentiment analysis model to be used. Defaults to "finiteautomata/bertweet-base-sentiment-analysis".
            chunk_size (int): The number of words in each text chunk for sentiment analysis. Defaults to 8.
            colors (dict): A dictionary mapping sentiment labels ("POS", "NEG", "NEU") to corresponding hex color codes.
                           Defaults to green for "POS", red for "NEG", and yellow for "NEU".
            font (str): The font to be used in the HTML output. Defaults to "Arial".
            font_size (str): The font size to be used in the HTML output. Defaults to "14px".
        """
        self.chunk_size = chunk_size
        self.model = pipeline("sentiment-analysis", model=model_name)
        self.font = font                   # Store the font choice
        self.font_size = font_size         # Store the font size choice
        nltk.download("punkt", quiet=True)

        # Default colors for HTML if not provided
        default_colors = {
            "POS": "#aec867",  # Green
            "NEG": "#e8a56c",  # Red
            "NEU": "#f0e8d2",  # Yellow
        }
        self.colors = colors if colors else default_colors

    def split_text(self, text):
        """
        Splits input text into sentences and further into smaller chunks of words based on chunk_size.

        Args:
            text (str): The input text to be split into chunks.

        Returns:
            list: A list of text chunks, each containing a maximum of chunk_size words.
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
        Analyzes the sentiment of each chunk of text using the pre-trained model.

        Args:
            chunks (list): A list of text chunks to analyze.

        Returns:
            list: A list of dictionaries, where each dictionary contains the label ("POS", "NEG", "NEU")
                  and score of the sentiment for the corresponding chunk.
        """
        return self.model(chunks)

    def generate_html(self, chunks, sentiments):
        """
        Generates an HTML string with colored background for each text chunk based on its sentiment, and applies the specified font and font size.

        Args:
            chunks (list): A list of text chunks.
            sentiments (list): A list of sentiment dictionaries corresponding to each chunk.

        Returns:
            str: An HTML string where each text chunk is wrapped in a span with a background color representing its sentiment, font, and font size.
        """
        html_output = f"<div style='font-family:{self.font}; font-size:{self.font_size};'>"  # Set font and font size
        for chunk, sentiment in zip(chunks, sentiments):
            label = sentiment["label"]
            score = sentiment["score"]
            color = self.get_color(label, score)
            tooltip = f"Label: {label}, Score: {score:.2f}"
            html_output += f"<span style='background-color:{color};' title='{tooltip}'>{chunk} </span>"
        html_output += "</div>"
        return html_output

    def hex_to_rgba(self, hex_color, alpha):
        """
        Converts a hex color code to an RGBA color string with a given opacity (alpha).

        Args:
            hex_color (str): A hex color code in the format "#RRGGBB".
            alpha (float): The opacity level (0.0 to 1.0) for the color.

        Returns:
            str: An RGBA color string in the format "rgba(R, G, B, alpha)".
        """
        hex_color = hex_color.lstrip("#")
        r, g, b = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
        return f"rgba({r}, {g}, {b}, {alpha})"

    def get_color(self, label, score):
        """
        Determines the background color based on the sentiment label and adjusts its transparency using the score.

        Args:
            label (str): The sentiment label, e.g., "POSITIVE", "NEGATIVE", or "NEUTRAL".
            score (float): The confidence score of the sentiment (between 0 and 1).

        Returns:
            str: A color in RGBA format, with the transparency adjusted based on the score.
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
        Full pipeline to process the input text: splits the text into chunks, performs sentiment analysis on each chunk,
        and generates HTML output with colored background based on sentiment.

        Args:
            text (str): The input text to be analyzed and visualized.

        Returns:
            str: An HTML string with text chunks highlighted based on their sentiment.
        """
        chunks = self.split_text(text)
        sentiments = self.analyze_chunks(chunks)
        html_output = self.generate_html(chunks, sentiments)
        return html_output

    def display_notebook(self, text):
        """
        Displays the generated HTML in a Jupyter notebook.

        Args:
            text (str): The input text to be analyzed and visualized.
        """
        html_output = self.visualize(text)
        display(HTML(html_output))

    def display_streamlit(self, text):
        """
        Displays the generated HTML in a Streamlit app.

        Args:
            text (str): The input text to be analyzed and visualized.
        """
        html_output = self.visualize(text)
        st.markdown(html_output, unsafe_allow_html=True)

    def get_terminal_color(self, label):
        """
        Determines the terminal color based on the sentiment label.

        Args:
            label (str): The sentiment label, e.g., "POSITIVE", "NEGATIVE", or "NEUTRAL".

        Returns:
            str: A color escape code from the colorama library for the terminal output.
        """
        label_upper = label.upper()
        if label_upper in ["POSITIVE", "POS"]:
            return Fore.GREEN
        elif label_upper in ["NEGATIVE", "NEG"]:
            return Fore.RED
        else:
            return Style.RESET_ALL  # No color (default terminal color)

    def display_terminal(self, text):
        """
        Full pipeline to process the input text: splits the text into chunks, performs sentiment analysis on each chunk,
        writes the output as an HTML file, and prints a terminal link to open the file.

        Args:
            text (str): The input text to be analyzed and visualized in the terminal.
        """
        # Step 1: Split the text into chunks and perform sentiment analysis
        chunks = self.split_text(text)
        sentiments = self.analyze_chunks(chunks)

        # Step 2: Generate the custom HTML output directly for the terminal
        html_output = """
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #e8e8e8;
                }
                .container {
                    width: 50%;
                    margin: 0 auto;
                    padding: 40px;
                    text-align: left;
                    background-color: #ffffff;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    border-radius: 10px;
                }
                h1 {
                    font-size: 14px;
                    margin-bottom: 20px;
                    color: #333;
                }
                span {
                    display: inline-block;
                    margin: 1px 0;
                    padding: 5px;
                    border-radius: 4px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>ToneTint Output:</h2>
        """

        for chunk, sentiment in zip(chunks, sentiments):
            label = sentiment["label"]
            score = sentiment["score"]
            color = self.get_color(label, score)
            tooltip = f"Label: {label}, Score: {score:.2f}"
            html_output += f"<span style='background-color:{color};' title='{tooltip}'>{chunk} </span>"

        html_output += """
            </div>
        </body>
        </html>
        """

        # Step 3: Define the file path for the HTML file in the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(downloads_folder, "tonetint_output.html")

        # Step 4: Write the HTML content to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_output)

        # Step 5: Print the chunks with terminal colors and provide a link to the HTML file
        for chunk, sentiment in zip(chunks, sentiments):
            label = sentiment["label"]
            score = sentiment["score"]
            color = self.get_terminal_color(label)
            print(f"{color}{chunk} {Style.RESET_ALL}")

        # Step 6: Provide the terminal link to the file
        print(f"\n💾 The full analysis has been saved to: {file_path}")
        print("Opening the file in your default browser...")

        # Automatically open the HTML file in the default web browser
        webbrowser.open(f"file://{file_path}")

    def get_terminal_color(self, label):
        """
        Returns the terminal color for a given sentiment label.

        Args:
            label (str): The sentiment label ("POS", "NEG", "NEU").

        Returns:
            str: The corresponding colorama color code.
        """
        if label == "POS":
            return Fore.GREEN
        elif label == "NEG":
            return Fore.RED
        else:
            return Fore.YELLOW
