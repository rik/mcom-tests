#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from selenium import selenium
from page import Page


class PerformancePage(Page):
            
    _perf_web = "css=#perf-web"
    _perf_app = "css=#perf-app"
    _perf_hardware = "css=#perf-hardware"
    _perf_web_img = "css=#web>.section-image"
    _perf_app_img = "css=#performance-chart>tbody"
    _perf_hardware_img = "css=#hardware>.section-image"
    
    @property
    def perf_web_ico(self):
        return self.is_element_present(self._perf_web)
        
    @property
    def perf_app_ico(self):
        return self.is_element_present(self._perf_app)
        
    @property
    def perf_hardware_ico(self):
        return self.is_element_present(self._perf_hardware)
        
    @property
    def perf_web_img(self):
        return self.is_element_present(self._perf_web_img)
        
    @property
    def perf_app_img(self):
        return self.is_element_present(self._perf_app_img)
        
    @property
    def perf_hardware_img(self):
        return self.is_element_present(self._perf_hardware_img)
        
        
    
    