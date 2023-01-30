from digift.API.products import JsTestTask
from digift.API.session import APIsession


def test_search_alcatel(base_session: APIsession):

    response = base_session.get_js_test_task(search='Alcatel', sort_field='name')
    result = JsTestTask(response.json()['products'])

    for item in result.products:
        assert 'Alcatel' in item['name'], f'Ошибка поиска, Alcatel не содержится в поле "name" продукта {item}'

    def sort_by_name(prod):
        return prod['name']

    produce = result.products.copy()
    result.products.sort(key=sort_by_name)

    assert produce == result.products, 'Ответ не отсортирован по полю "name"'


