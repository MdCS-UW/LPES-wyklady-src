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

code_zmienne = r"""
#include <stdio.h>

int main() {
	int a = 15;
	float b = 13.3;
	
	return 0;
}
"""

code_zmienne_printf = r"""
#include <stdio.h>

int main() {
	int a = 15;
	float b = 13.3;
	
	printf("ABC %d %x %f\n", a, a, b);
	
	return 0;
}
"""

code_zmienne_napis = r"""
#include <stdio.h>

int main() {
	int a = 15;
	float b = 13.3;
	char *napis = "Ala ma bota";
	
	printf("ABC %d %x %f %s\n", a, a, b, napis);
	
	return 0;
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'C zmienne i operacje' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_zmienne, "c")],
			["printf", eduMovie.clear + eduMovie.code2console(code_zmienne_printf, "c")],
			["napis", eduMovie.clear + eduMovie.code2console(code_zmienne_napis, "c")],
		],
		'consoleDown': [
			[0.0, ""],
			["printf", eduMovie.runCode(code_zmienne_printf, args=["&& ./a.out"], cmd="gcc")],
			["napis", eduMovie.runCode(code_zmienne_napis, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'C wymaga jawnego deklarowania zmiennych z określeniem ich typu. <m>'
			'W przykładzie na ekranie widzimy deklarację zmiennej całkowitej <m> typu int oraz zmiennoprzecinkowej typu float. <m>'
			'C posiada kilka typów zmiennych całkowitych, różniących się <m> dostępnością liczb ujemnych oraz maksymalną wartością jaką mogą reprezentować <m>'
			'zmienne danego typu, związaną z ilością bitów przeznaczonych na daną zmienną. <m>'
			'Posiada też dwa typy zmiennoprzecinkowe różniące się precyzją, <m> wynikającą z ilości bitów użytych do zapisu takiej zmiennej. <mark name="printf" />'
			
			'Do wypisywania wartości liczbowych w C <m> korzysta się głównie z funkcji <printf>[print f]. <m>'
			'Jako pierwszy argument przyjmuje ona napis, w którym możemy użyć <m> specjalnych sekwencji zaczynających się od znaku procent pod które podstawiane <m> będą kolejno zmienne przekazane w następnych argumentach. <m>'
			'Użyta sekwencja ma związek z typem zmiennej <m> do wypisania oraz pożądanym formatem tego wypisania. <m>'
			
			'W przykładzie widocznym na ekranie procent d wypisuje liczbę całkowitą <m> jako dziesiętną, procent x jako szesnastkową, <m> a procent f wypisuje liczbę zmiennoprzecinkową. <m>'
			'Pełen opis sekwencji używanych w napisie formatującym <m> można znaleźć w dokumentacji funkcji <printf>[print f] w man <3>[trzy] <printf>[print f]. <m>'
			'Napisy formatujące używane w tej funkcji okazały się na tyle wygodne <m> że stały się pewnym standardem i dostępne są także <m> w wielu innych językach i bibliotekach. <m>'
			'''Przykładem może być chociażby <shell'owa>[szelowa] komenda <printf>[print f]. <mark name="napis" />'''
			
			'Zmienna może przechowywać oczywiście także napisy. <m>'
			'Służy do tego typ <char>[czar] gwiazdka, <m> ale o tym co to dokładnie jest dowiemy się w dalszej części zajęć. <m>'
			'Napisy są ciągami ujętymi w cudzysłowia i w przypadku C oraz C++ <m> są to czudzysłowy podwójne. <m>'
			'Cudzysłowa pojedyncze, czyli apostrofy mają inne znaczenie. <m>'
			
			'Jeżeli chcemy wstawić zmienną napisową <m> w ramach napisu formatującego w <printf>[print f] możemy użyć procent s. <m>'
			'Zmienną taką możemy też wypisać bezpośrednio z użyciem <printf>[print f] lub puts. <m>'
		]
	},
]

code_arytmetyka_A = r"""
#include <stdio.h>

int main() {
	int a = 15;
	float b = 13.3;
	
	printf("ABC %d %f %d\n", 7-9, a * b, a + 14);
	
	return 0;
}
"""

code_arytmetyka_B = r"""
#include <stdio.h>

int main() {
	int a = 15, c = 4;
	float b = 13.3;
	
	float x = a / c;
	float y = a / b;
	float z = 1 / 2;
	float q = 1 / 2.0;
	
	printf("ABC %f %f %f\n", x, y, z, q);
	return 0;
}
"""

code_arytmetyka_C = r"""
#include <stdio.h>

int main() {
	printf("ABC %d\n", /* komentarz blokowy, reszta z dzielenia: */ 8 % 3);
	
	/* komentarz
	   blokowy  */
	
	printf("%d\n", (13 + 1) * 2);
	return 0; // komentarz liniowy
	
	#if 0
	komemntarz oparty na
		poleceniach prepocesora
	#endif
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_arytmetyka_A, "c")],
			["artB", eduMovie.clear + eduMovie.code2console(code_arytmetyka_B, "c")],
			["artC", eduMovie.clear + eduMovie.code2console(code_arytmetyka_C, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_arytmetyka_A, args=["&& ./a.out"], cmd="gcc")],
			["artB", eduMovie.runCode(code_arytmetyka_B, args=["&& ./a.out"], cmd="gcc")],
			["artC", eduMovie.runCode(code_arytmetyka_C, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'W C możemy wykonywać operację arytmetyczne, <m> takie jak dodawanie, odejmowanie, czy mnożenie i zapisywane są one standardowo. <mark name="artB" />'
			
			'Na trochę więcej uwagi zasługuje operacja dzielenia. <m>'
			'C potrafi operować na liczbach zmienno przecinkowych <m> i potrafi poprawnie podzielić 2 na 3, <m>'
			'ale w C nie ma osobnych operatorów dzielenia całkowitego <m> i zmiennoprzecinkowego (jakie mieliśmy w Pythonie). <m>'
			'Użycie jednego lub drugiego wariantu dzielenia zależy od typów argumentów <m> – jeżeli zarówno dzielna jak i dzielnik są całkowite, to zastosowane zostanie <m> dzielenie całkowite i wynik będzie liczbą całkowitą. <m>'
			'Jeżeli choć jeden z argumentów jest liczbą zmiennoprzecinkową <m> to zastosowane zostanie dzielenie zmiennoprzecinkowe <m> i wynik też będzie liczbą zmiennoprzecinkową. <mark name="artC" />'
			
			'Operatorem reszty z dzielenia jest procent. <m>'
			'C zachowuje kolejność działań związaną z priorytetem operacji, <m> możemy wymuszać inną kolejność grupując operacje z użyciem nawiasów. <m>'
			'W niektórych przypadkach nawiasy stosowane są także zgodnie <m> z kolejnością działań w celu zwiększenia czytelności <m> lub eliminacji ostrzeżeń ze strony kompilatora. <m>'
			
			'Komentarze w C mogą występować w kilku postaciach – jako komentarz liniowy <m> zaczynający się od dwóch ukośników i trwający do końca linii <m>'
			'lub komentarz blokowy (mogący obejmować fragment linii lub wiele linii) <m> rozpoczynający się od  ukośnik gwiazdka i trwający do gwiazdka ukośnik. <m>'
			'Pierwotnie C nie posiadał komentarza liniowego, <m> został on przejęty z C++ i dodany do standardu C99. <m>'
			'Inną formą komentarza blokowego obejmującego wiele linii <m> jest użycie instrukcji pre-procesora typu if zero - endif. <m>'
		]
	},
]

code_logiczne_A = r"""
#include <stdio.h>

int main() {
	int a = 15;
	int x = (a <= 10);
	
	printf("%d %d\n", a, x);
	
	return 0;
}
"""

code_logiczne_B = r"""
#include <stdio.h>

int main() {
	int a = 15;
	int x = (a <= 10) && !( 13 > 0);
	
	printf("%d %d\n", a, x);
	
	return 0;
}
"""

code_bitowe = r"""
#include <stdio.h>

int main() {
	int a = 1 << 2;
	
	printf("%x %x %x\n", a, a & 1, a | 1);
	printf("%x %x %x\n", 5 ^ 1 , 0xf >> 2, ~a);
	
	return 0;
}
"""

code_rzut = r"""
#include <stdio.h>

int main() {
	int a = 13;
	
	printf("%f\n", a);
	printf("%f %f\n", (float)a, (float)a/3);
	
	return 0;
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_logiczne_A, "c")],
			["logB", eduMovie.clear + eduMovie.code2console(code_logiczne_B, "c")],
			["bitowe", eduMovie.clear + eduMovie.code2console(code_bitowe, "c")],
			["rzut", eduMovie.clear + eduMovie.code2console(code_rzut, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_logiczne_A, args=["&& ./a.out"], cmd="gcc")],
			["logB", eduMovie.runCode(code_logiczne_B, args=["&& ./a.out"], cmd="gcc")],
			["bitowe", eduMovie.runCode(code_bitowe, args=["&& ./a.out"], cmd="gcc")],
			["rzut", eduMovie.runCode(code_rzut, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'C pozwala nam na sprawdzanie warunków typu równość, nierówność, itd. <m>'
			'Zapis tych warunków jest standardowy i identyczny jak w Pythonie. <m>'
			'Wynik takiej operacji możemy zapisać do zmiennej typu całkowitego, <m> zero będzie odpowiadało fałszowi a wartość niezerowa (typowo jeden) prawdzie. <mark name="logB" />'

			'Możemy wykonywać także logiczne operacje and oraz or, <m> zapisywane są one odpowiednio przy pomocy dwóch znaków ampersand <m> i dwóch pionowych kresek (czyli tak jak było to w łączeniu poleceń w bashu). <m>'
			'Negację zapisujemy jako wykrzyknik. <mark name="bitowe" />'
			
			'C pozwala także na wykonywanie operacji logicznych <m> na poziomie poszczególnych bitów z użyciem operatorów bitowych. <m>'
			'Zapisywane są one tak jak w Pythonie, <m> natomiast ze względu na niskopoziomowość C są w nim dużo częściej stosowane. <m>'
			'Niestety <printf>[print f] w C nie oferuje wsparcia dla wypisywania w formacie bitowym, <m> zatem w takich zastosowaniach najczęściej jest stosowane wypisywanie szesnastkowe. <mark name="rzut" />'
			
			'W Pythonie do konwersji pomiędzy typami używaliśmy wywołań <m> konstruktora typu na który konwertowaliśmy daną zmienną. <m>'
			'W C bardzo proste konwersje mogą zachodzić automatycznie <m> (np. pomiędzy liczbami całkowitymi różnych typów) <m> lub mogą być realizowane z użyciem operatorów rzutowania. <m>'
			'Operatory te są postaci nazwy typu docelowego umieszczonego <m> w nawiasach poprzedzających zmienną innego typu. <m>'
			'Nie pozwalają one na zaawansowane konwersje <m> jak np. zamianę liczby na jej reprezentację napisową, <m>'
			'a jedynie na proste konwersje nakazujące <m> inną interpretację danych związanych z rzutowaną zmienną. <m>'
		]
	},
]
