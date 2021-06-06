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
#include <stdio.h>

int main() {
	for (int i=0; i<12; ++i) {
		printf("%d ", i);
	}
	printf("\n");
}
"""

code_for_B = r"""
#include <stdio.h>

int main() {
	int i, j;
	for (j=1, i=0; i<12 && j<30; ++i, j=j*i) {
		printf("%d ", i);
	}
	printf("j=%5\n", j);
}
"""

code_for_C = r"""
#include <stdio.h>

int main() {
	int i=0, j=1;
	for (; i<12 && j<30; ++i, j=j*i) {
		printf("%d ", i);
	}
	printf("j=%5\n", j);
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'C C++ pętle warunki' },
	{
		'console': [
			[0.0, ""], # TODO może jakaś ilustracja ?
		],
		'text' : [
			'Zanim przejdziemy do omówienia konstrukcji składniowych takich jak <m> pętle i warunki warto powiedzieć trochę o technicznym tle ich działania. <m>'
			
			'Wiemy już że kod programu w C rozpoczyna się od funkcji main. <m>'
			'Wiemy także iż C jest kompilowany do kodu maszynowego, <m>'
			'czyli przyjazne programiście konstrukcje składniowe, <m> nazwy zmiennych, <itp.>[i tym podobne] zamieniane są na numeryczne identyfikatory <m> instrukcji, rejestrów, adresów w pamięci zrozumiałe dla procesora. <m>'
			
			'Procesor posiada coś takiego jak licznik programu <m> w którym trzyma adres kolejnej instrukcji do wykonania. <m>'
			'Jeżeli wykonujemy pętle to na końcu pętli <m> wykonywany jest skok do jej początku. <m>'
			"Jeżeli wykonujemy instrukcję if to w zależności od wyniku <m> sprawdzenia warunków wykonywany może być skok do kolejnego warunku <m> else if, bloku else lub za blok kodu związany z if'em. <m>"
			'Realizacja tych skoków to właśnie <m> warunkowa modyfikacja wartości tego licznika <m>'
			'– załadowanie do niego adresu pamięci pod którym jest cel naszego skoku <m> (np. początek pętli) zamiast prostego zwiększenia licznika o jeden <m> celem przejścia do kolejnej instrukcji. <m>'
			
			'Na większości architektur pętla jest instrukcją złożoną <m> realizowaną jako zestaw instrukcji <m> (na przykład inkrementacji zmiennej, sprawdzania warunku, skoku). <m>'
			'Niektóre procesory mogą mieć na przykład pętle typu "powtórz n razy" <m> realizowane sprzętowo przy pomocy pojedynczej instrukcji <m> – jest to częste w architekturach DSP dedykowanych cyfrowemu przetwarzaniu sygnałów. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_for_A, "c")],
			["forB", eduMovie.clear + eduMovie.code2console(code_for_B, "c")],
			["forC", eduMovie.clear + eduMovie.code2console(code_for_C, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_for_A, args=["&& ./a.out"], cmd="gcc")],
			["forB", eduMovie.runCode(code_for_B, args=["&& ./a.out"], cmd="gcc")],
			["forC", eduMovie.runCode(code_for_C, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Na ekranie widzimy jedną z pętli oferowanych przez język C, jest to pętla for. <m>'
			'W C mamy do dyspozycji trójargumentową pętlę for realizującą tak zwaną pętlę ogólną. <m>'
			'Nie mamy pętli iterującej po elementach jakiejś kolekcji, <m> czyli pętli typu for each takiej jak for znany z Pythona. <m>'
			
			'Struktura tej pętli jest taka że po słowie kluczowym for <m> w nawiasach okrągłych mamy 3 grupy instrukcji rozdzielane średnikami. <m>'
			'Najpierw rzeczy wykonywane przed rozpoczęciem pętli, dostępne w ramach tej pętli. <m>'
			'W widocznym przykładzie zmienna <i>[I] będzie dostępna <m> jedynie wewnątrz pętli, poza pętlą nie będzie zdefiniowana. <m>'
			'Drugą grupę stanowi warunek który jest sprawdzany przed <m> rozpoczęciem każdego obiegu pętli i od jego prawdziwości <m> zależy to czy obieg ten się rozpocznie, czy też pętla się zakończy. <m>'
			'Trzecią, ostatnią grupą są instrukcje wykonywane na końcu <m> każdego obiegu pętli (przed sprawdzeniem warunku dla następnego obiegu) <mark name="forB" />'
			
			'W pierwszej i ostatniej grupie możemy podać więcej instrukcji, <m> aby np. iterować po dwóch zmiennych, w takiej sytuacji oddzielamy je przecinkami. <m>'
			'Zmienne używane w pętli mogą być zadeklarowane także na zewnątrz pętli <m> (w starszych wersjach C nawet musiały być). <m>'
			'Pozwala to na poznanie, użycie ich wartości, <m> która przerwała obieg pętli. <mark name="forC" />'
			
			'Jeżeli mamy zmienne zainicjalizowane przed pętlą <m> to pierwszy blok może pozostać pusty. <m>'
			
			'Można używać i++ bądź ++i, natomiast ++i jest szybsze <m> z tego względu że jest prostszą operacją dla komputera. <m>'
			'Bo to tak naprawdę jest to zwiększ wartość i podstaw tą nową wartość, <m> albo zwiększ wartość ale podstaw nadal starą wartość. <m>'
			
			'W kodzie prezentowanych tutaj przykładów <m> pominięte zostało zwracanie wartości z funkcji main, <m>'
			'jest to dopuszczalne w nowszych wersjach C i C++ <m> – w takiej sytuacji zwrócone będzie zero. <m>'
		]
	},
]

code_if_A = r"""
#include <stdio.h>

int main() {
	for (int i=0; i<12; ++i) {
		if (i==4) continue;
		printf("%d ", i);
	}
	printf("\n");
}
"""

code_if_B = r"""
#include <stdio.h>

int main() {
	for (int i=0; i<12; ++i) {
		if (i==4) {
			continue;
		} else if (i==2) {
			printf("\n i było dwa! \n");
			continue;
		} else {
			printf(". ");
		}
		printf("%d ", i);
	}
	printf("\n");
}
"""

code_while = r"""
#include <stdio.h>

int main() {
	int i = 4;
	
	while (i>0) {
		printf(" b: %d\n", --i);
	}
	
	do {
		printf(" c: %d\n", ++i);
	} while (i<2);
}
"""

code_switch = r"""
#include <stdio.h>
int main() {
	int i = 4;
	switch(i) {
		case 1:
			puts("i==1");
			break;
		case 2:
		case 3:
			puts("i==2 lub i==3");
			break;
		default:
			puts("i!=1,2,3");
			break;
	}
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_if_A, "c")],
			["ifB", eduMovie.clear + eduMovie.code2console(code_if_B, "c")],
			["whileA", eduMovie.clear + eduMovie.code2console(code_while, "c")],
			["switchA", eduMovie.clear + eduMovie.code2console(code_switch, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_if_A, args=["&& ./a.out"], cmd="gcc")],
			["ifB", eduMovie.runCode(code_if_B, args=["&& ./a.out"], cmd="gcc")],
			["whileA", eduMovie.runCode(code_while, args=["&& ./a.out"], cmd="gcc")],
			["switchA", eduMovie.runCode(code_switch, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'W C możemy też korzystać z instrukcji warunkowej if. <m>'
			'Działa ona tak jak w Pythonie tyle że warunek zapisywany musi być <m> w nawiasach okrągłych, bloki wydzielane są klamerkami a nie wcięciami, <m> a dla bloku złożonego z jednej instrukcji mogą być one pominięte. <m>'
			
			'Podobnie jak w Pythonie możemy także używać słów kluczowych <m> break i continue do warunkowego pomijania <m> kroku iteracji lub przerwania pętli. <m>'
			'W pętli for continue realizuje skok do instrukcji inkrementacyjnych <m> (czyli trzeciego bloku podanego w nawiasach po for), <m> po których następuje sprawdzenie warunku <m> i ewentualne rozpoczęcie następnego obiegu pętli. <m>'
			'Natomiast break realizuje skok do pierwszej instrukcji za pętlą. <mark name="ifB" />'
			
			'Oczywiście możemy także tworzyć bardziej rozbudowane instrukcje if, <m> zawierające bloki else i else if. <m>'
			'Działają one tak samo jak te w Pythonie z dokładnością do różnic <m> składniowych – nawiasy, else if zamiast elif, itd. <mark name="whileA" />'
			
			'Język C oferuje nam także pętlę while, <m> działającą tak samo jak pętla while z Pythona <m> oraz rzadko stosowaną pętlę <do>[du] while, <m>'
				'która warunek sprawdza po wykonaniu bloku instrukcji <m> a nie przed (czyli blok wykona się co najmniej jeden raz). <mark name="switchA" />'
			
			'Mamy także do dyspozycji, instrukcję switch, która jest wydajniejszym <m> odpowiednikiem if - else if, ale dostępnym jedynie dla przypadku sprawdzania <m> czy dana zmienna całkowita ma jedną z podanych wartości. <m>'
			'Badana zmienna podawana jest w nawiasach po switch, <m> a kolejne przypadki rozpoczynają się od słowa kluczowego case, <m> po którym następuje wartość porównywana i dwukropek. <m>'
			'Przypadki kończone są słowem kluczowym break, <m> jeżeli ono nie wystąpi wykonywanie kodu przejdzie płynnie <m> do następnego przypadku – tak jak w prezentowanym przykładzie <m> ma to miejsce dla wartości dwa. <m>'
			'Warto zauważyć podobieństwo do case z basha. <m>'
		]
	},
]
