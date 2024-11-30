# HeartRate-and-StepCount

## Description

This project is part of the **Sabanci University DSA210 Introduction to Data Science Course Fall 2024-2025 Term Project**. It analyzes my personal health data focusing on heart rate and step count collected through my Apple Watch.

The analysis aims to uncover patterns in my daily activities, resting heart rate trends, and correlations between physical activity and heart rate. By examining this data, I hope to gain deeper insights into my physical health and lifestyle habits.

---

## Table of Contents

- [Motivation](#motivation)
- [Tools](#tools)
- [Data Source](#data-source)
- [Data Processing](#data-processing)
- [Data Visualizations](#data-visualizations)
- [Data Analysis](#data-analysis)
  - [Daily Trends](#daily-trends)
  - [Heart Rate Variability](#heart-rate-variability)
  - [Correlation Studies](#correlation-studies)
- [Findings](#findings)
- [Limitations](#limitations)
- [Future Work](#future-work)

---

## Motivation

The motivation behind this project is to better understand my physical health and activity patterns by analyzing heart rate and step count data. Specifically, I aim to:

- Identify trends in my activity levels and resting heart rate over time.
- Explore correlations between my physical activity (steps) and heart rate.
- Investigate how my habits (exercise, rest, etc.) impact my overall health metrics.

By analyzing this data, I hope to gain actionable insights into my daily routines and potential areas for improvement in my lifestyle.

---

## Tools

The following tools and libraries were used in the project:

- **Google Colab**: For coding, analysis, and documentation in a cloud-based environment.
- **Pandas**: For data cleaning and processing.
- **Matplotlib**: For data visualization.
- **NumPy**: For numerical computations.
- **Scipy**: For statistical analysis.

---

## Data Source

The data was collected using my Apple Watch and exported from the Apple Health app. Since the raw data format from Apple Health is not user-friendly, I used third-party apps to convert it into a more manageable format for analysis. The processed data includes:

- **Heart Rate Data**: Continuous measurements of heart rate at various intervals throughout the day.
- **Step Count Data**: Aggregated daily total steps.
- **Timestamps**: Datetime information for trend analysis and correlation studies.

All preprocessed data can be found in the `data/` folder.

---

## Data Processing

The raw data required significant cleaning and preprocessing. Steps included:

1. **Formatting Timestamps**: Standardizing timestamps for analysis.
2. **Handling Missing Values**: Filling or removing gaps caused by device limitations or battery constraints.
3. **Normalization**: Preparing the data for visualization and statistical analysis.

Details of these processes are documented in the `data_process.ipynb` file.

---

## Data Visualizations

Data visualization was performed using Matplotlib. These visualizations provided valuable insights into trends and patterns in the data. Visualizations include:

- Daily and weekly activity trends.
- Resting heart rate trends.
- Correlation heatmaps for heart rate and step counts.

Static versions of these visualizations can be found in the `plots/` folder.

---

## Data Analysis

### Daily Trends
Analyzed daily variations in step counts and heart rates to identify patterns in my activity levels and rest periods.

### Heart Rate Variability
Explored fluctuations in heart rate to understand the effects of different activities and rest periods on my cardiovascular health.

### Correlation Studies
Investigated the relationship between heart rate and step counts to determine how physical activity affects my heart rate metrics.

---

## Findings

Key findings from the analysis include:

- Clear daily and weekly patterns in activity levels, with peak activity during certain hours.
- Moderate correlation between step counts and heart rate during active hours.
- Resting heart rate trends indicate consistent improvement over time, potentially reflecting better fitness levels.

---

## Limitations

### Data Source Limitations
- **Battery Constraints**: The Apple Watch’s battery life limited data collection between **10 PM and 8 AM**, leading to gaps in nighttime heart rate and step data.
- **Third-Party Apps**: Data conversion using third-party apps may have introduced minor inconsistencies.

### Personal Limitations
- **Subjectivity**: As the dataset is personal, generalizability is limited.
- **Privacy Concerns**: To protect privacy, certain sensitive data points were omitted from the analysis.

---

## Future Work

- **Incorporate Additional Metrics**: Expand the dataset to include **calorie burn** for a more comprehensive analysis of physical activity.
- **Explore Phone Usage Data**: Investigate correlations between screen usage time (collected from phone settings) and activity levels. Since prolonged phone usage may correspond to sedentary periods, it could provide additional insights. However, this step may be excluded if extracting screen usage data proves to be too challenging.
- **Fill Data Gaps**: Explore alternative methods to collect continuous data during charging periods.

---
