Repozytorium zawiera źródła skryptów oraz wykładów video dla zajęć kursu
„[Linux i Python w Elektronicznej Sieci](http://ciekawi.icm.edu.pl/lpes/)”
prowadzonego w ramach projektu
„[Matematyka dla Ciekawych Świata](http://ciekawi.icm.edu.pl/)”.

## Zależności

Repozytorium korzysta z *git submodule* do śledzenia repozytoriów z których korzysta.

Główną tego typu zależnością jest [OpCode.eu.org](https://bitbucket.org/OpCode-eu-org/opcode-main) wraz z jego zależnościami.
Repozytorium to zawiera znaczną część treści skryptów i część obrazków używanych w wykładach.
Repozytorium to (wraz z jego zależnościami) dostarcza także systemu budowania dla skryptów i
dlatego w celu kompilacji skryptów do postaci PDF konieczna jest instalacja zależności opisanych w jego dokumentacji.

### Inicjalizacja i instalacja zależności

Po sklonowaniu repozytorium należy:

1. pobrać wykorzystywane submoduły przy pomocy polecenia `make init`
2. zapoznać się z [.OpCode.eu.org/README.md](.OpCode.eu.org/README.md) i zainstalować zależności tego submodułu

**Uwaga:** Samo wykonanie `make init` jest wystarczające do używanie tego repozytorium pod warunkiem posiadania zainstalowanych wymaganych do zbudowania danego pliku/katalogu narzędzi (np. wget, lualtex).
          **Nie ma potrzeby budowania repozytorium .OpCode.eu.org.**
          Sugerowane jest tylko zainstalowanie jego zależności (czyli tych narzędzi potrzebnych do budowania poszczególnych plików).
          Jednak polecenia `sudo make installDependencies` opisane w [.OpCode.eu.org/README.md](.OpCode.eu.org/README.md) używają apt do instalacji wymaganych pakietów oprogramowania i są dedykowane dla Debian Buster.

Uaktualnienie wersji submodułów używanej przez to repo możliwe jest przy pomocy polecenia: `make update-submodules`

## Budowanie dokumentów PDF

* Aby zbudować wszystkie pliki można użyć polecenia `make all` (w danym podkatalogu lub w katalogu głównym).
* Aby zbudować pojedynczy plik PDF w katalogu z jego źródłami należy uruchomić polecenie `make nazwa`, gdzie `nazwa` to nazwa pliku bez rozszerzenia, np. dla pliku `aaa.pdf` budowanego z `aaa.tex` będzie to `make aaa`.
* Aby zbudować wersję dla prowadzącego do nazwy należy dodać przyrostek `--teacher`, np. `make aaa--teacher`
* Aby wymusić przebudowanie pliku (ignorując śledzenie zależności *make*) należy dodać do polecenia `VERBOSE=1`, np. `make aaa VERBOSE=1`
* Pliki wynikowe znajdują się w katalogu `output-www`

## Struktura

Repozytorium składa się z kilku katalogów:

* **LPES-booklets** – skrypty „wykładowe”, zawierające informacje teoretyczne oraz zadania wraz z rozwiązaniami i ich omówieniem
  (materiały te złożone są w zdecydowanej większości z fragmentów „booklets-sections” pochodzących z repozytorium *OpCode.eu.org*)
* **LPES-logo** – logo kursu / plansza tytułowa filmów wykładowych
* **LPES-video** – scenariusze, elementy graficzne i system generowania filmów wykładowych

Repozytorium nie zawiera źródeł skryptów ćwiczeniowych i rozwiązań zadań znajdujących się w tych skryptach.

### Struktura katalogów i Makefile

Oprócz plików `.tex` i `.xml` katalogi ze źródłami (np. `booklets`) mogą zawierać także:

* katalog `extra-tex-files` przeznaczony na dodatkowe pliki używane przez LaTeX (np. obrazki lub pliki LaTeX)
	* w plikach LaTeX odwoływać się do nich należy z pominięciem nazwy tego katalogu – np. do pliku `extra-tex-files/abc/xyz.jpg` poprzez `abc/xyz.jpg` lub `abc/xyz`
* katalog `extra-web-files` przeznaczony na dodatkowe pliki używane w XML/XHTML (np. obrazki)
	* w plikach XML odwoływać się do nich należy z pominięciem nazwy tego katalogu – np. do pliku `extra-tex-files/abc/xyz.jpg` poprzez `abc/xyz.jpg`
* katalog `images-src` przeznaczony na źródłowe wersje obrazków które będą automatycznie konwertowane na formaty obsługiwane przez LaTeX lub WWW
	* obsługiwane są pliki:
		* grafiki wektorowej .svg (tylko LaTeX, konwersja na pdf)
		* schematy pakietu [gEDA](http://www.geda-project.org/) .sch (konwersja na .pdf dla LaTeX lub .svg dla XHTML)
	* w plikach LaTeX odwoływać się do nich należy z zastąpieniem nazwy tego katalogu przez `img` i pominięciem rozszerzenia – np. do pliku `images-src/abc/xyz.sch` poprzez `abc/xyz`
	* w plikach XML odwoływać się do nich należy z zastąpieniem nazwy tego katalogu przez `img` i zastąpieniem rozszerzenia na `.svg` – np. do pliku `images-src/abc/xyz.sch` poprzez `abc/xyz.svg`
* plik `Makefile` w którym należy określić zależność pliku wynikowego od plików z katalogów `extra-tex-files` i `images-src`
	*  na przykład dla skryptu o treści w pliku `aaa.tex` używającego plików w katalogu `images-src/abc` i pliku `extra-tex-files/xyz.png` będzie to:<br />
	   `$(OUTDIR)/aaa.pdf:  extra-tex-files/xyz.png  $(call img4tex_from_src,abc/*)`
	* pominięcie zależności z `images-src` spowoduje nie wykonanie konwersji i niedostępność tych plików w trakcie budowania pliku LaTeX
	* pominięcie zależności z `extra-tex-files` lub `extra-web-files` spowoduje jedynie brak przebudowania skryptu przez make po modyfikacji tych plików

