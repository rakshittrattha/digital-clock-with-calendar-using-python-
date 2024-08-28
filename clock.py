import tkinter as tk
from datetime import datetime
import time

class DigitalClockCalendar(tk.Tk):
    def __init__(self):
        """Initialize the main window and set up the clock and calendar displays."""
        super().__init__()
        self.title("Digital Clock and Calendar")
        self.geometry("300x250")

        # Frame and label for the clock display
        self.clock_frame = tk.Frame(self)
        self.clock_frame.pack(pady=10)
        self.time_label = tk.Label(self.clock_frame, font=('Helvetica', 48))
        self.time_label.pack()

        # Frame and label for the calendar display
        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.pack(pady=10)
        self.date_label = tk.Label(self.calendar_frame, font=('Helvetica', 20))
        self.date_label.pack()

        self.update_clock()
        self.update_calendar()

    def update_clock(self):
        """Update the time label every second."""
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.after(1000, self.update_clock)  # Update every second

    def update_calendar(self):
        """Update the date label every minute."""
        now = datetime.now()
        current_date = now.strftime('%A, %B %d, %Y')
        self.date_label.config(text=current_date)
        self.after(60000, self.update_calendar)  # Update every minute

if __name__ == "__main__":
    app = DigitalClockCalendar()
    app.mainloop()
