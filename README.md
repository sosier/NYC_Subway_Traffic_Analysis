# NYC Subway Traffic Analysis

###Data:  
 - [NYC MTA Turnstile Data](http://web.mta.info/developers/turnstile.html)  
 - [Tech Startups Heatmap](http://www.1776.vc/reports/innovation-that-matters/)  
 - [Women Tech Startups](https://www.cbinsights.com)  
 - [Average Income by Manhattan ZIP code](http://zipatlas.com/us/ny/new-york/zip-code-comparison/average-income-per-person.htm)  

###Technologies:  
 - Python  
 - Pandas  
 - UNIX  
 - Github  
 - MATLAB  
 - Google Fusion Tables  
 - Excel  
 - Powerpoint  

###Methodolgy:  
 1. Scrape, clean, and roll up MTA turnstile data to the station level  
 2. Aggregate data over all stations, and determine optimal days of the week for street team deployment  
 3. Looking at just target days of the week, determine optimal time of day  
 4. Looking at just optimal time and days of week, determine top stations by volume and plot on map  
 5. Layer in the density of tech startups and plot  
 6. Layer in neighborhood affluence (average income) and plot  
 7. Determine a final "score" for each station by combining the three factors (pure station traffic volume, density of tech startups, and neighborhood affuence) using a weight for each based its relative importance  
 8. Rank the stations by overall "score"
