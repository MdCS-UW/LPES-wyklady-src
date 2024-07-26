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

code_obiektowe = r"""
#include <iostream>
#include <stdint.h>

struct NazwaStruktury {
    // pola składowe
    int a;
    std::string d;
    
    // zmienna statyczna, wspólna dla wszystkich obiektów tej klasy
    static int x;
    
    // stała
    static const int y = 7;
    
    // pola binarne (jedno i trzy bitowe)
    uint8_t mA :1;
    uint8_t mB :3;
    
    // metody składowe
    void wypisz() {
        std::cout << " a=" << a << " d=" << d << "\n";
    }
    
    // deklaracja metody, definicja musi być podana gdzieś indziej
    int getSum(int b) ;
    
    /// metody statyczna
    static void info() {
        std::cout << "INFO\n";
    }
    
    // konstruktor i destruktor
    NazwaStruktury(int aa = 0) {
        std::cout << "konstruktor\n";
        a = aa;
        d = "abc ...";
    }
    ~NazwaStruktury() {
        // potrzebny gdy klasa tworzy jakieś
        // obiekty które nalezy usuwać, itp
        std::cout << "destruktor\n";
    }
};

// definicja zmiennej statycznej z nadaniem jej wartości
// jest to niezbędne aby była ona widoczna ...
int NazwaStruktury::x = 13;

// wcześniej zdeklarowane metody możemy definiować także poza deklaracją klasy
int NazwaStruktury::getSum(int b) {
    return a + b;
}

int main() {
    // korzystanie ze struktur
    NazwaStruktury s;
    s.a = 45;
    s.wypisz();

    // korzystanie z metod statycznych
    NazwaStruktury::info();
    // a także poprzez obiekt danej klasy
    s.info();

    // "manualna" alokacja pamięci dla struktury
    NazwaStruktury* sp = new NazwaStruktury();

    sp->wypisz();

    delete sp;
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#06.4", "", "Kilka słów o C++", "" ] },
	
	{ 'comment': 'C++ intro' },
	{
		'image': [
			[0.0, ""],
		],
		'text' : [
			"Jak być może zauważyliście programowanie w C jest dość mocno <m> niżej poziomowe od programowania np. w Pythonie. <m>"
			"A co za tym idzie często trudniejsze i wymagające więcej wysiłku i czasu. <m>"
			"Natomiast wykonanie takiego skompilowanego <m> do kodu maszynowego programu jest znacznie szybsze. <m>"
			"Jeżeli w jakimś zastosowaniu potrzebujemy kompilowalnego, <m> szybkiego języka takiego jak C, <m>"
				"ale z wyżejpoziomowymi mechanizmami, z jakimi można <m> spotkać się na przykład w Pythonie warto zwrócić uwagę na C++. <m>"
			"Język ten oferuje nam dynamiczne typowanie, <m> podobne do znanego z pythona z uzycie słowa kluczowego auto. <m>"
			"Pozwala na programowanie generyczne, niezależne od typów z użyciem szablonów. <m>"
			"Oferuję pętlę for iterującą po elementach kolekcji, <m> wsparcie dla programowania obiektowego, funkcji typu lambda." <m>
			"A także oferuje listy i słowniki i to znacznie bardziej rozbudowane <m> niż te z którymi mieliśmy doczynienia w Pythonie,  <m>"
				"możemy mieć np. słownik z wieloma jednakowymi kluczami, <m> zbiór samych unikalnych kluczy, itd. <m>",
			
			"Zarówno język C jak i C++ nie są językami nowymi, <m> C powstał z rozwinięcia języka B w 72 roku ubiegłego wieku, <m> C++ powstał jako rozwinięcie się języka C 7 lat później, w 79 roku ubiegłego wieku. <m>"
			"Języki te dość długo dojrzewały do uzyskania oficjalnego standardu, <m> pierwszy oficjalny standard C pochodzi z 1989 roku, a C++ dopiero z 1998 roku. <m>"
			"W chwili obecnej języki te są standaryzowane jako <m> standardy ISO IEC z odpowiednimi numerkami. <m>"
			"Języki te od czasu powstania, a także późniejszego ustandaryzowania, <m>"
			'rozwijają się niezależnie – najnowsze wersję pochodzą z <2017>[dwa tysiące siedemnastego] i <2018>[dwa tysiące osiemnastego] roku <m> i w chwili obecnej C ma wersję nowszą niż C++. <m>'
			"Jednak pomimo niezależnego rozwoju przez tyle lat języki te pozostają <m> bliskie sobie i jednym z założeń C++ jako takiego jest, <m> żeby utrzymywać kompatybilność z C. <m>"
			
			"C++ jest czymś więcej niż tylko obiektowym C, <m> bo programowanie pseudo-obiektowe można uzyskać także <m> bez większych problemów w samym C i istnieją programy <m> pisane w stylu obiektowym w czystym C bez użycia C++. <m>"
			"C++ to nie tylko C z klasami, <m> lecz oferuje sporo innych usprawnień w stosunku co do C. <m>"
			"Często te usprawnienia w późniejszym okresie są również adaptowane w samym języku C <m> – przykładem może być komentarz liniowy, czy też typ logiczny bool. <m>"
			'Również niektóre nowsze rzeczy z C są przejmowane przez C++, <m> niekiedy z pewnymi opóźnieniami. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCode(code_obiektowe, args=["&& ./a.out"], cmd="g++")],
			[7.0, eduMovie.runCommandString(r"clang++ przykład.cpp && ./a.out", cwd="/tmp")],
		],
		'text' : [
			'Będziemy używali kompilatora <clang++>[ce lang plus plus] lub g++ i języka w wersji co najmniej <11>[jedenastej]. <m>'
			'W przypadku nowoczesnych wersji kompilatorów nie ma potrzeby podawania <m> opcji <std>[STD] równa się C++11, ponieważ one zakładają jako domyślną <m> na przykład wersję <14>[czternastą] języka.<m>'
			'Jednak w przypadku starszych wersji kompilatora może być konieczne <m> podanie standardu w którym chcemy skompilować nasz program, <m> ponieważ domyślną wersją może być na przykład wersja z 98 roku. <m>'
			'Tak samo jak w przypadku C kompilatory C++ domyślnie tworzą plik <a.out>[a kropka out]. <m>'
		]
	},
	{
		'console': [
			[0.0, "x", eduMovie.prompt() + "view przykład.cpp"],
			[0.7, "x", "\n\r"],
			[0.8,  eduMovie.code2console(code_obiektowe, "cpp", first=1,  last=24, limit=24)],
			*[  [5.8+i,  eduMovie.clear + eduMovie.code2console(code_obiektowe, "cpp", first=1+i,  last=24+i, limit=24)] for i in range(1,20)  ],
			*[  [10.8+i, eduMovie.clear + eduMovie.code2console(code_obiektowe, "cpp", first=1+i,  last=24+i, limit=24)] for i in range(20,41)  ],
			*[  [15.8+i, eduMovie.clear + eduMovie.code2console(code_obiektowe, "cpp", first=1+i,  last=24+i, limit=24)] for i in range(41,48)  ],
		],
		'text' : [
			'Pierwszą najbardziej zauważalną rzeczą jest to <m> że C++ umożliwia programowanie obiektowe. <m>'
			'Programowanie obiektowe w C++ jest ogólnie <m> rozwinięciem koncepcji struktur znanych z języka C. <m>'
			'Tak samo dobrze możemy używać słowa kluczowego struct, <m> jak class i są one prawie równoważne. <m>'
			'W ramach struktury, czy też klasy definiujemy sobie różnego typu pola, <m> ale w odróżnieniu od struktur z języka C, w C++ możemy definiować również <m> w ramach takiej struktury funkcje, które stanowią metody takiej klasy. <m>'
			'Szczególnymi przypadkami takich funkcji definiowanych w ramach struktury <m> jest konstruktor (wywoływany przy tworzeniu obiektu danej klasy) <m> oraz destruktor (wywoływany przy usuwaniu obiektu danej klasy). <m>'
			
			'W C++ nie ma silnego rozróżnienia między strukturą a klasą <m> i terminów tych możemy zasadniczo używać wymiennie. <m>'
			'Jeżeli piszemy słowo struct to wszystkie pola tej klasy <m> domyślnie są dostępne z zewnątrz, czyli są publiczne. <m>'
			'Jeżeli piszemy class wszystkie pola domyślnie są prywatne, <m> czyli będą udawać nie dostępne z zewnątrz. <m>'
			'I to jest jedyna różnica pomiędzy słowem kluczowym struct a class. <m>'
			'Zachowanie to w obu wypadkach możemy zmienić <m> definiując odpowiednie pola w ramach sekcji public, protected lub private. <m>',
			
			'Metody są tak naprawdę funkcjami, które jako pierwszy, ukryty <m> argument przyjmują wskaźnik na obiekt danej klasy. <m>'
			'Do tego wskaźnika można się odwołać w sposób jawny <m> przy pomocy słowa kluczowego this.<m>'
			'W C++ argument ten jest dodawany niejawnie przez kompilator, <m> zarówno do listy argumentów metody, jak i we wszystkich odwołaniach <m> do elementów (pól i metod) tej klasy w jej kodzie. <m>'
			'Dla przypomnienia w Pythonie programista <m> zapisywał to w obu miejscach sposób jawny. <m>'
			
			'Metody statyczne, definiowane są z użyciem słowa kluczowego static <m> i nie otrzymują tego wskaźnika. <m>'
			'Są to po prostu zwykłe funkcje <m> umieszczone w przestrzeni nazw jaką jest klasa. <m>'
			
			'Zmienne statyczne w ramach struktury deklarowane są również z użyciem <m> słowa kluczowego static i są wspólne dla wszystkich obiektów tej struktury, <m>'
			'czyli są takimi zmiennymi globalnymi <m> w przestrzeni nazw jaką jest dana klasa. <m>'
			'W wielu nadal używanych wersjach C++ muszą być zdefiniowane <m> poza definicją samej struktury, czyli gdzieś w jakimś pliku kompilowanym, <m> a nie w pliku nagłówkowym zawierającym opis naszej klasy. <m>'
			
			'Korzystanie z klas bardzo przypomina korzystanie ze struktur, <m> tyle że możemy korzystać z metod obiektu danej klasy <m>'
			'(poprzez struktura kropka metoda <m> albo struktura myślnik znak większości metoda, <m> zależnie od tego czy mamy obiekt, czy wskaźnik na obiekt struktury). <m>'
			'W C++ aby utworzyć obiekt danej struktury nie musimy <m> również poprzedzać jej nazwy słowem kluczowym struct, jak było to w C. <m>'
			
			'Z metod i zmiennych statycznych możemy korzystać <m> poprzez nazwa klasy dwa dwukropki nazwa metody lub zmiennej. <m>'
			'Jeżeli metodę statyczną chcemy uruchomić z obiektu <m> czy też wskaźnika możemy ją uruchomić tak jak zwykłą metodę, <m>'
			'natomiast należy pamiętać że metoda statyczna nie dostaje wskaźnika <m> na strukturę z której została uruchomiona, ponieważ jest metodą <m> przeznaczoną do uruchamiania bez żadnego obiektu danej klasy. <m>'
			
			'Obiekt klasy możemy także utworzyć z użyciem operatora new. <m>'
			'W rezultacie czego zostanie on zaalokowany poza stosem, <m> czyli jego życie nie będzie ograniczone aktualnym blokiem, <m> a my dostaniemy wskaźnik na niego. <m>'
			'Musimy jednak pamiętać o ręcznym zwolnieniu tak przydzielonej pamięci, <m> gdy ten obiekt nie będzie nam potrzebny, z użyciem delete. <m>'
		]
	},
]
