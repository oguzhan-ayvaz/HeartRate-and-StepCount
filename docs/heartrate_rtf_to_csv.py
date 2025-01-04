#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:10:46 2025

@author: oguzhanayvaz
"""

import pandas as pd
import re

# Clean and parse the RTF file
def parse_rtf(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Remove RTF-specific formatting
    content = re.sub(r'[{}\n\\]', '', content)  # Remove RTF characters
    content = re.sub(r'\s+', ' ', content)  # Replace multiple spaces with a single space
    return content

# Extract relevant heart rate data
def extract_heart_rate_data(content):
    # Split the cleaned content into manageable lines
    data = []
    for match in re.finditer(r'<low value="(?P<timestamp>\d{14}\+\d{4})"/>.*?<value xsi:type="PQ" value="(?P<heart_rate>\d+)" unit="count/min"/>', content):
        try:
            timestamp = match.group('timestamp')
            heart_rate = match.group('heart_rate')
            data.append({
                "timestamp": pd.to_datetime(timestamp, format='%Y%m%d%H%M%S%z'),
                "heart_rate": float(heart_rate)
            })
        except Exception as e:
            print(f"Error processing match: {match.group(0)}, Error: {e}")
    return pd.DataFrame(data)

# Main processing
rtf_file_path = 'export_heartrate_v2.rtf'  # Ensure the file is in the working directory
content = parse_rtf(rtf_file_path)  # Read and clean RTF content
heart_rate_df = extract_heart_rate_data(content)  # Extract heart rate data

# Output the results
if not heart_rate_df.empty:
    print("Extracted Data:")
    print(heart_rate_df)
    # Save to a CSV for further analysis
    heart_rate_df.to_csv('heart_rate_extracted.csv', index=False)
    print("Data saved to 'heart_rate_extracted.csv'")
else:
    print("No valid data found in the file.")