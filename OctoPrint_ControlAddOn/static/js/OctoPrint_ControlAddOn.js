/*
 * View model for OctoPrint_ControlAddOn
 *
 * Author: Joshua Jarvis
 * License: AGPLv3
 */
$(function() {
    function OctoPrint_ControlAddOnViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: OctoPrint_ControlAddOnViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ /* "loginStateViewModel", "settingsViewModel" */ ],
        // Elements to bind to, e.g. #settings_plugin_OctoPrint_ControlAddOn, #tab_plugin_OctoPrint_ControlAddOn, ...
        elements: [ /* ... */ ]
    });
});
