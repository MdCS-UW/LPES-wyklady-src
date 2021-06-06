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

shenv = {
	"a":"17",
	"b":"abc def",
	"c":"xyz"
}

try: clipData
except NameError: clipData = []

endTitleSVG="JS.svg"

clipData += [
	{ 'title': [ "#05.1", "Wprowadzenie do", "programowania", "w bash'u"] },
	
	{ 'comment': 'zmienne' },
	{
		'console': [
			[0.0, ""],
			
			["vardef", eduMovie.runCommandString(r"a=17")],
			["vardef + 0.7", eduMovie.runCommandString(r'b="abc def"')],
			["vardef + 1.5", eduMovie.runCommandString(r"c=xyz")],
			
			["vardef2", eduMovie.runCommandString(r"d = 1", env=shenv)],
			["vardef2 + 0.8", eduMovie.runCommandString(r"d= 1", env=shenv)],
			["vardef2 + 1.9", eduMovie.runCommandString(r"d =1", env=shenv)],
			
			["echo1", eduMovie.runCommandString(r"echo $a", env=shenv)],
			["echo2", eduMovie.runCommandString(r"echo ${a}", env=shenv)],
			["echo3", eduMovie.runCommandString(r"echo $a_ABC", env=shenv)],
			["echo4", eduMovie.runCommandString(r"echo ${a}_ABC", env=shenv)],
			
			["echo5", eduMovie.runCommandString(r'echo "$a ${b} $c"', env=shenv)],
			["echo6", eduMovie.runCommandString(r"echo '$a ${b} $c'", env=shenv)],
		],
		'text' : [
			"Na standardową unixową powłokę zgodną z <sh>[es ha] (na przykład bash'a) <m> możemy patrzeć jak na język programowania. <m>"
			'Umożliwia ona definiowanie zmiennych, funkcji, <m> wykonywanie pętli, instrukcji warunkowych, itd. <mark name="vardef" />'
			
			'Zmienne definiujemy w sposób w miarę standardowy, <m> tak jak w wielu innych językach, <m> czyli nazwa zmiennej równa się wartość tej zmiennej. <mark name="vardef2" />'
			
			'Natomiast nietypowe jest to że nie możemy <m> wokół tego znaku równości wstawiać spacji, <m>'
				'czyli nie możemy napisać na przykład d spacja równa się spacja <1>[jeden], <itp>[i te pe]. <m>'
			'Bash w odróżnieniu od na przykład C, C++, <m> czy nawet Pythona jest bardzo wrażliwy na spację. <m>'
			'Wynika to z roli jaką spacja spełnia w poleceniach shellowych <m> – jest używana jako separator komendy od argumentów <m> i kolejnych argumentów od siebie na wzajem. <mark name="echo1" />'
			
			'Odwołanie do zmiennej odbywa się poprzez operator w postaci znaku dolara. <mark name="echo2" />'
			'Nazwę zmiennej po dolarze możemy ująć w klamerki, tak jak w widocznym przykładzie. <m>'
			'Są one potrzebne jeżeli bezpośrednio po zmiennej chcemy podać fragment napisu, <m> bez poprzedzającej spacji lub ujmowania go w cudzysłowa. <mark name="echo3" />'
			'Jeżeli nie zastosujemy klamerek bash będzie chciał użyć zmiennej <m> a podkreślnik ABC, która nie istnieje więc wypisze nam pusty napis. <mark name="echo4" />'
			'Użycie klamerek ogranicza nazwę zmiennej tylko do napisu w nich ujętego, <m> czyli wypisana zostanie zmienna a, a zaraz po niej napis. <m>'
			'Klamerki te mają też inne funkcje o których powiemy sobie później. <mark name="echo5" />'
			
			'Napis zawierający zmienne może zostać objęty cudzysłowem podwójnym, <m> który pozwoli przekazać go np. jako pojedynczy argument do jakiejś komendy, <m>'
				'ale jednocześnie pozwoli na interpretację odwołań do zmiennych. <mark name="echo6" />'
			
			'Użycie apostrofów (cudzysłowów pojedynczych) wyłączy <m> interpretację zmiennych w napisie. <m>'
			'Dlatego gdy na poprzednich zajęciach przekazywaliśmy kod programu do AWK, <m> czy wyrażenia regularne do grepa zabezpieczaliśmy je właśnie <m> apostrofami a nie cudzysłowami podwójnymi. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["unset", eduMovie.runCommandString(r"unset c; echo $c", env=shenv)],
			["export", eduMovie.runCommandString(r"""export a ;  bash -c 'echo "$a $b"'""", env={"a":"17"})],
			["specjalne", eduMovie.runCommandString(r"false ;  echo $? ;  echo $?", env=shenv)],
			["specjalne2", eduMovie.runCommandString(r"?=3 ; echo $?", env=shenv)],
		],
		'text' : [
			'Porównując typowanie w bashu do Pythona jest ono <m> wyraźnie mniej silne – standardowo wszystkie zmienne są napisami. <m>'
			'Ewentualna interpretacja jako coś innego ma miejsce <m> tylko w niektórych przypadkach odwołań do zmiennej. <m>'
			'Jak widzimy odwołania do wszystkich trzech naszych zmiennych <m> były jednakowe, pomimo że np. zmienna c nie była definiowana <m> z użyciem cudzysłowów, a zmienna a wydaje się być liczbą. <m>'
			'W tym miejscu należy też wspomnieć że w przypadku definiowania zmiennej b <m> musieliśmy użyć cudzysłowów, bo przypisywana wartość zawierała spacje. <mark name="unset" />'
			
			'Zmienną możemy usunąć używając polecenia unset, <m> któremu podajemy nazwę zmiennej. <mark name="export" />'
			"Jeżeli chcemy aby zmienna była widoczna przez programy <m> uruchamiane z naszej powłoki (w tym przez kolejne instancje bash'a, <m> odpowiedzialne np. za wykonywanie kodu skryptu uruchamianego z pliku) <m>"
				'należy ją wyeksportować za pomocą polecenia export nazwa zmiennej. <m>'
			
			'Typowo bash udostępnia także pewien zbiór predefiniowanych zmiennych <m> środowiskowych (takich jak np. path zawierający ścieżki wyszukiwania programów). <m>'
			'Operacje na nich odbywają się identycznie, <m> jak na zmiennych definiowanych przez nas. <m>'
			'Aby modyfikacje tych zmiennych wpływały na uruchamiane programy <m> należy je po takiej modyfikacji wyeksportować. <mark name="specjalne" />'
			
			'Bash zapewnia też zbiór zmiennych wbudowanych <m> (ustawianych automatycznie w związku z aktualnie wykonywanym kodem), <m>'
				'jak na przykład pytajnik, który przechowuje <m> kod powrotu ostatniego polecenia. <mark name="specjalne2" />'
			'Tym zmiennym nie możemy samodzielnie przypisywać wartości w sposób jawny. <m>'
		]
	},
]
