# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'mostek, wzmacniacze, ...' },
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/mostek_H_switche.sch", negate=True)],
		],
		'text' : [
			'Kolejną rzeczą związaną poniekąd z tranzystorami, <m> ale tak naprawdę nawet ze zwykłymi przełącznikami, <m> czy też przekaźnikami jest tak zwany mostek H. <m>'
			'Jest to układ czterech przełączników (którymi często są tranzystory), <m> którego obciążenie podłączone jest w taki dziwny sposób, <m> jaki widać na ekranie.  <m>'
			'Celem układu jest możliwość zmiany polaryzacji zasilania obciążenia. <m>'
			'Jeżeli załączymy S1 i S4 <m> to biegun dodatni mamy po lewej stronie, a biegun ujemny po prawej. <m>'
			'Jeżeli zamiast tego załączymy S2 i S3 <m> to biegun dodatni mamy po prawej, a ujemny po lewej. <m>'
			'Układ może być wykorzystywany na przykład w sterowaniu silników <m> których kierunek obrotu zależy od polaryzacji, <m> czy też innych tego typu układów zależnych od polaryzacji. <m>'
			
			'Pojedynczą taką gałąź nazywamy pół mostkiem. <m>'
			'Może on być wykorzystywany jako samodzielny element do załączania <m> jakiegoś odbiornika pod biegun dodatni bądź biegun ujemny. <m>'
			'Przykładem odbiornika wymagającego takiego załączania <m> jest bramka tranzystora mosfet. <m>'
			
			'Niekiedy do sterowania dużym tranzystorem mosfet, mającym też sporą pojemność, którą trzeba przeładować przy przełączaniu, używany jest półmostek <m>'
				'zbudowany z mniejszych tranzystorów mosfet, które mają mniejszą pojemność i szybciej się przełączają. <m>'
			
			'Mostki, czy też półmostki możemy budować zarówno <m> z tranzystorów <bipolarnych>[bi-polarnych] jak i polowych. <m>'
			'Budując mostek z tranzystorów należy zastosować oczywiście odpowiednie ich typy <m> – jako S1 i S3 używamy tranzystorów typu P czyli PNP lub P-MOSFET, <m> a jako S2 i S4 tranzystorów NPN lub N-MOSFET. <m>'
		]
	},
	{
		'image': [
			[0.0, ""],
			["opamp", eduMovie.circuitjs("opamp", 0, 1)],
			["opamp_run + 4", eduMovie.circuitjs("opamp", 4, 10, [("setSlider", 1, 0.3), ("wait", 0.8), ("setSlider", 1, 0.48), ("wait", 1.2), ("setSlider", 1, 0.52), ("wait", 0.8), ("setSlider", 1, 0.7)])],
			["opamp_loop", eduMovie.circuitjs("opamp_loop", 4, 6, preActions=[("setSlider", 1, 0.25)], actions=[
				("setSlider", 1, 0.5), ("wait", 1.3), ("setSlider", 1, 0.75), ("wait", 1.3), ("setSlider", 1, 0.25),
				("setSlider", 2, 0.2), ("wait", 1.3), ("setSlider", 1, 0.3), ("wait", 1.3), ("setSlider", 1, 0.405)
			])],
		],
		'text' : [
			'Kończąc temat tranzystorów należy wspomnieć jeszcze o dwóch zagadnieniach. <m>'
			'Pierwszym z nich są wzmacniacze. <m>'
			'Jak już pokazywaliśmy sam tranzystor może być użyty jako wzmacniacz, <m> chociażby na zasadzie wzmacniania prądu beta razy. <m>'
			'Istnieją też bardziej złożone układy wzmacniaczy <m> opartych o pojedynczy tranzystor, eliminujące problem bety, <m> w których wzmocnienie określane jest przez wartości rezystorów. <m>'
			
			'Często jednak do wzmacniania sygnałów używane są <m> dedykowane układy nazywane wzmacniaczem operacyjnym. <mark name="opamp" />'
			'Układ taki cechuje się bardzo dużym wzmocnieniem <m> różnicy napięcia pomiędzy swoimi dwoma wejściami. <m>'
			
			'Wzmacniacz operacyjny posiada wejście oznaczone jako plus <m> i wejście oznaczone jako minus. <mark name="opamp_run" />'
			'Wzmocnienie różnicy napięć pomiędzy wejściem plus a minus, <m> jest tak duże że już niewiele wyższy potencjał na wejściu plus niż minus, <m>'
				'powoduje pojawienie się na wyjściu napięcia <m> bliskiego dodatniemu napięciu zasilania. <m>'
			'A niewiele niższy potencjał na wejściu plus niż na wejściu minus <m> skutkuje pojawieniem się na wyjściu napięcia <m> bliskiego ujemnemu napięciu zasilania. <m>'
			'To jak bliskie będą te napięcia wyjściowe poziomom napięć zasilania <m> jest cechą danego układu i podane jest w jego dokumentacji. <mark name="opamp_loop" />'
			
			'Aby poradzić sobie z tak dużym wzmocnieniem stosuje się sprzężenie zwrotne. <m>'
			'Czyli na przykład w układzie wzmacniacza nieodwracalnego używamy dzielnika, <m> właśnie w roli podziału proporcjonalnego jakiegoś napięcia.  <m>'
			'W ten sposób na wejście minus wzmacniacza możemy podać napięcie wyjściowe <m> podzielone w takim stosunku żeby po uwzględnieniu wzmocnienia <m> było równe napięciu wejściowemu. <m>'
			
			'Jeżeli wzrośnie napięcie wejściowe (podawane na wejście plus), <m> to dopóki nie wzrośnie odpowiednio napięcie wyjściowe, <m> napięcie na wejściu minus jest mniejsze od napięcia podawanego na wejście plus. <m>'
			'W efekcie czego rośnie napięcie wyjściowe, <m> aż do momentu gdy napięcie podawane na wejście minus <m> będzie równe napięciu podawanemu na wejście plus. <m>'
			
			'Taka jest koncepcja działania wzmacniacza operacyjnego, <m> o którym niestety raczej też więcej na tym kursie nie porozmawiamy. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("triak.sch", negate=True)],
		],
		'text' : [
			'Drugim z tematów na zakończenie tranzystorów <m> są elementy do przełączania w obwodach prądu przemiennego. <m>'
			'Ponieważ tranzystory zarówno <bipolarne>[bi-polarne], jak i mosfety działają dobrze jako <m> przełączniki prądu stałego, ale nie nadają się do prądu przemiennego, <m>'
				'gdyż w każdym wypadku zakładamy że polaryzacja czegoś jest tam większa <m> od polaryzacji czegoś innego, a w prądzie przemiennym się to zmienia. <m>'
			'W takich układach do przełączania wykorzystywane są triaki, <m> które można powiedzieć że są odpowiednikiem tranzystora dla prądu przemiennego. <m>'
			'Jest to element który możemy wprowadzić w stan przewodzenia <m> podając mu odpowiedni sygnał i po załączeniu będzie on przewodził <m> do momentu aż z innych powodów ustanie przepływ prądu przez niego. <m>'
			"W obwodach prądu przemiennego wykres wartości prądu przechodzi przez zero, <m> więc triak bez podanego sygnału <wyzwalającego>[wyzwalają'cego] wyłącza się w zerze <m> i cecha ta nie stanowi problemu. <m>"
			'Natomiast jest to powodem dla którego triaki rzadko są stosowane <m> w prądzie stałym – potrzebny byłby osobny układ wyłączający. <m>'
			'Oczywiście zarówno dla prądu stałego, jak i przemiennego możemy też <m> używać przełączników mechanicznych, takich jak na przykład przekaźniki. <m>'
		]
	},
]
