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

code_struct = r"""
#include <stdio.h>

struct Struktura {
    int a, b;
    double c;
};

int main() {
    struct Struktura s;
    s.a = 13;
    s.c = 17.3;
    printf("%f\n", s.a + s.c);
}
"""

code_tabl_A = r"""
#include <stdio.h>

int main() {
    int t[4] = {1, 8, 3, 2};
    printf("%d -> \n", t[2]);
    t[2] = 55;
    printf("    %d \n", t[2]);
}
"""

code_tabl_B = r"""
#include <stdio.h>

int main() {
    int t[4] = {1, 8, 3, 2};
    printf("%d \n", 2[t]);
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'C funkcje' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
			["stru", eduMovie.clear + eduMovie.code2console(code_struct, "c")],
		],
		'consoleDown': [
			[0.0, ""],
			["stru", eduMovie.runCode(code_struct, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'C pozwala też na definiowanie bardziej złożonych struktur danych <m> takich jak na przykład tablice i struktury. <mark name="stru" />'
			
			'Struktura jest złożonym typem danych <m> służącym do grupowania powiązanych ze sobą logicznie zmiennych. <m>'
			'Zmienne wchodzące w skład struktury (czyli pola) <m> identyfikowane są nazwami i mogą być różnych typów. <m>'
			'Struktura zajmuje ciągły obszar pamięci, <m> w którym umieszczane są wartości kolejnych pól. <m>'
			
			'Definicje struktury rozpoczynamy od słowa kluczowego struct <m> po którym podajemy jej nazwę, a następnie w ramach <m> bloku ujętego w nawiasach klamrowych podajemy definicje kolejnych pól. <m>'
			'Utworzenie zmiennej której typem jest struktura wymaga również <m> użycia słowa kluczowego struct i nazwy tej struktury <m> (chyba że zrobimy odpowiednią definicję typu z użyciem <typedef>[type-def]). <m>'
			'Odwołania do pól składowych struktury realizowane są z użyciem kropki <m> i nazwy tego pola (podobnie jak było to w przypadku pól składowych klas w Pythonie). <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_tabl_A, "c")],
			["tablB", eduMovie.clear + eduMovie.code2console(code_tabl_B, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_tabl_A, args=["&& ./a.out"], cmd="gcc")],
			["tablB", eduMovie.runCode(code_tabl_B, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Kolejnym przykładem zmiennych bardziej złożonych <m> z których możemy korzystać w C są tablice. <m>'
			'Podobnie jak struktura jest to ciągły obszar pamięci, <m> jednak w odróżnieniu od struktury wszystkie elementy tablicy są takiego samego typu, <m> a odwołujemy się do nich z użyciem numerycznego indeksu a nie nazwy. <m>'
			
			'Tablice definiujemy poprzez określenie typu elementu tej tablicy, <m> po którym podajemy nazwę tablicy oraz ilość elementów w nawiasach kwadratowych. <m>'
			'Możemy od razu określić wartości tych elementów podając je <m> w nawiasach klamrowych po znaku równości, ale nie jest to wymagane. <m>'
			
			'Do elementu tablicy możemy odwołać się poprzez podanie <m> po nazwie zmiennej związanej z tablicą <m> numeru tego elementu w nawiasach kwadratowych. <m>'
			'Elementy numerujemy od zera. <m>'
			
			'Możemy odwoływać się do niezainicjalizowanych elementów, <m> ale musimy pamiętać że mogą być tam śmieci. <m>'
			'Zarówno w przypadku tablic jak i struktur nie możemy założyć, <m> że po ich utworzeniu elementy będą zainicjalizowane zerami, <m> jeżeli nie robimy tego jawnie. <m>'
			'C nie zeruje pamięci dla (zdecydowanej większości) zmiennych, <m> jeżeli potrzebujemy takiego wyzerowania musimy sami o nie zadbać. <mark name="tablB" />'
			
			'Jako ciekawostkę można wspomnieć że działanie <m> operatora nawiasu kwadratowego jest przemienne <m>'
				'– to znaczy możemy napisać tablica od index lub index od tablica <m> i w obu przypadkach zadziała to poprawnie i będzie poprawne składniowo. <m>'
			'A dlaczego tak jest to dowiemy się jeszcze dzisiaj. <m>'
		]
	},
]


code_nap_A = r"""
#include <stdio.h>
#include <string.h>

int main() {
    char* a="ABCdef";
    printf("%s %c == %d\n", a, a[1], a[1]);
    printf("długość: %d\n", strlen(a));
}
"""

code_nap_B = r"""
#include <stdio.h>

int main() {
    int a='A';
    printf("%c == %d\n", a, a);
}
"""

code_nap_C = r"""
#include <stdio.h>
#include <string.h>

int main() {
    char* a="ĄBĆ";
    printf("%c%c %c\n", a[0], a[1], a[2]);
    printf("%c %c %c\n", a[0], a[1], a[2]);
    printf("długość: %d\n", strlen(a));
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_nap_A, "c")],
			["napB", eduMovie.clear + eduMovie.code2console(code_nap_B, "c")],
			["napC", eduMovie.clear + eduMovie.code2console(code_nap_C, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_nap_A, args=["&& ./a.out"], cmd="gcc")],
			["napB", eduMovie.runCode(code_nap_B, args=["&& ./a.out"], cmd="gcc")],
			["napC", eduMovie.runCode(code_nap_C, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Napisy w języku C, o których już wspomnieliśmy, <m> są w istocie tablicami bajtów. <m>'
			'Tak jak tablice, tak również napisy indeksujemy od zera. <m>'
			'Jako że tablica w C nie przechowuje swojego rozmiaru, <m> to koniec napisu musi być w jakiś sposób oznaczany. <m>'
			'Jest to realizowane poprzez wystąpienie bajtu o wartości zero, <m> nazywanego znakiem <NULL>[nul] informującego że ciąg znakowy (napis) się skończył. <m>'
			
			'Taki sposób przechowywania informacji o długości napisu powoduje, <m> że funkcja <strlen>[STR-len] zwracająca długość napisu jest dość kosztowna czasowo, <m>'
				'gdyż musi przeczytać każdy bajt w napisie, <m> aż trafi na taki o wartości zero. <m>'
			'Bajt ten nie jest wliczany do wyniku tej funkcji. <m>'
			
			'Jeżeli znaki w naszym napisie są kodowane jednobajtowo <m> to każdy element tablicy odpowiada jednemu znakowi. <m>'
			'Taki pojedynczy znak możemy wypisać przy pomocy funkcji printf <m> jako jego numer lub jako znak (podając napis formatujący %c). <mark name="napB" />'
			
			'Apostrofy w C konwertują podany w nich znak na jego wartość numeryczną. <m>'
			'Jest to proste dopóki każdy znak odpowiada jednemu bajtowi. <mark name="napC" />'
			
			'Jednak jako że żyjemy w pierwszej połowie dwudziestego pierwszego wieku <m> to powszechne (zwłaszcza w świecie unixa) są kodowania wielobajtowe <m> takie jak na przykład UTF8, <m>'
			'gdzie jeden znak zajmuje od jednego do sześciu bajtów. <m>'
			'W takiej sytuacji należy patrzeć raczej na znaki jako podnapisy <m> (czyli też tablice) niż na pojedyncze bajty. <m>'
			
			'Jest to kolejne utrudnienie w poznaniu długości napisu, <m> wspomniana funkcja zwracająca długość napisu liczy bajty w napisie, <m> a nie znaki, a tych może być mniej niż bajtów. <m>'
			
			'W przykładzie na ekranie widzimy że wyłuskane dwa bajty z napisu <m> dają poprawny znak tylko jeżeli są wypisywane bezpośrednio po sobie. <m>'
			'Jeżeli znajdzie się coś pomiędzy nimi, lub zabraknie jakiegoś bajtu <m> wchodzącego w skład znaku UTF8 to nie zostanie on wypisany <m> lub mogą zostać wypisane jakieś krzaczki. <m>'
			'Biblioteki weryfikujące poprawność kodowania UTF8 <m> mogą także zgłosić błąd na takim znaku. <m>'
			'Dlatego modyfikując takie ciągi należy zwracać uwagę aby nie trafić <m> wewnątrz pod-ciągu opisującego jeden znak <m> (co akurat w UTF8 jest dość łatwo sprawdzić odpowiednią maską bitową). <m>'
		]
	},
]
