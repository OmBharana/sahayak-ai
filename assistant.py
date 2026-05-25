"""
Sahayak AI - Voice Assistant Logic
Handles text-to-speech and AI responses
"""

import pyttsx3
import datetime
import threading
from config import (
    SPEECH_RATE, SPEECH_VOLUME, VOICE_TYPE,
    GREETING_MESSAGE, TIME_PREFIX, HELP_MESSAGE, GOODBYE_MESSAGE
)

class SahayakAssistant:
    """Voice assistant for visually challenged people"""
    
    def __init__(self):
        """Initialize the text-to-speech engine"""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', SPEECH_RATE)
        self.engine.setProperty('volume', SPEECH_VOLUME)
        
        # Set voice (male/female based on config)
        voices = self.engine.getProperty('voices')
        if len(voices) > VOICE_TYPE:
            self.engine.setProperty('voice', voices[VOICE_TYPE].id)
        
        self.is_speaking = False
        self.current_text = ""
    
    def speak(self, text, async_mode=True):
        """
        Convert text to speech
        
        Args:
            text (str): Text to speak
            async_mode (bool): If True, speak asynchronously
        """
        self.current_text = text
        self.is_speaking = True
        
        def speak_sync():
            self.engine.say(text)
            self.engine.runAndWait()
            self.is_speaking = False
        
        if async_mode:
            thread = threading.Thread(target=speak_sync, daemon=True)
            thread.start()
        else:
            speak_sync()
    
    def stop_speaking(self):
        """Stop current speech"""
        try:
            self.engine.stop()
            self.is_speaking = False
        except Exception as e:
            print(f"[ERROR] Failed to stop speech: {str(e)}")
    
    def get_greeting(self):
        """Get greeting message"""
        return GREETING_MESSAGE
    
    def get_current_time(self):
        """Get current time as formatted string"""
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        am_pm = "AM" if hour < 12 else "PM"
        
        # Convert to 12-hour format
        if hour > 12:
            hour = hour - 12
        elif hour == 0:
            hour = 12
        
        time_string = f"{TIME_PREFIX} {hour}:{minute:02d} {am_pm}"
        return time_string
    
    def get_help_message(self):
        """Get help/emergency message"""
        return HELP_MESSAGE
    
    def get_goodbye_message(self):
        """Get goodbye message"""
        return GOODBYE_MESSAGE
    
    def handle_greeting(self, callback=None):
        """Handle greeting feature"""
        message = self.get_greeting()
        self.speak(message)
        if callback:
            callback(message)
    
    def handle_time(self, callback=None):
        """Handle time feature"""
        message = self.get_current_time()
        self.speak(message)
        if callback:
            callback(message)
    
    def handle_help(self, callback=None):
        """Handle help/emergency mode"""
        message = self.get_help_message()
        self.speak(message)
        if callback:
            callback(message)
    
    def handle_exit(self, callback=None):
        """Handle exit"""
        message = self.get_goodbye_message()
        self.speak(message, async_mode=False)
        if callback:
            callback(message)
    
    def __del__(self):
        """Cleanup when assistant is destroyed"""
        try:
            self.stop_speaking()
        except:
            pass