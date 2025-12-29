# Personal Voice Assistant - Mily

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

**Mily** is an intelligent voice assistant built with Python that integrates WolframAlpha, Wikipedia, and financial APIs to provide hands-free access to information through a modern web dashboard. Designed to provide a seamless experience, Mily understands human speech and executes a variety of tasks ranging from fetching real-time financial data to translating languages.

<img src="www/image1.jpeg" style="display: block; margin: auto;" width="400" />

### Key Features

- **Voice Interaction**: Seamless Speech-to-Text and Text-to-Speech capabilities using Google Speech Recognition and gTTS.
- **Real-Time Information**:
    - **Weather**: Current temperature and description for any city (via Weatherbit).
    - **News**: Top 5 headlines in the US.
    - **Finance**: Live stock prices (Tesla, Apple, Facebook) and cryptocurrency rates (Bitcoin, Dogecoin, Solana).
- **Knowledge Base**:
    - **WolframAlpha Integration**: Answers computational and geographical questions.
    - **Wikipedia**: Summarizes topics directly from Wikipedia.
- **Utilities**:
    - **Translator**: Bidirectional translation between English and Spanish.
    - **Date & Time**: Current time and day of the week.

### Technology Stack

- **Language**: Python 3
- **Speech Processing**: `SpeechRecognition`, `gTTS`, `playsound`
- **Data & APIs**: `yfinance`, `wolframalpha`, `wikipedia`, `requests`
- **Utilities**: `datetime`, `translators`, `streamlit`

## Prerequisites

Before setting up this project, ensure you have:
- **Python 3** installed.
- **PortAudio** (Required for `SpeechRecognition` to access your microphone).
    - *macOS*: `brew install portaudio`
    - *Linux*: `sudo apt-get install portaudio19-dev`
- **API Keys**: You will need valid API keys/endpoints for:
    - Weatherbit
    - WolframAlpha
    - News API source
    - Crypto API source

**Note**: Windows users may encounter compatibility issues with audio libraries. Using WSL2 or Linux/macOS is recommended.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Voice_Assistant.git
cd Voice_Assistant
```

### 2. Set Up Virtual Environment (Recommended)
```bash
virtualenv voiceassistant.venv
source voiceassistant.venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a file named `VA_Tokens.py` in the root directory. This file must contain your API keys and URLs as variables:

```python
# VA_Tokens.py
weather_api = "YOUR_WEATHERBIT_API_KEY"
wolframalpha_api = "YOUR_WOLFRAMALPHA_APP_ID"
news_url = "YOUR_NEWS_API_ENDPOINT"
crypto_api = "YOUR_CRYPTO_API_ENDPOINT"
```

## Usage

### Option 1: Web Interface (Recommended)
Run the application via Streamlit:
```bash
streamlit run Voice_Assistant_Mily.py
```

### Voice Commands

Mily will ask for your name and then listen for commands. Say "Stop" to exit.

| Intent | Command Example |
|--------|-----------------|
| **Weather** | "Hey Mily, tell me the weather" |
| **News** | "Hey Mily, tell me the news" |
| **Stocks** | "Tell me the Tesla stock price" |
| **Crypto** | "What is the price of Bitcoin?" |
| **Questions** | "I have a question" -> "What is the capital of France?" |
| **Translate** | "Translate for me" |
| **Wikipedia** | "Search in Wikipedia" |
| **Time** | "What time is it?" |

## Project Structure

```
Voice_Assistant/
├── Voice_Assistant_Mily.py   # Main application logic
├── VA_Tokens.py              # API Configuration (User created)
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── www/                      # Images
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
