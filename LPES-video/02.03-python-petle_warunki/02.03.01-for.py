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

code_for_A = r"""
for x in [1,2,3]:
    print("x to", x, end="   ")
    print(x**2)
"""

code_for_B = r"""
for x in range(3):
    print("x to", x, end="   ")
    print(x**2)
"""

code_for_C = r"""
for x in range(2, 5):
    print("x to", x, end="   ")
    print(x**2)
"""

code_for_D = r"""
for x in range(1, 9, 2):
    print("x to", x, end="   ")
    print(x**2)
"""

code_for_E = r"""
for x in range(9, 1, -2):
    print("x to", x, end="   ")
    print(x**2)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#02.3", "Python:", "pętle i warunki", "" ] },
	
	{ 'comment': 'python - for' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_for_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_for_A, [], cmd="python3")],
		],
		'text' : [
			"W programowaniu jeżeli jakąś operację <m> chcemy wykonać wielokrotnie to w tym celu używamy pętli. <m>"
			"Python oferuje nam kilka rodzajów pętli. <m> Pierwszym z nich jest pętla for, <m> służąca do iterowania po elementach pewnej kolekcji <m> (czyli jest to pętla typu <foreach>[for each]). <m>"
			"W Pythonie nie ma <tzw.>[tak zwanej] pętli ogólnej, <m> czyli odpowiednika for znanego na przykład z języka C, <m> gdzie mamy wydzielone sekcje inicjalizacji, warunku i zmiany wartości <m> oraz blok instrukcji wykonywany w ramach pętli. <m>"
			
			"Na ekranie widzimy przykład pętli <m> iterującej po kolekcji elementów zapisanej w nawiasach kwadratowych <m> (dokładniej jest to lista, ale do tematu różnych kolekcji jeszcze wrócimy). <m>"
			"Pętla rozpoczyna się od słowa kluczowego for <m> po którym występuje nazwa zmiennej pod którą będą podstawiane elementy kolekcji, <m>"
			"następnie mamy słowo kluczowe in <m> po którym podana jest kolekcja po której pętla będzie iterować. <m>"
			"Należy zwrócić uwagę na podobieństwo składniowe <m> do przypadku definiowania funkcji – tutaj również mamy dwukropek <m> rozpoczynający blok kodu i blok kodu wydzielony wcięciem. <m>"
			"Instrukcje składające się na ten blok kodu, <m> zostaną wykonane dla każdego obiegu pętli. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_for_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_for_B, [], cmd="python3")],
		],
		'text' : [
			"Metodą na symulowanie pętli ogólnej <m> w celu iterowania po przedziale liczb całkowitych <m> jest użycie instrukcji range, <m> która przyjmuje od jednego do trzech argumentów. <m>"
			"Jak widzimy na ekranie, użycie instrukcji range <m> z jednym argumentem odpowiada podaniu listy <m> liczb całkowitych od zera do elementu <m> o jeden mniejszy od podanego. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_for_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_for_C, [], cmd="python3")],
		],
		'text' : [
			"Wersja dwu argumentowa pozwala na określenie <m> obu krańców przedziału liczb całkowitych po których iterujemy. <m>"
			"Jak widzimy przedział ten jest lewostronnie domknięty <m> i prawostronnie otwarty, czyli pisząc <m> od 2 do 5 dostajemy 2, 3 i 4. <m>"
			"Jest to powszechna reguła dotycząca podawania zakresów w Pythonie. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_for_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_for_D, [], cmd="python3")],
		],
		'text' : [
			"Dodanie trzeciego argumentu pozwala na określenie <m> kroku iteracyjnego, czyli tego co którą wartość bierzemy. <m>"
			"W przykładzie widocznym na ekranie bierzemy <m> co drugą wartość od <1>[jeden], dopóki jest ona mniejsza od 9. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_for_E, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_for_E, [], cmd="python3")],
		],
		'text' : [
			"Zamieniając krańce przedziału i podając ujemną wartość kroku, <m> możemy uzyskiwać listy liczb w odwrotnej kolejności. <m>"
			"W prezentowanym przykładzie dostajemy 9 <m> i kolejne liczby o 2 mniejsze dopóki są większe od <1>[jeden]. <m>"
			"Instrukcja range pozwoli nam na iterowanie <m> po liczbach ujemnych, ale nie pozwoli na iterowanie <m> po liczbach niecałkowitych."
		]
	},
]
