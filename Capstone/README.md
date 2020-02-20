# Coursera_Capstone
This project was completed to satisfy the final project IBM's data science professional certificate on coursera.

Project Overview: Extract and clean data from various online sources in order to find comparable neighborhoods between the two cities based on nearby venue preferences. The foursquare API along with kmeans clustering were used to extract and evaluate venue data. This information will serve a figurative stakeholder who owns a business in New York and is interested in opening up a second location in a similar neighborhood in Toronto.



Table of Contents: 
-----------------
1. Description & Discussion of the Background
- We are gathering market research information on neighborhoods in Toronto and New York City in order to determine clusters of similar neighborhoods within the individual cities themselves and between the two cities. We will determine how alike the various neighborhoods are using an unsupervised machine learning algorithm called k-means clustering. This information will serve a figurative stakeholder who owns a business in New York and is interested in opening up a second location in a similar neighborhood in Toronto.

2. Data Used: 
- Wikipedia was used to extract the list of postal codes, neighborhoods, and boroughs in Toronto. Geospatial data was pulled from http://cocl.us/Geospatial_data to pair the latitude and longitude of each neighborhood.
- The neighborhood and borough information for New York was taken from the file "newyork_data.json", provided in the coursera class.
- The foursquare API was used to access venue data for all of the neighborhoods in Toronto and New York.

3. Methodology / Data
- The neighborhood, latitude, and longitude were collected from wikipedia and a given json file for Toronto and New York City respectively. The data was cleaned before heading into the next step. From there the foursquare API was utilized to combine the top ten venues for each neighborhood. Next, the Kmeans Elbow Method was used to determine the optimum number of clusters, which was 3. Clustering was then performed on the combined dataframe of Toronto and New York City neighborhoods to evaluate similar neighborhoods based on nearby Venues. 
- The data presented in the File illustrates the cluster of neighborhoods color coded on a map of both New York City and Toronto. Then each cluster is presented in a table to better see the similarities within each cluster. 

4. Conclusion
- The purpose of this project was to compare similar neighborhoods as one piece of a market research team. For an individual who does business in New York City and is looking to expand to Tornto, we can yield insightful information as to the flavor of each neighborhood based on its popular venues. 
