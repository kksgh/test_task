# test_task
Решение задачи разделено на две папки. В папке pages находятся файл locators.py, certificate_page.py и два csv файла, входной и выходной. 
locators.py - страница селекторов страницы. 
certificate_page.py - логика поведения страницы/методы  
Файл test_certificate.py - сам тест страницы, в нем вызваются методы, описанные в файле certificate_page.py.
Файл conftest.py - описана возможность запускать тест с разных браузеров - chrome и firefox.
Для запуска необходимо 