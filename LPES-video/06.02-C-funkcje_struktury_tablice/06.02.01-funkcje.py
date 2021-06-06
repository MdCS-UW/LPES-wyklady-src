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

code_fun_A = r"""
#include <stdio.h>

void f1() {
	puts("Witaj Świecie");
}

int main() {
	f1();
}
"""

code_fun_B = r"""
#include <stdio.h>

int f1() {
	puts("Witaj Świecie");
	return 2;
}

int main() {
	int x = f1();
	printf("x=%d\n", x);
	
	f1();
}
"""

code_fun_C = r"""
#include <stdio.h>

int f1(int a, float b) {
	puts("Witaj Świecie");
	return 2*a + b;
}

int main() {
	int a = 3;
	int x = f1(a, 1.3);
	printf("x=%d\n", x);
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#06.2", "Funkcje, struktury", "i tablice w C", "" ] },
	
	{ 'comment': 'C funkcje' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fun_A, "c")],
			["funB", eduMovie.clear + eduMovie.code2console(code_fun_B, "c")],
			["funC", eduMovie.clear + eduMovie.code2console(code_fun_C, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_fun_A, args=["&& ./a.out"], cmd="gcc")],
			["funB", eduMovie.runCode(code_fun_B, args=["&& ./a.out"], cmd="gcc")],
			["funC", eduMovie.runCode(code_fun_C, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'C oczywiście pozwala nam na definiowanie własnych funkcji. <m>'
			'Robimy to poprzez zapis: typ zwracany przez daną funkcję, <m> nazwa tej funkcji, nawiasy okrągłe oraz instrukcje, <m> które mają być wykonane w ramach funkcji ujęte w klamerki. <m>'
			'Użyty w przykładzie typ void oznacza że funkcja nie zwraca wartości. <m>'
			
			'Wywołanie funkcji odbywa się poprzez podanie jej nazwy <m> po której następują nawiasy okrągłe. <mark name="funB" />'
			
			'Jeżeli chcielibyśmy żeby nasza funkcja zwracała jakąś wartość to używamy return. <m>'
			'Wartość zwracaną przez funkcję możemy odebrać i na przykład zachować <m> w jakiejś zmiennej, możemy też ją zignorować. <mark name="funC" />'
			
			'Funkcje mogą też przyjmować argumenty. <m>'
			'Zmienne pod które zostaną podstawione argumenty zapisujemy <m> w nawiasach okrągłych po nazwie funkcji w jej definicji. <m>'
			'Przed nazwami zmiennych podajemy ich typy, <m> a kolejne zmienne rozdzielamy przecinkami. <m>'
			
			'Argumenty przekazywane do funkcji podajemy w nawiasach okrągłych <m> związanych z wywołaniem tej funkcji i także rozdzielamy je przecinkami. <m>'
		]
	},
]
