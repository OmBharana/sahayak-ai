# 🎤 Sahayak AI - Voice Assistant for Visually Challenged People

**Sahayak AI** is a modern, futuristic voice assistant application designed specifically to help visually challenged people perform daily tasks independently. Built with Python and featuring a sleek dark-themed interface with glowing effects and accessibility-first design principles.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

### 🎯 Core Functionality
- **Voice-Activated Assistance** - Speak responses using high-quality text-to-speech
- **Greeting Mode** - Personalized greeting with assistant introduction
- **Time Announcement** - Hear the current time spoken aloud
- **Emergency Help Mode** - Quick access to help with visual/audio alerts
- **Exit Function** - Graceful shutdown with goodbye message

### 🎨 UI/UX Design
- **Modern Dark Theme** - Easy on the eyes with black and blue color scheme
- **Futuristic Interface** - Glowing effects and smooth animations
- **Large Accessible Buttons** - Big touch targets for easy interaction
- **High Contrast Text** - Cyan and white text for better readability
- **Responsive Layout** - Adapts to different screen sizes

### ♿ Accessibility Features
- **Keyboard Navigation** - Full keyboard support (1-4 for buttons, ESC for exit)
- **Voice Output** - All interactions include audio feedback
- **Status Indicators** - Real-time status updates
- **Screen Reader Compatible** - Labels and descriptions for all elements
- **High Contrast Mode** - Bold colors for better visibility
- **Adjustable Speech Rate** - Configurable speed and volume

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Audio output capability on your system

### Step 1: Clone the Repository
```bash
git clone https://github.com/OmBharana/sahayak-ai.git
cd sahayak-ai
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

---

## 🎮 How to Use

### Starting the Application
1. Run `python main.py` from the project directory
2. The application window will open with the Sahayak AI interface

### Available Features

#### 🎤 Greeting (Button 1 / Press "1")
- Plays a personalized greeting message
- Introduces the assistant and its capabilities
- Perfect for first-time users

#### ⏰ Tell Time (Button 2 / Press "2")
- Announces the current time in 12-hour format
- Updates in real-time
- Great for keeping track of time

#### 🆘 Help Mode (Button 3 / Press "3")
- Activates emergency assistance mode
- Displays visual and audio alerts
- Press ESC or click again to deactivate

#### ❌ Exit (Button 4 / Press "4")
- Gracefully closes the application
- Plays goodbye message before exiting

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `1` | Greeting |
| `2` | Tell Time |
| `3` | Help Mode |
| `4` | Exit |
| `ESC` | Exit Help Mode |

---

## 🔧 Configuration

Edit `config.py` to customize:

### Colors
```python
COLOR_BG_PRIMARY = "#0a0e27"      # Main background
COLOR_PRIMARY = "#00d9ff"          # Accent color (cyan)
COLOR_SECONDARY = "#ff006e"        # Secondary accent (pink)
```

### Speech Settings
```python
SPEECH_RATE = 150                  # Words per minute
SPEECH_VOLUME = 0.9               # Volume (0.0 to 1.0)
VOICE_TYPE = 0                    # 0=Male, 1=Female
```

### Messages
```python
GREETING_MESSAGE = "Namaste! I am Sahayak AI..."
GOODBYE_MESSAGE = "Thank you for using Sahayak AI..."
```

---

## 📁 Project Structure

```
sahayak-ai/
├── main.py                 # Application entry point
├── gui.py                  # GUI interface (Tkinter)
├── assistant.py            # Voice assistant logic
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🛠️ Technical Stack

- **Python 3.7+** - Core programming language
- **Tkinter** - GUI framework (built-in with Python)
- **pyttsx3** - Text-to-Speech engine (cross-platform)
- **Threading** - Asynchronous speech output

---

## 🎨 Color Scheme

The interface uses a modern dark theme inspired by sci-fi UI designs:

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Blue-Black | #0a0e27 |
| Text Primary | White | #ffffff |
| Accent | Cyan | #00d9ff |
| Accent Secondary | Pink | #ff006e |

---

## 🐛 Troubleshooting

### No Audio Output
**Problem**: Application runs but no sound plays
- Check system volume is not muted
- Verify audio device is working
- Reinstall pyttsx3: `pip install --upgrade pyttsx3`

### Tkinter Not Found
**Problem**: `ModuleNotFoundError: No module named 'tkinter'`
- **macOS**: `brew install python-tk`
- **Linux**: `sudo apt-get install python3-tk`

---

## ♿ Accessibility Best Practices

### For Visually Impaired Users
- ✅ Large, high-contrast buttons
- ✅ All text is spoken aloud
- ✅ Status updates keep users informed
- ✅ Simple, consistent layout
- ✅ Clear keyboard navigation

---

## 📝 Use Cases

### Daily Activities
- Getting the current time
- Greeting the assistant
- Quick status checks

### Accessibility
- Independence for visually impaired users
- Hands-free interaction
- Audio-based feedback

---

## 🤝 Contributing

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Om Bharana**  
GitHub: [@OmBharana](https://github.com/OmBharana)

---

**Made with ❤️ for accessibility and inclusion**