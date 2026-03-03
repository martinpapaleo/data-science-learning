from pathlib import Path
import pandas as pd
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'
RAW_FILENAME = RAW_DIR / 'supermarket_sales.csv'
OUTPUT_FILENAME = PROCESSED_DIR / 'sales_clean.parquet'
debug = False
