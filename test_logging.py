import logging
import sys

def check_logger_levels():
    print("\nLogger Levels:")
    print(f"Root logger level: {logging.getLogger().getEffectiveLevel()}")
    print(f"'default' logger level: {logging.getLogger('default').getEffectiveLevel()}")
    print(f"'file_only' logger level: {logging.getLogger('file_only').getEffectiveLevel()}")
    print(f"'file_and_stream' logger level: {logging.getLogger('file_and_stream').getEffectiveLevel()}")

# Example 1: Default Behavior
def default_logging():
    print("Example 1: Default Logging")
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("default")
    logger.debug("Example1: This is a debug message")  # Won't be printed
    logger.info("Example1: This is an info message")  # Will be printed
    logger.warning("Example1: This is a warning")  # Will be printed

# Example 2: File Handler Only
def file_handler_only():
    print("\nExample 2: File Handler Only")
    logger = logging.getLogger("file_only")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Prevent propagation to root logger
    file_handler = logging.FileHandler("file_only.log")
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.debug("Example2: This debug message goes to file only")
    logger.info("Example2: This info message goes to file only")

# Example 3: File Handler and Stream Handler
def file_and_stream_handler():
    print("\nExample 3: File and Stream Handler")
    logger = logging.getLogger("file_and_stream")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Prevent propagation to root logger
    file_handler = logging.FileHandler("file_and_stream.log")
    file_handler.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.debug("Example3: This debug message goes to file only")
    logger.info("Example3: This info message goes to both file and console")

if __name__ == "__main__":
    default_logging()
    file_handler_only()
    file_and_stream_handler()
    check_logger_levels()