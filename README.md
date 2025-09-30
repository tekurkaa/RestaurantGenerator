# 🍽️ Restaurant Generator with Streamlit + LangChain

👉 **Live Demo:** [Click here to try the app](https://atv-restaurant-generator.streamlit.app/)

This is a basic Streamlit app that uses **LangChain** and **OpenAI** to:
- Generate a fancy restaurant name for a chosen cuisine
- Suggest a menu of items for that restaurant

---

## 🚀 Features
- Choose from multiple cuisines (Indian, Italian, Mexican, etc.)
- AI-generated restaurant name
- AI-generated menu items
- Clean, interactive UI with Streamlit

---

## 🛠 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/tekurkaa/restaurant-generator.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Add your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"   # Mac/Linux
   setx OPENAI_API_KEY "your_api_key_here"     # Windows PowerShell
   ```

---

## ▶️ Usage
Run the app locally with:
```bash
streamlit run main.py

  
