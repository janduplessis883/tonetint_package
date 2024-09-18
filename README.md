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
