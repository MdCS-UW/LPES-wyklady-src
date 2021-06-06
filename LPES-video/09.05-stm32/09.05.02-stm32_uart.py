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

code_uart_main = r"""
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

#include <stdio.h>
#include "uart.h"

int main(){
 rcc_periph_clock_enable(RCC_GPIOC);
 gpio_set_mode(GPIOC, GPIO_MODE_OUTPUT_2_MHZ, GPIO_CNF_OUTPUT_PUSHPULL, GPIO13);
 usart_setup();

 while(1){
   for (int i = 0; i < 150000; i++) __asm__("nop");
   gpio_toggle(GPIOC, GPIO13);
   printf("Hello, World!\n");
 }
}
"""

code_uart_setup = r"""
void usart_setup(void) {
  /* Setup GPIO pin GPIO_USART1_TX/GPIO9 on GPIO port A for transmit. */
  gpio_set_mode(GPIOA, GPIO_MODE_OUTPUT_50_MHZ,
                GPIO_CNF_OUTPUT_ALTFN_PUSHPULL, GPIO_USART1_TX);

  /* Setup UART parameters. */
  usart_set_baudrate(USART1, 9600);
  usart_set_databits(USART1, 8);
  usart_set_stopbits(USART1, USART_STOPBITS_1);
  usart_set_mode(USART1, USART_MODE_TX);
  usart_set_parity(USART1, USART_PARITY_NONE);
  usart_set_flow_control(USART1, USART_FLOWCONTROL_NONE);

  /* Finally enable the USART. */
  usart_enable(USART1);
}
"""

code_uart_write = r"""
int _write(int fd, char *ptr, int len){
  int i = 0;
  /*
   * Write "len" of char from "ptr" to file id "fd"
   * Return number of char written.
   *
   * Only work for STDOUT, STDIN, and STDERR
   */
  if (fd > 2) {
        return -1;
  }
  while (*ptr && (i < len)) {
      usart_send_blocking(USART1, *ptr);
    if (*ptr == '\n') {
      usart_send_blocking(USART1, '\r');
    }
    i++; 
    ptr++;
  }
  return i;
}
"""

clipData += [
	{ 'comment': 'mikrokontrolery stm32' },
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_uart_main, "c", first=1, last=24, limit=24)],
			["uart_setup", eduMovie.clear + eduMovie.code2console(code_uart_setup, "c", first=1, last=24, limit=24)],
			["uart_write", eduMovie.clear + eduMovie.code2console(code_uart_write, "c", first=1, last=24, limit=24)],
		],
		'text' : [
			'Oprócz możliwości bezpośredniej zmiany stanu wyjść i odczytu stanu <m> wejść cyfrowych mikrokontrolera, układy te oferują <m> sprzętowe wsparcie dla wielu interfejsów komunikacyjnych. <m>'
			'Konfiguracja i użytkowanie takich interfejsów opiera się na <m> wykonywaniu zapisów i odczytów rejestrów związanych z danym peryferium. <m>'
			
			'Kolejne dwa przykłady będą poświęcone korzystaniu z portu szeregowego <UART>[uart] <m> do komunikacji z mikrokontrolerem. <m>'
			'Pierwszy z nich pokazuje podstawową konfigurację nadajnika <UART>[uart] <m> oraz możliwość wykorzystania <UART>[uart] jako standardowego wyjścia <m> w programach opartych o <libopencm3>[lib open CM 3]. <m>'
			
			'Jak widzimy w głównym programie dodana została funkcja konfigurująca <UART>[uart] <m> oraz wywołanie znanej nam już funkcji printf w ramach pętli głównej. <m>'
			
			'Cała magia odbywa się w osobnym pliku uart.c, <m> gdyż będziemy z niego korzystać też w innych przykładach. <mark name="uart_setup" />'
			'Na początku w ramach funkcji usart setup mamy ustawienie <m> odpowiedniego trybu pinu związanego z sygnałem TX, <m>'
				'konfigurację parametrów transmisji <m> (takich jak prędkość, ilość bitów danych, bitów stopu, itd.) <m> oraz włączenie tego interfejsu. <m>'
			'W konfiguracji pinu informujemy też że ma on być podpięty <m> do funkcji alternatywnej, czyli do nadajnika <USART>[usart] <m> a nie być bezpośrednio sterowanym pinem GPIO. <mark name="uart_write" />'
			
			'Plik ten definiuje też funkcję podkreślnik write, <m> której nigdzie nie używamy jawnie, ale wykorzysta ją <m> biblioteka <open cm>[open CM] do realizacji standardowego wyjścia. <m>'
			
			'Funkcja ta przyjmuje kilka argumentów – pierwszym argumentem <m> jest deskryptor pliku na którym ma zostać wykonany zapis, <m>'
				'drugim jest ciąg bajtów który ma być zapisany, <m> a trzecim jest długość tego ciągu. <m>'
			
			'Funkcja ta w pętli przechodzi po kolejnych znakach bajtach do wypisania, <m> dopóki nie wyśle wskazanej ilości znaków <m> lub nie napotka bajtu o wartości zero oznaczającego koniec napisu. <m>'
			'Kolejne znaki wysyłane są z użyciem funkcji usart send blocking, <m> która blokuje wykonywanie aktualnego kodu, <m> aż do momentu zakończenia wysyłania podanego znaku. <m>'
			'Jeżeli wysyłanym znakiem był znak nowej linii to dodatkowo wysyłany jest <m> znak powrotu karetki, co wynika z specyfiki działania terminali szeregowych <m>'
				'(sam znak nowej linii powoduje przejście do następnej linii, <m> ale nie na jej początek). <m>'
			'Funkcja zwraca ilość wysłanych bajtów. <m>'
		]
	},
]

code_uart_receiver = r"""
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

#include <libopencm3/stm32/usart.h>
#include <libopencm3/cm3/nvic.h>
#include <libopencm3/cm3/scb.h>

#include <stdio.h>
#include "uart.h"

int main() {
 rcc_periph_clock_enable(RCC_GPIOC);
 gpio_set_mode(GPIOC, GPIO_MODE_OUTPUT_2_MHZ, GPIO_CNF_OUTPUT_PUSHPULL, GPIO13);
  
 // ustawiamy adres wektora przerwań na adres początkowy pamięci FLASH
 SCB_VTOR = FLASH_BASE;
 // aktywujemy przerwania z USART1
 nvic_enable_irq(NVIC_USART1_IRQ);
 // aktywujemy przerwania związane z odbiorem danych z USART1
 usart_enable_rx_interrupt(USART1);
  
 // aktywujemy USART1 jak wcześniej - parametry transmisji, etc
 usart_setup();
 // aktywujemy pin A10 jako wejściowy
 gpio_set_mode(GPIOA, GPIO_MODE_INPUT, GPIO_CNF_INPUT_FLOAT, GPIO10);
 // zmieniamy tryb na TX/RX
 usart_set_mode(USART1, USART_MODE_TX_RX);
  
 for(int j = 0; j < 10; j++) {
   printf("...%d\n", j);
   for (int i = 0; i < 150000; i++) __asm__("nop");
   gpio_toggle(GPIOC, GPIO13);
 }
  
 while(1) {
   __asm__("nop");
 }
}

void usart1_isr(void) {
  uint32_t flags = USART_SR(USART1);
  if ( flags & USART_SR_RXNE ) {
    // przerwanie było z powodu odebranego bajtu
    uint8_t data = usart_recv(USART1);
    if (data%2)
      gpio_set(GPIOC, GPIO13);
    else
      gpio_clear(GPIOC, GPIO13);
  }
}
"""

clipData += [
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_uart_receiver, "c", first=1, last=24, limit=24)],
			*[  [4+i,  eduMovie.clear + eduMovie.code2console(code_uart_receiver, "c", first=1+i,  last=24+i, limit=24)] for i in range(1,11)  ],
			["scb_vtor", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_uart_receiver, "c", first=11, last=34, limit=24), [5], False, "")], # podświetlenie: SCB_VTOR = FLASH_BASE
			*[  ["irq_en - " + str(17-i),  eduMovie.clear + eduMovie.code2console(code_uart_receiver, "c", first=1+i,  last=24+i, limit=24)] for i in range(11,15)  ],
			["irq_en", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_uart_receiver, "c", first=15, last=38, limit=24), [3,5], False, "")], # podświetlenie: nvic_enable_irq i usart_enable_rx_interrupt
		],
		'text' : [
			'Drugim przykładem związanym z obsługą portu szeregowego jest <m> odbieranie z niego danych, czyli korzystanie z tego portu jako wejścia. <m>'
			
			'Tym razem zrealizowane jest to z wykorzystaniem przerwań, <m> czyli w sposób asynchroniczny. <m>'
			'Dzięki temu nigdzie w programie nie wykonujemy aktywnego oczekiwania <m> na otrzymanie danych, tylko program będzie wykonywał swoje zadania (pętlę główną), <m>'
				'a odebranie danych spowoduje wstrzymanie jej wykonywania <m> i uruchomienie odpowiedniej funkcji. <m>'
			
			'Funkcje związane z przerwaniami w używanej bibliotece <m> określane są poprzez nadanie im odpowiedniej nazwy <m>'
				'(analogicznie jak określana jest funkcja główna od której zaczyna się <m> wykonywanie programu, poprzez nazwanie jej main). <m>'
			'W niektórych innych bibliotekach funkcję możemy nazwać dowolnie, ale musimy <m> zarejestrować ją do obsługi danego przerwania z użyciem stosownego makra. <m>'
			
			'Fakt że dana funkcja związana jest z obsługą jakiegoś przerwania, <m> wynika z zapisania adresu pod którym jest ona umieszczona <m> w specjalnym miejscu nazywanym wektorem przerwań. <m>'
			'W naszym wypadku wektor przerwań umieszczany jest na początku <m> binarnego kodu skompilowanego programu, <m>'
				'czyli po wgraniu tego kodu do pamięci mikrokontrolera <m> znajdzie się na samym początku pamięci flash. <mark name="scb_vtor" />'
			
			'Zatem na początku programu ustawiamy odpowiednio adres pod którym <m> znajduje się ten wektor, ustawiając wartość odpowiedniego rejestru procesora. <m>'
			'Zasadniczo można tu podać dowolny adres, ale nasza biblioteka domyślnie <m> umieszcza ten wektor na początku kodu i nie będziemy tego zmieniać. <m>'
			
			'Wektor przerwań jest klasyczną jedno wymiarową tablicą C, <m> w komórkach której umieszczone są adresy procedur obsługi <m> związanych z przerwaniem o danym numerze. <m>'
			'Jeden z tych numerów jest związany właśnie z przerwaniami od <m> interfejsu usart numer 1, inny od usart 2, a jeszcze inny z resetem procesora <m>'
				'– zawiera on adres funkcji uruchamianej po resecie, <m> czyli na przykład wewnętrznej funkcji bibliotecznej, <m> która uruchomi funkcję main lub po prostu samej funkcji main. <m>'
			'Wystąpienie przerwania powoduje wykonanie skoku do adresu wskazanego <m> w odpowiedniej pozycji wektora przerwań, <m>'
				'czyli ustawienie licznika programu na tą wartość <m> i wczytanie z pod tego adresu instrukcji do wykonania. <m>'
			'W ramach wykonywania takiego skoku stara wartość licznika programu <m> i grupy innych rejestrów umieszczana jest w pamięci <m> (dokładniej na stosie) <m>'
				'celem umożliwienia powrotu do miejsca i stanu procesora <m> w którym przerwanie zakłóciło wykonywanie standardowego kodu. <m>'
			'Działa to tak samo jak dla wywołań zwykłych funkcji. <m>'
			
			'Po zakończeniu procedury obsługi przerwania (tak samo jak po zakończeniu funkcji) <m> przywracane są ze stosu wartości tych rejestrów <m>'
				'i procesor kontynuuje wykonywanie kodu od miejsca w którym zostało przerwane <m> (będąc też w takim stanie w jakim zastało go przerwanie). <mark name="irq_en" />'
			
			'Wracając do naszego kodu i obsługi przerwań z portu szeregowego <m> – w ramach konfiguracji wykonywanej na początku funkcji main <m> widzimy także włączenie obsługi przerwań z interfejsu usart <m>'
				'i włączenie generowania przerwania związanego z odbiorem danych. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_uart_receiver, "c", first=15, last=38, limit=24), [10,12], False, "")], # podświetlenie: gpio_set_mode i usart_set_mode
			["usart1_irs", eduMovie.clear + eduMovie.code2console(code_uart_receiver, "c", first=39, last=55, limit=24)],
			["usart1_irs_A", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_uart_receiver, "c", first=39, last=55, limit=24), [2], False, "")],
			["usart1_irs_B", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_uart_receiver, "c", first=39, last=55, limit=24), [5], False, "")],
			["usart1_irs_C", eduMovie.clear + eduMovie.markLines(eduMovie.code2console(code_uart_receiver, "c", first=39, last=55, limit=24), [], False, "")],
		],
		'text' : [
			'Po znanej nam już funkcji usart setup dokonujemy dodatkowej konfiguracji <m> polegającej na aktywacji odbiornika tego interfejsu, <m>'
				'czyli konfigurujemy odpowiedni pin <m> i zmieniamy tryb pracy interfejsu na dwukierunkowy. <m>'
			
			'Dalej w ramach funkcji main nie ma nic ciekawego. <m>'
			'Nawet pętla główna jest pusta – wykonuje instrukcję nop, ale jak wiemy <m> musi się ona tam znaleźć bo funkcja main nie powinna się zakończyć. <mark name="usart1_irs" />'
			
			'Na ekranie widzimy funkcję <usart1_irs>[usart jeden ISR], która obsługuje przerwania <m> związane z interfejsem <USART>[usart] o numerze jeden <m> i jak wiemy w tej roli istotna jest jej nazwa. <mark name="usart1_irs_A" />'
			
			'W funkcji tej na wstępie dokonujemy sprawdzenia <m> czy przerwanie było w związku z odbiorem danych. <m>'
			'W tym przykładzie nie ma to większego znaczenia (byłoby użyteczne gdybyśmy <m> obsługiwali też inne przerwania z tego interfejsu), <m>'
				'natomiast samo odczytanie tego rejestru jest ważne <m> aby wyczyścić flagę przerwania (inaczej byłoby ono generowane powtórnie). <m>'
			'Warto zauważyć że wartość zwróconą przez <USART_SR>[usart sr] zapisaliśmy do zmiennej, <m> co byłoby użyteczne gdybyśmy chcieli rozbudować konstrukcję if <m>'
				'o obsługę innych powodów przerwań, <m> gdyż na skutek odczytu tego rejestru pewne flagi mogą być czyszczone <m> i kolejny odczyt może zwrócić inną wartość. <m>'
			
			'Jeżeli przerwanie było z powodu odbioru danych to <mark name="usart1_irs_B" /> odbieramy bajt danych i w zależności od jego parzystości <mark name="usart1_irs_C" /> zapalamy lub gasimy diodę na pinie C13. <m>'
			'Oczywiście możemy odbierać też więcej bajtów, gromadząc je w jakimś buforze <m> i dopiero w oparciu o jego zawartość podejmować jakieś działania. <m>'
		]
	},
]
