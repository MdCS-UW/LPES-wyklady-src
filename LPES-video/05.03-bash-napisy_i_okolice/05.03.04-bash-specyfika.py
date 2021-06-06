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

code_convert = r"""
for f in *.png; do
	convert "$f" "${f%.png}.jpg"
done
"""

clipData += [
	{ 'comment': 'specyfika basha' },
	{
		'console': [
			[0.0, eduMovie.code2console(code_convert, "sh")]
		],
		'text' : [
			'Bash jest dosyć specyficznym językiem programowania <m> w którym operujemy głównie na plikach i wywołujemy zewnętrzne programy. <m>'
			'Na ogół używany jest albo do wyciągania jakieś rzeczy z plików <m> albo do wykonywania operacji typu przenoszenie, czy zmiany nazw plików, <m>'
				'czyli wywoływania jakiś innych komend na plikach <m> lub odpowiednio przygotowanych nazwach przyszłych plików. <m>'
				
			'Programowanie w bashu polega w dużej mierze właśnie na wywoływaniu <m> zewnętrznych programów, na które można patrzeć trochę jak na biblioteki. <m>'
			'Na przykład grep programiście baszowemu dostarcza "bibliotekę" do obsługi <m> dopasowywania wyrażeń regularnych i wyszukiwania w oparciu o nie. <m>'
			'Image magic dostarcza bibliotekę do konwersji obrazków, <m> <ffmpeg>[ff em peg] bibliotekę do konwersji filmów, itd. <m>'
			
			'Często bash jest też traktowany jako język mający przygotować <m> środowisko pracy dla innej aplikacji, ustawić odpowiednie zmienne środowiskowe, <m> przygotować katalogi, przetworzyć ścieżki, itd. <m>'
		]
	},
]
