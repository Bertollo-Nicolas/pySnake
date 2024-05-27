import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.process = None

    def start_process(self):
        """Start the main.py script."""
        print("Starting new process...")
        self.process = subprocess.Popen([sys.executable, "main.py"])

    def stop_process(self):
        """Terminate the existing process if it exists."""
        if self.process:
            print("Terminating existing process...")
            self.process.terminate()
            self.process.wait()  # Ensure the process has completely terminated
            self.process = None

    def process_event(self, event):
        """Restart the script on file modification."""
        self.stop_process()
        self.start_process()

    def on_modified(self, event):
        self.process_event(event)

if __name__ == "__main__":
    path = "." if len(sys.argv) < 2 else sys.argv[1]
    observer = Observer()
    handler = MyHandler()
    observer.schedule(handler, path=path, recursive=True)
    observer.start()
    handler.start_process()  # Start the process initially
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    handler.stop_process()  # Ensure the process is terminated on exit
