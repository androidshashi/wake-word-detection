
# 🗣️ Offline Wake Word Detection (Custom Keyword)

A lightweight, privacy-first **offline wake word detection system** built with [Picovoice Porcupine](https://github.com/Picovoice/porcupine). It continuously listens for a custom keyword like “Jarvis”, “Echo”, “Hey Computer”, etc., and triggers an event when detected.

> 🎯 Ideal for offline AI assistants, smart home triggers, or embedded devices.

---

## ✨ Features

- 🔊 Custom wake word support
- ⚡ Fast and lightweight (low-latency)
- 🧠 Fully offline (no internet needed)
- 🔐 Privacy-preserving
- 💻 Cross-platform (macOS, Linux, Windows)

---

## 📦 Project Structure

```
wake-word-detection/
├── main.py              # Main script to run wake word listener
├── .env                 # Stores access key (excluded from git)
├── .env.example         # Sample env file format
├── models/              # Place your .ppn model here
│   └── your_keyword.ppn
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wake-word-detection.git
cd wake-word-detection
```

### 2. Create Virtual Environment (Optional but recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you face issues with `pyaudio`, install PortAudio:
> - macOS: `brew install portaudio`
> - Ubuntu: `sudo apt install portaudio19-dev`

### 4. Get Access Key & Wake Word Model

1. Go to [Picovoice Console](https://console.picovoice.ai)
2. Create an account / login
3. Generate a keyword (e.g., “Jarvis”)
4. Download the `.ppn` model file for your OS
5. Copy it to the `models/` directory
6. Copy your **Access Key**

### 5. Add Access Key to `.env`

Create a `.env` file in the root folder:

```
ACCESS_KEY=your_picovoice_access_key_here
```

> 🔐 The `.env` file is excluded from Git commits using `.gitignore`.

---

## ▶️ Run the Wake Word Listener

```bash
python main.py
```

Expected output:

```
🎤 Listening for your wake word...
✅ Wake word detected!
```

> You can now trigger any logic (e.g., start a voice assistant) once the keyword is detected.

---

## 🧠 Built With

- [Picovoice Porcupine](https://github.com/Picovoice/porcupine)
- Python 3
- PyAudio
- python-dotenv

---

## 🔒 Security & Best Practices

- Do **NOT** commit your `.env` file or `.ppn` keyword model
- Your access key and model are user-specific — each contributor must create their own
- Use `.env.example` to share expected format with others

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork and submit bug fixes, new features, or integrations (like speech recognition or voice assistant commands).

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- Thanks to [Picovoice](https://picovoice.ai) for enabling offline wake word technology.
