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

code_args = r"""
#include <stdio.h>

int main(int argc, char* argv[]) {
	for (int i=0; i<argc; ++i)
		printf("%d : %s\n", i, argv[i]);
	
	return 12;
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'C main' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_args, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_args, args=[], cmd="gcc")],
			[5.0, eduMovie.runCommandString(r"./a.out; echo $?", cwd="/tmp")],
			[17.5, eduMovie.runCommandString(r"/tmp/a.out ab 'c d' 13", cwd="/tmp")],
		],
		'text' : [
			'Mówiliśmy już trochę na temat funkcji main, <m> od której rozpoczyna się wykonywanie naszego programu. <m>'
			'Nie wspomnieliśmy jednak o argumentach, które funkcja main może przyjmować. <m>'
			'Dwa pierwsze, najczęściej używane, są związane z obsługą linii poleceń. <m>'
			'Pierwszy, będący liczbą całkowitą, <m> informuje nas o liczbie argumentów przekazanych w linii poleceń. <m>'
			'Drugi, będący tablicą napisów o ilości elementów równej <m> pierwszemu argumentowi, zawiera te argumenty linii poleceń. <m>'
			
			'Dokładniej pierwszy argument to liczba argumentów plus jeden, <m> gdyż (jak widzimy) w zerowym elemencie tablicy argumentów znajduje się <m> nazwa bądź ścieżka użyta do uruchomienia naszego programu. <m>'
			
			'Argumenty funkcji main standardowo nazywane są <argc>[arg ce] i <argv>[arg v], <m> ale to są tylko nazwy zmiennych, więc możemy nazwać je dowolnie. <m>'
			
			'Korzystanie z argumentów linii poleceń to podstawowa metoda <m> wpływania na sposób działania uruchamianych programów. <m>'
			'Tak jak widzieliśmy na przykładzie różnych komend uniksowych, <m> korzystają one na ogół właśnie z argumentów, <m> a rzadko kiedy pytają się użytkownika o to co mają zrobić podczas pracy. <m>'
			'Na ogół standardowe wejście używane jest tylko do przekazywania <m> strumienia danych a nie poleceń, argumentów i opcji. <m>'
			'Tak jest wygodniej – łatwiej jest odpalić na przykład <cp>[ce pe] <m> na <100>[stu] plikach w pętli jeżeli podajemy mu je w linii poleceń, <m>'
			'niż gdyby <cp>[ce pe] pytało interaktywnie <m> "podaj nazwę pliku źródłowego", "podaj nazwę pliku docelowego" <m> i oczekiwało na wprowadzenie tych nazw na standardowym wejściu. <m>'
			
			'Pokazany przykład używa kodu powrotu <12>[dwanaście], <m> celem zademonstrowania, że to działa <m> (poprzednio używaliśmy tylko standardowego zera). <m>'
			'Nie rekomendujemy jednak zwracania kodu różnego od zera <m> w programie który zadziałał poprawnie. <m>'
		]
	},
]

code_env_A = r"""
#include <stdio.h>

int main(int argc, char* argv[], char *envp[]) {
	for (int i=0; envp[i]; ++i)
		printf("%d : %s\n", i, envp[i]);
}
"""

code_env_B = r"""
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
  printf("LANG ma wartość: %s\n", getenv("LANG"));
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_env_A, "c")],
			["envB", eduMovie.clear + eduMovie.code2console(code_env_B, "c")],
		],
		'consoleDown': [
			[0.0, ""],
			[0.3, eduMovie.runCode(code_env_A, args=["&& ./a.out"], cmd="gcc")],
			["envB", eduMovie.runCode(code_env_B, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Na niektórych systemach możemy skorzystać także <m> z <3>[trój] argumentowej wersji funkcji main. <m>'
			'Trzeci argument jest także tablicą napisów, <m> tyle że zawiera zmienne środowiskowe, czyli wszystkie zmienne wyeksportowane <m> przez powłokę która uruchomiła nasz program. <mark name="envB" />'
			
			'Pokazujemy to bardziej jako ciekawostkę i nie polecamy stosować tego <m> w praktyce – istnieją lepsze metody dostępu do zmiennych środowiskowych, <m>'
			'z użyciem odpowiednich funkcji zapewniających przenośność <m> i możliwość łatwego korzystania z nich także poza funkcją main. <m>'
			'Przykład z użyciem funkcji getenv jest pokazany na ekranie. <m>'
		]
	},
]
