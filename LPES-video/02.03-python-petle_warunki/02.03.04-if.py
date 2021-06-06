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

code_if_A = r"""
a = 3
if a > 2:
    print("a>2", a)

a = 1
if a > 2:
    print("a>2", a)
"""

code_if_B = r"""
a = 1
if a > 2:
    print("a>2", a)
else:
    print("a<=2", a)
"""

code_if_C = r"""
a = 1
if a > 2:
    print("a>2", a)
elif a > 0:
    print("a>0", a)
else:
    print("a<=2", a)
"""

code_if_D = r"""
a = 3
if a > 2:
    print("a>2", a)
elif a == 3:
    print("a==3", a)
else:
    print("a<=2", a)
"""

code_if_E = r"""
for x in [1, 2, 3, 4, 5, 6]:
  print("start", x)
  if x == 2:
    continue
  if x == 4:
    break
  print("...")
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': '' },
	{ #  if cos: ... 
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console("while (a and x < 33) or not b:", "py")],
			["_if", eduMovie.clear + eduMovie.code2console(code_if_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			["_if", eduMovie.runCode(code_if_A, [], cmd="python3")],
		],
		'text' : [
			'Jak już widzieliśmy typ logiczny może być wykorzystany <m> w warunku pętli while i możemy tam umieszczać <m> skomplikowane wyrażenia logiczne, <m> a nie tylko proste nierówności. <mark name="_if" />'
			"Drugą instrukcją w której wykorzystujemy typ logiczny jest instrukcja if. <m>"
			"Pozwala ona na warunkowe wykonanie związanego z nią bloku kodu, <m> jeżeli podane wyrażenie logiczne (warunek) jest prawdziwe. <m>"
			'Instrukcja warunkowa if rozpoczyna się od słowa kluczowego if <m> po którym następuje warunek i dwukropek rozpoczynający blok kodu. <break time="200ms"/> <m>'
			'Podobnie jak w przypadku pętli while warunek <m> nie musi być ujęty w nawiasy, <m> ale ich napisanie nie jest błędem. <m>'
			"Istrukcja if posiada kilka wariantów związanych <m> z wystąpieniem lub nie opcjonalnych bloków. <m>"
		]
	},
	{ #  if cos: ... else: ...
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_if_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_if_B, [], cmd="python3")],
		],
		'text' : [
			"Do instrukcji if możemy dodać blok <else>[els] <m> zawierający instrukcje które będą wykonane <m> gdy warunek nie jest prawdziwy. <m>"
			"Należy zauważyć iż słowo kluczowe <else>[els] <m> występuje na tym samym poziomie wcięcia co if, <m> a po nim również mamy dwukropek rozpoczynający blok kodu. <m>"
		]
	},
	{ #  if cos: ... elif cos2: ... else: ...
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_if_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_if_C, [], cmd="python3")],
		],
		'text' : [
			"Pomiędzy blokiem kodu wykonywanym dla spełnionego warunku <m> a linią z <else>[els] możemy wstawić dodatkowe warunki do sprawdzenia <m> i bloki kodu do wykonania gdy warunki te będą prawdziwe. <m>"
			"Rozpoczynają się one od słowa kluczowego elif <m> po którym następuje wyrażenie logiczne i dwukropek <m> rozpoczynający blok kodu wykonywany gdy ten warunek jest prawdziwy. <m>"
		]
	},
	{ #  dwa pasujące
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_if_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_if_D, [], cmd="python3")],
		],
		'text' : [
			"Należy zauważyć że w ramach całej instrukcji if, elif, <else>[els] <m> wykonany będzie maksymalnie jeden blok kodu <m> związany z pierwszym spełnionym warunkiem <m>"
			"(pierwszym wyrażeniem logicznym będącym prawdą) <m> lub z <else>[els], jeżeli ten blok występuje a żaden z warunków nie był prawdą. <m>"
			"Warunki sprawdzane są w kolejności podanej w programie, a nie wg ich precyzyjności. <m>"
			"To programista musi zadbać, aby najpierw podać bardziej szczególne przypadki, <m> a dopiero po nich ogólne, które mogą je obejmować. <m>"
			"Jeżeli chcemy żeby bloki kodu były wykonywane przy spełnieniu warunku <m> bez względu na spełnienie lub nie innych warunków należy stosować osobne <m> instrukcje if, a nie konstrukcję if, elif. <m>"
		]
	},
	{ #  break continue
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_if_E, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_if_E, [], cmd="python3")],
		],
		'text' : [
			"Instrukcja if może być też wykorzystywana <m> do warunkowego przerywania pętli lub pomijania pewnych ich iteracji <m> z użyciem instrukcji break i continue. <m>"
			"Wykonanie instrukcji break powoduje przerwanie wykonywania pętli. <m>"
			"Natomiast wykonanie instrukcji continue powoduje przerwanie bieżącego kroku pętli <m> i przejście do następnego (jeżeli warunek pętli taki krok przewiduje. <m>"
			"W przykładzie widocznym na ekranie pominięte zostanie wypisanie <m> trzech kropek dla x równego dwa w związku z użyciem instrukcji continue. <m>"
			"Natomiast cała pętla zakończy się na x wynoszącym 4 <m> w skutek przerwania przez instrukcję break. <m>"
		]
	},
]

