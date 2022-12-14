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
	{ 'title': [ "#09.2", "Zatrzaski,", "przerzutniki", "i rejestry" ] },
	
	{ 'comment': 'rejestry - rs, zatrzask, przerzutnik' },
	{
		'image': [
			[0.0, ""],
			["rs", eduMovie.circuitjs("rs", 0, 1)],
			["rs_show", eduMovie.circuitjs("rs", 2, 30, [
				("longClick", 350, 180, 2), ("wait", 1), ("longClick", 350, 180, 1), ("wait", 1),
				("longClick", 350, 420, 2), ("wait", 1), ("longClick", 350, 420, 1), ("wait", 1),
				("longClick", 350, 180, 1), ("wait", 1), ("longClick", 350, 420, 1), ("wait", 1), ("longClick", 350, 180, 1)
			])],
		],
		'text' : [
			'Bramki logiczne, można powiedzieć, że dają odpowiedź "na żywo" <m> – czyli zmiana stanu ich wejść niemal natychmiast jest odzwierciedlana <m> w stanie ich wyjść i stan ten nie zależy od niczego innego, <m>'
				'nie zależy od jakiejkolwiek historii wejść, <m> a jedynie od stanu obecnego – nie posiadają pamięci. <m>'
			'Układy które działają w taki sposób nazywamy kombinacyjnymi. <m>'
			
			'Jak jednak wiemy, zarówno z życia codziennego jak i pracy z komputerami, <m> pamięć, możliwość zapamiętania jakiejś informacji się przydaje. <mark name="rs" />'
			
			'Podstawowym, najprostszym elementem pamięci w elektronice <m> jest przerzutnik (zatrzask) typu RS. <m>'
			'Umożliwia on zapamiętanie jednego bitu informacji, <m> czyli może zapamiętać że jest w stanie zero albo w stanie jeden. <m>'
			'Posiada on dwa wejścia – set i reset. <m>'
			'Wystąpienie, nawet krótkiego sygnału na wejściu set ustawia go w stan wysoki, <m> a na wejściu reset w stan niski. <m>'
			'Przy braku sygnałów na tych wejściach stan jest pamiętany. <m>',
			
			'W niektórych realizacjach, na przykład w widocznej na symulacji, <m> wejścia mogą być zanegowane – czyli sygnałem do ustawienia wyjścia w któryś <m> ze stanów jest impuls stanu niskiego na wejściu, a nie stanu wysokiego. <m>'
			'Posiada on także dwa wyjścia – zwykłe i zanegowane, <m> bo tak wychodzi konstrukcyjnie i często wyprowadzane są oba. <m>'
			'Jednak nie zawsze – w układach zawierających większą ilość <m> elementów pamięciowych wyjście zanegowane często nie jest wyprowadzone <m> na zewnątrz układu, po to żeby zaoszczędzić na ilości nóżek. <mark name="rs_show" />'
			
			'Widoczna symulacja pokazuje realizację układu RS złożonego z dwóch bramek NAND. <m>'
			'Podanie impulsu stanu niskiego na wejście set powoduje ustawienie wyjścia <m> w stan wysoki, kolejne impulsy na tym wejściu nie zmieniają stanu wyjścia. <m>'
			'Podanie impulsu niskiego na wejście reset powoduje ustawienie stanu niskiego <m> na wyjściu i tu również kolejne impulsy nic nie zmieniają. <m>'
			
			'Równoczesne wystąpienie sygnału set i reset określane jest jako <m> stan zabroniony i stan wyjść jest wtedy nieustalony. <m>'
			'W układzie zrealizowanym tak jak <m> na tej symulacji oba wyjścia byłyby w stanie wysokim. <m>',
			
			'Przy pomocy innych bramek moglibyśmy na przykład uzyskać sterowanie <m> sygnałami nie zanegowanymi, czyli impulsami stanu wysokiego.  <m>'
			'Warto tu zwrócić uwagę na takie charakterystyczne zapętlenie, <m> czyli sygnał z wyjścia jednej bramki podawany jest na wejście drugiej, <m> a z wyjścia tej drugiej na wejście pierwszej. <m>'
			'Tego typu sprzężenie zwrotne jest podstawą działania układów pamięciowych, <m> bo tak naprawdę to ono umożliwia zapamiętanie w czymś takim jakiegoś stanu. <m>',
			
			'Przerzutnik RS wymaga dwóch sygnałów sterujących <m> jednego dla ustawienia stanu wysokiego <m> oraz drugiego dla ustawienia stanu niskiego. <m>'
			'Niekiedy jest to wygodne, ale zdecydowanie częściej wolelibyśmy <m> mieć sygnał który ma zostać zapamiętany (jakieś dane) <m>'
				' i informację kiedy tamte dane mają być zapamiętane <m> (sygnał <zezwalający>[zezwala-jący] lub zegar). <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("zatrzask", 0, 1)],
			["zatrz_clk - 1.7", eduMovie.circuitjs("zatrzask", 1, 25, [
				# D  ‾‾\_/‾\_/‾‾
				("click", 310, 140), ("wait", 1), ("click", 310, 140), ("wait", 1), ("click", 310, 140), ("wait", 1), ("click", 310, 140),
				# ENABLE ‾‾‾\___
				("click", 310, 400),
				# D  ‾‾\_/‾\__
				("click", 310, 140), ("wait", 1), ("click", 310, 140), ("wait", 1), ("click", 310, 140), ("wait", 2), 
				# ENABLE __/‾\__
				("click", 310, 400), ("wait", 1), ("click", 310, 400), ("wait", 2),
				# D __/‾\__
				("click", 310, 140), ("wait", 1), ("click", 310, 140),
			])],
		],
		'text' : [
			'Układ taki możemy uzyskać na przykład dodając do przerzutnika RS <m> odpowiedni układ wejściowy, tak jak pokazane to jest na symulacji. <m>'
			'Symulacja ta prezentuje zatrzask typu D. <m>'
			'Posiada on dwa wejścia - wejście danych oznaczane jako D <m> oraz sygnał kontrolujący zapamiętywanie (oznaczony jako enable). <mark name="zatrz_clk" />'
			
			'Widzimy że przy stanie wysokim tego wejścia <zezwalającego>[zezwala-jącego], <m> sygnał z wejścia D przekazywany jest bezpośrednio na wyjście. <m>'
			'Jednak w przypadku stanu niskiego tego wejścia, sygnał z wejścia D <m> nie ma wpływu na stan wyjścia – na wyjściu pozostaje stan, <m> który był tam w momencie opadającego zbocza sygnału enable. <m>'
			'Czyli mamy tutaj fazę przezroczystą, <m> związaną z wysokim poziomem wejścia <zezwalającego>[zezwala-jącego] i fazę nieprzezroczystą, <m> w której na wyjściu wystawiany jest stan zapamiętany, <m> na zboczu opadającym sygnału <zezwalającego>[zezwala-jącego]. <m>'
		]
	},
	{
		'image': [
			[0.0, ""],
			["przerz", eduMovie.circuitjs("przerzutnik", 1, 15, [
				# CLK ‾‾\_/‾‾
				("click", 140, 480), ("wait", 0.5), ("click", 140, 480),
				# D  ‾‾‾\___
				("wait", 1), ("click", 180, 140), ("wait", 1),
				# CLK ‾‾\_/‾‾
				("click", 140, 480), ("wait", 0.5), ("click", 140, 480),
				# D  ___/‾‾‾
				("wait", 1), ("click", 180, 140), ("wait", 1),
				# CLK ‾‾\_/‾‾
				("click", 140, 480), ("wait", 0.5), ("click", 140, 480),
			])],
			["przerz2", eduMovie.circuitjs("przerzutnik", 1, 10, [
				# D  ‾‾\_/‾\_/‾‾
				("click", 180, 140), ("wait", 0.5), ("click", 180, 140), ("wait", 0.5), ("click", 180, 140), ("wait", 0.5), ("click", 180, 140),
				# CLK  ‾‾‾\___
				("wait", 1), ("click", 140, 480), ("wait", 1),
				# D  ‾‾\_/‾\_/‾‾
				("click", 180, 140), ("wait", 0.5), ("click", 180, 140), ("wait", 0.5), ("click", 180, 140), ("wait", 0.5), ("click", 180, 140),
			])],
		],
		'text' : [
			'W tym miejscu należy wprowadzić rozróżnienie pomiędzy <m> przerzutnikiem (flip-flop) a zatrzaskiem (latch). <m>'
			'W przypadku RS można zasadniczo tych pojęć używać wymiennie, <m> bo ciężko go jednoznacznie przypisać do którejś z grup, <m> aczkolwiek najczęściej określa się go mianem przerzutnika. <m>'
			'W przypadku D - zatrzask i przerzutnik to dwie inaczej zachowujące się konstrukcję. <m>'
			'Zatrzask jak widzieliśmy ma fazę przeźroczystą, <m> w  której sygnał z wejścia jest przenoszony bezpośrednio na wyjście. <m>'
			'Przerzutnik takiej nie ma. <mark name="przerz" />'
			
			'Na ekranie widzimy teraz symulację przerzutnika D <m> zbudowanego z dwóch zatrzasków. <m>'
			'Zapamiętuje on stan wejścia D i ustawia go na wyjściu <m> jedynie w momencie opadającego zbocza sygnału sterującego – zegara. <m>'
			'W żadnej fazie zegara nie przekazuje na wyjście bezpośrednio stanu wejścia. <mark name="przerz2" />'
			
			'Jak widać wyjście zmienia się dopiero w chwili opadającego zbocza zegara <m> przyjmując stan wejścia który był w tym momencie. <m>'
			'Bez względu na to na jakim poziomie sygnału zegarowego, zachodziły zmiany <m> stanu wejścia nie były one przenoszone bezpośrednio na wyjście. <m>'
			
			'Sygnał <zezwalający>[zezwala-jący], często określany jest mianem zegara <m> (z tego względu że często podłączanego właśnie do sygnału zegarowego). <m>'
			'W wielu zastosowaniach sposób działania przerzutnika <m> jest wygodniejszy w użyciu niż zatrzasku. <m>'
			'Często przeźroczystość zatrzasku przy jednym z poziomów zegara <m> jest po prostu niepożądana – chcemy aby wyjścia zmieniały się <m> tylko w konkretnej chwili związanej ze zboczem zegara. <m>'
			
			'Istnieje jeszcze kilka rodzajów przerzutników i zatrzasków, <m> różniących się typami wejść i algorytmem działania na nich, <m> jednak ich szczegółowe omawianie tutaj nie miałoby większego sensu. <m>'
		]
	},
]
