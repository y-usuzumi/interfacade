/**
 * Created by kj on 14-6-28.
 */

var ifutil = new function () {
    var self = this;
    var _dialog;
    var dialog = function () {
        if(!_dialog) {
            var expectedDialog = $(document).find('[ifdialog]');
            if (!expectedDialog.length) {
                // TODO:
            }
            _dialog = expectedDialog;
        }
        return _dialog;
    };

    self.render = function (url, selector) {
        $.get(url, function (data) {
            $(selector).html(data);
        });
    };

    self.popUp = function (url) {
        $.get(url, function (data) {
            dialog().find('[title]').text(data.title);
            dialog().find('[body]').text(data.body);
            dialog().modal('show')
        });
    }
};
