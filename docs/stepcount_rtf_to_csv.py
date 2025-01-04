#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:18:55 2025

@author: oguzhanayvaz
"""

import pandas as pd
import re
import math

# Load the RTF file content
file_path = 'export_stepcount.rtf'

# Extract relevant lines from the RTF
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Regular expression to extract records
record_pattern = re.compile(r'<Record.*?type="HKQuantityTypeIdentifierStepCount".*?startDate="(.*?)".*?endDate="(.*?)".*?value="(.*?)"/>')

# Parse the RTF content to extract step count data
data = []
for match in record_pattern.finditer(content):
    start_date, end_date, value = match.groups()
    try:
        step_value = math.ceil(float(value))  # Parse as float and round up
        data.append({
            'startDate': pd.to_datetime(start_date),
            'endDate': pd.to_datetime(end_date),
            'value': step_value
        })
    except ValueError:
        print(f"Skipping invalid value: {value}")

print(f"Extracted {len(data)} records from the RTF file.")

# Create a DataFrame from the parsed data
step_count_df = pd.DataFrame(data)

# Remove timezone information to make timestamps timezone-naive
step_count_df['startDate'] = step_count_df['startDate'].dt.tz_localize(None)
step_count_df['endDate'] = step_count_df['endDate'].dt.tz_localize(None)

# Filter data for October 2024
step_count_df = step_count_df[
    (step_count_df['startDate'] >= '2024-10-01') & (step_count_df['startDate'] < '2024-11-01')
]

# Generate all 10-minute periods for October 2024
all_periods = pd.date_range(start='2024-10-01 00:00:00', end='2024-10-31 23:50:00', freq='10min')

# Create an empty DataFrame for aggregation
step_count_agg = pd.DataFrame({'period': all_periods, 'total_steps': 0})

# Distribute step counts to appropriate intervals without duplication
for _, row in step_count_df.iterrows():
    start = row['startDate']
    end = row['endDate']
    value = row['value']

    # Find overlapping 10-minute intervals
    overlapping_periods = all_periods[(all_periods >= start) & (all_periods < end + pd.Timedelta(minutes=10))]

    if not overlapping_periods.empty:
        for period in overlapping_periods:
            step_count_agg.loc[step_count_agg['period'] == period, 'total_steps'] += value

# Save the processed data to a CSV file
output_file_path = 'step_count_extracted_no_fill.csv'
step_count_agg.to_csv(output_file_path, index=False)

print(f"Processed step count data for October saved to '{output_file_path}'")