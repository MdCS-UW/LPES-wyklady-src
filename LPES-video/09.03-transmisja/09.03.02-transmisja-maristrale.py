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
	{ 'section': 'magistrale' },
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets//images-src/elektronika/topologie.sch", dpi=210, negate=True)],
		],
		'text' : [
			'W zależności od układu fizycznych połączeń komunikujących się urządzeń <m> wyróżnia się różne topologie połączeń. <m>'
			'Wśród głównych topologii należy wymienić: <m>'
				'Magistralę (linear bus), w której wszystkie urządzenia są podłączone do jednej linii <m> (wspólnego medium transmisyjnego), okablowanie nie wyróżnia punktu centralnego. <m>'
				'Łańcuch (daisy chain), który jest podobny do magistrali, <m> ale medium transmisyjne jest podzielone. <m>'
				'Pierścień (ring), który jest zapętlonym na końcach łańcuchem. <m>'
				'Gwiazdę (star), w której wszystkie podłączenia biorą początek w węźle centralnym. <m>'
				'Krate (mesh), w której każde urządzenie ma bezpośrednie połączenie <m> punkt-punkt do każdego innego urządzenia. <m>'
			'Ponadto występują topologie mieszane takie jak: <m>'
				'gwiazda wielokrotna, czyli taka gwiazda gdzie niektóre z węzłów <m> stanowią punkty centralne kolejnych gwiazd, <m>'
				'magistrala lub ring pomiędzy punktami centralnymi gwiazd, <m>'
				'gwiazda w której w węzłach występują magistrale lub pierścienie, itd. <m>',
			
			'W zależności od potrzeb i możliwości, <m> komunikacja pomiędzy dwoma systemami może zachodzić w jednym z kilku różnych trybów, <m> takich jak simplex, half duplex i full duplex. <m>'
			'Simplex oznacza że mamy transmisję tylko w jedną stronę, <m> na przykład zapis do jakiś rejestrów. <m>'
			'Półdupleks oznacza że mamy komunikację dwukierunkową, <m> ale nie możemy równocześnie nadawać i odbierać, <m> czyli na przykład nadawanie i odbiór współdzieli ten sam przewód. <m>'
			'Full-duplex oznacza że mamy możliwość równoczesnego nadawania i odbioru, <m> nadajnik i odbiornik pracują na niezależnych przewodach. <m>',
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('szeregowa_rowolegla_sygnaly.svg', negate=True)],
			["rownolegla", eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/magistrala_rownolegla.sch", dpi=105, negate=True)], # TODO podświetlanie omawianego elementu
			["szeregowa - 5", eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/magistrala_szeregowa.sch", dpi=110, negate=True)], # TODO podświetlanie omawianego elementu
		],
		'text' : [
			'Przy okazji poznawania różnych rodzajów rejestrów, spotkaliśmy się <m> z pojęciem transmisji jakiś danych równolegle bądź szeregowo. <m>'
			'Generalnie transmisja szeregowa oznacza <m> przesył kolejnych bitów składających się na bajt (słowo) <m> jeden po drugim. W ramach kolejnych taktów zegara. <m>'
			'Natomiast w transmisji równoległej, jednocześnie (różnymi przewodami) <m> przesyłane sa wszystkie bity składające się na słowo. <m>'
			'A w kolejnym takcie zegara przesyłane jest kolejne słowo. <mark name="rownolegla" />'
			
			'Na ekranie widzimy przykład magistrali równoległej, <m> w trochę bardziej złożonej formie, umożliwiającej zapis do wybranego <m> urządzenia (rejestru) spośród podłączonych do tej magistrali. <m>'
			
			'Magistrala ta składa się z n bitowej szyny danych i adresów <m> oraz trzech sygnałów kontrolnych i jednego lub kilku sygnałów pomocniczych. <m>'
			'Sygnały kontrolne służą do przekazywania informacji o stanie magistrali, <m> czyli o tym czy wysyłany jest adres czy dane, o tym czy wykonujemy <m> odczyt czy zapis i oczywiście zegara taktującego te działania. <m>',
			
			'Oczywiście w innych realizacjach sygnały te mogą być inne – na przykład <m> zamiast sygnału odczyt-zapis możemy mieć osobne zegary do tych operacji. <m>'
			'Podobnie zamiast wspólnych linii adresu i danych oraz linii informującej <m> czy jest to adres czy dane możemy mieć osobne linie adresu i danych. <m>'
			'I tak dalej. <m>'
			'W wypadku gdy mamy wspólną szynę danych i adresu, współdzielone mogą być <m> tylko niektóre z jej linii, bo dane mogą mieć inną ilość bitów niż adresy <m>.'
			'Na przykład adres <16>[szesnasto] bitowy i dane <8>[ośmio] bitowe <m> lub adres <32>[trzydziesto dwu] bitowy i dane <64>[sześćdziesięcio cztero] bitowe. <m>',
			
			# dekoder adresu, sygnały sterujące
			
			'Pod szynę adresową podpięty jest układ dekodera adresu, <m> który rozpoznaje odpowiednią kombinację bitów na takiej szynie, <m> stanowiących adres danego urządzenia. <m>'
			'Dekoder też otrzymuje sygnał o tym że na współdzielonej szynie <m> jest transmitowany adres i tylko wtedy zajmuje się jego dekodowaniem. <m>'
			'W omawianym przykładzie sygnał ten pełni jednocześnie funkcję zegara adresu, <m> może jednak być tylko sygnałem informacyjnym, <m> a dekoder może korzystać z ogólnego zegara. <m>'
			'Jeżeli dekoder rozpozna swój adres zapamiętuje taką informację <m> do momentu wystawienia kolejnego adresu i przekazuje ją <m> do układów sterujących rejestrami podłączonymi do magistrali, <m>'
				'reprezentowanych na tym schemacie jako <m> bufory trójstanowe na liniach data out, data in<.>[ .] <m>'
			
			'Drugim sygnałem używanym do sterowania tymi buforami lub rejestrami <m> jest sygnał informujący o żądanym kierunku transmisji. <m>'
			'Jak widać w tym wypadku mamy transmisję half duplex, <m> umożliwiającą w danej chwili transmisję tylko w jedną stronę. <m>'
			
			'Rejestry urządzenia otrzymują także sygnał clock zgodnie z którym <m> wystawiają na szynę lub zczytują z szyny kolejne porcje danych. <m>'
			'Jak widać mogą robić to jednak tylko gdy wcześniej był wysłany <m> odpowiedni adres i ustawiony jest odpowiedni tryb – zapis albo odczyt. <m>',
			
			# IRQ
			
			'Często też z taką magistralą wiąże się możliwość zażądania obsługi <m> przez urządzenie do niej podpięte. <m>'
			'W taki sposób działają na przykład przerwania IRQ w komputerach PC. <m>'
			'Linii takich może być kilka tak aby ważnym urządzeniom zapewnić własne linie, <m> a inne móc jakoś grupować, stąd bierze się numer IRQ. <m>'
			'Na przykładowym schemacie mamy linie żądania obsługi, <m> która jest typu open collector, w związku z tym jeżeli jest zwarta do masy <m> to wiemy że obsługi żąda któreś z urządzeń podpiętych do tej linii przerwań. <m>'
			'Nie wiemy które, więc jeżeli mamy na tej linii więcej niż jedno urządzenie <m> to musimy wszystkie z nich zapytać o to czy to ono żądało obsługi. <m>'
			'Jednak dzięki zastosowaniu takiego rozwiązania nie musimy pytać urządzeń <m> podpiętych do innych linii przerwań ani też pytać urządzeń o to czy potrzebują obsługi, <m> wtedy kiedy nie są zainteresowane, <m>'
				'gdyż to same urządzenia mają możliwość zgłoszenia takiego faktu. <m>'
			
			'Jak widać rozwiązanie z sygnałem przerwań pozwala na odciążenie magistrali <m> od niepotrzebnych zapytań typu "czy chcesz być obsłużony", <m>'
				'a podzielenie takiego sygnału na kilka bitów pozwala na <m> ograniczenie ilości urządzeń które musimy od pytać o to czy ma być obsłużone <m> w momencie kiedy któreś z nich zgłosiło takie zapotrzebowanie. <m>'
			
			'Oczywiście takie odpytywanie można też zrobić niekiedy sprytniej, <m> na przykład jeżeli linia danych jest typu open collector <m>'
				'to w momencie potwierdzenia odbioru przerwania wszystkie urządzenia <m> mogą próbować wystawić tam na raz swoje adresy i będziemy mogli <m> je obsługiwać wg priorytetów związanych z ich adresami. <m>',
			
			# szeregowa
			
			'Drugim typem magistrali jest magistrala szeregowa. <mark name="szeregowa" />'
			'Podstawową różnicą jest to że wcześniej dane i adres <m> były n bitowe, a teraz dane są jedno bitowe. <m>'
			'W tym przypadku mamy akurat osobną szynę adresową, ale nie jest to regułą. <m>'
			'Może być tak jak poprzednio, że mamy wspólną szynę <m> adresową i danych oraz sygnał typu adres - dane. <m>'
			'Może być też tak, że to specyficzna postać danych <m> na tej szynie informuje o tym iż to jest adres, czyli możemy mieć <m> adresowanie określone w protokole przesyłu danych tą magistralą. <m>'
			'W pokazanym przykładzie mamy magistralę typu simplex, <m> czyli transmisja jest jednokierunkowa, <m> co pokazuje bufor umieszczony na linii danych. <m>',
			
			'Działanie magistrali pokazanej w przykładzie <m> oparte jest o rejestry przesuwne z buforem wyjściowym, <m>'
				'czyli w momencie jeżeli adres danego urządzenia, rejestru, jest wystawiony <m> na linii adresowej to aktywujemy sygnały zegara dochodzące do rejestrów. <m>'
			'W związku z tym dane transmitowane w taktach głównego zegara <m> zapisywane są do rejestru przesuwnego, a w momencie sygnału zegara wyjść, <m> nazwanego tutaj strobe wystawione zostaną na odpowiednie wyjścia. <m>'
			
			'W tym przykładzie są dwa rejestry połączone ze sobą szeregowo, <m> czyli wyjście szeregowe pierwszego podpięte jest do wejścia drugiego. <m>'
			'Dzięki temu dane które nie mieszczą się w pierwszym rejestrze zamiast <m> być tracone są przenoszone do drugiego i uzyskujemy tutaj 16 bitów wyjścia, <m> z użyciem dwóch rejestrów <8>[ośmio] bitowych. <m>'
			
			'Zatem po 16 cyklach zegara związanych z transmisją danych, <m> nowymi danymi zapełnione są oba rejestry przesuwne <m> i wtedy transmitowany jest sygnał strobe, <m>'
				'który wiąże się z przeniesieniem danych <m> z rejestru szeregowego (przesuwnego) do bufora wyjściowego. <m>'
			'Na ogół te dwie funkcje są realizowane przez jeden układ scalony, <m> natomiast z punktu widzenia sterowania to są dwa układy <m> sterowane dwoma niezależnymi zegarami. <m>'
			'Po takim cyklu możemy na przykład zmienić adres i w analogiczny sposób <m> przesłać dane do innego rejestru na tej magistrali. <m>'
		]
	},
]
