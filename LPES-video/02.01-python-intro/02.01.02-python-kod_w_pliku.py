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
	{ 'section': 'uruchamianie kodu z pliku \n i funkcja print' },
	{
		'console': [ # napisanie krótkiego programu w vim; zapisanie i uruchomienie python3 plik.py
			[0.062297, "o", eduMovie.prompt()],
			[1.133027, "o", "v"],
			[1.452898, "o", "i"],
			[1.741067, "o", " "],
			[2.020966, "o", "p"],
			[2.148982, "o", "r"],
			[2.437072, "o", "z"],
			[2.524925, "o", "y"],
			[2.780976, "o", "k"],
			[3.132993, "o", "ł"],
			[3.228927, "o", "a"],
			[3.479616, "o", "d"],
			[4.236879, "o", "."],
			[4.492741, "o", "p"],
			[4.812702, "o", "y"],
			[5.660957, "o", "\r\n"],
			[5.681729, "o", "\u001b[?1000h\u001b[?2004h\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\u001b[?2004h\u001b[1;23r\u001b[?12h\u001b[?12l\u001b[22;2t\u001b[22;1t"],
			[5.682213, "o", "\u001b[27m\u001b[23m\u001b[29m\u001b[m\u001b[H\u001b[2J\u001b[?25l\u001b[23;1H\"przykł\u001b[23;8Had.py\" [New File]"],
			[5.684381, "o", "\u001b[2;1H▽\u001b[6n\u001b[2;1H  \u001b[1;1H\u001b[>c\u001b]10;?\u0007\u001b]11;?\u0007"],
			[5.68478, "o", "\u001b[1;1H\u001b[1m\u001b[33m  1 \u001b[m\r\n\u001b[312m~                                                                               \u001b[3;1H~                                                                               \u001b[4;1H~                                                                               \u001b[5;1H~                                                                               \u001b[6;1H~                                                                               \u001b[7;1H~                                                                               \u001b[8;1H~                                                                               \u001b[9;1H~                                                                               \u001b[10;1H~                                                                               \u001b[11;1H~                                                                               \u001b[12;1H~                                                                               \u001b[13;1H~                                           "],
			[5.685032, "o", "                                    \u001b[14;1H~                                                                               \u001b[15;1H~                                                                               \u001b[16;1H~                                                                               \u001b[17;1H~                                                                               \u001b[18;1H~                                                                               \u001b[19;1H~                                                                               \u001b[20;1H~                                                                               \u001b[21;1H~                                                                               \u001b[m\u001b[22;1H\u001b[1m\u001b[7mprzykł\u001b[22;7Had.py                                                   0,0-1          All\u001b]2;przykład.py (.)\u0007\u001b[1;5H\u001b[?25h"],
			[6.645293, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[1m-- INSERT --\u001b[m\u001b[23;13H\u001b[K\u001b[22;65H\u001b[1m\u001b[7m1   \u001b[1;5H\u001b[?25h"],
			[7.43848, "o", "\u001b[?25l\u001b[ma\u001b[22;13H\u001b[1m\u001b[7m[+]\u001b[47C1,2 \u001b]2;przykład.py + (.)\u0007\u001b[1;6H\u001b[?25h"],
			[7.694354, "o", "\u001b[?25l\u001b[22;65H3 \u001b[1;7H\u001b[?25h"],
			[7.878338, "o", "\u001b[?25l\u001b[m=\u001b[22;65H\u001b[1m\u001b[7m4 \u001b[1;8H\u001b[?25h"],
			[8.070285, "o", "\u001b[?25l\u001b[22;65H5 \u001b[1;9H\u001b[?25h"],
			[9.054363, "o", "\u001b[?25l\u001b[m\u001b[1m\u001b[35m2\u001b[m\u001b[22;65H\u001b[1m\u001b[7m6 \u001b[1;10H\u001b[?25h"],
			[9.782555, "o", "\u001b[?25l\u001b[m+\u001b[22;65H\u001b[1m\u001b[7m7 \u001b[1;11H\u001b[?25h"],
			[11.80648, "o", "\u001b[?25l\u001b[m\u001b[1m\u001b[35m3\u001b[m\u001b[22;65H\u001b[1m\u001b[7m8 \u001b[1;12H\u001b[?25h"],
			[12.758535, "o", "\u001b[?25l\u001b[m\r\n\u001b[1m\u001b[33m  2 \u001b[m\u001b[2;5H\u001b[K\u001b[22;63H\u001b[1m\u001b[7m2,1 \u001b[2;5H\u001b[?25h"],
			[13.710338, "o", "\u001b[?25l\u001b[mp\u001b[22;65H\u001b[1m\u001b[7m2 \u001b[2;6H\u001b[?25h"],
			[13.934411, "o", "\u001b[?25l\u001b[mr\u001b[22;65H\u001b[1m\u001b[7m3 \u001b[2;7H\u001b[?25h"],
			[14.118302, "o", "\u001b[?25l\u001b[mi\u001b[22;65H\u001b[1m\u001b[7m4 \u001b[2;8H\u001b[?25h"],
			[14.342346, "o", "\u001b[?25l\u001b[mn\u001b[22;65H\u001b[1m\u001b[7m5 \u001b[2;9H\u001b[?25h"],
			[14.91025, "o", "\u001b[?25l\u001b[m\b\b\b\b\u001b[1m\u001b[36mprint\u001b[m\u001b[22;65H\u001b[1m\u001b[7m6 \u001b[2;10H\u001b[?25h"],
			[15.4241, "o", "\u001b[?25l\u001b[m(\u001b[22;65H\u001b[1m\u001b[7m7 \u001b[2;11H\u001b[?25h"],
			[16.238385, "o", "\u001b[?25l\u001b[ma\u001b[22;65H\u001b[1m\u001b[7m8 \u001b[2;12H\u001b[?25h"],
			[17.062406, "o", "\u001b[?25l\u001b[m*\u001b[22;65H\u001b[1m\u001b[7m9 \u001b[2;13H\u001b[?25h"],
			[18.742664, "o", "\u001b[?25l\u001b[m\u001b[1m\u001b[35m2\u001b[m\u001b[22;65H\u001b[1m\u001b[7m10\u001b[2;14H\u001b[?25h"],
			[19.408738, "o", "\u001b[?25l\u001b[m)\b\b\b\b\b\u001b[46m(\u001b[3C)\u001b[m\u001b[22;66H\u001b[1m\u001b[7m1 \u001b[2;15H\u001b[?25h"],
			[20.614013, "o", "\u001b[?25l\u001b[m\r\n\u001b[1m\u001b[33m  3 \u001b[m\u001b[3;5H\u001b[K\u001b[2;10H(\u001b[3C)\u001b[22;63H\u001b[1m\u001b[7m3,1  \u001b[3;5H\u001b[?25h"],
			[21.366442, "o", "\u001b[m\u001b[23;1H\u001b[K\u001b[3;5H"],
			[21.812975, "o", "\u001b[?25l"],
			[21.813314, "o", "\u001b[22;65H\u001b[1m\u001b[7m0-1\u001b[3;5H\u001b[?25h\u001b[?25l\u001b[23;1H\u001b[m:\u001b[?2004h\u001b[?25h"],
			[22.164997, "o", "w\u001b[?25l\u001b[?25h"],
			[22.317209, "o", "q\u001b[?25l\u001b[?25h"],
			[23.589149, "o", "\r"],
			[23.589283, "o", "\u001b[?25l\u001b[?1000l\u001b[?2004l"],
			[23.589545, "o", "\"przykł\u001b[23;8Had.py\""],
			[23.607085, "o", " [New] 3L, 20C written"],
			[23.610163, "o", "\r\u001b]2;Thanks for flying Vim\u0007\u001b[23;2t\u001b[23;1t\u001b[22;2t\u001b[22;1t\u001b[23;2t\u001b[23;1t"],
			[23.710469, "o", "\r\r\n\u001b[?2004l\u001b[?1l\u001b>\u001b[?25h\u001b[?1049l\u001b[23;0;0t"],
			[23.712937, "o", eduMovie.prompt()],
			[24.661018, "o", "p"],
			[25.013196, "o", "y"],
			[25.173078, "o", "t"],
			[25.303394, "o", "\u0007hon"],
			[26.245127, "o", "3"],
			[27.069121, "o", " "],
			[27.453158, "o", "p"],
			[27.605116, "o", "r"],
			[28.536422, "o", "zykład.py "],
			[29.221149, "o", "\r\n"],
			[29.245249, "o", "10\r\n"],
			[29.249325, "o", eduMovie.prompt()],
		],
		'text' : [
			"Praca z konsolą interaktywną jest wygodna <m> jeżeli robimy jakieś krótkie eksperymenty, <m> czy też używamy Pythona jako kalkulatora do policzenia czegoś na boku. <m>"
			"Natomiast jeżeli chcemy napisać jakikolwiek większy program <m> to wklepywanie za każdym razem po uruchomieniu interpretera poleceń <m> nawet jedynie kilkunastu linii kodu i ewentualnie <m> poprawianie w nich czegoś niekoniecznie jest przyjemne. <m>"
			"Dlatego kod pythonowy możemy pisać w pliku. <m>"
			"Typowo przyjmuje się że pliki pythonowe mają rozszerzenie <.py>[kropka py], <m> natomiast interpreter uruchomi również kod z pliku, <m> który nie będzie miał rozszerzenia lub będzie miał dowolne inne. <m>"
			"Należy unikać nazywania plików nazwami modułów importowanych <m> w ramach naszego programu – w niektórych sytuacjach <m> może to prowadzić do dziwnych błędów. <m>"
			"Kod zapisany w pliku możemy uruchomić <m> podając ten plik jako argument do wywołania polecenia <python3>[python trzy]. <m>"
		]
	},
	{
		'console': [ # python -i
			[2.32027, "o", "python3 przykład.py "],
			[3.780034, "o", "\b"],
			[4.040272, "o", "\b"],
			[4.080314, "o", "\b"],
			[4.120287, "o", "\b"],
			[4.159769, "o", "\b"],
			[4.200137, "o", "\b"],
			[4.240509, "o", "\b"],
			[4.281228, "o", "\b"],
			[4.321298, "o", "\b"],
			[4.360965, "o", "\b"],
			[4.400829, "o", "\b"],
			[4.441137, "o", "\b"],
			[4.48122, "o", "\b"],
			[5.756144, "o", "\u001b[C\u001b[1@ \b"],
			[6.548153, "o", "\u001b[1@-"],
			[6.93217, "o", "\u001b[1@i"],
			[9.875809, "o", "\r\n"],
			[9.906243, "o", "10\r\n"],
			[9.91872, "o", ">>> "],
			[11.836067, "o", "a"],
			[12.660051, "o", "\r\n"],
			[12.660775, "o", "5\r\n"],
			[12.661182, "o", ">>> "],
			[14.844138, "o", "\r\n"],
			[14.855546, "o", eduMovie.prompt()],
		],
		'text' : [
			"Jeżeli chcemy wczytać jakieś ustawienia <m> (np. wartości zmiennych) z pliku i uzyskać <m> konsolę interaktywną w której będą dostępne <m> możemy to zrobić dodając opcję <-i>[minus i]. <m>"
			"Python wykona wtedy polecenia zawarte <m> w wskazanym w linii poleceń pliku <m> i uruchomi konsolę interaktywną ze środowiskiem <m> takim jakby te polecenia były w niej wprowadzone. <m>"
			"Tworząc kod w pliku należy pamiętać, <m> iż w trybie tym nie mamy automatycznego wypisywania <m> nieprzypisanych wartości na ekran, <m> zatem jeżeli chcemy coś wypisać musimy skorzystać z funkcji print, <m>"
			"tak jak miało to miejsce w przykładach widocznych na ekranie. <m>"
		]
	},
]

code_print_A = r"""
a = 13
print(a, 17, a//3, "xyz")
print( "Ala ma kota" )
print()
print(13,17)
"""

code_print_B = r"""
a = 13
print(a, 17, a//3, "xyz")
print(a, 17, a//3, "xyz", sep="::")
"""

code_print_C = r"""
print("xyz", end="|")
print("abc")
print("123")

print(17, "xyz", sep="", end="")
print(15, "abc", sep="")
"""

clipData += [
	{ # print z kilkoma argumentami
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_print_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_print_A, [], cmd="python3")],
		],
		'text' : [
			"Wywołanie tej funkcji wygląda podobnie jak wywołanie <m> każdej innej funkcji w Pythonie – <m> po nazwie funkcji w nawiasach okrągłych podajemy argumenty, <m> które mają być do niej przekazane. <m>"
			"Kolejne argumenty rozdzielamy przecinkami. <m> W celu stworzenia estetycznego kodu możemy zastosować dowolny układ spacji <m>"
			"– mogą one być pomiędzy nazwą funkcji a nawiasami <m> oraz wokół argumentów lub może ich nie być wcale. <m>"
			"Argumentami mogą być zmienne, stałe, wyrażenia, itd. <m>"
			"Co do zasady najpierw zostanie ustalona wartość argumentów <m> (na przykład obliczona wartość wyrażenia arytmetycznego) <m> a dopiero potem wykonana funkcja, której to wyrażenie było argumentem. <m>"
			"Funkcja print wypisuje na ekran przekazane do niej argumenty, <m> rozdzielając je standardowo spacjami, <m> a wypisywanie kończy wypisaniem znaku nowej linii. <m>"
			"Wywołanie funkcji print bez argumentów wypisze nam znak nowej linii. <m>"
		]
	},
	{ #  print (sep="-")
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_print_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_print_B, [], cmd="python3")],
		],
		'text' : [
			"Print przyjmuje dowolną ilość argumentów pozycyjnych <m> które wypisze na ekran oraz może przyjąć kilka argumentów <m> identyfikowanych przez ich nazwę służących do sterowania jego zachowaniem. <m>"
			"Jednym z takich dodatkowych, opcjonalnych argumentów identyfikowanych przez nazwę <m> jest sep, ustawiający separator używany <m> do oddzielania poszczególnych wypisywanych wartości. <m>"
		]
	},
	{ #  print (end="  ")
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_print_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_print_C, [], cmd="python3")],
		],
		'text' : [
			"Drugim jest end używany do ustawienia separatora kończącego wypisywany tekst, <m> którym domyślnie jest znak nowej linii. <m>"
			"Oczywiście każdy z nich, a także oba <m> możemy ustawić na dowolną wartość, także na ciąg pusty. <m>"
		]
	},
]

code_napisy_A = r'''
print ('coś', "coś")
print ('abc " cudzysłów \' apostrof')
print ("abc \" cudzysłów ' apostrof")

a="""napis
wieloliniowy
może zawierać ' oraz " bez
zabezpieczania \' odwrotnym
ukośnikiem"""
print(a)
'''

code_napisy_B = r"""
a = 5 # komentarz liniowy
'''
blokowy komentarz
używany zazwyczaj jako dokumentacyjny
'''
print(a)
# i znowu liniowy
"""

clipData += [
	{ #  print ('coś', "coś") a="""xxx"""" print(a)
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_napisy_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_napisy_A, [], cmd="python3")],
		],
		'text' : [
			"Pojawiły nam się ciągi znaków ujęte w cudzysłowa – są to napisy. <m>"
			"W Pythonie napisami są ciągi znaków ujęte <m> w pojedyncze cudzysłowa (apostrofy) lub w podwójne cudzysłowa. <m>"
			"Nie ma tutaj żadnej różnicy pomiędzy stosowaniem pojedynczych a podwójnych cudzysłowów <m> (w niektórych językach programowania takie różnice występują) <m>"
			"– w Pythonie ważne jest jedynie aby napis zaczynać i kończyć w taki sam sposób. <m>"
			"Jeżeli chcemy aby nasz napis obejmował wiele linii <m> lub mógł zawierać nie zabezpieczane znaki cudzysłowa <m> i apostrofu możemy skorzystać z napisu wieloliniowego. <m>"
			"Do rozpoczęcia takiego napisu stosuje się <m> trzykrotne powtórzenie znaku apostrofu lub cudzysłowa <m> i w taki sam sposób się go kończy. <m>"
			"Oczywiście, jak widzimy na ekranie, napisy możemy też przypisywać do zmiennej. <m>"
			"Więcej o napisach będziemy mówić w dalszej części zajęć. <m>"
		]
	},
	{ #  komentarze
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_napisy_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_napisy_B, [], cmd="python3")],
		],
		'text' : [
			"Pewną formą napisu, czy też tworu napiso-podobnego jest komentarz. <m> Typowy komentarz w Pythonie rozpoczynamy od znaku hasza (czyli krzyżyka) i trwa on do końca linii. <m>"
			"Jest to tak zwany komentarz liniowy. <m> W Pythonie nie ma komentarzy blokowych, które wycinają fragment linii. <m>"
			"Jeżeli chcemy użyć komentarza wieloliniowego, <m> stosujemy w tym celu napis wieloliniowy <m> nie przypisany do żadnej zmiennej. <m>"
			"Typowo komentarze tego typu mają charakter komentarzy dokumentacyjnych, <m> czyli programista umieszcza je w kodzie (na ogół na początku funkcji, modułu, itp.) <m> celem opisania działania tego fragmentu kodu. <m>"
		]
	},
	{ # help('print') ... help(print)
		'console': [
			[3.990572, "o", "python3"],
			[3.995568, "o", "\r\n"],
			[4.020976, "o", "Python 3.7.3 (default, Jul 25 2020, 13:03:44) \r\n[GCC 8.3.0] on linux\r\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\r\n"],
			[4.028529, "o", ">>> "],
			[4.145505, "o", "h"],
			[4.401375, "o", "e"],
			[4.593413, "o", "l"],
			[4.809402, "o", "p"],
			[5.257526, "o", "("],
			[6.361502, "o", "p"],
			[6.617567, "o", "r"],
			[6.841433, "o", "i"],
			[7.185349, "o", "n"],
			[7.473374, "o", "t"],
			[7.945161, "o", ")"],
			[8.641522, "o", "\r\n"],
			[8.705498, "o", "\u001b[?1049h\u001b[?1h\u001b=\r"],
			[8.705878, "o", "Help on built-in function print in module builtins:\r\n\r\n\u001b[1mprint\u001b[0m(...)\r\n    print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\r\n    \r\n    Prints the values to a stream, or to sys.stdout by default.\r\n    Optional keyword arguments:\r\n    file:  a file-like object (stream); defaults to the current sys.stdout.\r\n    sep:   string inserted between values, default a space.\r\n    end:   string appended after the last value, default a newline.\r\n    flush: whether to forcibly flush the stream.\r\n\u001b[3m(END)\u001b[23m\u001b[K"],
			[10.449447, "o", "\r\u001b[K\u001b[?1l\u001b>\u001b[?1049l"],
			[10.4506, "o", "\r\n"],
			[10.450948, "o", ">>> "],
			[11.241632, "o", "help(print)"],
			[11.465474, "o", "\b"],
			[11.61737, "o", "\b"],
			[11.777367, "o", "\b"],
			[11.937415, "o", "\b"],
			[12.065428, "o", "\b"],
			[12.225399, "o", "\b"],
			[12.889542, "o", "'print)\b\b\b\b\b\b"],
			[13.13752, "o", "\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C"],
			[13.457529, "o", "\b"],
			[13.6495, "o", "')\b"],
			[14.345457, "o", "\r\n"],
			[14.355022, "o", "\u001b[?1049h\u001b[?1h\u001b=\r"],
			[14.355396, "o", "Help on built-in function print in module builtins:\r\n\r\n\u001b[1mprint\u001b[0m(...)\r\n    print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\r\n    \r\n    Prints the values to a stream, or to sys.stdout by default.\r\n    Optional keyword arguments:\r\n    file:  a file-like object (stream); defaults to the current sys.stdout.\r\n    sep:   string inserted between values, default a space.\r\n    end:   string appended after the last value, default a newline.\r\n    flush: whether to forcibly flush the stream.\r\n\u001b[3m(END)\u001b[23m\u001b[K"],
			[16.625588, "o", "\r\u001b[K\u001b[?1l\u001b>\u001b[?1049l"],
			[16.626644, "o", "\r\n"],
			[16.627007, "o", ">>> "],
		],
		'text' : [
			"Python oferuje wbudowany system dokumentacji, <m> z którego możemy korzystać uruchamiając funkcję help <m> i podając jej jako argument napis reprezentujący nazwę typu lub funkcji <m>"
			"o której chcemy uzyskać informację lub po prostu <m> funkcję, zmienną danego typu, itd. <m>"
			"W przypadku modułów i funkcji, <m> w których użyjemy komentarza dokumentacyjnego <m> zostanie on użyty do wygenerowania takiej dokumentacji. <m>"
		]
	},
]

code_error_A = r'''
print("ABC")
print(x)
'''

code_simple_A = r"""
a = 2+3
print(a*2)
"""

clipData += [
	{ #  błędny kod
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_error_A, "py")],
		],
		'consoleDown': [
			[0.0, "o", eduMovie.prompt()],
			[0.1, "o", 'python3 przykład.py'],
			[0.3, "o", '\n\r'],
			[0.35, "o", """ABC\n\rTraceback (most recent call last):\n\r  File "przykład.py", line 2, in <module>\n\rNameError: name 'x' is not defined\n\r"""],
			[0.37, "o", eduMovie.prompt()],
		],
		'text' : [
			"Na ekranie widzimy w tej chwili przykład komunikatu <m> o błędzie zwróconego przez Pythona. <m>"
			"Zawiera on informację o lokalizacji błędu – nazwę pliku <m> oraz numer linii w trakcie przetwarzania której wystąpił. <m>"
			"Ponadto zawiera także opis błędu informujący <m> o jego przyczynie – w tym wypadku jest to <m> odwołanie się do niezainicjalizowanej zmiennej x. <m>"
			"Komunikaty o błędach należy czytać i próbować zrozumieć, <m> gdyż zawarte w nich informacje mogą <m> pomóc zlokalizować i usunąć błąd. <m>"
		]
	},
	{ #  exec(open("przykład.py").read())
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_simple_A, "py")],
		],
		'consoleDown': [
			[0.066209, "o", eduMovie.prompt()],
			[0.982222, "o", "p"],
			[1.326145, "o", "y"],
			[1.518046, "o", "t"],
			[1.773916, "o", "h"],
			[2.054164, "o", "o"],
			[2.310141, "o", "n"],
			[2.630105, "o", "3"],
			[3.894223, "o", "\r\n"],
			[3.919981, "o", "Python 3.7.3 (default, Jul 25 2020, 13:03:44) \r\n[GCC 8.3.0] on linux\r\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\r\n"],
			[3.926974, "o", ">>> "],
			[4.610479, "o", "exec(open(\"przykład.py\").read())"],
			[15.350255, "o", "\r\n"],
			[15.351488, "o", "10\r\n"],
			[15.351873, "o", ">>> "],
			[16.236067, "o", "a"],
			[16.660051, "o", "\r\n"],
			[16.660775, "o", "5\r\n"],
			[16.661182, "o", ">>> "],
		],
		'text' : [
			"Mamy jeszcze jedną metodę wykonania kodu z pliku <m> – możemy tego dokonać takim magicznym zaklęciem, <m> jakie widoczne jest teraz na ekranie. <m>"
			"Ogólnie polega to na otwarciu i przeczytaniu <m> wskazanego pliku (dzięki czemu uzyskujemy napis reprezentujący jego treść) <m>, a następnie wywołaniu na tej treści funkcji exec, <m> która wykonuje podany napis jako kod pythonowy. <m>"
			"Po takim wykonaniu pliku, podobnie jak przy użyciu python <-i>[minus i], <m> zmienne i inne obiekty utworzone przez kod zawarty w tym pliku, <m> będą dostępne w bieżącym interpreterze Pythona. <m>"
			"Oczywiście do funkcji exec nie należy przekazywać <m> danych wprowadzonych przez użytkownika do naszego programu, <m> ponieważ umożliwia to stworzenie dziury bezpieczeństwa polegającej <m> na wykonaniu obcego kodu z prawami naszego programu. <m>"
			"O czytaniu i zapisywaniu plików będziemy mówić na dalszych zajęciach. <m>"
		]
	},
	{ # python3 -c 'print(2+2); print("ABC");'
		'console': [
			[0.065264, "o", eduMovie.prompt()],
			[1.625847, "o", "python3 -c 'print(2+2); print(\"ABC\");'"],
			[2.911673, "o", "\r\n"],
			[2.936416, "o", "4\r\nABC\r\n"],
			[2.940314, "o", eduMovie.prompt()],
		],
		'text' : [
			"Jak już pewnie wszyscy zauważyli instrukcje w Pythonie kończy znak nowej linii <m> i nie mamy tutaj potrzeby używania średnika. <m>"
			"Użycie go jednak na końcu instrukcji jest dozwolone <m> i nie jest traktowane jako błąd składniowy. <m>"
			"Ponadto średnik może być używany do rozdzielania <m> instrukcji w ramach kodu przekazywanego opcją <-c>[minus c]. <m>"
		]
	},
	{# ipython3
		'console': [
			[0.059016, "o", eduMovie.prompt()],
			[1.036739, "o", "i"],
			[1.260525, "o", "p"],
			[1.548519, "o", "y"],
			[1.740596, "o", "t"],
			[1.956524, "o", "h"],
			[2.086581, "o", "on3 "],
			[2.780634, "o", "\r\n"],
			[3.552578, "o", "Python 3.7.3 (default, Jul 25 2020, 13:03:44) \r\nType \"copyright\", \"credits\" or \"license\" for more information.\r\n\r\nIPython 5.8.0 -- An enhanced Interactive Python.\r\n?         -> Introduction and overview of IPython's features.\r\n%quickref -> Quick reference.\r\nhelp      -> Python's own help system.\r\nobject?   -> Details about 'object', use 'object??' for extra details.\r\n"],
			[3.554298, "o", "\r\n"],
			#[3.554585, "o", "\u001b[?1l\u001b[6n"],
			#[3.556293, "o", "\u001b[?2004h\u001b[?25l\u001b[0m\u001b[?7l\u001b[0m\u001b[J\u001b[0;38;5;28mIn [\u001b[0;38;5;10;1m1\u001b[0;38;5;28m]: \u001b[8D\u001b[8C\u001b[?7h\u001b[0m\u001b[?12l\u001b[?25h"],
			#[3.570647, "o", "\u001b[?25l\u001b[?7l\u001b[?7h\u001b[0m\u001b[?12l\u001b[?25h"],
			[3.554585, "o", "In [1]: "],
			[9.438005, "o", "\r\n"],
			#[9.438005, "o", "\u001b[?25l\u001b[?7l\u001b[8D\u001b[0m\u001b[J\u001b[0;38;5;102mIn [1]:                                                                 \r\u001b[72C \r\u001b[0m\r\r\n\u001b[J\u001b[?7h\u001b[0m\u001b[?12l\u001b[?25h"],
			#[9.438497, "o", "\u001b[?2004l"],
			[9.438926, "o", "Do you really want to exit ([y]/n)? "],
			[10.764451, "o", "y"],
			[11.172515, "o", "\r\n"],
			[11.29056, "o", eduMovie.prompt()],
		],
		'text' : [
			"Oprócz standardowego interpretera Pythona <m> mamy też interpreter iPython, <m> który jest stworzony z myślą o większej wygodzie w pracy interaktywnej, <m>"
			"czyli na przykład wygodniej <m> się w nim edytuje wielolinijkowe funkcje, itp. <m> Dla pythona 3 używamy polecenia <ipython3>[i python 3]."
		]
	},
]
