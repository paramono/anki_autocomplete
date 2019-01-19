from PyQt5.QtWidgets import QAction

import anki
from aqt import mw

from .ui import show_options


have_setup = False


def query_decor(func, obj):
    def callback():
        return func(obj)
    return callback


class Plugin:
    dialog_ready = False

    @classmethod
    def setup(cls):
        if not cls.dialog_ready:
            cls.setup_context_menu()
            cls.setup_options_menu()
            cls.dialog_ready = True

    @classmethod
    def setup_context_menu(cls):
        def on_setup_menus(web_view, menu):
            """
            add context menu to webview
            """
            wqmenu = menu.addMenu('Dictionary Query')
            action1 = wqmenu.addAction('Query All Fields')
            action2 = wqmenu.addAction('Query Current Field')
            action3 = wqmenu.addAction('Options')
            # action1.triggered.connect(query_decor(
            #     query_from_editor_all_fields, web_view.editor))
            # action2.triggered.connect(query_decor(
            #     query_from_editor_current_field, web_view.editor))
            # action3.triggered.connect(show_options)
            needs_separator = True
            # menu.addMenu(submenu)
        anki.hooks.addHook('EditorWebView.contextMenuEvent', on_setup_menus)
        # shortcuts = [(my_shortcut, query), ]
        # anki.hooks.addHook('setupEditorShortcuts', shortcuts)

    @classmethod
    def setup_options_menu(cls):
        # add options submenu to Tools menu
        # action = QAction(app_icon, "Autocomplete...", mw)
        action = QAction("Autocomplete...", mw)
        action.triggered.connect(show_options)
        mw.form.menuTools.addAction(action)
        cls.dialog_ready = True
