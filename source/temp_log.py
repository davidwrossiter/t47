# temp_log.py
# Samples the Pi's CPU temperature at a fixed interval and writes it as CSV.
# Usage: python3 temp_log.py [output.csv] [interval_seconds]
# Stop with Ctrl+C.

import re
import subprocess
import sys
import time

TEMP_RE = re.compile(r"temp=([\d.]+)")


def read_temp():
    out = subprocess.check_output(["vcgencmd", "measure_temp"], text=True)
    return float(TEMP_RE.search(out).group(1))


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    interval = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0

    out = open(out_path, "w", buffering=1) if out_path else sys.stdout
    out.write("timestamp,temp_c\n")

    try:
        while True:
            ts = time.time()
            temp = read_temp()
            out.write(f"{ts:.3f},{temp:.1f}\n")
            time.sleep(interval)
    except KeyboardInterrupt:
        pass
    finally:
        if out_path:
            out.close()


if __name__ == "__main__":
    main()
