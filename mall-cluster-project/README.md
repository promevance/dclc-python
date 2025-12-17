# 🛍️ Mall Customer Segmentation using K-Means Clustering

## Project Overview

This project applies **K-Means clustering** to analyze customer behavior data from a shopping mall. The goal was to segment customers based on **age**, **annual income**, and **spending score**, and use the resulting clusters to generate actionable marketing insights for the business.

The dataset contains information on **200 customers**, and the analysis was carried out using **Python**, **Jupyter Notebook**, **pandas**, **seaborn**, and **scikit-learn**. By grouping customers with similar characteristics, the project helps identify high-value customer segments and informs targeted marketing strategies.

---

## Problem Statement

The mall management team wanted to better understand their customer base in order to:

* Identify high-value customers
* Optimize marketing spend
* Design targeted campaigns for different customer segments
* Enable further customer-level analysis by the marketing team

Rather than treating all customers the same, clustering allows the business to make **data-driven decisions** based on actual purchasing behavior.

---

## Dataset Description

The original dataset includes the following key variables:

* **Age** – Customer age
* **Annual Income (k$)** – Annual income in thousands of dollars
* **Spending Score (1–100)** – A metric representing customer spending behavior at the mall

The dataset was provided as a CSV file and contained **200 customer records**.

---

## Methodology

1. **Data Exploration & Cleaning**

   * Loaded and inspected the dataset
   * Checked for missing values and data consistency

2. **Feature Selection**

   * Selected Age, Annual Income, and Spending Score as clustering features

3. **Determining Optimal Number of Clusters**

   * Used the **Elbow Method** to identify the optimal number of clusters
   * Visualized within-cluster sum of squares to guide cluster selection

4. **K-Means Clustering**

   * Applied K-Means using scikit-learn
   * Assigned cluster labels to each customer

5. **Visualization**

   * Plotted customer clusters with centroids
   * Clearly visualized how customers were grouped

---

## Key Findings & Insights

### Cluster 1: Prime Customers

* High annual income
* High spending score
* Predominantly aged **31–35**
* Represents the most valuable customer segment

**Recommendation:**
Marketing efforts should prioritize this group with premium offerings, loyalty programs, and exclusive promotions.

---

### Cluster 2: High Spenders with Moderate Income

* Moderate income levels
* Relatively high spending score
* Customers are selective but intentional with purchases

**Recommendation:**
Targeted campaigns highlighting trending products, promotions, and value-for-money offers would be effective for this group.

---

### Other Clusters

* Lower income and/or lower spending behavior
* Less immediate revenue potential

**Recommendation:**
Maintain general brand awareness and social media marketing, without heavy targeted investment.

---

## Deliverables

This project produced the following outputs:

* 📊 **Elbow Method & Cluster Visualization**

  * Shows cluster separation and centroids
  * Helps stakeholders visually understand customer segments

  🔗 View image:
  [https://github.com/promevance/dclc-python/blob/my-assignment/mall-cluster-project/clusters_with_centroids.png](https://github.com/promevance/dclc-python/blob/my-assignment/mall-cluster-project/clusters_with_centroids.png)

* 📁 **Clustered Dataset**

  * Original customer data with an added `Cluster` column
  * Enables customer-level drill-down for marketing analysis

  🔗 Download CSV:
  [https://github.com/promevance/dclc-python/blob/my-assignment/mall-cluster-project/mall_customers_clustered.csv](https://github.com/promevance/dclc-python/blob/my-assignment/mall-cluster-project/mall_customers_clustered.csv)

* 📓 **Jupyter Notebook**

  * Complete analysis workflow
  * Code, visualizations, and explanations

  🔗 View notebook:
  [https://github.com/promevance/dclc-python/blob/my-assignment/mall-cluster-project/mall-cluster.ipynb](https://github.com/promevance/dclc-python/blob/my-assignment/mall-cluster-project/mall-cluster.ipynb)

---

## Tools & Technologies

* Python
* Jupyter Notebook
* pandas
* seaborn
* scikit-learn
* matplotlib

---

## How This Can Be Used

* Marketing teams can directly use the clustered dataset for targeted campaigns
* Business stakeholders can reference cluster insights for strategy planning
* Data teams can extend the analysis with additional features or models

---

## Author

**Evan Promise Chukwubueze**
Data Analysis & Machine Learning Project
GitHub: [https://github.com/promevance](https://github.com/promevance)
