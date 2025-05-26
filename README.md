# 🎬 YouTube Thumbnail Creator with AI

This project is a web-based application built using **Streamlit** and **Google Gemini** API that generates YouTube thumbnail images based on a provided video summary or transcript. It uses generative AI to produce a creative prompt and generate an image accordingly.

## 🚀 Features

- Enter a YouTube video summary or transcript
- AI generates a prompt describing an ideal thumbnail
- Generates an image using Google Gemini's image generation model
- View and download the AI-generated thumbnail

## 🛠️ Technologies Used

- Streamlit (Web UI)
- LangChain
- Google Gemini API (via `langchain-google-genai`)
- dotenv for environment variable management

## 📂 Project Structure

```

├── app.py                 # Streamlit web app
├── main.py                # Core logic for prompt and image generation
├── .env                   # Stores your Google API Key
├── requirements.txt       # Python dependencies

````

## 📄 Requirements

- Python 3.8+
- Google API Key for Gemini models

## 🔑 Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/youtube-thumbnail-ai.git
   cd youtube-thumbnail-ai
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**

   Create a `.env` file in the root directory with your Google API key:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

## 🧠 How It Works

* `app.py`: Captures input from user and displays output.
* `main.py`:

  * Uses Gemini Pro (Text) to generate an image prompt.
  * Uses Gemini Pro (Image) to generate the thumbnail from that prompt.
* The image is returned as base64 and decoded for display.

## 📸 Example Usage

Paste a video summary like:

> "This video explains the rise of electric vehicles and the future of transportation in a world aiming for sustainability."

Click **Generate Thumbnail** and get a creative thumbnail image instantly!

---

**Made with 💡 by \[Jitendra Banjarey]**
