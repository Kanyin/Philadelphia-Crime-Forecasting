## I didn't do the crime, but I can still do the time...series! 
### Time Series Visualization and Forecasting
Did you know that there is a high chance of crime on any given Wednesday, in June, in Philly? 
<br>
I myself had no clue until I decided to look into things like this after my poor neighbors packages kept getting stolen. In doing some research, it was no surpise to see that theft was a top crime all over Philly. However, some of the other numbers were surprising as well. 2024 was one for the books. Philly in particular experienced some of the lowest homicide levels ever.  Please take a look.
<br><br><br>

###### Crime Forecasting with SARIMA
I looked at the overall crime rate in Philadelphia and using a SARIMA model, helped to predict crime rates in 2025.There's a very clear pattern that occurs every 7 days, or week,  which was later confirmed in plotting the average crime that occurs in a week. 
<br><br>
![image](https://github.com/user-attachments/assets/9d5abb18-3548-4a26-ad20-8796d52f6082)

<br><br><br>
Then were able to use the 2024 data to forecast 2025, and compare to 2025 so far. 
![image](https://github.com/user-attachments/assets/bc38f410-7491-4877-a927-2b7c715cc300)

<br><br>
###### Heatmaps are oldschool but still cool
Using Folium, here is a heatmap over time. This time last year, I bet there was much theft in Rittenhouse, the richest neighborhood in the city. Not much of a shocker. But still interesting to visualize. Please keep in mind that this is only the REPORTED crime. Imagine the amount of unrepported crime!

![image](https://github.com/user-attachments/assets/a548055e-5213-4ab9-8296-02643a69a160)

