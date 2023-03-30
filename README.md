# hello idol


---
1. start project
   1. pip install django ~= 3.2
   2. django-admin startproject _helloidol_ .
   3. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. _helloidol_/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달 : urls -> views -> (models ->)templates
   - 코드 작성 : (models ->)views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
      3. _playground/bye/_ -> _say_bye()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello/_ -> _say_hello_html()_
      3. _playground/_ -> _bye/_ -> _say_bye()_
5. startapp _shinee_
   1. Terminal
      1. python manage.py startapp _shinee_
   2. helloidol/settings.py
      1. '_shinee_', in INSTALLED_APPS
6. helloidol/urls
   1. _shinee_/-> shinee.urls
7. _shinee_/
   1. show_taemin()
   2. show_on()
2. urls
   1. shinee/ -> taemin/-> show_taemin()
   2. shinee/ -> on/-> show_on()
3. templates/shinee/
   1. ~~taemin.html~~
   2. ~~on.html~~
   3. 멤버.html