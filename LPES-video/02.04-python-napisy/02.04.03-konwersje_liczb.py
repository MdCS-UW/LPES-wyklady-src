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

code_suma_A = r'print( "13.3" + "17" )'
code_suma_B = r'print( float("13.3") + int("17") )'
code_napis_liczba_A = r'print( int("17"), int("17", 10), int("17", 8), int("17", 16), int("101", 2) )'
code_napis_liczba_B = r'print( int("17", 0), int("0o17", 0), int("0x17", 0), int("0b101", 0) )'
code_napis_liczba_C = r'print( 0b101 + 0xa )'

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'konwersje liczb i napisów\ni sposoby zapisu liczb' },
	{ #  konwersja napis → liczba
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_suma_A, "py")],
			["suma2", eduMovie.clear + eduMovie.code2console(code_suma_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_suma_A, [], cmd="python3")],
			["suma2", eduMovie.runCode(code_suma_B, [], cmd="python3")],
		],
		'text' : [
			"Dość często mamy potrzebę konwersji liczby <m> zawartej w napisie na odpowiadającą jej wartość liczbową, <m> aby móc wykonać na nich operacje arytmetyczne, <m>"
			"gdyż Python wykonując operacje na napisach <m> nie rozważa tego czy reprezentują one liczbę <m> i może należałoby je tak traktować. <m>"
			'Konwersje takie są potrzebne na przykład <m> przy wszystkich danych wczytywanych jako tekst – wczytanych z pliku tekstowego, <m> argumentów linii poleceń lub wczytanych z klawiatury. <mark name="suma2" />'
			"Konwersję taką umożliwiają nam <m> funkcje int i float (dokładniej są to konstruktory tych typów). <m>"
		]
	},
	{ #  systemy liczbowe
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_napis_liczba_A, "py")],
			["prefiksowane", eduMovie.clear + eduMovie.code2console(code_napis_liczba_B, "py")],
			["prefixy2", eduMovie.clear + eduMovie.code2console(code_napis_liczba_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_napis_liczba_A, [], cmd="python3")],
			["prefiksowane", eduMovie.runCode(code_napis_liczba_B, [], cmd="python3")],
			["prefixy2", eduMovie.runCode(code_napis_liczba_C, [], cmd="python3")],
		],
		'text' : [
			"Instrukcja int pozwala na podanie opcjonalnego, <m> drugiego argumentu określającego system liczbowy <m> w którym wyrażona jest liczba zawarta w napisie. <m>"
			"Domyślnie instrukcja ta zakłada że jest to system dziesiętny. <m>"
			'Jako drugi argument możemy podać dowolną wartość <m> stanowiącą podstawę systemu liczbowego użytego do zapisu liczby podanej jako napis, <m> np. 12 jeżeli stosowany byłby system o podstawie 12. <mark name="prefiksowane" />'
			"Jeżeli jako drugi argument podamy zero <m> to funkcja spróbuje dokonać automatycznej detekcji systemu <m> w oparciu o prefix podany w napisie. <m>"
			'Prefixem tym może być <0x>[zero x] dla systemu szesnastkowego, <m> <0b>[zero b] dla binarnego i <0o>[zero o] dla ósemkowego. <m> Brak prefixu oznacza system dziesiętny. <mark name="prefixy2" />'
			'Prefixy określające system liczbowy możemy używać także <m> do podawania liczb w innych systemach bezpośrednio w kodzie, <m> tak jak jest to pokazane na ekranie. <m>'
		]
	},
]

code_liczba_napis_A = r'print( str(13), str(17.5) )'
code_liczba_napis_B = r'print( hex(13), bin(13), oct(13) )'
code_liczba_napis_C = r'print( "ABC " + hex(13) + " " + str(13) )'
code_liczba_napis_D = r'print( "ABC {:x} {:d}".format(13, 13) )'
code_liczba_napis_E = r'help("FORMATTING")'

clipData += [
	{ #  liczba → napis
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_liczba_napis_A, "py")],
			["hexbinoct", eduMovie.clear + eduMovie.code2console(code_liczba_napis_B, "py")],
			["suma_napisow", eduMovie.clear + eduMovie.code2console(code_liczba_napis_C, "py")],
			["format", eduMovie.clear + eduMovie.code2console(code_liczba_napis_D, "py")],
			["help_formating", eduMovie.clear + eduMovie.code2console(code_liczba_napis_E, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_liczba_napis_A, [], cmd="python3")],
			["hexbinoct", eduMovie.runCode(code_liczba_napis_B, [], cmd="python3")],
			["suma_napisow", eduMovie.runCode(code_liczba_napis_C, [], cmd="python3")],
			["format", eduMovie.runCode(code_liczba_napis_D, [], cmd="python3")],
			["help_formating", ""],
		],
		'text' : [
			'Możliwe jest też konwertowanie liczby na napis <m> zawierający jej reprezentację w danym systemie liczbowym. <m>'
			'Dla systemu dziesiętnego jest to wywołanie konstruktora napisu <m> od wartości numerycznej, którą może być zarówno <m> liczba całkowita jak i zmiennoprzecinkowa. <mark name="hexbinoct" />'
			'Dla innych systemów liczbowych mamy odpowiednie funkcje <m> hex dla szesnastkowego, bin dla binarnego i oct dla ósemkowego. <m>'
			'Funkcje te zawsze dodają do tworzonego napisu odpowiedni prefix. <mark name="suma_napisow" />'
			'Funkcje dokonujące konwersji liczby na napis <m> są nam potrzebne między innymi po to aby móc umieścić liczbę <m> w jakimś napisie z użyciem łączenia napisów <m> przy pomocy operatora plus. <mark name="format" />'
			
			'Inną metodą na umieszczenie liczb w napisie <m> jest użycie metody format typu napisowego <m> z odpowiednio przygotowanym napisem formatującym. <mark name="help_formating" />'
			'Szczegóły można znaleźć w dokumentacji <m> po uruchomieniu help od <FORMATTING>[formating] pisanego wielkimi literami. <m>'
		]
	},
]

