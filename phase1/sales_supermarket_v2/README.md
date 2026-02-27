Ingest: Load raw data without modifying it. Establish raw schema + basic profiling.
Clean: Standardize types, handle nulls/duplicates, normalize categories. Minimal transformations.
Transform: Create derived columns and business-ready fields (e.g., datetime, weekday, hour).
Validate: Run assertions (pass/fail). If checks fail → stop.
Persist: Save processed dataset to data/processed/ in a stable format (prefer Parquet, CSV is fine).