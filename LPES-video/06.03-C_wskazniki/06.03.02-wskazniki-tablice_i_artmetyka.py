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

code_wsk_tab = r"""
#include <stdio.h>
#include <inttypes.h>

int main() {
  int32_t t[4] = {1, 8, 3, 2};
  int32_t *tt = t; // zauważ brak operatora pobrania adresu
  
  printf("%d %d\n", t[2], tt[2]);
  printf("%d %d\n", *(t + 2), *(tt + 2));
  printf("%p %p\n", tt, tt + 2);
}
"""

code_wsk_void = r"""
#include <stdio.h>
#include <inttypes.h>

int main() {
  int32_t a = 1013;
  void *b = &a;
  
  printf("%p %p\n", &a, b);
  printf("%p %p\n", &a+1, b+1);
  
  printf("%d %d %d\n", *(int32_t*)b, *(char*)b);
}
"""

code_byte_order = r"""
#include <stdio.h>
#include <inttypes.h>

int main() {
	uint16_t aa[4] = {0x1234, 0x5678, 0x9abc, 0xdeff};
	printf( "A: %x %x %x %x\n",
		(aa[0] >> 8) & 0xff, aa[0] & 0xff,
		(aa[1] >> 8) & 0xff, aa[1] & 0xff
	);
	
	uint8_t* bb = (uint8_t*) aa;
	printf( "B: %x %x %x %x\n",
		bb[0], bb[1],
		bb[2], bb[3]
	);
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'wskaźniki - tablice, arytmetyka, kolejnośc bajtów' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wsk_tab, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_wsk_tab, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Tablica tak naprawdę jest wskaźnikiem <m> i co więcej jest po prostu wskaźnikiem na pierwszy swój element. <m>'
			'Jak widzimy w przykładzie pokazanym na ekranie na wskaźnikach możemy <m> wykonywać operacje arytmetyczne takie jak dodawanie i odejmowanie. <m>'
			'Operacje te mają sens gdy wskaźnik wskazuje na jakiś zbiór zmiennych <m> zajmujących ciągły obszar pamięci, czyli właśnie np. tablicę. <m>'
			'Operacje te pozwalają dostać się do kolejnych, <m> bądź poprzednich zmiennych w tym obszarze. <m>'
			'Oczywiście operacje takie można też wykonać <m> również na wskaźnikach do zwykłych zmiennych, <m> jednak w większości przypadków nie mają one wtedy sensownego zastosowania. <m>'
			
			'Warto zauważyć że operator odwołania do n-tego elementu <m> tablicy w postaci nawiasu kwadratowego, <m>'
			'jest tym samym co operacja dodania n do wskaźnika na początek tablicy <m> i pobrania wartości na którą wskazuje tak uzyskany adres. <m>'
			'W rzeczywistości kompilator operator ten zamienia na taką operację <m> na wskaźnikach, co tłumaczy też dlaczego poprawnie działa indeks od tablica <m> – dodawanie liczb naturalnych jest przemienne. <m>'
			
			'Warto zauważyć że arytmetyka wskaźnikowa działa sprytnie, <m> gdyż zwiększenie wskaźnika typu int 32 o 2 nie spowodowało nam zwiększenia <m> adresu o 2, tylko o 2 razy rozmiar tego inta, czyli o osiem. <m>'
			'Takie działanie, obok wiedzy jak interpretować wartość wyłuskaną ze wskaźnika <m> są głównymi powodami dla których używa się wskaźników różnych typów, <m>'
			'bo przecież niezależnie od tego na jaki typ wskazują <m> są to adresy w tej samej pamięci. <m>'
			
			'W przykładzie tym celowo zostały użyte typy o jednoznacznie <m> określonej długości zdefiniowane w nagłówku <inttypes.h>[int types kropka h]. <m>'
			'Zamiast <int32_t>[int trzydzieści dwa t] moglibyśmy napisać tak jak wcześniej po prostu int, <m> ale jego rozmiar jest zależny od architektury i mogłoby się zdarzyć <m> że nie miałby 4 bajtów <m>(<32>[trzydziestu dwóch] bitów), tylko <np.>[na przykład] 2 bajty. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wsk_void, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_wsk_void, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Jeżeli potrzebujemy mieć wskaźnik na dowolny <m> typ danych stosuje się wskaźnik typu void. <m>'
			'Zwiększenie wskaźnika takiego typu o jeden <m> to zwiększenie adresu o jeden. <m>'
			'Nie możemy jednak bezpośrednio odwołać się do wartości wskazywanej <m> przez taki wskaźnik – musimy najpierw dokonać rzutowania na odpowiedni typ, <m>'
			'jeżeli dokonamy rzutowania na inny, <m> niewłaściwy typ to zwrócone dane mogą być niepoprawne. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_byte_order, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_byte_order, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Skoro zaczęliśmy używać rzutowania typów wskaźnikowych to zobaczmy <m> co się stanie jeżeli na tablicę liczb <16>[szesnasto] bitowych, <m> zaczniemy patrzeć jak na tablicę liczb <8>[ośmio] bitowych. <m>'
			'Zrobimy to na dwa sposoby <m> – z użyciem operacji bitowych oraz wykorzystując rzutowanie. <m>'
			'Pierwsza operacja działa chyba tak jak wszyscy się spodziewali – <m> jeżeli wypisujemy starsze <8>[osiem] bitów dostajemy dwie starsze cyfry szesnastkowe, <m>'
			'jeżeli wypisujemy młodsze osiem bitów to dostajemy dwie młodsze cyfry szesnastkowe. <m>'
			
			'Działanie drugiej operacji nie tylko jest nie oczywiste, <m> ale nawet niezdefiniowane przez standard. <m>'
			'Jest to jeden z licznych przypadków gdy twórcy języka C i C++ powiedzieli <m> że nie definiują danego zachowania i może ono być różne w zależności <m> np. od architektury, kompilatora czy systemu operacyjnego. <m>'
			
			'Zapewne większość osób intuicyjnie spodziewałaby się <m> że wynik będzie taki jak wcześniej czyli dostaniemy 12 34 56 i 78. <m>'
			'Jednak u większości osób które spróbowałyby uruchomić ten kod <m> wynik będzie inny – 34 12 78 i 56. <m>'
			'Wynika to z kolejności bajtów w liczbie wielobajtowej. <m>'
			'Istnieją dwa standardy – big endian i little endian. <m>'
			'W pierwszym z nich najbardziej znaczący bajt umieszczany jest jako pierwszy, <m> czyli tak jak ma to miejsce z cyframi w stosowanym na co dzień systemie pozycyjnym. <m>'
			'W drugim z nich najbardziej znaczący bajt umieszczany jest jako ostatni, <m> czyli kolejność bajtów jest odwrócona. <m>'
			'Najpopularniejsza aktualnie architektura komputerów domowych (i nie tylko), <m> czyli <x86>[iks osiem sześć] (względnie <amd64>[AMD sześćdziesiąt cztery]) stosuje właśnie little endian, <m> co tłumaczy ten dziwny wynik. <m>',
			'Procesory stosujące kolejność little endian to na przykład Motorola <68k>[sześćdziesiąt osiem tysięcy], <m> które były używane między innymi w komputerach domowych serii Amiga, <m>'
				'lub procesory <SPARC>[spark], na których oparte komputery używane są jeszcze w niektórych miejscach. <m>'
			'Jeżeli uruchomilibyśmy ten program na jednym z tych komputerów, to wynik miałby inną kolejność. <m>'
			'Niektóre procesory, na przykład ARM, mają możliwość programowej zmiany kolejności bajtów. <m>'
			'Konsekwencjami tej różnicy jest to że jeżeli wymieniamy informacje <m> w postaci binarnej pomiędzy różnymi systemami komputerowymi <m> to musimy ustalić jakiej kolejności bajtów używamy. <m>'
			'Stąd także na przykład w niektórych kodowaniach unicode takich jak <m> UTF-16 czy UTF-32 na początku pliku pojawiają się znaczniki <BOM>[byte order mark], <m> które służą właśnie do identyfikacji w kolejności bajtów. <m>'
			'W przypadku UTF-8 znacznik ten nie musi występować <m> (a nawet często uważa się że nie powinien) <m> ponieważ jest to kodowanie używające wartości jednobajtowych, <m>'
			'gdzie znaki wielobajtowe kodowane są tak jakby były one kolejnymi <m> znakami tekstu umieszczonymi na kolejnych pozycjach <m> i dodatkowo pierwszy bajt takiego znaku jest wyróżniony. <m>'
			
			'W większości protokołów sieciowych używane jest kodowanie big endian, <m> nazywane z tego względu także "network byte order". <m>'
		]
	},
]
