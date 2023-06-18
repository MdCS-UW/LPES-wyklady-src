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

code_if_1 = r"""
if [ $1 -lt 3 ]; then
	echo "$1 jest mniejsze od 3"
fi
"""

code_if_kot = r"""
if [ "$1" = "kot" -o "$1" = "pies" ]; then
	echo  "kot lub pies";
elif [ "$1" = "ryba" ];  then
	echo  "ryba"
else
	echo  "coś innego"
fi
"""

code_if_grep = r"""
if grep "$1" /etc/passwd  >/dev/null 2>&1; then
	echo "$1 jest w /etc/passwd"
else
	echo "$1 nie ma w /etc/passwd"
fi
"""

code_if_grep2 = r"""
grep "$1" /etc/passwd  >/dev/null 2>&1 && echo "$1 jest w /etc/passwd"
"""

code_if_not_grep = r"""
if ! grep "$1" /etc/passwd  >/dev/null 2>&1; then
	echo "$1 nie ma w /etc/passwd"
fi

grep "$1" /etc/passwd  >/dev/null 2>&1 || echo "$1 nie ma w /etc/passwd"
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'warunki' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
			["if1", eduMovie.clear + eduMovie.code2console(code_if_1, "sh")],
			["ifkot", eduMovie.clear + eduMovie.code2console(code_if_kot, "sh")],
			["ifgrep", eduMovie.clear + eduMovie.code2console(code_if_grep, "sh")],
			["ifgrep2", eduMovie.clear + eduMovie.code2console(code_if_grep2, "sh")],
			["ifnotgrep", eduMovie.clear + eduMovie.code2console(code_if_not_grep, "sh")],
		],
		'consoleDown': [
			[0.0, ""],
			["if1 + 1", eduMovie.runCode(code_if_1, [1], cmd="bash")],
			["if1 + 3", eduMovie.runCode(code_if_1, [7], cmd="bash")],
			["ifkot + 1", eduMovie.runCode(code_if_kot, ["pies"], cmd="bash")],
			["ifkot + 3", eduMovie.runCode(code_if_kot, ["ryba"], cmd="bash")],
			["ifkot + 5", eduMovie.runCode(code_if_kot, ["żółw"], cmd="bash")],
			["ifgrep + 1", eduMovie.runCode(code_if_grep, ["abc"], cmd="bash")],
			["ifgrep + 2", eduMovie.runCode(code_if_grep, ["root"], cmd="bash")],
			["ifgrep2 + 1", eduMovie.runCode(code_if_grep2, ["abc"], cmd="bash")],
			["ifgrep2 + 2", eduMovie.runCode(code_if_grep2, ["root"], cmd="bash")],
			["ifnotgrep + 1", eduMovie.runCode(code_if_not_grep, ["abc"], cmd="bash")],
			["ifnotgrep + 2", eduMovie.runCode(code_if_not_grep, ["root"], cmd="bash")],
		],
		'text' : [
			'W bashu mamy dwa typy instrukcji warunkowych <m> – if oraz case. <mark name="if1" />'
			
			'Instrukcja if rozpoczyna się słowem kluczowym if, <m> po którym występuje warunek zakończony średnikiem. <m>'
			'Tak samo jak w przypadku pętli while oceniany jest <m> kod powrotu polecenia pełniącego rolę warunku. <m>'
			'Następnie występuje słowo kluczowe then rozpoczynające blok kodu <m> związany z instrukcją if, blok ten kończy się słowem kluczowym fi. <mark name="ifkot" />'
			
			'Podobnie jak było to w Pythonie instrukcja ta może posiadać <m> blok else oraz bloki elif – tak jak pokazano to na ekranie. <mark name="ifgrep" />'
			
			'Instrukcji if możemy użyć także do warunkowego wykonywania jakiś <m> instrukcji w zależności od wyniku działania innego polecenia. <m>'
			'W pokazanym przykładzie używamy polecenia grep aby sprawdzić czy <m> pierwszy argument przekazany do skryptu występuje w pliku <passwd>[pass wu de]. <m>'
			'Standardowe wyjście i wyjście błędu grep przekierowane jest do </dev/null>[dev null] <m> aby grep jedynie zwracał kod powrotu nie wypisując nic na ekran. <m>'
			'Jeżeli grep zakończył się sukcesem, czyli znalazł szukany ciąg znaków <m> w pliku <passwd>[pass wu de] to wypisujemy odpowiedni komunikat. <mark name="ifgrep2" />'
			
			'Rolę instrukcji if może pełnić też poznany już podwójny ampersand <m> służący do łączenia poleceń w taki sposób że kolejne wykonywane <m> jest tylko gdy poprzednie zakończyło się sukcesem. <mark name="ifnotgrep" />'
			
			'Warunek w if może być zanegowany z użyciem wykrzyknika. <m>'
			'Jako równoważnik takiego zapisu możemy użyć dwóch pionowych kresek <m> do połączenia poleceń - drugie wykona się tylko gdy pierwsze zawiodło. <m>'
		]
	},
]

code_case = r"""
echo "argument: $1"
case $1 in
	kot | pies)
		echo  "kot"
		echo  "lub pies"
		;;
	"ryba")
		echo  "ryba"
		;;
	*)
		echo  "cos innego"
		;;
esac
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_case, "sh")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_case, ["ryba"], cmd="bash")],
			[1.0, eduMovie.runCode(code_case, ["kot"], cmd="bash")],
			[2.0, eduMovie.runCode(code_case, ["smok"], cmd="bash")],
		],
		'text' : [
			'Drugi typ instrukcji warunkowej to case. <m>'
			'Działa on trochę podobnie jak switch z C, <m> jednak w odróżnieniu od niego nie operuje na liczbach tylko na napisach. <m>'
			'Konstrukcja rozpoczyna się od słowa kluczowego case po którym występuje <m> jakaś wartość (typowo zmienna) która będzie dopasowywana do poszczególnych przypadków. <m>'
			'Po niej występuje słowo kluczowe in, <m> po którym rozpoczynamy wymienianie poszczególnych przypadków. <m>'
			
			'Każdy taki przypadek zaczyna się od podania wartości <m> która będzie porównywana z wartością zmiennej podanej przed in, <m>'
				'po czym następuje prawy nawias okrągły <m> i instrukcje związane z danym przypadkiem, rozdzielane od siebie średnikami <m> lub znakami nowej linii a zakończone podwójnym średnikiem. <m>'
			'Wartość może być podana w cudzysłowach lub bez nich <m> (chyba że musimy zabezpieczyć w niej jakieś znaki specjalne). <m>'
			'Możemy podać też kilka wartości rozdzielając je pojedynczą pionową kreską. <m>'
			'Wykonany będzie pierwszy w kolejności z pasujących przypadków. <m>'
			'Gwiazdka często używana w ostatnim przypadku oznacza dowolne dopasowanie, <m> czyli przypadek wykonywany domyślnie gdy inne nie pasuje (tak jak blok else). <m>'
			'Całość konstrukcji kończymy słowem kluczowym esac, czyli case pisanym od tyłu. <m>'
		]
	},
]
