# HeartRate-and-StepCount Analysis

## Description

This project is part of the **Sabanci University DSA210 Introduction to Data Science Course Fall 2024-2025 Term Project**. It involves an in-depth analysis of my personal health data, specifically focusing on heart rate and step count metrics collected via my Apple Watch and iPhone.

The objective is to uncover patterns in daily activities, resting heart rate trends, and the correlation between physical activity and heart rate. By doing so, I aim to gain actionable insights into my lifestyle and physical health.

---

## Table of Contents

- [Motivation](#motivation)
- [Tools](#tools)
- [Data Source](#data-source)
- [Data Processing](#data-processing)
- [Visualizations](#visualizations)
- [Findings](#findings)
- [Limitations](#limitations)
- [Future Work](#future-work)

---

## Motivation

The key motivations behind this project include:

- Understanding activity levels and resting heart rate trends.
- Exploring how physical activity affects cardiovascular health.
- Gaining actionable insights for improving daily routines and lifestyle habits.

---

## Tools

The following tools and libraries were used in the project:

- **Google Colab**: For cloud-based analysis and coding.
- **Pandas**: For data cleaning, processing, and aggregation.
- **Matplotlib**: For creating detailed visualizations.
- **NumPy**: For numerical calculations and handling arrays.
- **Math**: For numerical operations, such as rounding step counts and handling averages.
- **Regular Expressions (re)**: For parsing raw RTF data and extracting meaningful content.
- **Datetime**: For managing and manipulating time-series data within Pandas.

---

## Data Source

The dataset consists of:

1. **Heart Rate Data**: Captured exclusively from the Apple Watch at regular intervals.
2. **Step Count Data**: Aggregated step counts collected from both the Apple Watch and iPhone, requiring careful handling to avoid duplication.
3. **Timestamps**: Used for synchronization and trend analysis.

### Raw Data Format and Challenges:
- The data was exported from the **Apple Health App** in RTF format, which is not user-friendly.
- Heart rate data is device-specific (Apple Watch), whereas step count data is recorded from both the Apple Watch and iPhone. These dual sources introduce complexity in ensuring no duplication while aggregating data.
- Recording intervals are inconsistent across devices, requiring conversion to consistent 10-minute periods for analysis.

All preprocessed data can be found in the `data/` folder.

---

## Data Processing

Key steps in data processing:

1. **Parsing Raw Data**:
   - Developed Python scripts to parse RTF files and convert them into structured CSV files for analysis.
   - Timestamps were standardized to ensure consistent time-based operations.

2. **Handling Missing Data**:
   - For heart rates: Missing values were interpolated using averages of the last 5, 4, 3, or 2 values to maintain meaningful trends.
   - For step counts: Gaps were filled as zero, ensuring consistency without artificially inflating activity levels.

3. **Avoiding Duplication**:
   - Step count data from both the Apple Watch and iPhone was aggregated without duplication by aligning recording periods and redistributing overlapping data.

4. **Time Aggregation**:
   - Both datasets were synchronized into 10-minute intervals for accurate correlation analysis.

5. **Filtering Static Data**:
   - Periods with zero step counts or identical heart rates over 5 consecutive intervals were excluded to focus on dynamic data.

---

## Visualizations

### Daily Aggregated Trends
- **Heart Rate and Step Counts**: Visualized as separate daily line graphs to observe high-level trends.
- **Annotations**: Specific values highlighted for clarity.

### Time-Series Correlation
- **Step Count Intensity and Heart Rate**: Combined bar and scatter plots to showcase the interplay between physical activity and heart rate.
- **Color Mapping**: Heart rate markers were color-coded based on step intensity.

### Weekly Highlights
- Weekly trends and intra-day activity patterns were visualized for specific periods (e.g., October 4–6 and October 7–11).

---

## Findings

1. **Activity Peaks**: Higher step counts during specific periods correlated with increased heart rates.
2. **Resting Trends**: Resting heart rates indicated consistent patterns, reflecting improved fitness over time.
3. **Correlations**: Moderate correlations were identified between step intensity and heart rate metrics.

---

## Limitations

### Data Limitations
- **Battery Constraints**: Charging periods resulted in data gaps.
- **Data Aggregation**: Synchronizing step count data from two devices posed challenges in ensuring accuracy.

### Analytical Constraints
- **Personal Dataset**: Results are not generalizable to broader populations.

---

## Future Work

1. **Expand Metrics**: Include additional data like calorie burn and sleep patterns. (Not Possible to record sleep patterns since Battery of Apple Watch, our recorder has a constraint)
2. **Combine Data Sources**: Integrate phone usage and other lifestyle metrics for a holistic view. (Planned to take recordings from iPhone -> Settings -> Screen Time, but on my personal phone this settings was OFF position on October 2024)

---

## Contributions

1. **Raw Data Handling**:
   - Developed scripts to parse raw RTF data from the Apple Health app into structured CSV files.
   - Addressed challenges in synchronizing multi-device data.

2. **Exploration of Trends**:
   - Analyzed correlations between physical activity and heart rate trends over time.

3. **Visualization Techniques**:
   - Created detailed charts and graphs to highlight relationships between activity and cardiovascular health.

4. **Data Cleaning and Filtering**:
   - Enhanced the accuracy and usability of raw health data for meaningful analysis.

---
