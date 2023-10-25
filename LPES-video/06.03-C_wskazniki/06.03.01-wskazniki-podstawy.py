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

code_wsk_A = r"""
#include <stdio.h>

int main() {
    int a = 13;
    int *b = &a;
    printf("%p %p\n", &a, b);
}
"""

code_wsk_B = r"""
#include <stdio.h>

int main() {
    int a = 13;
    int *b = &a;
    printf("%d %d\n", a, *b);

    *b = 17;
    printf("%d %d\n", a, *b);
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#06.3", "", "Wskaźniki w C", "" ] },
	
	{ 'comment': 'wskaźniki - podstawy' },
	{
		'image': [
			[0.0, ""]
		],
		'text' : [
			'Wszystkie dane na których operuje program komputerowy, <m> w tym oczywiście zmienne, są przechowywane w jakimś rodzaju pamięci. <m>'
			'Najczęściej w tak zwanej pamięci operacyjnej. <m>'
			'Może się jednak zdarzyć że niektóre zmienne są przechowywane tylko <m> w rejestrach procesora, czy też rejestrach urządzeń wejścia-wyjścia. <m>'
			'Jednak są to przypadki dosyć szczególne i jeżeli będziemy chcieli <m> taką zmienną potraktować tak jakby była w pamięci operacyjnej <m> to kompilator będzie udawał że jest to zmienna w pamięci. <m>'
			
			'W programowaniu na wyższym poziomie (czyli takim jak C) <m> praktycznie zawsze to właśnie kompilatorowi pozostawia się decyzję <m> gdzie będzie przechowywana dana zmienna.  <m>'
			'Oczywiście z pewnymi wyjątkami - jak na przykład gdy zaalokujemy jakiś <m> ciągły obszar pamięci to rzeczami w nim umieszczonymi możemy sami zarządzać. <m>'
			
			'Z każdą zmienną która znajduje się gdzieś w pamięci skojarzony <m> jest pewien adres, informujący o tym gdzie ona jest. <m>'
			'Na współczesnych komputerach jest to liczba <64>[sześćdziesięcio-cztero] bitowa, <m> na starszych komputerach może być liczba <32>[trzydziesto-dwu] bitowa, <m>'
			'a na niektórych systemach mogą to też być <m> liczby mniejsze, na przykład <16>[szesnasto] bitowe. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wsk_A, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_wsk_A, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'W przypadku C możemy poznać taki adres <m> i możemy operować na tych adresach w sposób dosyć niskopoziomowy, <m>'
			'czyli na przykład wziąć adres jednej zmiennej <m> i zobaczyć co jest pod adresem o <3>[trzy] większym. <m>'
			'Adresy takie, nazywamy wskaźnikami i mogą one być przechowywane w zmiennych. <m>'
			
			'Adres zmiennej możemy uzyskać poprzedzając jej nazwę znakiem ampersand. <m>'
			'Natomiast zmienną przechowującą adres możemy zdefiniować <m> podając pomiędzy typem zmiennej a jej nazwą gwiazdkę. <m>'
			'Zmienną taką, jak każdą inną w C możemy zainicjalizować od razu <m> lub pozostawić nie zainicjalizowaną. <m>'
			'Zmienną przechowującą adres nazywamy wskaźnikiem. <m>'
			'Często wskaźniki przed przypisaniem właściwego adresu inicjalizuje <m> się wartością <NULL>[nul], czyli zero aby móc sprawdzić czy zawiera on adres czy nie. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wsk_B, "c")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_wsk_B, args=["&& ./a.out"], cmd="gcc")],
		],
		'text' : [
			'Poprzedzenie nazwy zmiennej będącej wskaźnikiem gwiazdką <m> pozwala na odwołanie się do wartości zmiennej na którą mamy wskaźnik. <m>'
			'Jeżeli wskaźnik wskazuje na adres zero lub wskazuje na nie przydzielony <m> naszemu programowi obszar pamięci spowoduje to błąd <m> segmentation fault (określany też jako naruszenie ochrony pamięci). <m>'
			'Jeżeli wskaźnik wskazuje na niepoprawny, ale należący do naszego procesu <m> adres w pamięci to operowanie na wartości przez niego wskazywanej może prowadzić <m> do dziwnych i trudnych w diagnostyce błędów. <m>'
			
			'Jak widzimy w pokazanym przykładzie użycie operatora gwiazdki <m> na zmiennej będącej wskaźnikiem (czyli przechowującej adres innej zmiennej) <m>'
			'pozwala pobrać czy też zmodyfikować nie sam wskaźnik (czyli adres) <m> lecz to co jest w pamięci pod tym adresem. <m>'
			'Operację tą określa się mianem wyłuskania wskaźnika. <m>'
			
			'Oczywiście jeżeli pracujemy na systemie operacyjnym <m> używającym technologii pamięci wirtualnej, stronicowania, <itp.>[i tym podobnych] <m> to wskaźnik taki nie jest adresem w fizycznej pamięci RAM <m>'
			'a jedynie adresem w wirtualnej przestrzeni adresowej naszego procesu, <m> który przez system operacyjny jest dopiero mapowany na adres fizyczny. <m>'
			'Jednak na chwilę obecną nie ma to dla nas znaczenia. <m>'
		]
	},
]
