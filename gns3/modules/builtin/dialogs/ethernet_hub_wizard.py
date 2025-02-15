# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Wizard for Ethernet hubs.
"""

from gns3.qt import QtGui, QtWidgets
from gns3.node import Node
from gns3.dialogs.vm_wizard import VMWizard

from ..ui.ethernet_hub_wizard_ui import Ui_EthernetHubWizard


class EthernetHubWizard(VMWizard, Ui_EthernetHubWizard):

    """
    Wizard to create an Ethernet hub.

    :param parent: parent widget
    """

    def __init__(self, ethernet_hubs, parent):

        super().__init__(ethernet_hubs, parent)

        self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/hub.svg"))
        self.uiNameWizardPage.registerField("name*", self.uiNameLineEdit)

    def getSettings(self):
        """
        Returns the settings set in this Wizard.

        :return: settings dict
        """

        ports = []
        for port_number in range(0, self.uiPortsSpinBox.value()):
            ports.append({"port_number": int(port_number),
                          "name": "Ethernet{}".format(port_number)})

        settings = {"name": self.uiNameLineEdit.text(),
                    "symbol": "hub",
                    "category": Node.switches,
                    "compute_id": self._compute_id,
                    "ports_mapping": ports}

        return settings
