from PyQt5.QtWidgets import (
    QDialog, QTabWidget, QWidget, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout,
    QRadioButton, QCheckBox, QLabel
)
from PyQt5.QtCore import Qt
from aqt import mw


class OptionsTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("tab demo")

    def tab1UI(self):
        self.setTabText(0, "Autocomplete")
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        self.tab1.setLayout(layout)

    def tab2UI(self):
        self.setTabText(1, "Autotranslate")
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.setTabText(2, "Education Details")
        self.tab3.setLayout(layout)


class OptionsDialog(QDialog):
    def __init__(self, parent=0):
        super(OptionsDialog, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint |
                            Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinMaxButtonsHint)
        self.parent = parent
        # self.setWindowIcon(app_icon)
        self.setWindowTitle('Options')
        self.build()

    def build(self):
        self.main_layout = QVBoxLayout()
        self.tabs = OptionsTabWidget()
        self.main_layout.addWidget(self.tabs)
        # tabs.addTab
    #     models_layout = QHBoxLayout()
    #     # add buttons
    #     mdx_button = QPushButton(_('DICTS_FOLDERS'))
    #     mdx_button.clicked.connect(self.show_fm_dialog)
    #     self.models_button = QPushButton(_('CHOOSE_NOTE_TYPES'))
    #     self.models_button.clicked.connect(self.btn_models_pressed)
    #     models_layout.addWidget(mdx_button)
    #     models_layout.addWidget(self.models_button)
    #     self.main_layout.addLayout(models_layout)
    #     # add dicts mapping
    #     dicts_widget = QWidget()
    #     self.dicts_layout = QGridLayout()
    #     self.dicts_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
    #     dicts_widget.setLayout(self.dicts_layout)

    #     scroll_area = QScrollArea()
    #     scroll_area.setWidgetResizable(True)
    #     scroll_area.setWidget(dicts_widget)

    #     self.main_layout.addWidget(scroll_area)
    #     # add description of radio buttons AND ok button
    #     bottom_layout = QHBoxLayout()
    #     paras_btn = QPushButton(_('SETTINGS'))
    #     paras_btn.clicked.connect(self.show_paras)
    #     about_btn = QPushButton(_('ABOUT'))
    #     # about_btn.clicked.connect(self.show_about)
    #     about_btn.clicked.connect(self.show_paras)
    #     chk_update_btn = QPushButton(_('UPDATE'))
    #     chk_update_btn.clicked.connect(self.check_updates)
    #     home_label = QLabel(
    #         '<a href="{url}">User Guide</a>'.format(url=Endpoint.user_guide))
    #     home_label.setOpenExternalLinks(True)
    #     # shop_label = QLabel(
    #     #     '<a href="{url}">Service Shop</a>'.format(url=Endpoint.service_shop))
    #     # shop_label.setOpenExternalLinks(True)
    #     btnbox = QDialogButtonBox(QDialogButtonBox.Ok, Qt.Horizontal, self)
    #     btnbox.accepted.connect(self.accept)
    #     bottom_layout.addWidget(paras_btn)
    #     bottom_layout.addWidget(chk_update_btn)
    #     bottom_layout.addWidget(about_btn)
    #     bottom_layout.addWidget(home_label)
    #     # bottom_layout.addWidget(shop_label)
    #     bottom_layout.addWidget(btnbox)
    #     self.main_layout.addLayout(bottom_layout)
    #     self.setLayout(self.main_layout)
    #     # init from saved data
    #     self.current_model = None
    #     if config.last_model_id:
    #         self.current_model = get_model_byId(
    #             mw.col.models, config.last_model_id)
    #         if self.current_model:
    #             self.models_button.setText(
    #                 u'%s [%s]' % (_('CHOOSE_NOTE_TYPES'),  self.current_model['name']))
    #             # build fields -- dicts layout
    #             self.build_mappings_layout(self.current_model)

    # def show_paras(self):
    #     dialog = ParasDialog(self)
    #     dialog.exec_()

    # def show_about(self):
    #     QMessageBox.about(self, _('ABOUT'), Template.tmpl_about)

    # def show_fm_dialog(self):
    #     fm_dialog = FoldersManageDialog(self)
    #     fm_dialog.activateWindow()
    #     fm_dialog.raise_()
    #     if fm_dialog.exec_() == QDialog.Accepted:
    #         dict_paths = fm_dialog.dict_paths
    #         fm_dialog.save()
    #         # update local services
    #         service_manager.update_services()
    #         # update_dicts_combo
    #         dict_cbs = self._get_combos(DICT_COMBOS)
    #         for i, cb in enumerate(dict_cbs):
    #             current_text = cb.currentText()
    #             self.fill_dict_combo_options(cb, current_text)

    # def accept(self):
    #     self.save()
    #     self.close()

    # def btn_models_pressed(self):
    #     self.save()
    #     self.current_model = self.show_models()
    #     if self.current_model:
    #         self.build_mappings_layout(self.current_model)

    # def build_mappings_layout(self, model):

    #     def clear_layout(layout):
    #         if layout is not None:
    #             while layout.count():
    #                 item = layout.takeAt(0)
    #                 widget = item.widget()
    #                 if widget is not None:
    #                     widget.deleteLater()
    #                 else:
    #                     clear_layout(item.layout())

    #     clear_layout(self.dicts_layout)

    #     label1 = QLabel("")
    #     label1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    #     label2 = QLabel(_("DICTS"))
    #     label2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    #     label3 = QLabel(_("DICT_FIELDS"))
    #     label3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    #     self.dicts_layout.addWidget(label1, 0, 0)
    #     self.dicts_layout.addWidget(label2, 0, 1)
    #     self.dicts_layout.addWidget(label3, 0, 2)

    #     maps = config.get_maps(model['id'])
    #     self.radio_group = QButtonGroup()
    #     for i, fld in enumerate(model['flds']):
    #         ord = fld['ord']
    #         name = fld['name']
    #         if maps:
    #             for j, each in enumerate(maps):
    #                 if each.get('fld_ord', -1) == ord:
    #                     self.add_dict_layout(j, fld_name=name, **each)
    #                     break
    #             else:
    #                 self.add_dict_layout(i, fld_name=name)
    #         else:
    #             self.add_dict_layout(i, fld_name=name)

        self.setLayout(self.main_layout)
        # self.resize(widget_size.dialog_width,
        #             (i + 1) * widget_size.map_max_height + widget_size.dialog_height_margin)

    # def show_models(self):
    #     edit = QPushButton(anki.lang._("Manage"),
    #                        clicked=lambda: aqt.models.Models(mw, self))
    #     ret = StudyDeck(mw, names=lambda: sorted(mw.col.models.allNames()),
    #                     accept=anki.lang._("Choose"), title=anki.lang._("Choose Note Type"),
    #                     help="_notes", parent=self, buttons=[edit],
    #                     cancel=True, geomKey="selectModel")
    #     if ret.name:
    #         model = mw.col.models.byName(ret.name)
    #         self.models_button.setText(
    #             u'%s [%s]' % (_('CHOOSE_NOTE_TYPES'), ret.name))
    #         return model

    # def dict_combobox_index_changed(self, index):
    #     # showInfo("combo index changed")
    #     dict_combos, field_combos = self._get_combos(ALL_COMBOS)
    #     assert len(dict_combos) == len(field_combos)
    #     for i, dict_combo in enumerate(dict_combos):
    #         # in windows and linux: the combo has current focus,
    #         # in mac: the combo's listview has current focus, and the listview can
    #         # be got by view()
    #         # showInfo('to check focus')
    #         if dict_combo.hasFocus() or dict_combo.view().hasFocus():
    #             self.fill_field_combo_options(
    #                 field_combos[i], dict_combo.currentText(), dict_combo.itemData(index))
    #             break

    # def fill_dict_combo_options(self, dict_combo, current_text):
    #     dict_combo.clear()
    #     dict_combo.addItem(_('NOT_DICT_FIELD'))
    #     dict_combo.insertSeparator(dict_combo.count())
    #     for service in service_manager.local_services:
    #         # combo_data.insert("data", each.label)
    #         dict_combo.addItem(
    #             service.title, userData=service.unique)
    #     dict_combo.insertSeparator(dict_combo.count())
    #     for service in service_manager.web_services:
    #         dict_combo.addItem(
    #             service.title, userData=service.unique)

    #     def set_dict_combo_index():
    #         dict_combo.setCurrentIndex(-1)
    #         for i in range(dict_combo.count()):
    #             if current_text in _sl('NOT_DICT_FIELD'):
    #                 dict_combo.setCurrentIndex(0)
    #             if dict_combo.itemText(i) == current_text:
    #                 dict_combo.setCurrentIndex(i)

    #     set_dict_combo_index()

    # def fill_field_combo_options(self, field_combo, dict_combo_text, dict_combo_itemdata):
    #     field_combo.clear()
    #     field_combo.setEnabled(True)
    #     if dict_combo_text in _sl('NOT_DICT_FIELD'):
    #         field_combo.setEnabled(False)
    #     elif dict_combo_text in _sl('MDX_SERVER'):
    #         field_combo.setEditText('http://')
    #         field_combo.setFocus(Qt.MouseFocusReason)  # MouseFocusReason
    #     else:
    #         field_text = field_combo.currentText()
    #         service_unique = dict_combo_itemdata
    #         current_service = service_manager.get_service(service_unique)
    #         # problem
    #         if current_service and current_service.fields:
    #             for each in current_service.fields:
    #                 field_combo.addItem(each)
    #                 if each == field_text:
    #                     field_combo.setEditText(field_text)

    # def radio_btn_checked(self):
    #     rbs = self.findChildren(QRadioButton)
    #     dict_cbs, fld_cbs = self._get_combos(ALL_COMBOS)
    #     for i, rb in enumerate(rbs):
    #         dict_cbs[i].setEnabled(not rb.isChecked())
    #         fld_cbs[i].setEnabled(
    #             (dict_cbs[i].currentText() != _('NOT_DICT_FIELD')) and (not rb.isChecked()))

    # def add_dict_layout(self, i, **kwargs):
    #     """
    #     kwargs:
    #     word_checked  dict  fld_name dict_field
    #     """
    #     word_checked, dict_name, dict_unique, fld_name, dict_field = (
    #         kwargs.get('word_checked', False),
    #         kwargs.get('dict', _('NOT_DICT_FIELD')),
    #         kwargs.get('dict_unique', ''),
    #         kwargs.get('fld_name', ''),
    #         kwargs.get('dict_field', ''),)

    #     word_check_btn = QRadioButton(fld_name)
    #     word_check_btn.setMinimumSize(widget_size.map_fld_width, 0)
    #     word_check_btn.setMaximumSize(widget_size.map_fld_width,
    #                                   widget_size.map_max_height)
    #     word_check_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    #     word_check_btn.setCheckable(True)
    #     word_check_btn.clicked.connect(self.radio_btn_checked)
    #     if i == 0:
    #         word_checked = True
    #     word_check_btn.setChecked(word_checked)
    #     self.radio_group.addButton(word_check_btn)

    #     dict_combo = QComboBox()
    #     dict_combo.setMinimumSize(widget_size.map_dictname_width, 0)
    #     dict_combo.setFocusPolicy(
    #         Qt.TabFocus | Qt.ClickFocus | Qt.StrongFocus | Qt.WheelFocus)
    #     dict_combo.setEnabled(not word_checked)
    #     dict_combo.currentIndexChanged.connect(
    #         self.dict_combobox_index_changed)
    #     self.fill_dict_combo_options(dict_combo, dict_name)

    #     field_combo = QComboBox()
    #     field_combo.setMinimumSize(widget_size.map_dictfield_width, 0)
    #     # field_combo.setMaximumSize(130, 30)
    #     field_combo.setEnabled((not word_checked) and (
    #         dict_name != _('NOT_DICT_FIELD')))
    #     field_combo.setEditable(True)
    #     field_combo.setEditText(dict_field)
    #     self.fill_field_combo_options(field_combo, dict_name, dict_unique)

    #     self.dicts_layout.addWidget(word_check_btn, i + 1, 0)
    #     self.dicts_layout.addWidget(dict_combo, i + 1, 1)
    #     self.dicts_layout.addWidget(field_combo, i + 1, 2)

    # def _get_combos(self, flag):
    #     # 0 : dict_combox, 1:field_combox
    #     dict_combos = self.findChildren(QComboBox)
    #     if flag in [DICT_COMBOS, DICT_FILED_COMBOS]:
    #         return dict_combos[flag::2]
    #     if flag == ALL_COMBOS:
    #         return dict_combos[::2], dict_combos[1::2]

    # def save(self):
    #     if not self.current_model:
    #         return
    #     data = dict()
    #     labels = self.findChildren(QRadioButton)
    #     dict_cbs, field_cbs = self._get_combos(ALL_COMBOS)
    #     maps = [{"word_checked": label.isChecked(),
    #              "dict": dict_cb.currentText().strip(),
    #              "dict_unique": dict_cb.itemData(dict_cb.currentIndex()) if dict_cb.itemData(dict_cb.currentIndex()) else "",
    #              "dict_field": field_cb.currentText().strip(),
    #              "fld_ord": get_ord_from_fldname(self.current_model, label.text()
    #                                              )}
    #             for (dict_cb, field_cb, label) in zip(dict_cbs, field_cbs, labels)]
    #     current_model_id = str(self.current_model['id'])
    #     data[current_model_id] = maps
    #     data['last_model'] = self.current_model['id']
    #     config.update(data)

    # def check_updates(self):

    #     self.updater = Updater()
    #     self.updater.chk_finish_signal.connect(self._show_update_result)
    #     self.updater.start()

    # @pyqtSlot(dict)
    # def _show_update_result(self, data):
    #     if data['result'] == 'ok':
    #         version = data['version']
    #         if version.decode() > VERSION:
    #             showInfo(Template.new_version.format(version=version))
    #         elif version.decode() == VERSION:
    #             showInfo(Template.latest_version)
    #         else:
    #             showInfo(Template.abnormal_version)
    #     else:
    #         showInfo(Template.check_failure.format(msg=data['msg']))


# class Updater(QThread):
    # chk_finish_signal = pyqtSignal(dict)

    # def __init__(self):
    #     super(QThread, self).__init__()

    # def run(self):
    #     try:
    #         import urllib2
    #     except:
    #         import urllib.request as urllib2
    #     try:
    #         req = urllib2.Request(Endpoint.check_version)
    #         req.add_header('Pragma', 'no-cache')
    #         resp = urllib2.urlopen(req, timeout=10)
    #         version = resp.read().strip()
    #         data = {'result': 'ok', 'version': version}
    #     except:
    #         info = _('CHECK_FAILURE')
    #         data = {'result': 'error', 'msg': info}

    #     self.chk_finish_signal.emit(data)


def show_options():
    # config.read()
    config = mw.addonManager.getConfig(__name__)
    opt_dialog = OptionsDialog(mw)
    opt_dialog.exec_()
    opt_dialog.activateWindow()
    opt_dialog.raise_()
# service_manager.fetch_headers()
