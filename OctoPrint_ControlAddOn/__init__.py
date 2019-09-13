# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import octoprint.settings

class OctoPrint_ControlAddOnPlugin(octoprint.plugin.StartupPlugin,
                      octoprint.plugin.TemplatePlugin,
                      octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin):

    def get_assets(self):
        return dict(
            js=["js/OctoPrint_ControlAddOn.js"],
        )

    def on_after_startup(self):
        self._logger.info("OctoPrint_ControlAddOn Loaded! (more: %s)" % self._settings.get(["OctoPrint_ControlAddOn_profiles"]))

    def get_settings_version(self):
        return 1

    def on_settings_migrate(self, target, current=None):
        if current is None or current < self.get_settings_version():
            self._logger.debug("Settings Migration Needed! Resetting to defaults!")
            # Reset plug settings to defaults.
            self._settings.set(['OctoPrint_ControlAddOn_profiles'], self.get_settings_defaults()["OctoPrint_ControlAddOn_profiles"])

    def get_settings_defaults(self):
        return dict(OctoPrint_ControlAddOn_profiles=[{'name':'Lights On','command':'M420 R255 B255', 'isButtonEnabled':'true'}])

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=True),
            dict(type="generic", template="OctoPrint_ControlAddOn.jinja2", custom_bindings=True)
        ]

    ##~~ Softwareupdate hook
    def get_version(self):
        return self._plugin_version

    def get_update_information(self):
        return dict(
            OctoPrint_ControlAddOn=dict(
                displayName="OctoPrint_ControlAddOn",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="jmj3886",
                repo="OctoPrint_ControlAddOn",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/jmj3886/OctoPrint_ControlAddOn/archive/{target_version}.zip"
            )
        )

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = OctoPrint_ControlAddOnPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

