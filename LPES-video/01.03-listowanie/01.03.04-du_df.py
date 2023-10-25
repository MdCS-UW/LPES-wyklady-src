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
	{ 'section': 'polecenia du i df' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"du bb.txt", cwd='demo')],
			[3.0, eduMovie.runCommandString(r"du -h bb.txt", cwd='demo')],
			["duvsls", eduMovie.runCommandString(r"ls -lh bb.txt", cwd='demo')],
			["duvsls2", eduMovie.runCommandString(r"du -h abc", cwd='demo')],
			["duvsls2+1.3", eduMovie.runCommandString(r"ls -lh abc", cwd='demo')],
			["duvsls3", eduMovie.runCommandString(r"du -h sparse-file", cwd='demo')],
			["duvsls3+1.3", eduMovie.runCommandString(r"ls -l sparse-file", cwd='demo')],
			["df", eduMovie.runCommandString(r"df -h .", cwd='demo')],
		],
		'text' : [
			'Kolejnym programem związanym poniekąd z listowaniem plików <m> jest polecenie <du>[D U], które pozwala na uzyskanie informacji na temat rozmiaru danego pliku. <m>'
			'Jeżeli dodamy opcje <-h>[minus h] będziemy mieli podawane to "po ludzku", <m> czyli w kilobajtach, megabajtach, itd. <m>'
			'Jeżeli nie podamy tej opcji, wynik będzie podawany w blokach <m> o wielkości 1 kilobajta albo (na niektórych systemach) pół kilobajtowych. <mark name="duvsls" />',
			
			'Warto zwrócić uwagę na różnicę rozmiaru podawanego <m> przez polecenie <ls>[LS] oraz podawanego przez <du>[D U]. <m>'
			'<ls>[LS] mówi nam że ten plik zajmuje 25 bajtów, <m> a <du>[D U] mówi nam że ten plik zajmuje 4 kilobajty. <m>'
			'Żadna z tych komend tak naprawdę nie kłamie, po mimo że mówią co innego. <m>'
			'<ls>[LS] informuje o tym ile mamy informacji w tym pliku, <m> czyli jaki jest rozmiar zawartości tego pliku <m> i zawartość tego pliku obejmuje 25 bajtów. <m>'
			'Natomiast <du>[D U] mówi ile ten plik zajmuje na dysku twardym <m> w tym przypadku 4 kilo bajty. <m>'
			'Dzieje się tak dlatego, <m> że miejsce na dysku twardym <alokowane>[a-lokowoane] jest w pewnych jednostkach, <m> zwanych blokami i w tym wypadku rozmiar bloku wynosi 4 kilobajty, <m>'
			'czyli jest to najmniejsza część dysku, którą plik może zająć. <m>'
			'Nawet jeżeli plik ma mieć jeden bajt danych, to na dysku twardym <m> musimy na niego przeznaczyć cztery kilobajty. <mark name="duvsls2" />',
			
			'Możemy też sprawdzić ile miejsca na dysku zajmuje plik pusty. <m>'
			'Jak widać, pusty plik zajmuje na dysku zero miejsca, <m> ponieważ nie ma potrzeby alokowania na niego przestrzeni dyskowej, <m> gdyż w tym pliku nie ma żadnych informacji. <mark name="duvsls3" />'
			'Można się spotkać także z sytuacją, że deklarowany rozmiar pliku <m> jest większy niż jego rzeczywista zawartość oraz zajmowane miejsce na dysku. <m>'
			'Pliki tego typu nazywane są plikami rzadkimi (sparse files). <m>',
			
			'Z kolei przy pomocy polecenia <df>[DF] możemy sprawdzać <m> dostępność miejsca na dysku twardym. <mark name="df" />'
			'Również polecam opcje <-h>[minus h], <m> dzięki której zostanie to wypisane w ludzkich jednostkach. <m>'
			'Jeżeli jej nie użyjemy to mamy informację dużo bardziej precyzyjną <m> (bo w pojedynczych blokach), <m> ale też mniej czytelną dla człowieka. <m>'
			
			'Gdy chcemy sprawdzić ile mamy miejsca dostępnego w bieżącym katalogu, <m> oczywiście pomijając zagadnienia limitu miejsca dla danego użytkownika typu quota <m> i tym podobne, '
				'możemy napisać <df -h .>[DF minus h kropka] <m> i wtedy polecenie to <m> wypiszę informację wyłącznie dla systemu plików <m> na którym znajduje się podany katalog <m> w tym wypadku katalog bieżący oznaczony kropką. <m>'
		]
	},
]
