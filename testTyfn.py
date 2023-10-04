import pandas as pd
import pm4py
import matplotlib.pyplot as plt
import seaborn as sns

# Load the XES file into a DataFrame
log_path = 'data/renting_log_medium.xes'
log = pm4py.read_xes(log_path)

# Extract traces
traces = pm4py.convert_to_event_stream(log)

# Extract events from traces
events = [event for trace in traces for event in trace]

# Summary Report
print("Summary Report for Renting Process Analysis")
print("=" * 40)

# Traces Analysis
case_id_column = 'concept:name'
activity_column = 'activity'
timestamp_column = 'time:timestamp'

print("Traces Analysis:")
print(f"Case ID Column: {case_id_column}")
print(f"Activity Column: {activity_column}")
print(f"Timestamp Column: {timestamp_column}")
print("=" * 40)

# Statistics
num_cases = len(log)
variants = pm4py.get_variants(log)
num_variants = len(variants)

activity_counts = [len(trace) for trace in log]
avg_activities = sum(activity_counts) / num_cases
min_activities = min(activity_counts)
max_activities = max(activity_counts)

print("Statistics:")
print(f"Number of Cases/Traces: {num_cases}")
print(f"Number of Variants: {num_variants}")
print(f"Average Number of Activities per Case: {avg_activities:.2f}")
print(f"Minimum Number of Activities per Case: {min_activities}")
print(f"Maximum Number of Activities per Case: {max_activities}")
print("=" * 40)

# Add more sections and analysis results as needed...

# Privacy Preservation, Outliers, Missing Data, Sampling, Subset Selection, Model Discovery,
# Quality Criteria, Fuzzy Mining Analysis, Business Process Analysis, Objectives, etc.

# End of Report
print("End of Report")
