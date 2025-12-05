# COVID-19 Daily Cases Plot Report

## Introduction

This report explains the steps taken to generate a line plot showing UK
daily COVID-19 cases using Python in a Jupyter Notebook environment.

## Data Preparation

The dataset was loaded into a pandas DataFrame and sorted by date. Two
arrays, `x` for dates and `y` for daily case numbers, were extracted for
plotting.

## Plotting Process

Matplotlib was used to generate the line plot. The following key
features were applied: - `figure.figsize = (16, 6)` was set to create a
wide visual layout. - Labels were added for the x-axis (Date), y-axis
(Number of Daily Cases), and plot title. - `mplcursors` was used to
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

## Conclusion

The resulting plot provides a visual representation of COVID‑19 case
fluctuations over time, with an interactive feature that improves data
exploration.
