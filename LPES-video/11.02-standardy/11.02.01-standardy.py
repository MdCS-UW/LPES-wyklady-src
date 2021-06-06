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

if not eduMovie.checkCachedFile("cache/rfc760.txt", "rfc760"):
	os.system("wget -O cache/rfc760.txt https://www.rfc-editor.org/rfc/rfc760.txt")

if not eduMovie.checkCachedFile("cache/rfc791.txt", "rfc791"):
	os.system("wget -O cache/rfc791.txt https://www.rfc-editor.org/rfc/rfc791.txt")

try: clipData
except NameError: clipData = []

rfc760 = open("cache/rfc760.txt").read().split("\n")
rfc791 = open("cache/rfc791.txt").read().split("\n")

clipData += [
	{ 'title': [ "#11.2", "Standardy", "sieciowe", "" ] },
	
	{ 'comment': 'standardy' },
	{
		'image': [
			[0.0, ""],
		],
		'text' : [
			'Ethernet jest standaryzowany przez <IEEE>[aj tripol i], <m> czyli amerykański Instytut Inżynierów Elektryków i Elektroników. <m>'
			'Zasadniczo jest to cała rodzina standardów, <m> wśród najpopularniejszych należy wspomnieć o 100BASE-TX i 1000BASE-T. <m>'
			'Pierwszy z nich zapewnia prędkość 100 megabitów na sekundę, <m> wykorzystując tylko dwie pary skrętki. <m>'
			'Drugi zapewnia gigabit na sekundę, <m> jednak do tego celu używa wszystkich czterech par skrętki. <m>'
			
			'Skoro jesteśmy przy standardach i wiemy że za Ethernet odpowiada <IEEE>[aj tripol i]. <m>'
			'To jak wygląda z kwestia z protokołami IP? <break time="500ms"/> <m>'
			
			'Internet, czy też protokoły z nim związane, nie są standaryzowane przez żadną <m> z powszechnie uznanych organizacji standaryzacyjnych, <m> takich jak <IEEE>[aj tripol i], ISO, IEC, ANSI i tym podobne. <m>'
		]
	},
	{
		'console': [
			["0.0", eduMovie.clear + "\n\r".join(rfc760[0:24])],
			*[ [i*0.04,  "\n\r" + rfc760[i] + "\n\r" + rfc760[i+1] + "\n\r" + rfc760[i+2]] for i in range(0,len(rfc760)//3,3) ], # szybkie przewijanie
		],
		'text' : [
			'Prawie wszystkie standardy sieciowe związane z działaniem Internetu <m> są tworzone przez Internet Engineering Task Force, <m> w ramach numerowanej serii dokumentów RFC. <m>'
			'I z punktu widzenia prawa, organizacji standaryzacyjnych, <itd>[i te de] <m> są to standardy de facto. <m>'
			'Nie ma czegoś takiego jak Polska Norma opisująca protokół IP. <m>'
			
			'Dokumenty RFC (z jednym wyjątkiem) są zwykłymi plikami tekstowymi <m> i wyglądają tak jak widzimy na ekranie. <m>'
			'W odróżnieniu od innych "poważnych" standardów wszystkie <m> są publicznie dostępne w Internecie bez jakichkolwiek opłat <m> – można sobie taki dokument bez problemu pobrać, przeczytać i zastosować. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + "\n\r".join(rfc760[2:2+24])], # pierwsza strona
			*[  ["rfc2a - " + str((32-i)*0.1),  "\n\r" + rfc760[24+i]] for i in range(32) ],
			["rfc2a", eduMovie.clear + "\n\r".join(rfc760[33:33+24])],
			
			["rfc3", eduMovie.clear + "\n\r".join(rfc760[479:479+24])], # obrazek nr 1
			["rfc4", eduMovie.clear + "\n\r".join(rfc760[831:831+24])], # obrazek nr 3
			["rfc5", eduMovie.clear + "\n\r".join(rfc791[2:2+24])], # rfc 791 - pierwsza strona
		],
		'text' : [
			'Dokument który tutaj widzimy ma numerek 760 i nazywa się Internet Protocol, <m> jest on standardem DOD czyli amerykańskiego departamentu obrony, <m> opracowanym w styczniu 1980 roku. <m>'
			'Jest to dokument opisujący pierwszą <m> wyspecyfikowaną publicznie wersje protokołu IP. <m>'
			
			'Jak widzimy pochodzi on z 1980 roku, czyli internet ma już ponad 40 lat. <mark name="rfc2a" />'
			'Dokument został opracowany dla Agencji Zaawansowanych Projektów Badawczych <m> w Obszarze Obronności, znanej także z wielu innych projektów <m> jako ARPA bądź DARPA. <m>'
			'I został opracowany przez Uniwersytet Południowej Kalifornii. <mark name="rfc3" />'
			
			'Widzimy w nim na przykład strukturę warstwową protokołów, <m> czyli mamy protokoły warstwy aplikacyjnej (na przykład telnet, FTP), <m> protokoły warstwy transportowej, jakiś protokół sieci lokalnej, <m>'
				'a pomiędzy nimi właśnie protokół IP, <m> który jest opisywany w tym dokumencie. <mark name="rfc4" />'
			
			'W dokumencie możemy znaleźć także znaną nam już <m> ilustrację prezentującą nagłówek pakietu IP. <mark name="rfc5" />'
			
			'Dokument ten we wrześniu 1981 roku został zastąpiony dokumentem RFC 791, <m> który do dzisiaj pozostaje standardem opisującym IP w wersji czwartej. <m>',
			
			'Większość tak zwanych nowych technologii i otaczającej nas nowoczesności <m> wywodzi się właśnie z lat 70tych i 80tych ubiegłego wieku. <m>'
			'Na przykład większość komend uniksowych które poznawaliśmy działało <m> tak samo w latach 80tych ubiegłego wieku, tylko często miało trochę mniej opcji. <m>'
			'Więc nowoczesność ma tak około 40 lat. <m>'
			'Warto też zauważyć że świat systemów uniksowych rozwijał się <m> wraz z internetem i są one mocno związane, <m> czego ślady można znaleźć także w wielu dokumentach RFC. <m>'
			
			'Dokumenty RFC są zarówno poważnymi dokumentami opisującymi <m> fundamenty działania Internetu, takimi jak na przykład wspomniany 791, <m> jak również możemy spotkać dokumenty mniej poważne. <m>'
			'Przykładem może być RFC 1149, który opisuje sposób przesyłu pakietów IP <m> przy pomocy gołębi pocztowych, czyli w naszej strukturze warstwowej <m> warstwę sieci lokalnej, dostępu do sieci zastępujemy gołębiami pocztowymi. <m>'
			'RFC 3251 pochyla się nad zagadnieniem przesyłu energii elektrycznej <m> przy pomocy pakietów IP. <m>'
                        'Natomiast RFC 2324 opisuje standard kontroli ekspresów do kawy za pomocą protokołu podobnego do HTTP<m>'
			'Te mniej poważne dokumenty RFC ukazują się z datą pierwszego kwietnia <m> i stanowią ciąg dowcipów primaaprilisowych. <m>'

			'Ogólnie w odróżnieniu od wielu innych standardów, dokumenty RFC <m> (zarówno te poważne jak i primaaprilisowe) czyta się na ogół dosyć dobrze <m> i przede wszystkim można je czytać bo są publicznie dostępne. <m>'
			'Zatem warto niekiedy zajrzeć do takiego dokumentu, <m> aby zobaczyć jak tak naprawdę działa dany protokół, <m> jak go możemy zaimplementować i tak dalej. <m>'
		]
	},
]
