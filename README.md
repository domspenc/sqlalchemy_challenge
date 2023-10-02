<h1>SQL Alchemy Challenge</h1>
<img
        src="https://assets.editorial.aetnd.com/uploads/2009/12/gettyimages-1352563243.jpg"
        alt="Photograph of a Hawaii island"
        width="650"
      />
</br>
<h3><u>Description</u></h3>
<p>
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area.
</p>
</br>
<h3><u>Part 1: Analyse and Explore the Climate Data</u></h3>
</br>
<p>Python and SQLAlchemy (specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib) were used to do a basic climate analysis and data exploration of the climate database.</p> 
</br>
<h5>The following steps were taken to perform an analysis of precipitation at the destination:</h5> 
</br>
<p>1. Find the most recent date in the dataset.</p> 
</br>
<p>2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.</p> 
</br>
<p>3. Select only the "date" and "prcp" values.</p> 
</br>
<p>4. Load the query results into a Pandas DataFrame. Explicitly set the column names.</p> 
</br>
<p>5. Sort the DataFrame values by "date", then plot the results.</p> 
</br>
<p>6. Print the summary statistics for the precipitation data.</p>
</br>
<h5>The following steps were taken to perform an analysis of data collected by weather stations at the destination:</h5> 
</br>
<p>1. Design a query to calculate the total number of stations in the dataset.</p> 
</br>
<p>2. Design a query to find the most-active stations, then list the stations and observation counts in descending order.</p> 
</br>
<p>3. Find which station id has the greatest number of observations, then calculate the lowest, highest, and average temperatures.</p> 
</br>
<p>4. Design a query to get the previous 12 months of temperature observation (TOBS) data, then plot the results as a histogram.</p> 
</br>
<h3><u>Part 2: Design Your Climate App</u></h3>
</br>
<p>With the initial analysis complete, a Flask API was designed based on the queries from part 1.
</br>
It contains the following routes:</p> 
</br>
<p>1. Precipitation.</p> 
</br>
<p>2. Stations.</p> 
</br>
<p>3. Temperature Observation Data.</p> 
</br>
<p>4. Start Year Data.</p> 
</br>
<p>5. Start and End Year Data.</p>
</br>
<p>The app can be found in the app.py file.</p> 
</br>
<p>----------------------------------------------------------</p> 
</br>
<p>Thank you for reading!</p> 
<h3>🌈🌈🌈</h3>
</br>
<p><a>I utilised some additional resources for this project, in particular my bootcamp tutor.</a></p>
</br>
<p><a>Image sourced from History.com</a></p>