# windows_log_analysis_ps.py
import pandas as pd

# Read exported Windows Application logs
logs = pd.read_csv("application_logs.csv")

# Count by Level (Error, Warning, Information)
level_counts = logs['LevelDisplayName'].value_counts()
print("\n=== Event Log Levels ===")
print(level_counts.to_frame().reset_index().rename(columns={'index':'Level', 'LevelDisplayName':'Count'}))

# Top 10 log sources
top_sources = logs['ProviderName'].value_counts().head(10)
print("\n=== Top 10 Log Sources ===")
print(top_sources.to_frame().reset_index().rename(columns={'index':'Source', 'ProviderName':'Count'}))


