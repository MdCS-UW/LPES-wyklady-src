v 20220529 2
C 35400 51000 1 0 0 transistor-nmosfet-1.sym
{
T 35795 52495 5 10 0 0 0 0 1
slot=1
}
C 38900 52000 1 180 1 transistor-pmosfet-1.sym
{
T 39295 50505 5 10 0 0 180 6 1
slot=1
}
C 35400 49400 1 0 0 transistor-nmosfet-deppletion-1.sym
{
T 35779 50679 5 10 0 0 0 0 1
slotdef=1:G,D,S
}
C 38900 50400 1 180 1 transistor-pmosfet-deppletion-1.sym
{
T 39279 49121 5 10 0 0 180 6 1
slotdef=1:G,D,S
}
C 34300 51000 1 0 0 transistor-nmosfet-2.sym
{
T 34695 52495 5 10 0 0 0 0 1
slot=1
}
C 37800 52000 1 180 1 transistor-pmosfet-2.sym
{
T 38195 50505 5 10 0 0 180 6 1
slot=1
}
B 34000 50700 3500 1600 3 0 0 0 -1 -1 0 -1 -1 -1 -1 -1
T 35400 52400 9 10 1 0 0 0 1
N-MOSFET
T 39000 52400 9 10 1 0 0 0 1
P-MOSFET
T 33900 51000 9 10 1 0 90 0 1
wzbogacony
B 37500 49100 3500 1600 3 0 0 0 -1 -1 0 -1 -1 -1 -1 -1
B 34000 49100 3500 1600 3 0 0 0 -1 -1 0 -1 -1 -1 -1 -1
T 33900 49400 9 10 1 0 90 0 1
zubożony
C 40100 52000 1 180 1 transistor-nmos-1.sym
{
T 40479 50721 5 10 0 0 180 6 1
slotdef=1:G,D,S
}
C 36600 51000 1 0 0 transistor-pmos-1.sym
{
T 36995 52495 5 10 0 0 0 0 1
slot=1
}
B 37500 50700 3500 1600 3 0 0 0 -1 -1 0 -1 -1 -1 -1 -1
L 41400 50200 41400 49400 3 16 1 0 -1 -1
L 41400 49400 41500 49600 3 16 1 0 -1 -1
L 41400 49400 41300 49600 3 16 1 0 -1 -1
T 37500 48900 9 13 1 0 0 5 1
S = źródło    G = bramka    D = dren
T 41400 50400 9 11 1 0 90 1 1
przepływ prądu
