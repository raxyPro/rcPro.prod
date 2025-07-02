import subprocess
import sys

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    print("✅ Flask installed successfully.")
except subprocess.CalledProcessError as e:
    print("❌ Failed to install Flask:", e)
