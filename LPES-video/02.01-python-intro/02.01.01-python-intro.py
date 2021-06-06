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
	{ 'title': [ "#02.1", "Python:", "wprowadzenie", "" ] },
	
	{ 'comment': 'Python - intro' },
	{
		'image': [
			[0.0,  eduMovie.convertFile('image1.svg', margins=0)],
			[17.0, eduMovie.convertFile('image2.svg', margins=0)],
			[34.0, eduMovie.convertFile('image3.svg', margins=0)],
			[51.0, eduMovie.convertFile('image4.svg', margins=0)],
		],
		'text' : [
			"Python jest interpretowanym językiem programowania, <m> czyli nie ma potrzeby kompilacji kodu źródłowego do kodu maszynowego. <m>"
			"Interpreter Pythona potrafi bezpośrednio czytać, <m> interpretować i wykonywać kod źródłowy tego języka, <m> możliwa jest jednak kompilacja do pythonowego kodu pośredniego. <m>"
			"Python jest też językiem przenośnym pomiędzy różnymi platformami, <m> czyli w większości wypadków możemy tego samego kodu pythonowego <m> używać na różnych systemach operacyjnych <m> takich jak Linux, Windows, <Mac OS>[mak OS] i wiele innych. <m>"
			"Jest przyjazny pod względem dydaktycznym, <m> mianowicie program w Pythonie potrafi być kilkukrotnie krótszy <m> niż taki sam program napisany np. w C, <m> więc łatwiej go pokazać na ekranie i omówić. <m>"
			"Jest najpopularniejszym językiem skryptowym <m> i jednym z najpopularniejszych języków programowania w ogóle, <m> więc nie jest tak zwaną egzotyką dydaktyczną, która później nikomu się nie przydaje. <m>"
			"Posiada wiele bibliotek i jest łatwo rozszerzalny, <m> czyli możemy tworzyć własne moduły, biblioteki <m> zarówno w Pythonie jak i na przykład w C czy w C++. <m>"
			"Najpopularniejszy interpreter Pythona stworzony jest właśnie w języku C. <m>"
		]
	},
	{
		'console': [
			[0.0, "o", eduMovie.prompt()],
			[1.0, "o", "p"],
			[1.262, "o", "y"],
			[1.44729, "o", "t"],
			[1.69228, "o", "h"],
			[1.779238, "o", "o"],
			[1.982661, "o", "n"],
			[2.266715, "o", "3"],
			[2.390717, "o", "\r\n"],
			[2.52192, "o", "Python 3.7.3 (default, Jul 25 2020, 13:03:44) \r\n[GCC 8.3.0] on linux\r\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\r\n"],
			[2.535747, "o", ">>> "]
		],
		'text' : [
			"Po uruchomieniu komendy <python3>[python 3] <m> dostajemy konsolę interaktywną Pythona, <m> w której możemy zacząć wykonywać jakieś operacje. <m>"
		]
	},
	{
		'console': [ # operacje artmetyczne
			[4.122317, "o", "2"],
			[4.594335, "o", "+"],
			[4.946171, "o", "2"],
			[5.290201, "o", "\r\n"],
			[5.290952, "o", "4\r\n"],
			[5.291425, "o", ">>> "],
			
			[6.338306, "o", "2+2"],
			[7.194399, "o", "*"],
			[7.954032, "o", "3"],
			[8.394376, "o", "\r\n"],
			[8.395124, "o", "8\r\n"],
			[8.395567, "o", ">>> "],
			
			[9.002311, "o", "2+2*3"],
			[9.410383, "o", "\b"],
			[9.634314, "o", "\b"],
			[10.394482, "o", ")*3\b\b"],
			[10.618327, "o", "\b"],
			[10.738315, "o", "\b"],
			[10.898316, "o", "\b"],
			[11.058324, "o", "\b"],
			[11.474557, "o", "(2+2)*3\b\b\b\b\b\b"],
			[11.818323, "o", "\r\n"],
			[11.819406, "o", "12\r\n"],
			[11.8197, "o", ">>> "],
			
			[13.40251, "o", "(2+2)*3"],
			[13.786393, "o", "\b"],
			[14.194498, "o", "\b\u001b[1P3\b"],
			[14.922435, "o", "-3\b"],
			[15.522426, "o", "\r\n"],
			[15.523566, "o", "1\r\n"],
			[15.523922, "o", ">>> "],
			
			[19.298538, "o", "2"],
			[19.962411, "o", "*"],
			[20.122178, "o", "*"],
			[20.40246, "o", "5"],
			[20.882442, "o", "\r\n"],
			[20.883125, "o", "32\r\n"],
			[20.883406, "o", ">>> "],
			
			[25.186629, "o", "3"],
			[25.314507, "o", "3"],
			[25.602543, "o", "/"],
			[26.930595, "o", "4"],
			[27.314581, "o", "\r\n"],
			[27.315316, "o", "8.25\r\n"],
			[27.315656, "o", ">>> "],
			
			[28.234647, "o", "33/4"],
			[29.090597, "o", "\b"],
			[29.882628, "o", "/4\b"],
			[30.226597, "o", "\r\n"],
			[30.227471, "o", "8\r\n>>> "],
			
			[30.890652, "o", "33//4"],
			[31.114563, "o", "\b\u001b[1P4\b"],
			[31.594574, "o", "\b\u001b[1P4\b"],
			[32.346636, "o", "\b\u001b[1P4\b"],
			[33.906845, "o", "%4\b"],
			[34.506679, "o", "\r\n"],
			[34.50823, "o", "1\r\n"],
			[34.508584, "o", ">>> "],
			
			[35.394749, "o", "33%4"],
			[35.610696, "o", "\b"],
			[35.898695, "o", " 4\b"],
			[36.090699, "o", "\b"],
			[36.250689, "o", "\b"],
			[36.410687, "o", "\u001b[1@ "],
			[36.658628, "o", "\r\n"],
			[36.659703, "o", "1\r\n"],
			[36.660072, "o", ">>> "],
		],
		'text' : [
			"Python w tym trybie działa jako prosty kalkulator. <m>"
			"Jak widzimy na ekranie po napisaniu jakiś działań arytmetycznych <m> i naciśnięciu klawisza enter na terminal <m> wypisywany jest wynik takiej operacji. <m>"
			"Jest to cecha charakterystyczna <m> dla pracy interaktywnej z Pythonem <m> – jeżeli tworzymy program który jest zapisany w jakimś pliku, <m>"
				"to tego zachowania już nie będzie <m> i aby coś wypisać będziemy musieli użyć odpowiedniej funkcji. <m>"
			"Większość operatorów ma dość oczywiste znaczenie, <m> warto zwrócić uwagę na podwójną gwiazdkę, <m> która oznacza potęgowanie, <m> podwójny ukośnik, który oznacza dzielenie całkowite <m> i procent, który oznacza resztę z dzielenia. <m>"
			"Jak widzimy operacje można grupować przy pomocy nawiasów, <m> spacje nie odgrywają roli (używamy ich tylko dla zwiększenia czytelności). <m>"
		]
	},
	{
		'console': [ # użycie historii
			[4.938061, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[2P33 % 4"],
			[5.570056, "o", "\b\b\b\b\u001b[2P%4"],
			[6.906122, "o", "\b\b//4"],
			[9.434106, "o", "\b"],
			[9.657975, "o", "\b"],
			[10.074023, "o", "\b"],
			[10.706001, "o", " //4\b\b\b"],
			[10.921945, "o", "\u001b[C"],
			[11.08202, "o", "\u001b[C"],
			[11.402024, "o", " 4\b"],
			[12.065928, "o", "\r\n"],
			[12.067047, "o", "8\r\n"],
			[12.067612, "o", ">>> "],
			[12.601964, "o", "33 // 4"],
			[13.393999, "o", "\b"],
			[13.585861, "o", "\b"],
			[13.745961, "o", "\b"],
			[13.905994, "o", "\b"],
			[14.025838, "o", "\b"],
			[14.730051, "o", "\b\u001b[1P"],
			[15.426011, "o", "\u001b[1@4"],
			[15.993947, "o", "\r\n"],
			[15.995093, "o", "8\r\n"],
			[15.995465, "o", ">>> "],
			[17.610095, "o", "34 // 4"],
			[18.08212, "o", "\b"],
			[18.273974, "o", "\b"],
			[18.626036, "o", "\b\u001b[1P 4\b\b"],
			[18.810088, "o", "\b\u001b[1P 4\b\b"],
			[20.458232, "o", "% 4\b\b"],
			[20.938022, "o", "\r\n"],
			[20.939517, "o", "2\r\n"],
			[20.93983, "o", ">>> "],
		],
		'text' : [
			"Powłoka interaktywna Pythona <m> działa w sposób podobny do powłoki interaktywnej Bash'a <m> której używaliśmy na ostatnich zajęciach,"
			"<m> czyli możemy przy pomocy strzałek góra-dół <m> przeglądać historię wydanych poleceń, <m> strzałki prawo-lewo umożliwiają nam edytowanie tych poleceń, <m> mamy też skrót Control R do przeszukiwania historii. <m>"
			"Jeżeli jakąś operację chcemy przerwać możemy to zrobić przy pomocy Control C. <m>"
		]
	},
	{
		'console': [ # zmienne w tym wynik operacji na zmiennych do zmiennej
			[4.271806, "o", "a"],
			[4.688157, "o", "="],
			[5.60803, "o", "1"],
			[6.176233, "o", "+"],
			[7.312157, "o", "2"],
			[8.072109, "o", "\r\n"],
			[8.072932, "o", ">>> "],
			[9.880218, "o", "b"],
			[10.121, "o", " "],
			[10.296121, "o", "="],
			[10.421, "o", " "],
			[10.736116, "o", "a"],
			[11.688249, "o", "*"],
			[12.920023, "o", "3"],
			[13.240121, "o", "\r\n"],
			[13.240967, "o", ">>> "],
			[14.000131, "o", "b"],
			[14.344177, "o", "\r\n"],
			[14.344922, "o", "9\r\n"],
			[14.34527, "o", ">>> "],
		],
		'text' : [
			"W Pythonie możemy korzystać z pamięci w postaci zmiennych, <m> czyli możemy pod jakąś nazwę przepisać pewną wartość. <m>"
			"Następnie możemy się do niej odwoływać w różnych operacjach używając tej nazwy. <m>"
			"Oczywiście zmiennych możemy mieć wiele <m> i Python tutaj również jest liberalny pod względem składni, <m>"
			"czyli możemy w operacji przypisania <m> czy też odwołania się do nazwy zmiennej <m> dość swobodnie używać spacji <m> celem poprawy czytelności takiego zapisu. <m>"
		]
	},
	{
		'console': [
			[5.625673, "o", "i"],
			[5.849535, "o", "m"],
			[6.065545, "o", "p"],
			[6.257461, "o", "o"],
			[6.513511, "o", "r"],
			[6.705498, "o", "t"],
			[8.6336, "o", " "],
			[9.105474, "o", "m"],
			[9.297538, "o", "a"],
			[9.489487, "o", "t"],
			[9.745406, "o", "h"],
			[10.089436, "o", "\r\n"],
			[10.090225, "o", ">>> "],
			[11.137193, "o", "m"],
			[11.353573, "o", "a"],
			[11.57739, "o", "t"],
			[12.113451, "o", "h"],
			[12.529452, "o", "."],
			[12.817344, "o", "s"],
			[13.097447, "o", "i"],
			[13.353478, "o", "n"],
			[14.40153, "o", "("],
			[14.681345, "o", "m"],
			[14.841361, "o", "a"],
			[15.033266, "o", "t"],
			[15.249266, "o", "h"],
			[15.697285, "o", "."],
			[15.945211, "o", "p"],
			[16.201219, "o", "i"],
			[16.521367, "o", ")"],
			[17.441333, "o", "\r\n"],
			[17.442196, "o", "1.2246467991473532e-16\r\n"],
			[17.44265, "o", ">>> "],
			["importfrom + 0.638951", "o", "f"],
			["importfrom + 0.854728", "o", "r"],
			["importfrom + 0.950718", "o", "o"],
			["importfrom + 1.206846", "o", "m"],
			["importfrom + 1.902816", "o", " "],
			["importfrom + 2.09488", "o", "m"],
			["importfrom + 2.254788", "o", "a"],
			["importfrom + 2.438783", "o", "t"],
			["importfrom + 2.662598", "o", "h"],
			["importfrom + 3.150898", "o", " "],
			["importfrom + 3.438773", "o", "i"],
			["importfrom + 3.622762", "o", "m"],
			["importfrom + 3.846786", "o", "p"],
			["importfrom + 4.070619", "o", "o"],
			["importfrom + 4.32674", "o", "r"],
			["importfrom + 4.510571", "o", "t"],
			["importfrom + 4.958872", "o", " "],
			["importfrom + 5.206748", "o", "*"],
			["importfrom + 5.718554", "o", "\r\n"],
			["importfrom + 5.719248", "o", ">>> "],
			["importfrom + 6.462877", "o", "s"],
			["importfrom + 6.614726", "o", "i"],
			["importfrom + 6.838659", "o", "n"],
			["importfrom + 7.278883", "o", "("],
			["importfrom + 7.358688", "o", "2"],
			["importfrom + 7.830832", "o", "*"],
			["importfrom + 8.246806", "o", "p"],
			["importfrom + 8.470592", "o", "i"],
			["importfrom + 8.974802", "o", ")"],
			["importfrom + 9.830716", "o", "\r\n"],
			["importfrom + 9.831565", "o", "-2.4492935982947064e-16\r\n"],
			["importfrom + 9.832165", "o", ">>> "],
		],
		'text' : [
			"Pythona możemy używać jako bardziej zaawansowanego kalkulatora, <m> czyli na przykład możemy obliczać w nim <m> funkcje trygonometryczne i tym podobne rzeczy. <m>"
			"Jednak w tym celu potrzebne jest zaimportowanie odpowiedniego modułu, <m> czyli de facto takiej biblioteki pythonowej. <m>"
			"Mamy ogólnie dwie metody włączania modułów. <m>"
			'Możemy napisać import nazwa modułu <m> i żeby korzystać z elementów znajdujących się w tym module <m> musimy każdą funkcję, czy też zmienną w nim znajdującą się <m> poprzedzać nazwą tego modułu i kropką. <mark name="importfrom"/>'
			"Możemy też napisać że z jakiegoś modułu importujemy coś <m> (jeżeli podamy gwiazdkę to wtedy importujemy wszystko) <m> i następnie po prostu używać elementów znajdujących się w tym module <m> bez ich prefixowania. <m>"
		]
	},
	{
		'console': [ # import math as m .... nadpisanie zmienna ←→ moduł o tej samej nazwie 
			[3.920535, "o", "i"],
			[4.144485, "o", "m"],
			[4.360414, "o", "p"],
			[4.520504, "o", "o"],
			[4.712494, "o", "r"],
			[4.90447, "o", "t"],
			[5.47249, "o", " "],
			[5.728516, "o", "m"],
			[5.944512, "o", "a"],
			[6.072447, "o", "t"],
			[6.296463, "o", "h"],
			[6.92852, "o", " "],
			[7.08848, "o", "a"],
			[7.280458, "o", "s"],
			[7.432461, "o", " "],
			[7.656561, "o", "m"],
			[8.320515, "o", "\r\n"],
			[8.321728, "o", ">>> "],
			[9.840565, "o", "m"],
			[10.192485, "o", "."],
			[10.53649, "o", "s"],
			[10.696321, "o", "i"],
			[10.888538, "o", "n"],
			[11.264553, "o", "("],
			[11.52054, "o", "m"],
			[11.776511, "o", "."],
			[11.992439, "o", "p"],
			[12.216446, "o", "i"],
			[12.568669, "o", ")"],
			[13.608632, "o", "\r\n"],
			[13.609552, "o", "1.2246467991473532e-16\r\n"],
			[13.609862, "o", ">>> "],
			[15.824573, "o", "m"],
			[16.208474, "o", "="],
			[16.808621, "o", "1"],
			[17.064485, "o", "3"],
			[17.376462, "o", "\r\n"],
			[17.377231, "o", ">>> "],
			[18.776595, "o", "m"],
			[19.024471, "o", "\r\n"],
			[19.025184, "o", "13\r\n"],
			[19.025481, "o", ">>> "],
			[20.864705, "o", "m"],
			[21.088609, "o", "=13"],
			[21.368563, "o", "\b\b\b.sin(m.pi)"],
			[21.944587, "o", "\r\n"],
			[21.944952, "o", "Traceback (most recent call last):\r\n  File \"<stdin>\", line 1, in <module>\r\n"],
			[21.945205, "o", "AttributeError: 'int' object has no attribute 'sin'\r\n"],
			[21.945435, "o", ">>> "],
			[24.824719, "o", "m.sin(m.pi)"],
			[25.016541, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[K"],
			[25.200507, "o", "=13"],
			[25.360554, "o", "\b\b\b.sin(m.pi)"],
			[25.552475, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[Cimport math as m"],
			[26.472564, "o", "\r\n"],
			[26.472947, "o", ">>> "],
			[27.832739, "o", "import math as m"],
			[28.056613, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[5Pm.sin(m.pi)"],
			[29.03255, "o", "\r\n"],
			[29.032991, "o", "1.2246467991473532e-16\r\n>>> "],
			[29.8885, "o", "m"],
			[30.176459, "o", "\r\n"],
			[31.177574, "o", "<module 'math' (built-in)>\r\n>>> "],
		],
		'text' : [
			"Mamy też możliwość importowania pod inną nazwą, <m> co niekiedy może być przydatne. <m>"
			"Na przykład gdy mamy do zmodyfikowania jakiś kod programu <m> który przypadkowo używa zmiennej o nazwie modułu <m> który chcemy zaimportować <m> to wtedy ten moduł możemy zaimportować pod inną nazwą. <m>"
			"Tu należy zaznaczyć że Python używa <m> tej samej przestrzeni nazw dla zmiennych, modułów, funkcji, i tak dalej. <m>"
			'Inaczej mówiąc "żyją one w tym samym świecie", <m> zatem jeżeli mamy zmienną math to import modułu math <m> pod jego nazwą spowoduje utratę tej zmiennej. <m>'
		]
	},
]
