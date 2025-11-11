import pandas as pd
import matplotlib.pyplot as plt

# Read CSV with encoding fallback
try:
    df = pd.read_csv("network_traffic.csv", encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv("network_traffic.csv", encoding='latin1')

# --- Top 5 Protocols ---
if 'Protocol' in df.columns:
    top5_protocols = df['Protocol'].value_counts().head(5)
    top5_protocols.to_csv("top5_protocols.csv", header=["Count"])
    print("Top 5 protocols:")
    print(top5_protocols)
    top5_protocols.plot(kind='bar', title='Top 5 Protocols', color='skyblue')
    plt.ylabel("Count")
    plt.savefig("top5_protocols.png")
else:
    print("Column 'Protocol' not found in CSV.")

# --- Top 5 Source IPs ---
source_col = next((c for c in df.columns if 'source' in c.lower()), None)
if source_col:
    top5_sources = df[source_col].value_counts().head(5)
    top5_sources.to_csv("top5_source_ips.csv", header=["Count"])
    print("\nTop 5 Source IPs:")
    print(top5_sources)
    top5_sources.plot(kind='bar', title='Top 5 Source IPs', color='green')
    plt.ylabel("Count")
    plt.savefig("top5_source_ips.png")
else:
    print("No source IP column found in CSV.")

# --- Top 5 Destination IPs ---
dest_col = next((c for c in df.columns if 'dest' in c.lower()), None)
if dest_col:
    top5_dests = df[dest_col].value_counts().head(5)
    top5_dests.to_csv("top5_destination_ips.csv", header=["Count"])
    print("\nTop 5 Destination IPs:")
    print(top5_dests)
    top5_dests.plot(kind='bar', title='Top 5 Destination IPs', color='orange')
    plt.ylabel("Count")
    plt.savefig("top5_destination_ips.png")
else:
    print("No destination IP column found in CSV.")

print("\nNetwork traffic analysis completed. CSV summaries and plots generated.")
