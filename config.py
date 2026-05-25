"""
Configuration settings for Sahayak AI
"""

# Application Settings
APP_NAME = "Sahayak AI"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Voice Assistant for Visually Challenged People"

# GUI Settings
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
WINDOW_TITLE = "Sahayak AI - Voice Assistant"

# Colors (Dark Theme with Blue Accents)
COLOR_BG_PRIMARY = "#0a0e27"      # Dark blue-black background
COLOR_BG_SECONDARY = "#1a1f3a"    # Slightly lighter background
COLOR_PRIMARY = "#00d9ff"          # Cyan/Light blue (glowing)
COLOR_PRIMARY_DARK = "#0099cc"     # Darker blue
COLOR_SECONDARY = "#ff006e"        # Pink accent
COLOR_TEXT_PRIMARY = "#ffffff"     # White text
COLOR_TEXT_SECONDARY = "#00d9ff"   # Cyan text
COLOR_BUTTON = "#00d9ff"           # Button color
COLOR_BUTTON_HOVER = "#00b8d4"     # Button hover color
COLOR_BUTTON_ACTIVE = "#0088aa"    # Button active color
COLOR_ACCENT = "#ff006e"           # Accent color

# Font Settings
FONT_FAMILY = "Arial"
FONT_SIZE_TITLE = 28
FONT_SIZE_BUTTON = 16
FONT_SIZE_NORMAL = 14
FONT_SIZE_SMALL = 12

# Speech Settings
SPEECH_RATE = 150                  # Words per minute
SPEECH_VOLUME = 0.9               # Volume level (0.0 to 1.0)
VOICE_TYPE = 0                    # 0 for male, 1 for female (varies by OS)

# Button Settings
BUTTON_WIDTH = 25
BUTTON_HEIGHT = 3
BUTTON_PADDING = 10

# Accessibility Settings
CONTRAST_MODE = True               # High contrast mode
KEYBOARD_NAVIGATION = True        # Enable keyboard navigation
FOCUS_HIGHLIGHT = True            # Highlight focused elements

# Messages
GREETING_MESSAGE = "Namaste! I am Sahayak AI, your personal voice assistant. I am here to help you with daily tasks."
TIME_PREFIX = "The current time is"
HELP_MESSAGE = "Emergency Help Mode Activated. Press ESC to exit or call emergency services if needed."
GOODBYE_MESSAGE = "Thank you for using Sahayak AI. Goodbye!"

# Feature Flags
ENABLE_TTS = True                 # Text-to-Speech enabled
ENABLE_VOICE_RECOGNITION = False  # Voice recognition (future feature)
ENABLE_EMERGENCY_MODE = True      # Emergency help mode