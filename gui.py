"""
Sahayak AI - GUI Interface
Modern futuristic interface with accessibility features
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
from assistant import SahayakAssistant
from config import (
    APP_NAME, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,
    COLOR_BG_PRIMARY, COLOR_BG_SECONDARY, COLOR_PRIMARY, COLOR_PRIMARY_DARK,
    COLOR_SECONDARY, COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_BUTTON,
    COLOR_BUTTON_HOVER, COLOR_BUTTON_ACTIVE, FONT_FAMILY, FONT_SIZE_TITLE,
    FONT_SIZE_BUTTON, FONT_SIZE_NORMAL, BUTTON_WIDTH, BUTTON_HEIGHT,
    BUTTON_PADDING
)

class SahayakAIGUI:
    """GUI interface for Sahayak AI voice assistant"""
    
    def __init__(self):
        """Initialize the GUI"""
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG_PRIMARY)
        
        # Initialize assistant
        self.assistant = SahayakAssistant()
        
        # State variables
        self.is_help_mode = False
        self.last_response = ""
        
        # Configure styles
        self.setup_styles()
        
        # Build UI
        self.create_header()
        self.create_main_content()
        self.create_footer()
        
        # Bind keyboard events
        self.bind_keyboard_events()
        
        # Set window icon
        try:
            self.root.iconbitmap(default='')
        except:
            pass
    
    def setup_styles(self):
        """Configure custom styles for widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button style
        style.configure(
            'Custom.TButton',
            background=COLOR_BUTTON,
            foreground=COLOR_TEXT_PRIMARY,
            borderwidth=2,
            focuscolor='none',
            font=(FONT_FAMILY, FONT_SIZE_BUTTON, 'bold')
        )
    
    def create_header(self):
        """Create header section with title"""
        header_frame = tk.Frame(self.root, bg=COLOR_BG_SECONDARY, height=100)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Add glowing effect line
        glow_line = tk.Frame(header_frame, bg=COLOR_PRIMARY, height=3)
        glow_line.pack(fill=tk.X, padx=0, pady=0)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text=APP_NAME,
            font=(FONT_FAMILY, FONT_SIZE_TITLE, 'bold'),
            bg=COLOR_BG_SECONDARY,
            fg=COLOR_PRIMARY,
            pady=15
        )
        title_label.pack(expand=True)
        
        # Add glow effect by creating shadow text
        shadow_label = tk.Label(
            header_frame,
            text="AI Voice Assistant for Everyone",
            font=(FONT_FAMILY, FONT_SIZE_NORMAL),
            bg=COLOR_BG_SECONDARY,
            fg=COLOR_TEXT_SECONDARY,
            pady=5
        )
        shadow_label.pack(expand=True)
    
    def create_main_content(self):
        """Create main content area with buttons"""
        main_frame = tk.Frame(self.root, bg=COLOR_BG_PRIMARY)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=30)
        
        # Response display area
        display_frame = tk.Frame(main_frame, bg=COLOR_BG_SECONDARY, relief=tk.FLAT, bd=2)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=15)
        
        # Add border glow effect
        border_frame = tk.Frame(display_frame, bg=COLOR_PRIMARY, height=2)
        border_frame.pack(fill=tk.X, padx=0, pady=0)
        border_frame.pack_propagate(False)
        
        # Response text display
        self.response_text = tk.Label(
            display_frame,
            text="Welcome to Sahayak AI\nPress a button below to get started",
            font=(FONT_FAMILY, FONT_SIZE_NORMAL),
            bg=COLOR_BG_SECONDARY,
            fg=COLOR_TEXT_SECONDARY,
            wraplength=700,
            justify=tk.CENTER,
            pady=40
        )
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Buttons container
        buttons_frame = tk.Frame(main_frame, bg=COLOR_BG_PRIMARY)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=20)
        
        # Create buttons
        self.create_button(
            buttons_frame, "🎤 GREETING",
            self.on_greeting, 0, 0, "greeting"
        )
        self.create_button(
            buttons_frame, "⏰ TELL TIME",
            self.on_time, 0, 1, "time"
        )
        self.create_button(
            buttons_frame, "🆘 HELP MODE",
            self.on_help, 1, 0, "help"
        )
        self.create_button(
            buttons_frame, "❌ EXIT",
            self.on_exit, 1, 1, "exit"
        )
        
        # Status bar
        status_frame = tk.Frame(main_frame, bg=COLOR_BG_SECONDARY, height=50)
        status_frame.pack(fill=tk.X, padx=10, pady=15)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready to assist",
            font=(FONT_FAMILY, FONT_SIZE_SMALL),
            bg=COLOR_BG_SECONDARY,
            fg=COLOR_TEXT_SECONDARY,
            pady=15
        )
        self.status_label.pack(side=tk.LEFT, padx=20)
    
    def create_button(self, parent, text, command, row, col, button_id):
        """
        Create a custom button with glowing effect
        
        Args:
            parent: Parent frame
            text: Button text
            command: Button click command
            row: Grid row
            col: Grid column
            button_id: Unique button identifier
        """
        # Button container for glow effect
        button_container = tk.Frame(parent, bg=COLOR_BG_PRIMARY)
        button_container.grid(row=row, col=col, padx=BUTTON_PADDING, pady=BUTTON_PADDING, sticky="nsew")
        
        # Glow background
        glow_bg = tk.Frame(button_container, bg=COLOR_PRIMARY, relief=tk.FLAT)
        glow_bg.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Actual button
        button = tk.Button(
            glow_bg,
            text=text,
            command=command,
            font=(FONT_FAMILY, FONT_SIZE_BUTTON, 'bold'),
            bg=COLOR_BUTTON,
            fg=COLOR_TEXT_PRIMARY,
            activebackground=COLOR_BUTTON_HOVER,
            activeforeground=COLOR_TEXT_PRIMARY,
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=15,
            cursor="hand2",
            wraplength=150
        )
        button.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Bind hover effects
        button.bind("<Enter>", lambda e: self.on_button_hover(button, True))
        button.bind("<Leave>", lambda e: self.on_button_hover(button, False))
        
        # Store button reference
        if not hasattr(self, 'buttons'):
            self.buttons = {}
        self.buttons[button_id] = {'button': button, 'container': button_container}
        
        # Configure grid weights
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)
    
    def on_button_hover(self, button, is_hover):
        """Handle button hover effect"""
        if is_hover:
            button.config(bg=COLOR_BUTTON_HOVER)
        else:
            button.config(bg=COLOR_BUTTON)
    
    def create_footer(self):
        """Create footer with version info"""
        footer_frame = tk.Frame(self.root, bg=COLOR_BG_SECONDARY, height=40)
        footer_frame.pack(fill=tk.X, padx=0, pady=0)
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text=f"{APP_NAME} v{APP_VERSION} | Designed for Accessibility | Press ESC to Exit Help Mode",
            font=(FONT_FAMILY, FONT_SIZE_SMALL),
            bg=COLOR_BG_SECONDARY,
            fg=COLOR_TEXT_SECONDARY
        )
        footer_label.pack(expand=True, pady=10)
    
    def bind_keyboard_events(self):
        """Bind keyboard shortcuts"""
        self.root.bind('<Escape>', self.on_escape)
        self.root.bind('1', lambda e: self.on_greeting())
        self.root.bind('2', lambda e: self.on_time())
        self.root.bind('3', lambda e: self.on_help())
        self.root.bind('4', lambda e: self.on_exit())
    
    def on_escape(self, event=None):
        """Handle ESC key press"""
        if self.is_help_mode:
            self.exit_help_mode()
    
    def update_response(self, text):
        """Update response display"""
        self.last_response = text
        self.response_text.config(text=text, fg=COLOR_PRIMARY)
        self.root.after(3000, lambda: self.response_text.config(fg=COLOR_TEXT_SECONDARY))
    
    def update_status(self, text):
        """Update status bar"""
        self.status_label.config(text=text)
    
    def on_greeting(self):
        """Handle greeting button"""
        self.update_status("🎤 Speaking greeting...")
        self.assistant.handle_greeting(callback=self.update_response)
    
    def on_time(self):
        """Handle time button"""
        self.update_status("⏰ Announcing current time...")
        self.assistant.handle_time(callback=self.update_response)
    
    def on_help(self):
        """Handle help/emergency button"""
        if self.is_help_mode:
            self.exit_help_mode()
        else:
            self.enter_help_mode()
    
    def enter_help_mode(self):
        """Enter emergency help mode"""
        self.is_help_mode = True
        self.update_status("🆘 EMERGENCY HELP MODE ACTIVE - Press ESC to Exit")
        self.response_text.config(fg=COLOR_SECONDARY)
        self.assistant.handle_help(callback=self.update_response)
        
        # Flash effect
        self.root.config(bg=COLOR_SECONDARY)
        self.root.after(200, lambda: self.root.config(bg=COLOR_BG_PRIMARY))
        self.root.after(400, lambda: self.root.config(bg=COLOR_SECONDARY))
        self.root.after(600, lambda: self.root.config(bg=COLOR_BG_PRIMARY))
    
    def exit_help_mode(self):
        """Exit emergency help mode"""
        self.is_help_mode = False
        self.update_status("Help mode deactivated. Ready to assist.")
        self.response_text.config(fg=COLOR_TEXT_SECONDARY)
        self.response_text.config(text="Help mode exited. Select an option to continue.")
    
    def on_exit(self):
        """Handle exit button"""
        self.update_status("👋 Goodbye!")
        self.assistant.handle_exit()
        self.root.after(1500, self.root.quit)
    
    def run(self):
        """Run the GUI application"""
        self.root.mainloop()