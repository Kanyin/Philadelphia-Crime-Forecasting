## Crime Forecasting with SARIMA
Did you know that there is a high chance of crime on a day like this, a Wednesday, in June in Philly? A beautiful ordinary day like this may be high in theft. Well, I decided to look into things like this by pure curiosity inspired by my poor neighbors. In 2024, my then next-door neighbors consistently got their packages stolen while our own house was unscathed. In doing some research, it was no surpise to see that theft was a top crime all over Philly. However, some of the other numbers were surprising as well. 2024 was one for the books. Philly in particular experienced some of the lowest homicide levels ever.  Please take a look.

![image](https://github.com/user-attachments/assets/ec4bb21b-7b92-46d9-a62a-1dfc1514720b)


###### Crime Forecasting with SARIMA
I looked at the overall crime rate in Philadelphia and using a SARIMA model, helped to predict crime rates in 2025.

There's a very clear pattern that occurs every 7 days, or week,  which was later confirmed in plotting the average crime that occurs in a week. 

![image](https://github.com/user-attachments/assets/9d5abb18-3548-4a26-ad20-8796d52f6082)


Then were able to use the 2024 data to forecast 2025, and compare to 2025 so far. 
![image](https://github.com/user-attachments/assets/bc38f410-7491-4877-a927-2b7c715cc300)


###### Heatmaps are oldschool but still cool
Using Folium, here is a heatmap over time. This time last year, I bet there was much theft in Rittenhouse, the richest neighborhood in the city. Not much of a shocker. But still interesting to visualize. Please keep in mind that this is only the REPORTED crime. Imagine the amount of unrepported crime!

![image](https://github.com/user-attachments/assets/a548055e-5213-4ab9-8296-02643a69a160)

