# informed-and-uninformed-search-in-python
uninformed search - uniform cost search 
infromed search - a* search 


below are the output of my code in my cmd. 

1. Uninformed search :- 
--------------------------------------------------------------------------------------
	
	>python find_route.py input1.txt Bremen Berlin
	
	output:-
	node expanded :16
	node generated :25
	max node in memory :11
	distance:407.0
	route:
	Bremen  to      Hamburg,116 km
	Hamburg to      Berlin,291 km


	
	


2. Informed search :-
--------------------------------------------------------------------------------------
   
   >python find_route.py input1.txt Berlin Kassel h_kassel.txt
   
	Output :

	node expanded :7
	node generated :15
	max node in memory :11
	distance:479.0
	route:
	Berlin  to      Magdeburg,166 km
	Magdeburg       to      Hannover,148 km
	Hannover        to      Kassel,165 km

