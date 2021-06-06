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

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#09.4", "Układy", "programowalne", "" ] },
	
	{ 'comment': 'programowalne' },
	{
		'image': [
			[0.0, ""],
			["memory", eduMovie.convertFile('pamięć.svg', negate=True)],
			["hdl", eduMovie.convertFile('przerzutnik.vhdl.tex', margins=12, viaCairo=True, dpi=140, negate=True)],
		],
		'text' : [
			"Układy programowalne można podzielić na dwie podstawowe grupy, <m> czyli układy z programowalną strukturą logiczną oraz systemy <procesorowe>[procesor'owe]. <m>"
			
			'Układy z programowalną strukturą logiczną, oparte są na tym że <m> wewnątrz takiego układu programujemy jakiś układ bramek logicznych, <m> przerzutników i tym podobnych elementów oraz ich połączeń. <mark name="memory" />'
			
			'Najprostszym koncepcyjnie sposobem realizacji czegoś takiego jest <m> układ pamięciowy, który pozwala na zrealizowanie dowolnej funkcji logicznej, <m> czyli dowolnego układu bramek. <m>'
			'Jeżeli weźmiemy pamięć która będzie miała 2 do n-tej bitów <m> i będzie adresowana n-bitową szyną adresową <m>'
				'to z każdym adresem związany jest jakiś jeden bit <m> i każdy bit odpowiada jednemu adresowi. <m>'
			'Pamięć tego typu pozwala nam na zapisanie tabeli prawdy <m> dowolnej funkcji która posiada n wejść i jedno wyjście <m> – każdemu wejściu odpowiada jeden bit adresu, <m>'
				'a związana z daną kombinacją wejść, <m> wartość wyjścia zapisana jest w naszej pamięci. <m>'
			
			"Układy tego typu mają spore zastosowanie praktyczne i pozwalają na <m> konstruowanie układów działających szybciej niż układy <procesorowe>[procesor'owe]. <m>"
			'Zastosowanie programowalnych układów logicznych jest prostsze i szybsze <m> niż konstruowanie takich rozwiązań z pojedynczych elementów takich jak bramki, <m>'
				'a przy produkcji na małą i średnią skalę także tańsze <m> od projektowania i produkcji dedykowanych układów scalonych. <m>'
			'Pozwala też na aktualizację takiego <"sprzętu">[sprzętu] poprzez <m> zaprogramowanie poprawionej jego wersji. <mark name="hdl" />'
			'Do programowania tego typu układów służą języki opisu sprzętu <m> typu HDL (hardware description language). <m>'
			'Najczęściej jest to VHDL lub verilog. <m>'
			'Niestety bliżej tych języków w ramach tych zajęć nie poznamy <m> i też nie nauczymy się korzystać z tego typu układów. <m>'
			'Natomiast warto wiedzieć że tego typu układy w których <m> możemy zaprogramować pewien algorytm realizowany czysto sprzętowo istnieją. <m>'
			'Taka realizacja sprzętowa, dzięki urównolegleniu wielu procesów jest <m> zazwyczaj znacznie szybsza w działaniu niż wersja programowa. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('cpu.svg', negate=True)],
		],
		'text' : [
			'Zajmiemy się trochę bliżej popularniejszy mimo wszystko systemami procesorowymi. <m>'
			
			'Są to systemy wykonujące ciąg instrukcji pobieranych z jakieś pamięci. <m>'
			'Składają się one z procesora, pamięci programu i pamięci danych. <m>'
			'W zależności od stosowanej architektury kod programu, <m> a raczej kod maszynowy utworzony w wyniku kompilacji kodu programu, <m>'
				'może znajdować się albo w tej samej pamięci w której <m> przechowujemy również dane albo może mieć osobną, wydzieloną pamięć. <m>'
			
			'Systemami procesorowymi są zarówno systemy komputerowe, <m> takie jak nasze <PCty>[Pe Cety] czy laptopy, <m> są nimi telefony komórkowe, zarówno smartfony jak i te bardziej prymitywne, <m>'
				'są nimi duże systemy obliczeniowe, a także różnego rodzaju mikrokontrolery <m> znajdujące się w sterownikach przemysłowych, centralkach alarmowych, <m> telewizorach, sprzęcie AGD i tak dalej. <m>'
			'Procesor pracuję w cyklach rozkazowych, czyli w ramach <m> jednego bądź kilku cykli zegara wykonuje ciąg kroków służący <m> pobraniu z pamięci kolejnej instrukcji i jej przetworzeniu. <m>',
			
			'Trochę uproszczony model tego może wyglądać w sposób następujący: <m>'
			'Procesor wystawia na szynę adresową magistrali umożliwiającej dostęp do pamięci <m> adres będący zawartością tak zwanego licznika programu. <m>'
			'Jest to adres instrukcji, która ma zostać pobrana i wykonana. <m>'
			'Po wystawieniu tego adresu generowany jest cykl odczytu na tej szynie. <m>'
			'A odczytany kod instrukcji zapamiętywany jest w rejestrze instrukcji, <m> następuje też zwiększenie licznika programu o 1 <m> po to żeby móc w następnym cyklu pobrać kolejną instrukcję. <m>',
			
			'Następnym krokiem jest dekodowanie instrukcji <m> – znajdujący się w procesorze układ dekodera dokonuje zdekodowania <m> instrukcji znajdującej się we wspomnianym rejestrze <m>'
				'i konfiguracji procesora w zależności od jej kodu i opcjonalnie argumentów. <m>'
			'Konfiguracja ta może polegać na ustawienie odpowiednich multiplekserów, <m> czyli właśnie takich przełączników elektronicznych pomiędzy rejestrami <m> a jednostką wykonującą obliczenia <m>'
				'(tak zwanym ALU – jednostką arytmetyczno-logiczną), <m> wystawieniu odpowiedniego kodu operacji dla ALU <m> (celem wykonanie operacji na przykład na zawartości określonych rejestrów). <m>'
			'Może to być także podpięcie wskazanego rejestru do szyny danych <m> (celem skomunikowania go z pamięcią - wykonania odczytu lub zapisu do pamięci, <m>'
				'bądź celem załadowania jego wartości <m> do licznika programu aby wykonać skok) i tym podobne operacje. <m>'
			'Ostatnim krokiem takiego cyklu jest wykonanie tych operacji, <m> czyli wykonanie wcześniej zdekodowanej instrukcji, <m> zgodnie z ustawioną konfiguracją procesora. <m>',
			
			'Oczywiście przedstawiony model jest przykładowy <m> – w rzeczywistości działanie realnego procesora może wyglądać trochę inaczej. <m>'
			'Na przykład długość instrukcji może być większa od długości słowa, <m> więc będzie ładowana w kilku fazach, <m> gdyż cała instrukcja nie mieści się jednorazowo na szynie danych. <m>'
			'Może występować więcej faz i tak dalej. <m>'
			
			'Procesor może również działać potokowo, <m> czyli fazy mogą się na siebie nakładać – podczas gdy jedna instrukcja <m> jest wykonywana to kolejna może być już dekodowana. <m>'
			'Oczywiście wtedy procesor musi wykonywać pewne założenia <m> co do prawdziwości skoków warunkowych, <m> czyli na przykład wykonuje instrukcje skoku warunkowego, <m>'
				'ale dekoduje już instrukcję która jest po niej, <m> tak jakby skok miał nie zajść. <m>'
			'W takiej sytuacji jeżeli skok zachodzi to wtedy ta zdekodowane instrukcja <m> jest unieważniona, potok należy zapełnić od nowa <m>'
				'i nie udaje się wykorzystać przyspieszenia związanego z wielopotokowością. <m>'
			'Na takiej pracy potokowej opiera się tak zwany Hyper Threading <m> dostępny w niektórych procesorach, jednak jak się przekonaliśmy <m>'
				'taka praca potokowa nie jest równoważna z większą ilością niezależnych rdzeni. <m>'
		]
	},
]

code_C_ASM = r"""
# fragment kodu asemblerowego wygenerowanego poleceniem "gcc -S" z kodu C:
#    if (argc == 1)
#        puts("A");
#    else
#        puts("B");
#    puts("C");

# operacja porównania                                      --- warunek if
	cmpl	$1, -4(%rbp)
# skok jeżeli nie równe do bloku else
	jne	.L2
# odłożenie argumentu "A" na stos i wywołanie funkcji puts --- blok if
	leaq	.LC0(%rip), %rdi
	call	puts@PLT
# skok bezwarunkowy za blok if - else
	jmp	.L3
.L2:
# odłożenie argumentu "B" na stos i wywołanie funkcji puts --- blok else
	leaq	.LC1(%rip), %rdi
	call	puts@PLT
.L3:
# odłożenie argumentu "C" na stos i wywołanie funkcji puts --- kod po if-else
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
"""

code_C_ASM = eduMovie.code2console(code_C_ASM, "s", limit=24)

clipData += [
	{
		'console': [
			[0.0, ""],
			["c_asm", eduMovie.clear + code_C_ASM],
			["c_asm_if",    eduMovie.clear + eduMovie.markLines(code_C_ASM, [1], False, "")],
			["c_asm_cmpl",  eduMovie.clear + eduMovie.markLines(code_C_ASM, [1,7,8], False, "")],
			["c_asm_jne",   eduMovie.clear + eduMovie.markLines(code_C_ASM, [9,10], False, "")],
			["c_asm_l2",    eduMovie.clear + eduMovie.markLines(code_C_ASM, [16], False, "")],
			["c_asm_jmp",   eduMovie.clear + eduMovie.markLines(code_C_ASM, [14,15], False, "")],
			["c_asm_l3",    eduMovie.clear + eduMovie.markLines(code_C_ASM, [20], False, "")],
			["c_asm_clear", eduMovie.clear + code_C_ASM],
		],
		'text' : [
			'Instrukcje skoku które w programowaniu są związane z <m> takimi konstrukcjami jak pętle i warunki polegają, jak wspomniałem, <m> na załadowaniu nowej wartości do licznika programu. <m>'
			'W przypadku skoków warunkowych (takich jakich używają instrukcje warunkowe) <m> może to być np. zależne od rejestru flag jednostki ALU, <m> ustawianych w wyniku wykonania poprzedniej operacji arytmetycznej. <mark name="c_asm" />'
			
			'Na ekranie widzimy fragment kodu asemblerowego x86 wygenerowanego <m> przez kompilator gcc dla widocznej konstrukcji if - else. <mark name="c_asm_if" />'
			'Celem wykonania warunku if, sprawdzającego czy jakaś zmienna jest jeden, <mark name="c_asm_cmpl" /> najpierw wykonywana jest ta operacja arytmetyczna porównania. <mark name="c_asm_jne" />'
				'A następnie wykonywana jest instrukcja skoku warunkowego zależna od <m> ustawienia bądź nie ustawienia flagi informującej że była równość. <m>'
			'Jako że nasz if ma blok else to skok warunkowy (dla niespełnionego warunku) <mark name="c_asm_l2" /> realizowany jest na pierwszą instrukcje bloku else, <m>'
			'	czyli adres tej instrukcji zostanie załadowany do licznika programu.  <mark name="c_asm_jmp" />'
			'Natomiast po ostatniej instrukcji bloku if mamy skok bezwarunkowy na pierwszą <mark name="c_asm_l3" /> instrukcję po całej konstrukcji if - else, tak aby ominąć blok else. <mark name="c_asm_clear" />'
			'Skok bezwarunkowy jest po prostu instrukcją, <m> która ładuje odpowiednią wartość adresu do licznika programu. <m>',
		]
	},
	{
		'image': [
			[0.0, ""], # TODO jakiś obrazek
		],
		'text' : [
			'Magistrala pomiędzy procesorem a pamięcią często jest magistralą równoległą, <m> na której mogą się znaleźć też inne urządzenia wejść wyjść <m> dostępne pod innymi adresami. <m>'
			'W niektórych konstrukcjach mają one wydzieloną przestrzeń adresową, <m> a w innych wspólną z pamięcią. <m>'
			
			'Przykładem systemu mikroprocesorowego, <m> będącego także przykładem układu typu system on chip, są mikrokontrolery. <m>'
			'W jednym układzie scalonym zawierają one procesor, pamięć operacyjną RAM, <m> pamięć stałą typu flash do przechowywania kodu programu <m>'
				'(nie jest on w ich wypadku ładowany do RAMu, <m> tylko wykonywany bezpośrednio z pamięci flash). <m>'
			'Bardzo często w układzie tym znajdują się również różnego rodzaju układy <m> wejścia-wyjścia, takie jak porty GPIO, które umożliwiają ustawienie lub odczyt <m>'
				'stanu danej nóżki układu, mogą nimi być bardziej zaawansowane interfejsy <m> jak porty szeregowe <USART>[usart], I2C, <SPI>[eS Pi aj]. <m>'
			'Mogą to być także przetworniki analogowo-cyfrowe <m> (umożliwiające pomiar wartości jakiegoś napięcia – sygnału analogowego) <m> i cyfrowo analogowe (umożliwiające wystawienie napięcia o danej wartości). <m>'
		]
	},
]
