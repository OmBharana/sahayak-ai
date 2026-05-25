#!/usr/bin/env python3
"""
Sahayak AI - Voice Assistant for Visually Challenged People
Main entry point for the application
"""

import sys
from gui import SahayakAIGUI

def main():
    """Initialize and run the Sahayak AI application"""
    try:
        app = SahayakAIGUI()
        app.run()
    except KeyboardInterrupt:
        print("\n[INFO] Application terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()