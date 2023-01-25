
def test_api_js_test_task(base_session):
    name = 'Alcatel'

    result = base_session.get(url='/api/js-test-task',
                              params={'search': 'Alcatel', 'sort_field': 'name'})

    assert result.status_code == 200
    assert result.json()['name'] == name


