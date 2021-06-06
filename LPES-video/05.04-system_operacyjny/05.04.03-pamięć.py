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
	{ 'section': 'pamięć wirtualna' },
	{
		'image': [
			[0.0, eduMovie.convertFile('../../LPES-booklets/images-src/linux/pamięć_wirtualna.svg', negate=True)]
		],
		'text' : [
			"Jedną z funkcji systemu operacyjnego jest zarządzanie pamięcią. <m>"
			"System operacyjny każdemu procesowi przydziela pełną przestrzeń <m> adresową pamięci, czyli są to adresy od zera do pewnej maksymalnej liczby. <m>"
			"Każdy adres adresuje pojedynczy bajt, czyli adresowanie mamy bajtowe, <m> zatem każdy adres wskazuje na komórkę w której możemy mieć <m> wartość od zera do FF, czyli 256. <m>"
			
			"Nie oznacza to jednak, że dla każdego procesu <m> system operacyjny faktycznie rezerwuje tyle pamięci, <m>"
			"ponieważ ta liczba jest duża (i odpowiada tysiącom petabajtów) <m> i może być znacznie większa od ilości dostępnego RAMu, <m> a także możliwości adresowych procesora (ograniczonych na ogół do 256 <TB>[tera bajtów]). <m>"
			
			"Adres dzielony jest na kilka pól, oznaczmy je sobie x y z. <m>"
			
			"Na podstawie adresu, a dokładniej pól x i y, <m> system ustala adres obszaru fizycznej pamięci, nazywanego stroną. <m>"
			"Nie jest to zwykłe przypisanie jeden do jeden. <m>"
			"Natomiast realizowane jest to z użyciem wielopoziomowej tablicy stron. <m>"
			"Właśnie w celu realizacji tej wielopoziomowości mamy wydzielone pole x i y. <m>"
			"X wskazuje katalog stron, a y stronę w tym katalogu. <m>"
			"Zależnie od architektury poziomów takich może być więcej. <m>"
			
			"W tablicy stron dla każdej zaalokowanej strony przechowywana jest <m> informacja o adresie w pamięci fizycznej, <m> pod którym rozpoczyna się dana strona. <m>"
			"<Z>[zet] jest po przesunięciem względem początku strony. <m>"
			"Zatem w oparciu o adres początku strony <m> (ustalony na podstawie pól x i y oraz katalogu stron) <m> i pole <z>[zet] znany jest konkretny adres w pamięci RAM. <m>"
			"Mechanizm ten określany jest mianem stronicowania pamięci. <m>"
			
			"Czyli jeżeli programista dostanie od systemu albo z jakiegoś powodu <m> zaalokuje sobie pamięć na początku i pamięć gdzieś w środku przestrzeni adresowej, <m> a pamięci pomiędzy tymi obszarami i poza nimi w ogóle nie użyje. <m>"
			"To te zaalokowane obszary zostaną zamapowane na jakieś strony. <m> A pozostałe, nieużywane, fragmenty przestrzeni adresowej <m> nie będą zamapowane na prawdziwą fizyczną pamięć. <m>"
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('pamięć_wirtualna+hdd.svg', negate=True)]
		],
		'text' : [
			"W szczególności adres w pamięci wirtualnej nie musi być zamapowany <m> na coś co jest w RAMie, może być również zamapowany <m> na coś co jest na dysku twardym. <m>"
			"Ma to dwa zastosowania – pierwszym jest tak zwane mapowanie plików <m> do pamięci poprzez funkcję <mmap>[em map], a drugim używanie <m> pliku wymiany, w unix'ach nazywanego swap'em. <m>"
			"Jeżeli brakuje nam RAMu to nieużywane strony mogą zostać przeniesione <m> na dysk i zostać przeniesione z powrotem do pamięci <m> dopiero wtedy kiedy proces będzie chciał z nich korzystać. <m>"
			"W celu realizacji takich operacji w tablicy stron oprócz adresu początku <m> strony przechowywane są dodatkowe informacje na temat <m> jej statusu, położenia na dysku, <itp.>[i te pe.] <m>"
			
			"Mechanizm stronnicowania odpowiada także za to że potomek dostaje <m> tą samą pamięć co rodzic bez jej fizycznego kopiowania. <m>"
			'Dzieje się tak ponieważ dostaje dokładnie takie same mapowania, <m> które są oznaczone jedynie jako "copy on write", czyli mapowanie <m> zostaje zmienione na inną stronę dopiero w momencie modyfikacji, zapisu. <m>'
		]
	},
]
