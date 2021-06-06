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

code_encode_A = r"print( 'a ą B ∞ → 龍'.encode() )"
code_bajtowy_A = r'print(b"\x61 \xc4\x85 \x42 \xe2\x88\x9e \xe2\x86\x92 \xe9\xbe\x8d XYZ")'
code_bajtowy_B = r'print(b"\x61 \xc4\x85 \x42 \xe2\x88\x9e \xe2\x86\x92 \xe9\xbe\x8d XYZ".decode())'

code_utf7_A = r'''
print( 'a ą B ∞ → 龍'.encode('utf7') )
print( b'a +AQU B +Ih4 +IZI +n40-'.decode('utf7') )
'''

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'kodowanie tekstu' },
	{
		'image': [
			[0.0,  eduMovie.convertFile("kodowanie.tex", margins=8, viaCairo=True, negate=True)],
		],
		'text' : [
			"Kolejnym zagadnieniem związanym z napisami jest kodowanie znaków. <m>"
			
			"Napis pythonowy jest zasadniczo abstrakcyjnym typem <m> reprezentującym ideę tego czym jest napis, <m> czyli jest po prostu ciągiem jakiś znaków. <m>"
			"I podobnie jak typ związany z liczbami całkowitymi <m> jest niezależny od ich reprezentacji <m> w jakimś systemie liczbowym, <m>"
			"tak na napis pythonowy można patrzeć jako na <m> niezależny od sposobu kodowania <m> znaków używanego do wprowadzania i wyprowadzania <m> danych z Pythona do świata zewnętrznego. <m>"
			
			"Jednak jako że dla komputera wszystko jest liczbą <m> (na dodatek binarną) to tym znakom <m> należy też przypisać jakieś liczby. <m>"
			"Wewnętrznie Python znaki napisu koduje z użyciem Unicode, <m> co umożliwia użycie praktycznie wszystkich <m> znaków najróżniejszych alfabetów oraz <m> mnóstwa znaków specjalnych. <m>"
			
			"Unicode określa przypisania wartości numerycznych do znaków. <m> Natomiast istnieje wiele metod zapisu tych liczb, ich kodowań. <m>"
			"Oprócz kodowania samego Unicode <m> (określających jedynie sposób zapisu liczby) <m> istnieją także kodowania związane z mapowaniem <m> podzbioru znaków Unicode na mniejszy zbiór znaków, <m>"
			"który można zapisać na przykład jedynie <m> z użyciem jednego bajtu (tak jak w <ISO-8859-2>[iso 88 59 2]). <m>"

			"Nie związany jawnie z żadnym takim kodowaniem <m> napis może żyć sobie w świecie Pythona. <m>"
			"Natomiast jeżeli chcemy już coś takiego zapisać do pliku <m> lub przesłać siecią komputerową to należy to zapisać, bądź <m> wysłać w jakimś określonym kodowaniu. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_encode_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_encode_A, [], cmd="python3")],
		],
		'text' : [
			"Zakodować można to przy pomocy <m> metody encode typu napisowego. <m>"
			"W efekcie jej działania otrzymaliśmy <m> coś co przypomina napis (też jest umieszczone w apostrofach), <m> ale napisem nie jest o czym świadczy poprzedzający <m> go prefix w postaci literki b. <m>"
			"Jest to ciąg bajtowy. <m>"
			"Tak jak napis był ciągiem kolejnych znaków, <m> tak ciąg bajtowy jest ciągiem kolejnych bajtów, <m> czyli <8>[ośmio] bitowych liczb reprezentujących wartości <m> z przedziału od zera do 255. <m>"
			"Jak widzimy Python wypisując ciągi bajtowe, <m> wartości odpowiadające znakom <m> drukowanym z zakresu ASCII <m> wypisuje jako te znaki. <m>"
			"Natomiast wszystkie inne wartości wypisuje <m> w postaci odwrotny ukośnik x <m> i wartość zapisana jako dwie cyfry szesnastkowe <m> (jeżeli trzeba to z poprzedzającym zerem). <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_bajtowy_A, "py")],
			["decode", eduMovie.clear + eduMovie.code2console(code_bajtowy_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_bajtowy_A, [], cmd="python3")],
			["decode", eduMovie.runCode(code_bajtowy_B, [], cmd="python3")],
		],
		'text' : [
			'Ciągi bajtowe w kod programu możemy <m> wprowadzić w taki sam sposób czyli w apostrofach, <m> bądź cudzysłowach poprzedzonych literą b. <mark name="decode"/>'
			'Na ciągu bajtowym możemy wykonać metodę decode, <m> która spróbuje dokonać konwersji tego ciągu na napis. <m>'
			'Domyślnie metody decode i encode używają kodowania UTF8, <m>'
			'które pozwala na zapis dowolnych znaków unicode, <m> w sposób kompatybilny z kodowaniem ASCII <m> (obejmującym znaki alfabetu łacińskiego oraz <m> podstawowe znaki specjalne jak przecinek kropka, nawiasy, itd.). <m>'
			'Kompatybilność ta polega na tym że <m> 128 znaków ASCII zapisywanych jest bez jakiejkolwiek zmiany <m> – identycznie jak w tamtym kodowaniu. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_utf7_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_utf7_A, [], cmd="python3")],
		],
		'text' : [
			"Obu tym metodom możemy podać opcjonalny argument <m> będący napisem określającym kodowanie. <m>"
			"Użyte w widocznym przykładzie kodowanie UTF7 <m> wykorzystuje tylko 7 bitów wynikowego znaku <m> (nie używa najstarszego bitu), co potrafi być użyteczne, <m>"
			"bo nadal funkcjonują systemy siedmiobitowe <m> (np. część usług poczty elektronicznej). <m>"
				"Co ciekawe jak powstawał standard poczty elektronicznej <m> były już sieci komputerowe przesyłające osiem bitów, <m> ale był on tworzony z myślą o kompatybilności <m> z sieciami które tego nie potrafiły. <m>"
				"Aktualnie tamtych sieci nikt już nie używa, <m> za to poczty wszyscy używają nadal według <m> standardu który przesyła 7 bitów. <m>"
		]
	},
]

code_ukosnik_A = r'print( "\u221e \U0001f914 \U0000221e" )'

code_ordchr_A = code_ukosnik_A + r'''
print( hex(ord('∞')) )
print( chr(0x221e), chr(0x1f914) )
'''

code_ordchr_B = code_ordchr_A + r'''
print( "ABC\nDEF\n\tGHI" )
'''

code_codecs_A = r'''
import codecs

x = codecs.encode(b'\x01\x02\x03\x04', 'base64')
print(x)

x = codecs.decode(b'AQIDBA==\n', 'base64')
print(x)
'''

clipData += [
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_ukosnik_A, "py")],
			["ordchr", eduMovie.clear + eduMovie.code2console(code_ordchr_A, "py")],
			["ordchr + 13", eduMovie.clear + eduMovie.code2console(code_ordchr_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_ukosnik_A, [], cmd="python3")],
			["ordchr", eduMovie.runCode(code_ordchr_A, [], cmd="python3")],
			["ordchr + 13", eduMovie.runCode(code_ordchr_B, [], cmd="python3")],
		],
		'text' : [
			'W ramach napisu pythonowego możemy umieszczać <m> dowolne znaki unicode bezpośrednio, <m> jak było to widoczne w poprzednich przykładach. <m>'
			'Możemy je też wprowadzać także numerycznie <m> jako odwrotny ukośnik, małe u i 4 cyfry szesnastkowe <m> lub odwrotny ukośnik, duże u i 8 cyfr szesnastkowych. <m>'
			
			'Oczywiście warunkiem poprawnego wyświetlenia znaku <m> jest używanie czcionki posiadającej reprezentację graficzną takiego znaku, <m> dlatego też używanie numerycznego wprowadzania <m> dziwnych znaków może być bardzo przydatne. <m>'
			'Zwłaszcza dla programistów którzy <m> otworzą nasz kod nie mając odpowiednich fontów. <mark name="ordchr"/>'
			
			'Python dostarcza też funkcje <ord>[O R D] i <chr>[C H R], <m> pierwsza z nich konwertuje napis zawierający jeden znak <m> na wartość numeryczną tego znaku, <m> druga konwertuje numer znaku na napis go reprezentujący. <m>'
			
			'Niektóre znaki specjalne, jak na przykład znak nowej linii, <m> czy tabulator możemy wprowadzić z użyciem krótszych <m> i łatwiejszych do zapamiętania sekwencji niż opartych o ich numer. <m>'
			'Dla znaku nowej linii jest to odwrotny ukośnik n, <m> a dla tabulatora odwrotny ukośnik t. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_codecs_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_codecs_A, [], cmd="python3")],
		],
		'text' : [
			"Niekiedy zachodzi potrzeba zapisania w postaci tekstu <m> czegoś co tekstem ewidentnie nie jest, <m> jest danymi binarnymi. <m>"
			"Przykładem czegoś takiego może być obrazek, plik dźwiękowy, itd. <m>"
			"Takie dane również można zakodować w postaci tekstowej <m> i na przykład tak zakodowane nasze zdjęcia wydrukować na kartce. <m>"
			"Zaletą takiego wydruku w stosunku co do wydruku <m> zdjęcia jako zdjęcia jest brak utraty jakości – mamy te same dane binarne <m> co w oryginalnym zdjęciu tylko w postaci literek, <m> które możemy wprowadzić ponownie do komputera. <m>"
			"Jest to analogiczne do qr kodów, <m> które są przykładem takiego kodowania <m> w postaci graficznej a nie tekstowej. <m>"
			
			"Python ma moduł <codecs>[kodeks] pozwalający na kodowanie <m> danych binarnych do postaci tekstowej. <m>"
			"Udostępnia on funkcję encode, <m> która umożliwia tego typu kodowanie <m> i funkcję decode, która umożliwia dekodowanie <m> w różnych tego typu standardach. <m>"
			
			"Jednym z popularniejszych tego typu standardów <m> jest <base64>[base sześćdziesiąt cztery], zapisujący dowolne dane binarne z użyciem <m> 64 drukowalnych znaków ASCII, głównie liter i cyfr. <m>"
		]
	},

]
