from aqt import mw
# from aqt.utils import showInfo
# from aqt.qt import *
from aqt import editor
from aqt.utils import showInfo
from anki.hooks import addHook, wrap

# import requests
from .engines.glosbe import AutocompleteGlosbe
from .prepare import Plugin



noAutocompleteFields = []


class Engine(object):
    def query(self, text, **kwargs):
        pass


class AnkiEngine(object):
    def query(self, text, **kwargs):
        pass


def setNote(self, note, hide=True, focusTo=None):
    self.prevAutocomplete = ""

    # only initialize the autocompleter on Add Cards not in browser
    # showInfo('In custom setup')
    if self.note and self.addMode:
        # showInfo('Note and addMode')
        self.web.eval("""
            document.styleSheets[0].addRule(
                '.autocomplete',
                'margin: 0.3em 0 1.0em 0; z-index: 1;');
            document.styleSheets[0].addRule(
                '.autocomplete-entry',
                'color: blue; text-decoration: underline; cursor: pointer;'
            );
            $(document).on("click", ".autocomplete-entry", function () {{
                // pycmd("log:clicked entry");
                var entry = $(this).attr('data-entry');
                document.currentField.focus();
                document.currentField.innerHTML = entry;
                saveField("key");
            }});
        """)


def onBridgeCmd(self, cmd, _old=None):
    # if not cmd.startswith('blur'):
    #     showInfo('cmd: %s' % cmd)
    _old(self, cmd)
    if cmd.startswith('log'):
        type, text = cmd.split(':', 1)
        showInfo('innerHTML: %s' % text)
    if cmd.startswith('key'):
        # type, json_text = cmd.split(":", 1)
        type, ord, nid, txt = cmd.split(":", 3)
        # result = self.currentField.innerHTML
        # result = txt
        text = self.mungeHTML(txt)
        # result = json.loads(txt)
        # text = self.mungeHTML(result['text'])

        # bail out if the user hasn't actually changed the field
        previous = "%d:%s" % (self.currentField, text)
        if self.prevAutocomplete == previous:
            return
        self.prevAutocomplete = previous

        if text == "" or len(text) > 500 or self.note is None:
            self.web.eval("$('.autocomplete').remove();")
            return

        field = self.note.model()['flds'][self.currentField]

        if field['name'] in noAutocompleteFields:
            field['no_autocomplete'] = True

        if 'no_autocomplete' in field.keys() and field['no_autocomplete']:
            return


        # glosbe_url = 'https://glosbe.com/ajax/phrasesAutosuggest?from=pl&dest=ru&phrase=%s' % text
        # r = requests.get(glosbe_url)
        # if not r.status_code == 200:
        #     showInfo('Request failed: %s' % r.status_code)
        #     return

        # entries = r.json()
        entries = AutocompleteGlosbe.query(text)

        # suggestions_str = '<br>'.join(suggestions)

        html_container = '''
            $('.autocomplete').remove();
            if (currentField) {
                $('<div class="autocomplete"></div>').insertAfter(currentField);
            }
        '''

        template_entry = '''
            if (currentField) {{
                document.currentField = currentField;
                $('<div data-entry="{entry}" class="autocomplete-entry">{entry}</div>').appendTo($('.autocomplete'));
            }}
        '''

        self.web.eval(html_container)
        for entry in entries:
            html_entry = template_entry.format(entry=entry)
            self.web.eval(html_entry)


def main():
    # from . import prepare
    # cardCount = mw.col.cardCount()
    # wquery.config.read()
    Plugin.setup()
    # showInfo("Card count: %d" % cardCount)

# action = QAction("test", mw)
# action.triggered.connect(testFunction)
# mw.form.menuTools.addAction(action)

addHook("profileLoaded", main)

editor.Editor.onBridgeCmd = wrap(editor.Editor.onBridgeCmd, onBridgeCmd, 'around')
editor.Editor.setNote = wrap(editor.Editor.setNote, setNote, 'after')
