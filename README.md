# NFL-combine-project
Aim:
Can you predict rookie year performance from a metric which uses the NFL combine event results, and how does it compare to using draft position only and a metric which uses both combine results and draft position as predictors?

Description:
The performance was measured by: yards gained by passing for QB, receiving yards for WR, rushing yards gained for RB.
I used data from 2000-2015 on NFL combine results and NFL stats to find lines of best fit for performance in rookie year against draft position, combine metric (for all 6 combine events), and a new metric (which used the combine metric+draft position). This was done for WR+RB positions. Lines of best fit compared with data from years 2016-2019.
I used CSV file data from 2000-2019 on NFL combine results, rushing stats, defence stats, and 2000-2015 for passing stats (all data was taken from www.pro-football-reference.com).

The following applies to the 1st part of my code which used data from the years 2000-2015:
In my code, all players who did not have results for all 6 combine events AND/OR not drafted were removed, then the combine event stats and draft positions were added position-specific arrays. When doing this the number of remaining QB players was incredibly small, thus no further code was written for analysis of their performance (the code for filtering them and adding their stats to arrays has been kept but is commented out and CSV files have been kept in repository which are the _qbstats.csv files). 
The positions which I then analysed were WR and RB separately:
Coefficients were assigned to each combine event result, for example: metric=coeff1*[40yd time]+coeff2*[vertical]+...
Using a gradient descent algorithm coefficients and y-intercept (in the code this is the first entry of k0,k1,k2,k3 arrays) were found which would minimise R^2 value of the fitted line, thus finding the line of best fit. This was done for a metric which only used combine results, but also a new metric was created which used both combine results and draft psoition.
Using the curve_fit function from the scipy.optimize library, the line of best fit for performance against draft position was found for both positions.
R^2 values were calculated for every line of best fit.
All figures with the scatters and lines of best fit are shown at the end of my code.

The following applies to the 2nd part of my code which used data from the years 2016-2019:
All players who did not have results for all 6 combine events AND/OR not drafted were removed, then the combine event stats and draft positions were added position-specific arrays. This was done for WR and RB positions.
I plotted the lines of best fit (for 2000-2015) on top of scatters of performance against draft position, combine metric, and new metric for data from the years 2016-2019.
Then, R^2 values were found for the lines of best fit (for 2000-2015).
All figures with the scatters and lines of best fit are shown at the end of my code.

Results+Conclusion:
For the years 2000-2015:
The R^2 values for the combine metric were found to be around 0.013 and 0.016 for WR and RB positions, respectively. Thus, a linear model does not fit to predict rookie year performance from metric which uses NFL combine results. Interestingly, R2 values were greater for using draft position as a predictor and using the new metric. 
For WR, the R^2 value was slightly higher for the new metric (around 0.224) than the draft position (around 0.221). For RB, it was the other case and the new metric R2 value (0.279) was slightly lower than the draft position R2 value (0.287).
For the years 2016-2019:
This is where we can see how well the lines of best fit (for 2000-2015) predict rookie year performance when the data is not data that the lines of best fit were taken from.
For WR: 
The R^2 values are all lower, with the metric one being negative (i.e. a horizontal line at the mean would be a better prediction for performance). For draft position the R^2 value is around 0.228 and for the new metric it is around 0.222.
For RB:
The R^2 values are actually higher for the draft position and new metric. For the metric the R^2 value is again negative. The R^2 values for the draft position and new metric are approximately 0.408 and 0.433.

Overall, it seems that draft position, and new metric are better predictors of rookie year performance than a metric for NFL combine event results. It is inconclusive whether using the new metric which incorporates both combine event results and draft position improves predictions as R^2 values were higher than draft position as a predic for RB and lower for WR when using the new metric
