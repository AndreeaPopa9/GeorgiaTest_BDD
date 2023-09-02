Testare site Georgia and Lulu 

Proiectul are ca scop testarea funcționalității și comportamentului site-ului Georgia and Lulu prin metoda BDD.
Scenariile sunt descrise într-un limbaj simplu de înțeles folosind sintaxa Gherkin.

Cerințe preliminare:
1. Instalare Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
2. Instalare Python: https://www.python.org/downloads/
3. Instalare Browser Chrome: testele sunt concepute pentru a rula în Chrome.

Instalare:
1. Clonare repository prin introducere comandă în Git Bash: 
git clone https://github.com/AndreeaPopa9/ExamProject_BDD.
Pentru a naviga la folderul proiectului rulați următoarea comandă:
cd ExamProject_BDD.
2. Instalare librăria Selenium prin introducere în terminal a comenzii: pip install selenium sau sau pip install -U selenium (pentru update la zi)
3. Instalare WebDriver prin introducere în terminal a comenzii: pip install webdriver-manager 
4. Instalare librăria Behave prin introducere în terminal a comenzii: pip install behave
5. Pentru a genera rapoarte BDD se introduce următoarea comandă în terminal: pip install behave-html-formatter

Troubleshooting:
1. Dacă nu merge 2., încercați comanda: py -m pip install selenium
2. Dacă nu merge 3., încercați comanda: py -m pip install webdriver-manager
O altă variantă:
File -> Settings -> Click pe Proiect: ExamProject_BDD -> Python Interpreter -> +
Căutați "selenium" -> Install Package
Căutați "webdriver-manager" -> Install Package

Rulare:
1. Rularea completă a testelor se realizează prin introducere în terminal a comenzii: -behave
2. Rularea unui singur test se realizează prin introducerea în terminal a comenzii: -behave -i urmată de fișierul feature dorit -> -behave -i signin.feature
3. Rularea unui tag dintr-un test se realizează prin introducerea în terminal a comenzii: -behave --tags=nume_tag

Generare rapoarte:
1. Pentru toate testele se folosește comanda: behave -f html -o behave-report.html
2. Pentru un anumit test se folosește comanda: behave -f html -o behave-report.html -i urmată de fișierul feature dorit
3. Pentru un anumit tag se folosește comanda: behave -f html -o behave-report.html --tags=nume_tag

Accesare rapoarte:
1. Click pe fișierul behave-report.html 
2. Click pe icon-ul din dreapta a paginii pentru a se deschide în browser-ul dorit sau pe icon-ul Python pentru a se deschide în Python




