# Copyright (c) 2020-2022 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2022 Robert Ryszard Paciorek <rrp@opcode.eu.org>
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

code_argv_A = r"""
import sys
print(sys.argv)
"""

code_argv_B = r"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
  '-v', "--verbose", action="store_true",
  help='opcja typu przełącznik'
)
parser.add_argument(
  'ARG', nargs='?',
  help='argument pozycyjny (opcjonalny)'
)
args = parser.parse_args()
print(args)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#02.6", "Python:", "argumenty", "linii poleceń" ] },
	
	{ 'comment': 'argumenty linii poleceń' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_argv_A, "py")],
			["argparse", eduMovie.clear + eduMovie.code2console(code_argv_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_argv_A, ["argument1", "--opcja", "argument2"], cmd="python3")],
			["argparse", eduMovie.prompt() + "python3 przykład.py --help"],
			["argparse + 3.0", eduMovie.runCode(code_argv_B, ["--help"], cmd="python3")],
			["argparse + 8.0", eduMovie.runCode(code_argv_B, ["-v", "aa"], cmd="python3")],
		],
		'text' : [
			'Standardowym sposobem przekazywania opcji i danych do programów, <m> z którym spotkaliśmy się już przy omawianiu poleceń unixowych, <m> jest podawanie ich jako argumentów linii poleceń. <m>'
			'Takie podejście, w odróżnieniu od interaktywnego odpytywania <m> użytkownika o kolejne opcje i wczytywania ich "z klawiatury", <m>'
				'pozwala na łatwe używanie programu w skryptach <m> i dzięki temu automatyzację wykonywanych czynności. <m>'
			'Także tworzone przez nas programy pythonowe <m> mogą przyjmować w ten sposób opcje i argumenty. <m>'
			'Aby mieć dostęp do listy argumentów przekazanych w linii poleceń <m> należy skorzystać z predefiniowanej listy argv dostępnej w module sys. <mark name="argparse" />'
			
			'Jeżeli w naszym programie chcemy korzystać z opcji <m> w standardowej unixowej notacji, czyli takich z myślnikami, <m> to możemy do ich przetwarzania skorzystać z modułu <argparse>[arg parse].'
			'Na ekranie widzimy prosty przykład jego użycia. <m>'
			'Więcej szczegółów jak zwykle można znaleźć w dokumentacji. <m>'
		]
	},
]
