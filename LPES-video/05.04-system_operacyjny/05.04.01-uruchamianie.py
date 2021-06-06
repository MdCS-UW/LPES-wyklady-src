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

endTitleSVG="JS.svg"

clipData += [
	{ 'title': [ "#05.4", "Wprowadzenie", "do systemów", "operacyjnych" ] },
	
	{ 'comment': '' },
	{
		'image': [
			[0.0, ""]
		],
		'text' : [
			"Należy powiedzieć także kilka słów na temat samego systemu operacyjnego, <m> jako takiego, gdyż Linux czy też inne unixy, <m> o których już sporo mówiliśmy są przykładami systemów operacyjnych. <m>"
			"Ponadto Zagadnienia z tego zakresu dobrze obrazują samo działanie komputerów. <m>"
			
			"Na początek zastanówmy się jak wygląda w ogóle proces startu komputera, <m> czyli co komputer zaczyna robić po jego uruchomieniu? <m>"
			"Naciskamy przycisk power na obudowie, <m> procesor (tak jak i inne elementy) dostaje zasilanie. <m>"
			"Typowo procesory są wprowadzane w stan Power On Reset, <m> czyli resetują się w momencie uzyskania zasilania. <m>"
			
			"Ze stanem resetu procesora związane jest to, że z konkretnego adresu <m> na swojej szynie zaczynają pobierać instrukcje do wykonania. <m>"
			"W przypadku komputerów PC te instrukcje są pobierane z systemu BIOS, <m> w niektórych dawnych komputerach były one wczytywane z karty perforowanej <m> lub ustawiane mechanicznymi przełącznikami na obudowie. <m>"
			
			"W momencie jak procesor przetworzy już te pierwsze instrukcje <m> i na przykład nauczy się obsługiwać dysk twardy <m> to może przejść do załadowania bootloadera. <m>"
			"Bootloader jest prostym programem mającym za zadanie załadować <m> z odpowiedniego miejsca jądro systemu operacyjnego. <m>"
			
			"Po załadowaniu jądra uruchamiany jest pierwszy proces, <m> który otrzymuje identyfikator PID o wartości jeden. <m>"
			"Proces ten działa na prawach <root'a>[ruta] <m> i może nim być na przykład init lub <systemd>[system di]. <m>"
		]
	},
	{
		'image': [
			[0.0, ""]
		],
		'text' : [
			"Uzyskanie dostępu do danych na komputerze do którego mamy <m> fizyczny dostęp, zalogowanie się na takim komputerze <m> jest proste pod warunkiem że dysk nie został zaszyfrowany. <m>"
			"Takie włamanie na lokalny komputer w najprostszym przypadku <m> polega na wskazaniu w opcjach uruchomieniowych jądra <m> innego niż domyślny programu, który ma zostać uruchomiony jako pierwszy proces. <m>"
			"Czyli jeżeli mamy bootloader niezabezpieczony hasłem <m> to w opcjach jądra możemy dopisać np. <init=/bin/bash>[init równa się ukośnik bin ukośnik bash] <m>"
				"i jako pierwszy proces zostanie uruchomiona powłoka bash <m> działająca na prawach <root'a>[ruta], bez podawania hasła. <m>"
			
			"W tym momencie raczej nie będą zamontowane dyski twarde w trybie <m> do zapisu i tak dalej, ale wszystkie te operacje, jeżeli są nam potrzebne, <m> możemy wykonać manualnie w uzyskanej powłoce. <m>"
			"W związku z tym jeżeli mamy fizyczny dostęp do maszyny z linuxem, <m> na której dyski są nie szyfrowane, to zasadniczo mamy na niej <root'a>[ruta]. <m>"
			
			"Nawet jeżeli bootloader nie pozwala nam na modyfikację <m> tych opcji to możemy użyć bootowalnego <pendrive>[pendrajwa]. <m>"
			"Jeżeli BIOS zabezpieczony jest hasłem to można je zresetować <m> za pomocą bateryjki i tak dalej. <m>"
			"W ostateczności możemy podpiąć dysk do innego komputera. <m>"
			
			"Dostęp fizyczny jest równoważny z prawami roota <m> i jest to feature a nie <bug>[bag] <m>"
				"– po prostu nie można sobie pozwolić, aby śmierć administratora <m> wymagała na przykład zaorania kluczowych systemów, <m> bo tylko administrator znał hasło. <m>"
		]
	},
]
