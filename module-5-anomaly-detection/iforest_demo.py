import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# ==========================================
# 1. Generate Synthetic Telemetry (The Baseline)
# ==========================================
np.random.seed(42)
num_normal_pods = 500

# Normal Pod Behavior:
# - Egress Network: ~10 to 50 MB/s
# - Unique IPs: ~2 to 10
# - CPU Syscalls: ~500 to 1500 / sec
normal_data = {
    'pod_id': [f'pod-normal-{i}' for i in range(num_normal_pods)],
    'egress_mb_s': np.random.normal(30, 10, num_normal_pods).clip(5, 60),
    'unique_ips': np.random.poisson(5, num_normal_pods).clip(1, 15),
    'cpu_syscalls': np.random.normal(1000, 200, num_normal_pods).clip(300, 2000),
    'label': 'normal'
}
df_normal = pd.DataFrame(normal_data)

# ==========================================
# 2. Inject Rogue Pod Data (The Zero-Day Abuse)
# ==========================================
# Rogue Pod Behavior: compromised pod scanning the network
# It throttles CPU to look semi-normal, but network connections are high.
num_rogue_pods = 3
rogue_data = {
    'pod_id': [f'pod-ROGUE-{i}' for i in range(num_rogue_pods)],
    'egress_mb_s': np.random.normal(45, 5, num_rogue_pods),    # Slightly elevated, but might pass a static threshold
    'unique_ips': np.random.normal(450, 50, num_rogue_pods),   # MASSIVE spike in unique IPs (scanning)
    'cpu_syscalls': np.random.normal(800, 100, num_rogue_pods), # Trying to stay quiet on CPU
    'label': 'rogue'
}
df_rogue = pd.DataFrame(rogue_data)

# Combine datasets
df = pd.concat([df_normal, df_rogue], ignore_index=True)

# Feature Matrix used for AIOps Training
features = ['egress_mb_s', 'unique_ips', 'cpu_syscalls']
X = df[features]

# ==========================================
# 3. Train Isolation Forest Engine
# ==========================================
print("Training Isolation Forest to learn dynamic baseline...")
# contamination=0.01 tells the model we expect ~1% anomalies
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
model.fit(X)

# ==========================================
# 4. Evaluate and Isolate
# ==========================================
# Predict anomaly labels: 1 for normal, -1 for anomaly
df['anomaly_prediction'] = model.predict(X)

# Calculate anomaly scores. 
# scikit-learn's decision_function returns negative values for outliers and positive for normal data.
df['anomaly_score'] = model.decision_function(X)

# Display results
print("\n--- Detection Results ---")
print("Rogue Pods Detected (Score < 0):")
print(df[df['anomaly_prediction'] == -1][['pod_id', 'egress_mb_s', 'unique_ips', 'cpu_syscalls', 'anomaly_score']])

print("\nSample Normal Pods (Score > 0):")
print(df[df['anomaly_prediction'] == 1][['pod_id', 'egress_mb_s', 'unique_ips', 'cpu_syscalls', 'anomaly_score']].head(5))


# ==========================================
# 5. Visualization
# ==========================================
print("\nGenerating 3D Visualization: 'anomaly_plot.png'...")
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot normal data
normal_mask = df['anomaly_prediction'] == 1
ax.scatter(df[normal_mask]['egress_mb_s'], 
           df[normal_mask]['unique_ips'], 
           df[normal_mask]['cpu_syscalls'], 
           c='blue', label='Normal Baseline', alpha=0.5, marker='o')

# Plot anomalous data
anomaly_mask = df['anomaly_prediction'] == -1
ax.scatter(df[anomaly_mask]['egress_mb_s'], 
           df[anomaly_mask]['unique_ips'], 
           df[anomaly_mask]['cpu_syscalls'], 
           c='red', label='Isolated Anomaly (Rogue)', s=100, marker='x')

ax.set_xlabel('Egress Network (MB/s)')
ax.set_ylabel('Unique Outbound IPs')
ax.set_zlabel('CPU Syscalls/sec')
ax.set_title('AIOps: Multi-Dimensional Isolation of Rogue Pods')
ax.legend()

plt.savefig('anomaly_plot.png')
print("Visualization saved as 'anomaly_plot.png'.")
