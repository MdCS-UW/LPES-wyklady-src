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
	{ 'comment': 'mikrokontrolery stm32' },
	{
		'image': [
			[0.0, ""],
			["adc",  eduMovie.convertFile('adc.svg')], # plot sin(x) lc "blue", floor(16*sin(x))/16.0+1/32.0 with histeps lc "red"
			["xEOL", eduMovie.convertFile('xEOL.sch', negate=True, dpi=140)],
			["pwm",  eduMovie.convertFile('pwm.svg', negate=True)],
			["dac",  eduMovie.convertFile("dac.sch", negate=True, dpi=140)],
		],
		'text' : [
			"W materiałach do zajęć z programowania mikrokontrolerów STM32 <m> znajdują się także przykładowe kody związane z użyciem <m>"
				"przetwornika analogowo-cyfrowego, interfejsu I2C <m> oraz timer'a użytego do automatycznego generowania sygnału typu PWM. <m>"
			'Nie będziemy ich jednak szczegółowo omawiać w tym miejscu, <m> gdyż sprowadzają się jedynie do konfiguracji i użycia odpowiedniego peryferium. <m>'
			'Oczywiście należy pamiętać że są to przykłady <m> i można to zrealizować inaczej, także lepiej bądź wydajniej. <m>'
			'Na przykład stosując przerwania zamiast aktywnego czekania <m> na zakończenie operacji takiej jak konwersja analogowo-cyfrowa. <m>'
			'W tym miejscu należy jednak powiedzieć kilka słów o samym <m> przetworniku analogowo-cyfrowym i sygnale PWM. <mark name="adc" />'
			
			'Przetwornik analogowo cyfrowy jest to zasadniczo woltomierz, który umożliwia <m> pomiar napięcia – konwersję wartości napięcia na liczbę ją reprezentującą. <m>'
			'Nie zwraca on jednak tej wartości w woltach, a używając własnej skali związanej <m> z wartością napięcia referencyjnego i ilością bitów przetwornika. <m>'
			'Ogólnie zero oznacza zero napięcia, a największa możliwa liczba <m> (czyli dla przetwornika n bitowego dwa do <n-tej>[entej] minus jeden) <m> maksymalne napięcie w danym trybie – często równe napięciu referencyjnemu. <m>'
			'Skala jest liniowa, więc znając wartość tego maksymalnego napięcia <m> łatwo możemy przeliczyć wynik na wartość napięcia w woltach. <m>'
			'Jednak nie zawsze tego potrzebujemy – np. pliki dźwiękowe zapisywane są <m> w postaci takich liczb (odpowiadających procentowi maksymalnego poziomu sygnału) <m> a nie wartości napięcia w woltach. <m>'
			
			'Możliwość pomiaru napięcia pozwala na zastosowanie wejść ADC do obsługi <m> różnego rodzaju czujników – zasadniczo wszystkie pomiary elektryczne <m> sprowadzają się do pomiaru napięcia. <mark name="xEOL" />'
				'Wejścia ADC mogą być też użyte jako wejścia wielostanowe, pozwalające np. <m> na monitoring stanu jakiegoś styku wraz z poprawnością linii do niego prowadzącej. <m>'
			'Dzięki czemu możemy wykryć nie tylko stan zwarty i rozwarty styku <m> ale też uszkodzenie w postaci przerwania lub zwarcia kabla. <m>'
			'Tego typu wejścia, określane jako <xEOL>[iks EOL], są bardzo często stosowane <m> w systemach alarmowych. <mark name="pwm" />'
			
			'Sygnał PWM jest to sygnał prostokątny, w którym informacja znajduje się <m> nie w jego amplitudzie czy częstotliwości, a procencie wypełnienia, <m>'
				'czyli stosunku czasu gdy mamy stan wysoki do okresu tego sygnału. <m>'
			"Mikrokontrolery z użyciem układów odliczających nazywanych timer'ami <m> są w stanie generować taki sygnał automatycznie <m> (bez wywoływania kodu programu w tym celu). <m>"
			
			'Sygnał ten może być użyty do prostego sterowania np. jasnością diody LED. <m>'
			'Jeżeli jego częstotliwość jest odpowiednio duża to fakt włączania wyłączania <m> nie będzie zauważalny bezpośrednio dla oka, natomiast będzie to <m> obserwowane jako regulacja jasności w funkcji tego wypełnienia. <mark name="dac" />'
			
			'Jeżeli jakiś układ potrzebuje jednak sygnału analogowego o danym napięciu <m> to sygnał PWM można na taki zamienić używając rezystora i kondensatora. <m>'
			'Uzyskując w ten sposób jeden z wariantów konwertera cyfrowo-analogowego. <m>'
		]
	},
]
