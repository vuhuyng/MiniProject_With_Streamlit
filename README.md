# MiniProject With Streamlit

This project demonstrates deploying various models using Streamlit in a black-box direction. It covers object detection, a chatbot, and word correction using Levenshtein distance. This is part of the curriculum for Week 4, Module 1: Python toward AI/DS.

![demo0.gif](https://github.com/vuhuyng/MiniProject_With_Streamlit/blob/main/demo1.gif)



## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Object Detection](#object-detection)
  - [Chatbot](#chatbot)
  - [Word Correction](#word-correction)
- [Acknowledgements](#acknowledgements)

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/vuhuyng/MiniProject_With_Streamlit.git
    cd MiniProject_With_Streamlit
    ```

2. **Install required libraries:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Navigate to the `src` directory and run the respective Streamlit applications as described below.

### Object Detection

To run the object detection module:

```sh
cd src
python -m streamlit run object_detection.py
```

### Chatbot

To use the chatbot module:

Sign up on Hugging Face: Go to Hugging Face Chat and create an account if you don’t have one.
https://huggingface.co/chat/

Run the chatbot application:

```sh
cd src
python -m streamlit run object_detection.py
```

### Word Correction
Run the word correction application:

```sh
cd src
python -m streamlit run levenshtein_distance.py
```




