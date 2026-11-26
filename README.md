# ToneTint

[![PyPI version](https://badge.fury.io/py/ToneTint.svg)](https://badge.fury.io/py/ToneTint)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**ToneTint** is a Python package that provides an intuitive way to perform sentiment analysis on text data and visualize the results. It splits the input text into manageable chunks, analyzes each chunk using a pre-trained sentiment analysis model, and highlights the text with background colors corresponding to the sentiment. Additionally, it displays tooltips with detailed sentiment scores when hovering over each text chunk. Perfect for Jupyter Notebooks & Steamlit.

![images](https://github.com/janduplessis883/tonetint_package/raw/master/images/social.png)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Example](#basic-example)
  - [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Sentiment Analysis**: Uses pre-trained models to analyze the sentiment of text chunks.
- **Color-Coded Visualization**: Highlights text with colors representing positive, negative, or neutral sentiments.
- **Opacity Adjustment**: Adjusts the opacity of the highlight based on the confidence score of the sentiment prediction.
- **Interactive Tooltips**: Displays sentiment labels and scores when hovering over text chunks.
- **Customizable Colors**: Allows customization of highlight colors for different sentiments.
- **Flexible Text Chunking**: Splits text into sentences and further into chunks of specified sizes for detailed analysis.

## Installation

You can install **ToneTint** via pip:

```bash
pip install tonetint
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/janduplessis883/tonetint_package.git
cd tonetint_package
python setup.py install
```

## Usage

### Basic Example - Jupyter Notebook

```python
from tonetint.sentiment_visualizer import ToneTint

# Initialize the visualizer
visualizer = ToneTint()

# Your input text
text = "I love sunny days. However, I hate the rain. The weather today is okay."

# Display the sentiment visualization in Jupyter Notebook
visualizer.display_notebook(text)
```
### Basic Example - Stremlit App
```python
from tonetint.sentiment_visualizer import ToneTint

# Initialize the visualizer
visualizer = ToneTint()

# Your input text
text = "I love sunny days. However, I hate the rain. The weather today is okay."

# Display the sentiment visualization in a Streamlit app
visualizer.display_streamlit(text)
```
This code will display your text with:

- **Positive sentiments** highlighted in green.
- **Negative sentiments** highlighted in red.
- **Neutral sentiments** highlighted in yellow.

Hovering over each text chunk will show a tooltip with the sentiment label and confidence score.

### Customization

**Customizing Highlight Colors**

You can specify custom `colors` for positive, negative, and neutral sentiments by passing a dictionary to the `ToneTint` constructor:

```python
custom_colors = {
        "POS": "#aec867",  # Green
        "NEG": "#e8a56c",  # Red
        "NEU": "#f0e8d2",  # Yellow
}

visualizer = ToneTint(colors=custom_colors)
```

**Adjusting Chunk Size**

You can adjust the chunk size (number of words per chunk) for more granular or broader analysis:

```python
visualizer = ToneTint(chunk_size=10)
```

**Using a Different Model**

By default **ToneTint** uses `nlptown/bert-base-multilingual-uncased-sentiment` from [Huggingface.co](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) The model performs well on most sentiment analysis tasks.

You can specify a different pre-trained model, more suited to your sentiment analysis usecase:

```python
visualizer = ToneTint(model_name='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
```

## Dependencies

- **Python 3.6 or higher**
- **Transformers**: For using pre-trained sentiment analysis models.
- **NLTK**: For text tokenization.
- **IPython**: For displaying HTML in Jupyter notebooks.
- **Torch**: Required by some Transformer models.
- **SentencePiece**: For certain tokenizer models.

You can install the dependencies via pip:

```bash
pip install transformers nltk ipython torch sentencepiece
```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

1. **Fork** the repository.
2. **Create** your feature branch (`git checkout -b feature/YourFeature`).
3. **Commit** your changes (`git commit -am 'Add some feature'`).
4. **Push** to the branch (`git push origin feature/YourFeature`).
5. **Open** a pull request.

Please ensure your code adheres to the existing style conventions and that all tests pass.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This package uses pre-trained models from Hugging Face's Transformers library. The performance and accuracy of sentiment analysis depend on the chosen model. Always verify the outputs, especially when used for critical applications.

---
## Release Notes for ToneTint v0.0.15

We are excited to announce the release of **ToneTint v0.0.15**, which includes new features to improve the customization and usability of text sentiment analysis output. This update introduces the ability to customize font settings and enhances the terminal output experience, providing better interactivity and visual feedback. Below is a comprehensive breakdown of the new features and updates included in this release.

### New Features

#### 1. **Font and Font Size Customization for HTML Output**
In this release, we have introduced two new parameters, `font` and `font_size`, allowing users to define custom fonts and font sizes for the generated HTML output. This provides greater flexibility in how the sentiment analysis results are displayed.

- **Font**: The default is set to `"Arial"`. This can be changed to any desired font by passing a different font name when initializing the `ToneTint` class.
- **Font Size**: The default size is `"14px"`. You can customize this value to match your preferred text size.

**Usage Example:**
```python
# Initialize the ToneTint class with custom font and font size
tone_tint = ToneTint(font="Helvetica", font_size="16px")
```

**Impact:**
- Custom fonts and font sizes are applied to the text chunks displayed in the generated HTML file, allowing better control over the visual presentation of sentiment analysis results.

### Updates

#### 2. **Enhanced `display_terminal` Function**
The `display_terminal` function has been updated to provide a more polished and interactive output experience. In addition to displaying sentiment-colored text directly in the terminal, the function now generates a more refined HTML report that is automatically saved to the user's `Downloads` folder.

Key improvements include:

- **HTML Report Generation**:
  - The function now writes the sentiment analysis results to an HTML file (`tonetint_output.html`) located in the user's `Downloads` folder.
  - The HTML report includes a **centered container** that takes up 50% of the page width, making the output look clean and professional.
  - A new **heading** (`<h1>`) titled "ToneTint Output:" is included at the top of the report for clear identification.

- **Automatic File Opening**: After generating the HTML file, the `display_terminal` function will automatically open the file in the user's default web browser, providing instant access to the full sentiment analysis output.

- **Terminal Link**: The terminal now prints the path to the generated HTML file, allowing the user to manually open it if desired.

**Usage Example:**
```python
# Analyze text and generate a terminal output with an HTML report
tone_tint.display_terminal("This is a test sentence for sentiment analysis.")
```

**Sample Output in Terminal**:
```
This is a test sentence for sentiment analysis.
The full analysis has been saved to: /path/to/Downloads/tonetint_output.html
Opening the file in your default browser...
```

### Bug Fixes

- **Minor Performance Enhancements**: Optimized the chunk splitting and HTML generation processes to handle larger texts more efficiently.
- **Robust Path Handling**: Ensured cross-platform compatibility for saving files to the `Downloads` folder, making the function reliable on both Windows and macOS/Linux.

---

### Summary of Changes:
- **New**: `font` and `font_size` parameters for HTML output customization.
- **Updated**: `display_terminal` function now generates an interactive, visually refined HTML report and opens it automatically in the user's browser.
- **Bug Fixes**: Improved performance and cross-platform file handling.

### How to Upgrade
To upgrade to the latest version of ToneTint, run the following command:
```bash
pip install --upgrade tonetint
```

We hope these updates enhance your experience with ToneTint. As always, feedback and contributions are welcome. Feel free to open issues or submit pull requests on [GitHub](https://github.com/your-repo/tonetint).

Thank you for using ToneTint!
