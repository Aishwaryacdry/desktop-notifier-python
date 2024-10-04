from plyer import notification
import time

def show_notification(title, message, interval):
    while True:
        notification.notify(
            title=title,
            message=message,
            app_icon=None,  # You can add a path to a .ico file for the icon
            timeout=10      # Notification stays for 10 seconds
        )
        time.sleep(interval)

if __name__ == "__main__":
    title = "Reminder"
    message = "Take a break! Stretch and drink water."
    interval = 60 * 60  # Notification every 1 hour
    show_notification(title, message, interval)
