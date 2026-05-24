# Module 5: Anomaly Detection with Isolation Forest

This module provides a hands-on exercise demonstrating how to use the **Isolation Forest (iForest)** algorithm to detect infrastructure abuse, such as a compromised container scanning the network.

## Why this is true AIOps

This exercise qualifies perfectly as **AIOps (Artificial Intelligence for IT Operations)** because it replaces static, brittle human rules with data-driven machine intelligence. In traditional operations, systems are monitored using static thresholds (e.g., "Alert me if CPU > 85%"). In modern architectures, this approach breaks down.

Here is the architectural shift that elevates this from basic scripting to true AIOps:

### 1. Multi-Dimensional Correlation vs. Single-Metric Alerts
Traditional monitoring tools look at metrics in isolated silos. An attacker mining crypto or running a network scan might purposely throttle their malware to bypass individual alerts.
* **The AIOps Approach:** Isolation Forest evaluates the **joint mathematical space** of all features simultaneously. It realizes that while 40% CPU is normal, and 20 MB/s network is normal, having 40% CPU *combined* with an explosion of 450 unique outbound IPs is highly abnormal.

### 2. Dynamic Baseline Learning (No Magic Numbers)
In standard DevOps, engineers guess threshold values, leading to either alert fatigue or missed breaches.
* **The AIOps Approach:** The algorithm has no pre-programmed threshold numbers. It looks at the real-time telemetry matrix and natively figures out the structural baseline on its own, adapting dynamically to the environment's specific signature.

### 3. Mathematical Isolation vs. Rule Writing
In traditional systems, new abuse requires writing a new rule post-mortem.
* **The AIOps Approach:** The Isolation Forest relies purely on the unsupervised mathematical properties of anomalies—that they are **rare** and **different**. By isolating outliers natively through data partitioning, it can catch **Zero-Day infrastructure behavior** that you have never seen before.

## The AIOps Workflow Pipeline

In a production enterprise framework, this script represents the "Compute & Analyze" engine of a complete pipeline:

```text
[ Infra Telemetry Streams ] 
       │ (Prometheus / OpenTelemetry Vectors)
       ▼
[ Data Aggregator Node ] 
       │ (Pandas / Feature Matrix Engineering)
       ▼
[ Isolation Forest Engine ]  <--- (This module's iforest_demo.py script)
       │ (Unsupervised Isolation Scoring)
       ▼
[ Incident Deduplication ] 
       │ (Groups similar low-score paths)
       ▼
[ Smart Alerting Engine ] 
         (PagerDuty / Slack: "High-probability anomalous profile detected")
```

## Quick Start

1. Create a virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the demonstration script:
```bash
python iforest_demo.py
```

The script will generate a synthetic baseline of cluster telemetry, inject a "Rogue Pod" simulating a breach, and run the Isolation Forest algorithm. It will output the anomaly scores and generate a 3D visualization (`anomaly_plot.png`) proving the isolation.
