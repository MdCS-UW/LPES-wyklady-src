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

code_fun_struct = r"""
#include <stdio.h>
struct Struktura {  int a, b;  };

void ff(int a, struct Struktura s) {
	printf("%d %d\n", a, s.a);
	a = 15;
	s.a = 17;
	printf("%d %d\n", a, s.a);
}
int main() {
	int x = 10;
	struct Struktura s;  s.a = 11;
	
	ff(x, s);
	printf("%d %d\n", x, s.a);
}
"""

code_fun_struct_ptr = r"""
#include <stdio.h>
struct Struktura {  int a, b;  };
void ff(int* a, struct Struktura* s) {
	printf("%d %d\n", *a, (*s).a);
	*a = 15;
	(*s).a = 17;
	printf("%d %d\n", *a, s->a);
}
int main() {
	int x = 10;
	struct Struktura s;  s.a = 11;
	ff(&x, &s);
	printf("%d %d\n", x, s.a);
}
"""

code_fun_struct_ptr_const_A = r"""
#include <stdio.h>
struct Struktura {  int a, b;  };

void ff(int* a, const struct Struktura* s) {
	printf("%d %d\n", *a, (*s).a);
	*a = 15;
	(*s).a = 17;
	printf("%d %d\n", *a, s->a);
}
int main() {
	int x = 10;
	struct Struktura s;  s.a = 11;
	
	ff(&x, &s);
	printf("%d %d\n", x, s.a);
}
"""

code_fun_struct_ptr_const_B = r"""
#include <stdio.h>
struct Struktura {  int a, b;  };

void ff(int* a, const struct Struktura* s) {
	printf("%d %d\n", *a, (*s).a);
	*a = 15;
	//(*s).a = 17;
	printf("%d %d\n", *a, s->a);
}
int main() {
	int x = 10;
	struct Struktura s;  s.a = 11;
	
	ff(&x, &s);
	printf("%d %d\n", x, s.a);
}
""" 

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'wskaźniki - argumenty funkcji' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fun_struct, "c")],
			["struct_ptr", eduMovie.clear + eduMovie.code2console(code_fun_struct_ptr, "c")],
			["const_ptr", eduMovie.clear + eduMovie.code2console(code_fun_struct_ptr_const_A, "c")],
			["const_ptr + 10", eduMovie.clear + eduMovie.code2console(code_fun_struct_ptr_const_B, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_fun_struct, args=["&& ./a.out"], cmd="gcc")],
			["struct_ptr", eduMovie.runCode(code_fun_struct_ptr, args=["&& ./a.out"], cmd="gcc")],
			["const_ptr", eduMovie.runCode(code_fun_struct_ptr_const_A, args=["&& ./a.out"], cmd="gcc")],
			["const_ptr + 10", eduMovie.runCode(code_fun_struct_ptr_const_B, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'W C zmienne do funkcji przekazywane są przez kopiowanie, <m> czyli tak jak było to w Pythonie dla obiektów nie modyfikowalnych. <m>'
			'W efekcie funkcja nie może modyfikować danych przekazywanych przez argumenty. <m>'
			'W C dotyczy to także złożonych zmiennych jak na przykład struktury, <m> ale nie tablice (gdyż te jak już wiemy są wskaźnikami). <mark name="struct_ptr" />'
			
			'Funkcje mogą przyjmować także wskaźniki i wtedy również otrzymują kopię, <m> lecz samego wskaźnika a nie danych na które wskazuje. <m>'
			'Pozwala to na modyfikowanie takich obiektów, <m> a także pozwala uniknąć kopiowania dużych obiektów przy wywołaniu funkcji. <m>'
			
			'Zamiast stosować operator wyłuskania zawartości wskazanej przez wskaźnik <m> w postaci gwiazdki i operator odwołania do pola struktury w postaci kropki, <m>'
			'co dodatkowo wymaga jeszcze użycia nawiasów, <m> możemy użyć operatora odwołania do pola struktury określonej wskaźnikiem <m> w postaci myślnik znak większości, jak pokazano to w drugim printf. <m>'
			'Różni się on od kropki tylko tym że zakłada iż po lewej jego stronie <m> jest wskaźnik na strukturę, a kropka zakłada że po jej lewej <m> stronie jest obiekt struktury (a nie wskaźnik). <mark name="const_ptr" />'
			
			'Jeżeli chcemy tylko uniknąć kopiowania możemy użyć dodatkowo <m> słowa kluczowego const, co zabezpieczy nas przed wieloma sytuacjami <m> przypadkowej modyfikacji takiej zmiennej. <m>'
			'Na const nie należy patrzeć jednak jako na coś co czyni naszą zmienną <m> całkowicie niepodatną na modyfikacje (jak na jakąś flagę read-only). <m>'
			'Const należy traktować jako wskazówkę dla kompilatora <m> i nie chroni on programisty przed własną nieostrożnością. <m>'
			'W wielu wypadkach aby pozbyć się modyfikator const z zmiennej <m> wystarczy wykonać odpowiednie rzutowanie. <m>'
		]
	},
]

code_fun_tab = r"""
#include <stdio.h>

void ff(int* a, int s) {
	for (int i=0; i<s; ++i) {
		*a = *a * 2;
		++a;
	}
}
int main() {
	int t[4] = {1, 8, 3, 2};
	printf("%p\n", t);
	ff(t, 4);
	printf("%p\n", t);
	for (int i=0; i<4; ++i) printf("%d ", t[i]);
	printf("\n");
}
"""

code_art_A = r"""
#include <stdio.h>

int main() {
	char* s ="ABCD";
	for(; *s; ++s) {
		printf("litera: %c\n", *s);
	}
}
"""

code_art_B = r"""
#include <stdio.h>

int main() {
	char* s = "AĄBCĆ€D";
	for(; *s; ++s) {
		printf("litera: %c", *s);
		while ((*(s+1) & 0xC0) == 0x80)
			printf("%c", *(++s));
		printf("\n");
	}
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fun_tab, "c")],
			["artA", eduMovie.clear + eduMovie.code2console(code_art_A, "c")],
			["artB", eduMovie.clear + eduMovie.code2console(code_art_B, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_fun_tab, args=["&& ./a.out"], cmd="gcc")],
			["artA", eduMovie.runCode(code_art_A, args=["&& ./a.out"], cmd="gcc")],
			["artB", eduMovie.runCode(code_art_B, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Tak samo jak każdy inny wskaźnik, do funkcji możemy przekazać także tablicę, <m> wraz z nią powinniśmy też przekazać rozmiar (chyba że jest powszechnie znany), <m> gdyż sama tablica nie trzyma takiej informacji. <m>'
			'W przykładzie pokazanym na ekranie widzimy że funkcja <m> zmodyfikowała zawartość przekazanej tablicy. <m>'
			'Funkcja zmodyfikowała też wartość przekazanego wskaźnika, jednak ta modyfikacja <m> nie jest widoczna na zewnątrz, bo funkcja operowała na swojej kopii wskaźnika. <m>'
			'Jeżeli chcielibyśmy móc modyfikować sam wskaźnik w funkcji, <m> tak aby zmiana ta była widoczna poza nią powinna ona otrzymać wskaźnik na wskaźnik. <m>'
			
			'Warto też zwrócić uwagę na użycie operatora plus plus do wskaźnika. <mark name="artA" />'
			'Jest to wygodne zwłaszcza przy napisach, <m> które (jak wiemy) są tablicami z informacją o swoim końcu zapisaną w treści. <m>'
			'W ich wypadku inkrementacja wskaźnika pozwala na iterowanie <m> po napisie bez użycia dodatkowej zmiennej. '
			'Warto też zwrócić uwagę na to, że warunkiem pokazanej pętli jest sama wartość pod wskaźnikiem, gdyż chcemy aby pętla zakończyła się gdy trafimy na koniec napisu oznaczony bajtem zero. <mark name="artB" />'
			'Kod ten można nawet łatwo rozbudować aby działał poprawnie <m> dla znaków kodowanych w UTF8, dodając wewnętrzną pętle, <m>'
			'która wypisze wszystkie bajty mające flagę <m> oznaczającą kontynuację rozpoczętego znaku przed znakiem nowej linii. <m>'
			'Zaznaczyć należy że jest to bardzo proste podejście, <m> nie weryfikujące poprawności kodowania UTF8. <m>'
		]
	},
]

code_zasieg_A = r"""
#include <stdio.h>

int main() {
  {
    char x =5;
    printf("%d\n", x);
  }
  // zmienna x nie jest już tutaj dostępna
  // printf("%d\n", x);
  // powyższa linia wywoła zatem błąd
}
"""

code_zasieg_B = r"""
#include <stdio.h>
#include <stdlib.h>

int main() {
  {
    char* x = malloc(10);
  }
  // pamięć przydzielona do wskaźnika x
  // jest nadal zaalokowana, ale nie umiemy
  // się do niej dostać ani jej zwolnić
  // bo straciliśmy wskaźnik
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_zasieg_A, "c")],
			["zasB", eduMovie.clear + eduMovie.code2console(code_zasieg_B, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_zasieg_A, args=["&& ./a.out"], cmd="gcc")],
			["zasB", eduMovie.runCode(code_zasieg_B, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'W C zasięg zmiennych ograniczany jest poprzez klamerki <m> – zmienne zdefiniowane wewnątrz bloku ujętego w klamerki <m> nie są dostępne poza tym blokiem. <m>'
			'Wraz z końcem bloku zmienne takie są usuwane <m> i zwalniana jest zajmowana przez nie pamięć. <m>'
			'Dotyczy to także zmiennych definiowanych wewnątrz funkcji <m> – nie są one dostępne poza tą funkcją. <mark name="zasB" />'
			
			'Natomiast jeżeli zaalokujemy pamięć w sposób jawny czyli na przykład <m> funkcją malloc (lub w C++ operatorem new) <m> to nie zostanie ona zwolniona wraz z końcem bloku. <m>'
			'W przykładzie widocznym na ekranie utracimy jedynie wskaźnik do niej, <m> gdyż zmienna wskaźnikowa x zostanie usunięta. <m>'
			
			'Sytuację taką określa się wyciekiem pamięci <m> – mamy zaalokowany fragment pamięci (który przez system operacyjny <m> jest traktowany jako zajęty, bo go nie zwolniliśmy), <m>'
			'ale nie możemy się do niego odwoływać ani nawet go zwolnić, <m> ponieważ straciliśmy wskaźnik do tego obszaru. <m>'
			
			'Pamięć alokowaną jawnie musimy również jawnie zwolnić, <m> w przeciwnym razie zostanie ona zwolniona <m> dopiero po zakończeniu działania całego programu. <m>'
			
			'Z użyciem wskaźników w C możemy przekazywać też funkcje do innych funkcji <m> jako ich argumenty, podobnie jak robiliśmy to w Pythonie. <m>'
			'Natomiast składnia tego jest na tyle potworna, że nie ma sensu jej omawiać, <m> czy nawet pokazywać na dzisiejszym wykładzie. <m>'
		]
	},
]
