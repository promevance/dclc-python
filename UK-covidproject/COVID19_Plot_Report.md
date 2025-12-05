# COVID-19 Daily Cases Plot Report

## Introduction

This report explains the steps I took to generate a line plot showing UK
daily COVID-19 cases using Python in a Jupyter Notebook environment.

## Environment Preparation

I wanted to use VScode for this, as previously I had been using 
Jupyter Notebook from web browser (through Anaconda). So I had to create
the notebook on VScode and linked it to the appropriate kernel. Then 
I installed the necessary libraries needed while calling the modules.

## Data Preparation

I downloaded the dataset and loaded it into a pandas DataFrame 
which I sorted by date. I extracted two arrays, `x` for dates 
and `y` for daily case numbers, to make plotting easy.

## Plotting Process

I used Matplotlib to generate the line plot. I applied the following 
key features: - `figure.figsize = (16, 6)` to create a
wide visual layout. - Labels for the x-axis (Date), y-axis
(Number of Daily Cases), and plot title. - `mplcursors` to
enable interactive hovering, allowing users to see the exact date and
number of cases when moving the cursor over the plot.

## Code Used

``` python
%matplotlib inline
import matplotlib.pyplot as mplt
import mplcursors

mplt.plot(x, y)
mplt.xlabel('Date')
mplt.ylabel('Number of Daily Cases')
mplt.title('UK Daily COVID-19 Cases Over Time')

mplt.rcParams["figure.figsize"] = (16, 6)

cursor = mplcursors.cursor(hover=True)

mplt.show()
```

## Resulting Plot

Here is the resulting plot below

![Chart Showing Visualisation for the Project]([UK-covidproject/uk-covidproject visualisation.png](https://github.com/promevance/dclc-python/blob/my-assignment/UK-covidproject/uk-covidproject%20visualisation.png) "UK Covid-19 Data Visualisation")

## Conclusion

The resulting plot provides a visual representation of COVID‑19 case
fluctuations over time, with an interactive feature that improves data
exploration.
