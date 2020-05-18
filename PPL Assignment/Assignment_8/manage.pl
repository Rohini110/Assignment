:- initialization(main).
main :- write('     ****** Air System *******          ').

/*flight(from, airline, to, price, duration)*/

/*flight from *** London *** */
flight(london,air_Canada,toronto,500,360).
flight(london,iberia,barcelona,220,240).
flight(london,united,toronto,650,420).

/*flight from *** Toronto *** */
flight(toronto,air_Canada,london,500,360).
flight(toronto,united,london,650,420).
flight(toronto,air_Canada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).

/*flight from *** Barcelona *** */
flight(barcelona,iberia,london,220,240).
flight(barcelona,air_Canada,madrid,100,60).
flight(barcelona,iberia,madrid,120,65).
flight(barcelona,iberia,valencia,110,75).

/*flight from ***Madrid *** */
flight(madrid,air_Canada,toronto,900,480).
flight(madrid,united,toronto,950,540).
flight(madrid,iberia,toronto,800,480).
flight(madrid,air_Canada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,iberia,valencia,40,50).
flight(madrid,iberia,malaga,50,60).

/*flight from ***Valencia*** */
flight(valencia,iberia,barcelona,110,75).
flight(valencia,iberia,malaga,80,120).
flight(valencia,iberia,madrid,40,50).

/*flight from ***Malaga*** */
flight(malaga,iberia,madrid,50,60).
flight(malaga,iberia,valencia,80,120).

/*flight from ***Paris*** */
flight(paris,united,toulouse,35,120).

/*flight from ***Toulouse*** */
flight(toulouse,united,paris,35,120).


/************ Airppot *************/

airpot(london,75,80).
airpot(toronto,50,60).
airpot(barcelona,40,30).
airpot(madrid,75,45).
airpot(valencia,40,20).
airpot(malaga,50,30).
airpot(paris,50,60).
airpot(toulouse,40,30).

/* is there a flight from toronto to madrid? */

isflight():-
	flight(toronto,_,madrid,_,_),
	write('Yes There is a flight....').

/* A flight from city A to city B with airline C is cheap if its price is less than $400? */
ischeap(A, C, B):-
	flight(A, B, C, D, E),
	D < 400.

/* is it possible to go from toronto to madrid */

isflightpossible():-
	flight(toronto,A,madrid,C,D),
	write('yes').

/*A flight from city A to city B with airline C is preferred if it's cheap(see(b)) or it's with with air_Canada ? */

ischeap_and_air(A,B):-
	ischeap(A, B, air_Canada).




/* if there is a flight from city A to city B with united , then there is a flight from city A to city B with air_Canada? */

flightsearch(A, B):-
	flight(A,united,B,_,_),
	write("Yes.. ! There is a flight with air-line United      "),
	flight(A,air_Canada,B,_,_),
	write('Yes.. ! There is a flight with air-line Air_Canada').
