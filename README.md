# Проект автоматизации тестирования для <a target="_blank" >Lenvendo</a>


## :gear: В проекте используются следующие технологии и инструменты:
<p align="center">
<img width="5%" title="Python" src="https://github.com/Margolog/diplom_API/blob/master/resources/python.png">
<img width="6%" title="Pytest" src="https://github.com/Margolog/diplom_API/blob/master/resources/pytest.png">
<img width="5%" title="PyCharm" src="https://github.com/Margolog/diplom_API/blob/master/resources/pycharm.png">
<img width="6%" title="Allure" src="https://github.com/Margolog/diplom_UI/blob/master/resources/allure_report.png">
<img width="6%" title="Selene" src="https://github.com/Margolog/diplom_API/blob/master/resources/selene.png">
</p>


## :heavy_check_mark: Описание
В проекте автоматизирована UI проверка подарочных карт различным наминалом и проверка GET https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name'

## :heavy_check_mark: Что проверяем

> - UI - Активация кнопки с выбранным наминалом;
> - UI - Отображение выбранного наминала;
> - API - Все поля "name" в ответе на запрос содержат значение "Alcatel";
> - API - Все элементы в ответе отсортированы по полю 'name' по алфавиту от А до Я.

