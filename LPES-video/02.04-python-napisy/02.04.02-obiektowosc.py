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

code_metody_A = r"""
a="napis"

# zmienna a jest obiektem klasy str, co możemy sprawdzić:
print(type(a))

# możemy uruchomić na nim metody tej klasy – na przykład:
print(a.upper())

# wywołanie konstruktora klasy str od wartości numerycznej
# zwróci jej reprezentację napisową w systemie dziesiętnym
print(a + str(12))
"""
try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'obiektowość' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_metody_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_metody_A, [], cmd="python3")],
		],
		'text' : [
			"Jak być może dało się już zauważyć <m> wszystkie podstawowe typy w Pythonie są klasami, <m> a wszystkie zmienne obiektami pewnych klas. <m>"
			"Związane z tym jest między innymi to <m> że posiadają one metody służące do operowania na nich. <m>"
			"Metodą nazywamy funkcję związaną z danym typem <m> i wykonywaną na obiekcie tego typu. <m>"
			"Zapisywane jest to z użyciem nazwy zmiennej związanej z danym obiektem, <m> kropki, nazwy metody i nawiasów okrągłych które <m> mogą zawierać dodatkowe argumenty. <m>"
			"Jeżeli chcemy korzystać z metod jakiegoś typu <m> warto sprawdzić help na jego temat, <m> bo uczenie się na pamięć wszystkich metod <m> danego typu niekoniecznie ma sens. <m>"
			
			"Klasy posiadają również konstruktory, <m> które możemy wywołać używając nazwy danej klasy jak funkcji <m> i użyć np. do konwersji pomiędzy różnymi typami. <m>"
			"Jak już wiemy wszystkie nazwy w Pythonie <m> żyją w jednym świecie, dotyczy to też nazw klas. <m>"
			"Dlatego warto uważać aby nie nazywać swoich zmiennych <m> zarówno tak jak nazywają się wbudowane funkcje, <m> ani tak jak nazywają się wbudowane typy danych <m> (takie jak int, bool, <str>[S T R], float i tak dalej), <m>"
			"gdyż może to utrudnić korzystanie z nich <m> (a jak zrobimy to odpowiednio skutecznie to wręcz uniemożliwić dalsze działanie programu). <m>"
		]
	},
]

