# 🚀 Sahayak AI - Complete Setup Guide

This guide will walk you through setting up and running Sahayak AI on your system.

---

## 📋 Prerequisites

- **Python 3.7 or higher** - Download from [python.org](https://www.python.org/downloads/)
- **pip** - Usually comes with Python
- **Audio output** - Working speakers or headphones
- **Git** (optional) - For cloning the repository

### Verify Prerequisites

Check if Python and pip are installed:

```bash
python --version
pip --version
```

---

## 🔧 Installation Steps

### Step 1: Get the Code

#### Option A: Clone with Git
```bash
git clone https://github.com/OmBharana/sahayak-ai.git
cd sahayak-ai
```

#### Option B: Download ZIP
1. Visit [https://github.com/OmBharana/sahayak-ai](https://github.com/OmBharana/sahayak-ai)
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal/cmd in the extracted folder

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import pyttsx3; print('✓ pyttsx3 installed successfully')"
```

---

## 🖥️ Platform-Specific Setup

### Windows Setup

1. **No additional setup needed!** Windows includes SAPI5 for text-to-speech.

2. Run the application:
```bash
python main.py
```

### macOS Setup

1. **No additional setup needed!** macOS has native speech synthesis.

2. Run the application:
```bash
python3 main.py
```

### Linux Setup

1. **Install required packages**:
```bash
# Ubuntu/Debian
sudo apt-get install espeak ffmpeg libespeak1 python3-tk

# Fedora/RHEL
sudo dnf install espeak ffmpeg libespeak python3-tkinter

# Arch
sudo pacman -S espeak ffmpeg tk
```

2. Run the application:
```bash
python3 main.py
```

---

## ▶️ Running the Application

### Basic Run

```bash
python main.py
```

### Troubleshooting Runs

#### If you get "command not found":
```bash
# Try with python3
python3 main.py

# Or if in a virtual environment
./venv/Scripts/python main.py  # Windows
./venv/bin/python main.py      # macOS/Linux
```

---

## 🎮 First Run Checklist

- [ ] Application window opens
- [ ] "Sahayak AI" title visible in cyan
- [ ] All 4 buttons are visible with glow effect
- [ ] Click "Greeting" button
- [ ] Hear audio greeting message
- [ ] Text appears in display area
- [ ] Try "Tell Time" button
- [ ] Hear time announcement
- [ ] Try "Help Mode" button
- [ ] See red flash and hear alert
- [ ] Press ESC to exit Help Mode
- [ ] Click "Exit" button
- [ ] Hear goodbye and window closes

---

## ⚙️ Configuration

### Changing Voice

Edit `config.py`:

```python
VOICE_TYPE = 0  # 0 for male, 1 for female (varies by OS)
```

### Adjusting Speech Speed

Edit `config.py`:

```python
SPEECH_RATE = 150  # Lower = slower, Higher = faster
```

### Changing Speech Volume

Edit `config.py`:

```python
SPEECH_VOLUME = 0.9  # 0.0 to 1.0
```

---

## 🐛 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'tkinter'"

**Solution**:
```bash
# Windows - Reinstall Python and check "tcl/tk and IDLE" option

# macOS
brew install python-tk@3.9

# Linux - Ubuntu/Debian
sudo apt-get install python3-tk

# Linux - Fedora
sudo dnf install python3-tkinter
```

### Issue: "ModuleNotFoundError: No module named 'pyttsx3'"

**Solution**:
```bash
pip install --upgrade pyttsx3
```

### Issue: No Audio Output

**Solution**:
1. Check system volume is not muted
2. Verify audio device works
3. Try reinstalling pyttsx3:
   ```bash
   pip uninstall pyttsx3
   pip install pyttsx3
   ```

### Issue: Application Crashes on Startup

**Solution**:
1. Check Python version: `python --version` (should be 3.7+)
2. Verify dependencies: `pip install -r requirements.txt`
3. Try with Python 3.9 if using older version

---

## 📊 Checking Your Setup

Run this verification:

```bash
python -c "
import sys
print('=== Sahayak AI Setup Verification ===')
print(f'Python Version: {sys.version}')

try:
    import tkinter
    print('✓ Tkinter: OK')
except:
    print('✗ Tkinter: NOT FOUND')

try:
    import pyttsx3
    print('✓ pyttsx3: OK')
except:
    print('✗ pyttsx3: NOT FOUND')

print('=== End Verification ===')
"
```

---

## ✅ You're Ready!

You now have Sahayak AI installed and ready to use.

**Next Steps**:
1. Run `python main.py`
2. Click the "Greeting" button to start
3. Explore other features
4. Customize colors and messages as needed
5. Share your experience!

---

**Enjoy Sahayak AI!** 🎤✨