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

code_bin_A = r"""
print( bin(13), 0b100 )
"""

code_bin_B = r"""
print(2 and 1, 2 & 1)
"""

code_bin_C = r"""
print(0b10 & 0b01)
"""

code_funkcja_pb = r"""
def pb(x):
	print("0b{0:04b}".format(x & 0xf))
"""

code_pb_A = code_funkcja_pb + r"""
pb(0b1010 & 0b1001)
pb(0b1010 | 0b1001)
pb(0b0101 ^ 0b1110)
"""

code_pb_B = code_funkcja_pb + r"""
pb(~ 0b0100)
pb(0b0100 ^ 0b1111)
"""

code_pb_C = code_funkcja_pb + r"""
pb(0b0011 << 1)
pb(0b0011 << 2)
pb(0b1100 >> 1)
pb(0b1100 >> 2)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.1", "Python:", "operacje bitowe", "" ] },
	
	{ 'comment': 'operacje bitowe' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_bin_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_bin_A, [], cmd="python3")],
		],
		'text' : [
			'Jak wiemy liczby możemy zapisywać w różnych systemach liczbowych. <m> Jednym z nich jest system dwójkowy, nazywany też binarnym. <m>'
			'Taka reprezentacja liczb jest podstawą działania <m> elektroniki cyfrowej, w tym współczesnych komputerów. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('nkb.tex', margins=12, viaCairo=True, negate=True)],
			["ujemne", eduMovie.convertFile('u2.tex', margins=12, viaCairo=True, negate=True)],
		],
		'text' : [
			'Liczby dodatnie w systemie binarnym zapisuje się praktycznie zawsze w postaci NKB. <m>'
			'Zapis taki jest analogiczny do zapisu dziesiętnego stosowanego na codzień, <m> z tym że kolejne cyfry liczby mają wagę dwa to <n>[en-tej] a nie dziesięć do <n>[en-tej] <m>'
			'Gdzie wartość potęgi jest numerem cyfry. <m> Skrajna cyfra od prawej ma numer zero. <mark name="ujemne" />'
			
			'Liczby ujemne mogą być zapisywane na różne sposoby. <m>'
			'Stosowany może być na przykład kod moduł-znak, <m> polegający na zapisie modułu liczby w postaci NKB <m> oraz umieszczenia flagi znaku w najstarszym bicie. <m>'
			'Najczęściej jednak stosowany jest kod uzupełnień do dwóch. <m> Przypomina on NKB, tyle że najstarszy n-ty bit wchodzi z wagą ujemną. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_bin_B, "py")],
			["binC", eduMovie.clear + eduMovie.code2console(code_bin_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_bin_B, [], cmd="python3")],
			["binC", eduMovie.runCode(code_bin_C, [], cmd="python3")],
		],
		'text' : [
			'Przy okazji omawiania operatorów logicznych not, and i or <m> wspomnieliśmy o operatorach bitowych, <m> ale nie wchodziliśmy głębiej w ten temat. <m>'
			'Są to operatory wykonujące operacje algebry boolowskiej takie jak <m> na przykład AND, ale nie na poziomie liczb jako całości <m> a na poziomie poszczególnych bitów tych liczb. <m>'
			'Jak widzimy na ekranie mogą dawać one inny efekt od operacji logicznej. <m>'
			
			'Jeżeli operację and logicznego wykonamy na dwóch <m> wartościach niezerowych (odpowiadających prawdzie) <m> dostaniemy wartość nie zerową, czyli prawdę. <m>'
			'Natomiast jeżeli operację taką będziemy wykonywać niezależnie <m> na kolejnych cyfrach reprezentacji binarnej <m> tych liczb to wynik może być różny. <mark name="binC" />'
			
			'W przykładzie widocznym na ekranie użyliśmy liczb jeden i dwa. <m> Liczba dwa to w systemie binarnym <1 0>[jeden zero], a liczba jeden to <0 1>[zero jeden]. <m>'
			'Zatem jeżeli wykonujemy operację and na poszczególnych bitach to mamy po kolei: <m> 0 i 1, czyli zero <break time="100ms"/> oraz 1 i 0, czyli też zero, <m> zatem wynikiem jest liczba o bitach <0>[zero] i <0>[zero], czyli zero. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_pb, "py")],
			["pbA", eduMovie.clear + eduMovie.code2console(code_pb_A, "py")],
			["pbB", eduMovie.clear + eduMovie.code2console(code_pb_B, "py")],
			["pbC", eduMovie.clear + eduMovie.code2console(code_pb_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_funkcja_pb, [], cmd="python3")],
			["pbA", eduMovie.runCode(code_pb_A, [], cmd="python3")],
			["pbB", eduMovie.runCode(code_pb_B, [], cmd="python3")],
			["pbC", eduMovie.runCode(code_pb_C, [], cmd="python3")],
		],
		'text' : [
			'Jako że funkcja bin, używana do konwersji liczby na napis <m> w reprezentacji bitowej nie wypisuje jej wiernie, <m> a używa reprezentacji wartości ujemnych oraz pomija wiodące zera <m>'
			'to na potrzeby tego przykładu zdefiniujmy sobie funkcję <pb>[P B], <m> która będzie wierniej wypisywała reprezentacje binarną liczby <4>[cztero] bitowej. <m>'
			'Dzięki niej możemy się przyjrzeć działaniu różnych operacji bitowych. <mark name="pbA" />'
			
			'Przy pomocy znaku ampersand zapisujemy operację bitowego and, <m> pionowej kreski bitowego or, dzióbka w górę bitowego xor. <m>'
			'xor to operacja alternatywy wykluczającej <m> – zwraca jeden gdy argumenty różne, zero gdy jednakowe). <mark name="pbB" />'
			
			'Tylda neguje poszczególne bity w liczbie, <m> czyli bit zero zastępuje bitem jeden a jeden bitem zero. <m>'
			'Można zauważyć że jest to to samo co xor z samymi jedynkami <m> i obserwacja ta potrafi być użyteczna <m> – xor może być użyty jako sterowany negator. <mark name="pbC" />'
			
			'Podwójne znaki mniejszości i większości służą do realizacji <m> przesunięć bitowych o podaną ilość bitów w lewo, bądź w prawo. <m>'
			'Operacja przesunięcia w lewo odpowiada mnożeniu o dwa do potęgi, którą jest wartość przesunięcia. <m>'
			'Natomiast operacja przesunięcia w prawo to dzielenie przez dwa do potęgi będącej wartością przesunięcia. <m>'
			'Operacje takie są przydatne do sprawdzania <m> bądź ustawiania wartości poszczególnych bitów. <m>'
			'Są to operacje dość niskopoziomowe i nie są często stosowane w samym Pythonie, <m> ale wiedza o nich przyda nam się w niedalekiej przyszłości. <m>'
		]
	},
]

