from modal.application_manager import ApplicationManager



def test_choose_500(app: ApplicationManager):

    (
        app.certificate.click_on_the_500()

        .check_value_500()
        .check_active_500()
     )


def test_choose_1000(app: ApplicationManager):

    (
        app.certificate.click_on_the_1000()

        .check_value_1000()
        .check_active_1000()
     )


def test_choose_2000(app: ApplicationManager):

    (
         app.certificate.click_on_the_2000()

         .check_value_2000()
         .check_active_2000()
    )


def test_choose_3000(app: ApplicationManager):

    (
        app.certificate.click_on_the_3000()

        .check_value_3000()
        .check_active_3000()
    )


def test_choose_5000(app: ApplicationManager):

    (
        app.certificate.click_on_the_5000()

        .check_value_5000()
        .check_active_5000()
    )


def test_choose_10000(app: ApplicationManager):

    (
        app.certificate.click_on_the_10000()

        .check_value_10000()
        .check_active_10000()
    )


