from pathlib import Path
import time
import pandas as pd

BASE_DIR = Path.cwd()
STREAM_SOURCE_FILE = BASE_DIR / "power_streaming_data.csv"
OUTPUT_DIR = BASE_DIR / "power_stream_input"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

stream_df = pd.read_csv(STREAM_SOURCE_FILE)

for i in range(20):
    sample_df = stream_df.sample(n=5, replace=False, random_state=None)
    out_file = OUTPUT_DIR / f"power_stream_batch_{i:03d}.csv"
    sample_df.to_csv(out_file, index=False)
    print(f"Wrote {out_file}")
    time.sleep(10)

print("finished writing streaming files.")
