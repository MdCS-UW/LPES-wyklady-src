v 20130925 2
C 30900 52500 1 0 0 transistor-npn-1.sym
{
T 31650 52750 5 10 1 1 180 6 1
refdes=NPN
}
C 29800 52900 1 0 0 resistor-2.sym
{
T 30100 53200 5 10 1 1 0 0 1
refdes=Rb
}
N 30700 53000 30900 53000 4
C 31400 52000 1 0 0 net-gnd-1.sym
N 31500 52500 31500 52300 4
C 31400 54600 1 270 0 resistor-2.sym
{
T 31700 54400 5 10 1 1 270 0 1
refdes=R load
}
N 31500 53700 31500 53500 4
C 31400 55500 1 270 0 terminal-end_line.sym
{
T 31525 55250 5 10 1 1 0 3 1
refdes=V zasilania
T 32400 55190 5 10 0 0 270 0 1
footprint=CONNECTOR 1 1
}
N 31500 54800 31500 54600 4
C 29400 53800 1 270 0 terminal-end_line.sym
{
T 29525 53550 5 10 1 1 0 3 1
refdes=V ster
T 30400 53490 5 10 0 0 270 0 1
footprint=CONNECTOR 1 1
}
N 29500 53100 29500 53000 4
N 29500 53000 29800 53000 4
C 33300 54000 1 0 0 resistor-2.sym
{
T 33600 54300 5 10 1 1 0 0 1
refdes=Rb
}
N 34200 54100 34400 54100 4
C 34900 52000 1 0 0 net-gnd-1.sym
N 35000 52500 35000 52300 4
C 34900 53400 1 270 0 resistor-2.sym
{
T 35200 53200 5 10 1 1 270 0 1
refdes=R load
}
C 34900 55500 1 270 0 terminal-end_line.sym
{
T 35900 55190 5 10 0 0 270 0 1
footprint=CONNECTOR 1 1
T 35025 55250 5 10 1 1 0 3 1
refdes=V zasilania
}
C 32900 54900 1 270 0 terminal-end_line.sym
{
T 33900 54590 5 10 0 0 270 0 1
footprint=CONNECTOR 1 1
T 33025 54650 5 10 1 1 0 3 1
refdes=V ster
}
N 33000 54200 33000 54100 4
N 33000 54100 33300 54100 4
C 34400 54600 1 180 1 transistor-pnp-1.sym
{
T 35150 53850 5 10 1 1 180 6 1
refdes=PNP
}
N 35000 54800 35000 54600 4
N 35000 53600 35000 53400 4
T 32500 51600 9 13 1 0 0 5 5
prąd bazy = Ib = V ster / Rb 	prąd kolektora = Ic = β · Ib

spadek napięcia na (przewodzącym) tranzystorze =
	= max( V zasilania - R load · Ic , 0.2V )
	= max( V zasilania - R load · β · Vster / Rb , 0.2V )
