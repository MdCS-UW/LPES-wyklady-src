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

# TODO brać kody dla STM32 z repo

# TODO: video + skrypt:  dodać schemat obrazkowy budowy gpio - kierunki, podciąganie, bit w słowie, ... + jego omówienie

code_blink = r"""
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

int main() {
  // Uruchomienie peryferium portu C
  // Włączenie sygnału zegara dla portu C
  rcc_periph_clock_enable(RCC_GPIOC);

  // Ustawienie pinu C13 w trybie wyjścia
  gpio_set_mode(
    GPIOC, GPIO_MODE_OUTPUT_2_MHZ, GPIO_CNF_OUTPUT_PUSHPULL, GPIO13
  );

  while(1) {
    // Poczekaj chwilkę
    for (int i = 0; i < 150000; i++) __asm__("nop");
    // Przełącz stan pinu 13 w porcie C
    gpio_toggle(GPIOC, GPIO13);
  }
}
"""

code_di = r"""
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

int main() {
 // Uruchomienie peryferiów portów A, C
 // Włączenie sygnału zegara dla portów A, C
 rcc_periph_clock_enable(RCC_GPIOA);
 rcc_periph_clock_enable(RCC_GPIOC);

 // Ustawienie pinu C13 w trybie wyjścia
 gpio_set_mode(GPIOC, GPIO_MODE_OUTPUT_2_MHZ, GPIO_CNF_OUTPUT_PUSHPULL, GPIO13);

 //Ustawienie pinu A0 w trybie wejścia
 gpio_set_mode(GPIOA, GPIO_MODE_INPUT, GPIO_CNF_INPUT_FLOAT, GPIO0);

 int16_t stan_a;

 while(1) {
   // odczytaj wartość z portu A
   stan_a = gpio_port_read(GPIOA);
   // Przełącz stan pinu 13 w porcie C bazując na wejściu na porcie A
   if(stan_a & 0x01) {
     gpio_set(GPIOC, GPIO13);
   } else {
     gpio_clear(GPIOC, GPIO13);
   }
   // czekamy chwilę ...
   for (int i = 0; i < 150000; i++) __asm__("nop");
 }
}
"""

code_blink = eduMovie.code2console(code_blink, "c", limit=24)

clipData += [
	{ 'title': [ "#09.5", "Mikrokontrolery", "STM32", "" ] },
	
	{ 'comment': 'mikrokontrolery stm32' },
	{
		'console': [
			[0.0, ""],
			["blink",  eduMovie.clear + code_blink],
			["blink1", eduMovie.clear + eduMovie.markLines(code_blink, [6], False, "")],       # podświetlenie: rcc_periph_clock_enable
			["blink2", eduMovie.clear + eduMovie.markLines(code_blink, [9,10,11], False, "")], # podświetlenie: gpio_set_mode
			["blink3", eduMovie.clear + eduMovie.markLines(code_blink, [15], False, "")],      # podświetlenie: for ... __asm__("nop")
			["blink4", eduMovie.clear + eduMovie.markLines(code_blink, [17], False, "")],      # podświetlenie: gpio_toggle
		],
		'text' : [
			'STM32 jest dużą rodziną mikrokontrolerów opartych o architekturę ARM. <m>'
			'Zapoznamy się z kilkoma aspektami związanymi z programowaniem takiego <m> mikrokontrolera, dokładnie <STM32 F103 C8>[STM32 F103 C8], z wykorzystaniem biblioteki <libopencm3>[lib open CM 3]. <mark name="blink" />'
			
			'Pierwszym programem, który uruchamiamy na nowo poznawanym <m> typie mikrokontrolerów jest zazwyczaj miganie diodą, <m> będące odpowiednikiem programu "hello world" w świecie mikrokontrolerów. <m>'
			
			'Na ekranie widzimy kod takiego programu stworzonego w C. <m>'
			'Mamy tutaj jedynie funkcję main, w której najpierw przygotowujemy <m> nasz mikrokontroler do zadań, które chcemy wykonywać, <m> a następnie uruchamiamy nieskończoną pętlę w trakcie której będą one wykonywane. <m>'
			'Jest to typowe podejście w programowaniu mikrokontrolerów, <m> funkcja main w programowaniu mikrokontrolerów na ogół nigdy się nie kończy <m> – jest w niej realizowana pętla nieskończona, nazywana pętlą główną. <m>'
			
			'Program ma za zadanie migać diodą świecącą podłączoną do pinu C13. <mark name="blink1" />'
			
			'Na wstępie podłączamy zegar do odpowiedniego peryferium naszego mikrokontrolera. <m>'
			'Jak już wiemy układy <CMOS>[Ce mos], a w takiej technologii jest też wykonany <m> ten mikrokontroler, pobierają prąd w trakcie przełączania. <m>'
			'Aby ograniczyć to zużycie energii sygnały zegarowe są domyślnie odłączone <m> od większości układów wchodzących w skład mikrokontrolera. <m>'
			'Operacji podłączenia zegara dokonujemy dla całego portu GPIO, <m> z fragmentu którego chcemy korzystać. <mark name="blink2" />'
			
			'Po aktywacji zegara konfigurujemy odpowiedni tryb wybranego pinu <m> – ustawiamy tryb wyjścia z wymuszeniem silnego stanu logicznego. <m>'
			'Moglibyśmy też ustawić wyjście open collector, wejście pływające, <m> wejście z podciąganiem, itp. <mark name="blink3" />'
			
			'W ramach pętli głównej mamy pętlę for wykonującą 150 tysięcy razy <m> instrukcję asemblerową nop, która jest instrukcją pustą – nie robi nic. <m>'
			'Pętla ta służy wprowadzeniu opóźnienia i jest standardowym <m> rozwiązaniem takiego aktywnego czekania. <m>'
			'Jak wiemy pętla for nie jest pojedynczą instrukcją procesora, <m> zatem wykonanie takiej pętli zajmie kilka razy więcej niż 150 tysięcy cykli. <m>'
			'Użycie wstawki asemblerowej z instrukcją pustą, <m> zamiast zakończenia tej pętli średnikiem, <m> służy uniemożliwieniu zoptymalizowania takiej pętli przez kompilator. <mark name="blink4" />'
			
			'Następnie dokonujemy zmiany stanu pinu wyjściowego na przeciwny <m> – czyli jeżeli był niski ustawiamy wysoki, a gdy był wysoki ustawiamy niski. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_di, "c", first=1, last=24, limit=24)],
			*[  [8+i, eduMovie.clear + eduMovie.code2console(code_di, "c", first=1+i,  last=24+i, limit=24)] for i in range(1,7)  ],
			["di1", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_di, "c", first=7, last=30, limit=24), [13], False, "")], #  podświetlenie linii: gpio_port_read
			["di2", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_di, "c", first=7, last=30, limit=24), [16,18], False, "")],
			["di3", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_di, "c", first=7, last=30, limit=24), [21], False, "")],
		],
		'text' : [
			'Kolejnym aspektem, który należy poznać jest odczytanie stanu wejścia. <m>'
			'Struktura widocznego na ekranie programu jest podobna do poprzedniego <m>'
				'– przed pętlą dodane zostało włączenie zegara dla portu A, konfiguracja <m> pinu A0 jako wejścia oraz została zmieniona struktura pętli głównej. <m>'
			'W tym wypadku ustawiamy wejście typu pływającego, czyli takie jak w <m> standardowej bramce, gdzie użytkownik musi wymusić oba stany logiczne. <m>'
			'Moglibyśmy także skonfigurować to wejście jako podciągnięte do zasilania, <m> bądź do masy z użyciem wewnętrznych rezystorów podciągających. <mark name="di1" />'
			
			'W ramach tej pętli dokonujemy odczytu wartości portu A <break time="150ms"/> do zmiennej stan a. <m>'
			'Warto zauważyć że czytamy cały szesnastobitowy port A, <m> czyli stan wszystkich pinów składających się na ten port, <m> a nie tylko jeden bit z tego portu. <m>'
			'W związku z tym sprawdzamy w warunku if tylko stan tego jednego, najmłodszego <m> bitu – w tym celu korzystamy z operacji bitowego and z odpowiednią maską. <mark name="di2" />'
			
			'W zależności od wyniku tej operacji ustawiamy stan <m> wysoki lub niski na pinie C13 odpowiednimi funkcjami. <mark name="di3" />'
			
			'Na końcu mamy też pętlę opóźniającą, <m> która eliminuje nam między innymi problem drgań styków. <m>'
			
			'Warto jeszcze wspomnieć, że biblioteka oferuje także <m> analogiczną do <gpio_port_read>[gpio port read] funkcję <gpio_port_write>[gpio port write], <m> która pozwala na równoczesne ustawienie stanu całego portu. <m>'
		]
	},
]
