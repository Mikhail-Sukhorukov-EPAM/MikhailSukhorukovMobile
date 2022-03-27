from pages.contact_manager_helper import CMHelper


def test_simple1111111(app):
    app = CMHelper(app)
    app.add_contact()
    app.contact_name_edit_text_selectable(text="znay, ti samechtelniy")

    assert app.WARNING_TEXT == app.get_warning_message()
