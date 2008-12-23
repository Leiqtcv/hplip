# -*- coding: utf-8 -*-
#
# (c) Copyright 2001-2008 Hewlett-Packard Development Company, L.P.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# Authors: Don Welch
#

# StdLib
import operator

# Local
from base.g import *
from base import device, utils
from prnt import cups
from base.codes import *
from ui_utils import *
from fax import fax

# Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Ui
from faxsetupdialog_base import Ui_Dialog
from deviceuricombobox import DEVICEURICOMBOBOX_TYPE_FAX_ONLY


class FaxSetupDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, device_uri):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.device_uri = device_uri
        self.initUi()
        self.dev = None
        QTimer.singleShot(0, self.updateUi)


    def initUi(self):
        # connect signals/slots
        self.connect(self.CancelButton, SIGNAL("clicked()"), self.CancelButton_clicked)
        self.connect(self.FaxComboBox, SIGNAL("DeviceUriComboBox_noDevices"), self.FaxComboBox_noDevices)
        self.connect(self.FaxComboBox, SIGNAL("DeviceUriComboBox_currentChanged"), self.FaxComboBox_currentChanged)
        self.FaxComboBox.setType(DEVICEURICOMBOBOX_TYPE_FAX_ONLY)

        # Application icon
        self.setWindowIcon(QIcon(load_pixmap('prog', '48x48')))

        if self.device_uri:
            self.FaxComboBox.setInitialDevice(self.device_uri)

        self.NameCompanyLineEdit.setMaxLength(50)
        self.FaxNumberLineEdit.setMaxLength(50)
        self.FaxNumberLineEdit.setValidator(PhoneNumValidator(self.FaxNumberLineEdit))
        self.VoiceNumberLineEdit.setMaxLength(50)
        self.VoiceNumberLineEdit.setValidator(PhoneNumValidator(self.VoiceNumberLineEdit))
        self.EmailLineEdit.setMaxLength(50)

        self.connect(self.NameCompanyLineEdit, SIGNAL("editingFinished()"),
                     self.NameCompanyLineEdit_editingFinished)

        self.connect(self.NameCompanyLineEdit, SIGNAL("textChanged(const QString &)"),
                     self.NameCompanyLineEdit_textChanged)

        self.connect(self.FaxNumberLineEdit, SIGNAL("editingFinished()"),
                     self.FaxNumberLineEdit_editingFinished)

        self.connect(self.FaxNumberLineEdit, SIGNAL("textChanged(const QString &)"),
                     self.FaxNumberLineEdit_textChanged)

        self.connect(self.VoiceNumberLineEdit, SIGNAL("editingFinished()"),
                     self.VoiceNumberLineEdit_editingFinished)

        self.connect(self.VoiceNumberLineEdit, SIGNAL("textChanged(const QString &)"),
                     self.VoiceNumberLineEdit_textChanged)

        self.connect(self.EmailLineEdit, SIGNAL("editingFinished()"),
                     self.EmailLineEdit_editingFinished)

        self.connect(self.EmailLineEdit, SIGNAL("textChanged(const QString &)"),
                     self.EmailLineEdit_textChanged)

        self.name_company_dirty = False
        self.fax_number_dirty = False
        self.voice_number_dirty = False
        self.email_dirty = False


    def updateUi(self):
        self.FaxComboBox.updateUi()


    def FaxComboBox_currentChanged(self, device_uri):
        self.device_uri = device_uri
        self.updateCoverpageTab()

        if self.dev is not None:
            self.dev.close()

        try:
            self.dev = fax.getFaxDevice(self.device_uri)
        except Error:
            CheckDeviceUI(self)
            return

        self.updateHeaderTab()



    def FaxComboBox_noDevices(self):
        FailureUI(self, self.__tr("<b>No devices that require fax setup found.</b>"))
        self.close()

    #
    # Name/Company (for TTI header) (stored in device)
    #

    def NameCompanyLineEdit_editingFinished(self):
        self.saveNameCompany(unicode(self.NameCompanyLineEdit.text()))


    def NameCompanyLineEdit_textChanged(self, s):
        self.name_company_dirty = True


    def saveNameCompany(self, s):
        self.name_company_dirty = False
        beginWaitCursor()
        try:
            try:
                log.debug("Saving station name %s to device" % s)
                self.dev.setStationName(s)
            except Error:
                CheckDeviceUI()
        finally:
            endWaitCursor()

    #
    # Fax Number (for TTI header) (stored in device)
    #

    def FaxNumberLineEdit_editingFinished(self):
        self.saveFaxNumber(unicode(self.FaxNumberLineEdit.text()))


    def FaxNumberLineEdit_textChanged(self, s):
        self.fax_number_dirty = True


    def saveFaxNumber(self, s):
        self.fax_number_dirty = False
        beginWaitCursor()
        try:
            try:
                log.debug("Saving fax number %s to device" % s)
                self.dev.setPhoneNum(s)
            except Error:
                CheckDeviceUI()
        finally:
            endWaitCursor()

    #
    # Voice Number (for coverpage) (stored in ~/.hplip/hplip.conf)
    #

    def VoiceNumberLineEdit_editingFinished(self):
        self.saveVoiceNumber(unicode(self.VoiceNumberLineEdit.text()))


    def VoiceNumberLineEdit_textChanged(self, s):
        self.voice_number_dirty = True


    def saveVoiceNumber(self, s):
        log.debug("Saving voice number (%s) to ~/.hplip/hplip.conf" % s)
        self.voice_number_dirty = False
        user_cfg.fax.voice_phone = s

    #
    # EMail (for coverpage) (stored in ~/.hplip/hplip.conf)
    #

    def EmailLineEdit_editingFinished(self):
        self.saveEmail(unicode(self.EmailLineEdit.text()))


    def EmailLineEdit_textChanged(self, s):
        self.email_dirty = True


    def saveEmail(self, s):
        log.debug("Saving email address (%s) to ~/.hplip/hplip.conf" % s)
        self.email_dirty = False
        user_cfg.fax.email_address = s

    #
    #
    #

    def CancelButton_clicked(self):
        self.close()


    def updateHeaderTab(self):
        beginWaitCursor()
        try:
            try:
                name_company = self.dev.getStationName()
                self.NameCompanyLineEdit.setText(name_company)

                fax_number = self.dev.getPhoneNum()
                self.FaxNumberLineEdit.setText(fax_number)
            except Error:
                CheckDeviceUI()
        finally:
            endWaitCursor()


    def updateCoverpageTab(self):
        self.VoiceNumberLineEdit.setText(user_cfg.fax.voice_phone or u'')
        self.EmailLineEdit.setText(user_cfg.fax.email_address or u'')


    def closeEvent(self, e):
        if self.voice_number_dirty:
            self.VoiceNumberLineEdit.emit(SIGNAL("editingFinished()"))
        if self.name_company_dirty:
            self.NameCompanyLineEdit.emit(SIGNAL("editingFinished()"))
        if self.email_dirty:
            self.EmailLineEdit.emit(SIGNAL("editingFinished()"))
        if self.fax_number_dirty:
            self.FaxNumberLineEdit.emit(SIGNAL("editingFinished()"))
        e.accept()

    #
    # Misc
    #

    def __tr(self,s,c = None):
        return qApp.translate("FaxSetupDialog",s,c)


