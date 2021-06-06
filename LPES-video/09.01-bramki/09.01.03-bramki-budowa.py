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
	{ 'comment': 'bramki - budowa' },
	{
		'image': [
			[0.0, ""],
			["_not", eduMovie.circuitjs("not", 0, 1)],
			["not2", eduMovie.circuitjs("not", 1, 2, [("switch", 410, 290)])],
			["nand", eduMovie.circuitjs("nand", 0, 1)],
			["nand2", eduMovie.circuitjs("nand", 0, 9, [
				("switch", 330, 300), ("wait", 2.3), ("switch", 330, 300), ("wait", 0.2), ("switch", 330, 400), ("wait", 2.3), ("switch", 330, 300)
			])],
			["nand3", eduMovie.circuitjs("nand", 0, 1)],
			["nor", eduMovie.circuitjs("nor", 2, 9, [
				("switch", 350, 170), ("wait", 2.3), ("switch", 350, 170), ("wait", 0.2), ("switch", 350, 270), ("wait", 2.3), ("switch", 350, 170)
			])],
		],
		'text' : [
			'Można się zastanowić w jaki sposób bramka skonstruowana jest wewnętrznie. <m>'
			'Współcześnie bramki budowane są z tranzystorów typu mosfet w technologii cmos, <m> czyli używającej zarówno tranzystorów n-mosfet jak i p-mosfet w jednym układzie <mark name="_not" />'
			
			'Na ekranie zaprezentowana jest konstrukcja <m> najprostszej z bramek, czyli bramki NOT. <m>'
			'Składa się ona z dwóch tranzystorów w znanym nam już układzie półmostka. <m>'
			'Jeżeli na wejście podamy stan wysoki, czyli napięcie zasilania naszego półmostka, <m> to przewodzi dolny tranzystor n-mosfet, a górny p-mosfet jest zatkany, <m> na wyjściu mamy zatem stan niski. <mark name="not2" />'
			'Jeżeli na wejście podamy stan niski, czyli masę, to przewodzi górny tranzystor, <m> a dolny jest zatkany – na wyjściu mamy stan wysoki. <m>'
			'Zaletą takiego wyjścia jest możliwość zarówno wypuszczenia, jak i wpuszczenia <m> do niego prądu, więc może ono wydajnie sterować wejściami innych bramek, <m>'
				'czy nawet zasilić poprzez odpowiedni rezystor jakąś diodę sygnalizacyjną. <m>'
			'Jeżeli wydajność prądowa bramki, określona w dokumentacji, jest niewystarczająca <m> możemy z jej pomocą wysterować tranzystor, który pozwoli <m> na kontrolowanie bardziej prądożernych odbiorników. <mark name="nand" />'
			
			'Bardziej rozbudowane bramki niż sam not <m> składają się z większej ilości tranzystorów. <m>'
			'Natomiast nadal można tutaj wyróżnić coś na kształt dwóch pół mostków, <m> czyli mamy półmostek sterowany z jednego wejścia <m> i drugi sterowany z drugiego wejścia. <m>'
			'Półmostki te są połączone w ten sposób że tranzystory z jednej części <m> obu pół mostków (np. tej od strony zasilania) są połączone równolegle, <m> a te z drugiej części szeregowo. <mark name="nand2" />'
			
			'W efekcie przy takim połączeniu aby na wyjściu pojawił się stan wysoki <m> wystarczy aby jeden z półmostków miał wyjście w stanie wysokim, <m> czyli wejście w stanie niskim. <m>'
			'Dzięki łączeniu równoległemu do zasilania poda on stan wysoki na wyjście <m> bez względu nas tan drugiego półmostka, <m>'
				'a dzięki łączeniu szeregowemu od strony masy zapobiegnie podaniu <m> stanu niskiego przez drugi półmostek, co doprowadziłoby do zwarcia. <mark name="nand3" />'
			
			'Aby pojawił się stan niski oba półmostki muszą mieć na swoim wyjściu stan niski <m> (aby łączenie szeregowe mogło przewodzić do masy), <m> czyli mieć wejścia w stanie wysokim. <m>'
			'Powstała nam tutaj funkcja NAND. <mark name="nor" />'
			
			'Jeżeli zamienimy miejscami te połączenia równoległe z szeregowymi, <m> uzyskamy bramkę NOR. <m>'
			
			'Jest to też odpowiedź na nurtujące niekiedy pytanie <m> dlaczego w elektronice na ogół mamy bramki zanegowane. <m>'
			'Wynika to z faktu że takie naturalnie wychodzą, <m> a uzyskanie bramki nie zanegowanej wymaga dołożenia do jej wyjścia <m> negatora w postaci kolejnego półmostka. <m>'
		]
	},
]
