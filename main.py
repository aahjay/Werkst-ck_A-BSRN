import os
import signal
import sys

# Pfade zu den einzelnen Skripten
scripts = {
    "conv": "Conv.py",
    "log": "Log.py",
    "stat": "Stat.py",
    "report": "Report.py"
}

# Liste der gestarteten Kindprozesse
processes = []