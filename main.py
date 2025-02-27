from src.app import App
import sys

if __name__ == "__main__":
    try:
        app = App()
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)