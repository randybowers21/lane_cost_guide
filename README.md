# Lane Cost Guide
A Tkinter app that queries google maps api to get miles and runs calculations of Cost vs money Gained.

**Features**
1. Takes up to ten inputs of citys to travel destinations.
2. Calls google api to get distances between destinations.
3. Option to change the Cost per mile.
4. Prints each "Leg" of the trip to the screen with distances.
5. Options to mark each leg loaded/empty.
	- When marked empty that leg contributes to total empty miles, as well as deadhead percent.
6. Options to add a rate per mile for each leg as well.
7. Calculate totals of the entire trip including Total Miles, Empty Miles, Deadhead, Total Cost, Total Revenue, Difference, as well as the Total Rate Per Mile
  
##  What I've Learned
A go at Tkinter and CustomTkinter and first time with GUIs in python.

This will help my company run a quick lane analysis for lanes that we are offered. It speeds things up from our old Excel ways of doing it. Manually typing in city's and states, and googling distance for each individual leg, as well as copy pasting formulas to check costs. 

I used CustomTkinter for the first time and just like my other front end stuff. I can make it work but I struggle with making it look good. It looks much better than regular Tkinter but still could use some work.

I initially connected to google maps manually and was making my requests that way but I ran in to some hang ups with specific request types .I then found google maps on pip. Connecting to google maps this way was easier for me and worked great.

##  Technologies
-  [GoogleMaps](https://pypi.org/project/googlemaps/)
-  [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)