/*
 * Simplified non-AMD version of frontend's Formstack module:
 * https://github.com/guardian/frontend/blob/694b3ab490198cdad4159ae5b3425171d1c04e7a/static/src/javascripts/projects/common/modules/identity/formstack.js
 *
 * Removed Identity integration
 * Removed iframe messaging
 * Use jQuery since it's a Formstack dependency anyway
 */
var FormstackForm = function ($) {

    var self = this,
        el = $('.formstackForm')[0],
        dom = {};

    config = {
        idClasses: {
            form: 'form',
            field: 'form-field',
            note: 'form-field__note form-field__note--below',
            label: 'label',
            checkboxLabel: 'check-label',
            textInput: 'text-input',
            textArea: 'textarea textarea--no-resize',
            submit: 'submit-input',
            fieldError: 'form-field--error',
            formError: 'form__error',
            fieldset: 'formstack-fieldset',
            required: 'formstack-required',
            sectionHeader: 'formstack-heading',
            sectionHeaderFirst: 'formstack-heading--first',
            sectionText: 'formstack-section',
            characterCount: 'formstack-count',
            hide: 'is-hidden'
        },
        fsSelectors: {
            form: '#' + $('.fsForm').attr('id'),
            field: '.fsRow',
            note: '.fsSupporting, .showMobile',
            label: '.fsLabel',
            checkboxLabel: '.fsOptionLabel',
            textInput: '.fsField[type="text"], .fsField[type="email"], .fsField[type="number"], .fsField[type="tel"]',
            textArea: 'textarea.fsField',
            submit: '.fsSubmitButton',
            fieldError: '.fsValidationError',
            formError: '.fsError',
            fieldset: 'fieldset',
            required: '.fsRequiredMarker',
            sectionHeader: '.fsSectionHeading',
            sectionHeaderFirst: '.fsSection:first-child .fsSectionHeading',
            sectionText: '.fsSectionText',
            characterCount: '.fsCounter',
            hide: '.hidden, .fsHidden, .ui-datepicker-trigger'
        },
        hiddenSelectors: {
            userId: '[type="number"]',
            email: '[type="email"]'
        }
    };

    self.init = function () {
        self.dom();
        self.styles();
    };

    self.styles = function () {
        $('link, style', el).remove();
        $(el).removeClass(config.idClasses.hide);
    };

    self.dom = function () {
        var selector;

        // Formstack generates some awful HTML, so we'll remove the CSS links,
        // loop their selectors and add our own classes instead
        dom.$form = $(config.fsSelectors.form, el).addClass(config.idClasses.form);

        for (selector in config.fsSelectors) {
            $(config.fsSelectors[selector], dom.$form).addClass(config.idClasses[selector]);
        }

        // Events
        $(dom.$form[0]).on('submit', self.submit);
    };

    self.submit = function (event) {
        event.preventDefault();

        setTimeout(function () {
            // Remove any existing errors
            $('.' + config.idClasses.formError, dom.$form).removeClass(config.idClasses.formError);
            $('.' + config.idClasses.fieldError, dom.$form).removeClass(config.idClasses.fieldError);

            // Handle new errors
            $(config.fsSelectors.formError, dom.$form).addClass(config.idClasses.formError);
            $(config.fsSelectors.fieldError, dom.$form).addClass(config.idClasses.fieldError);

            // Update character count absolute positions
            $(config.fsSelectors.textArea, dom.$form).each(function () {
                $(this).trigger('keyup');
            });

            // if no errors, submit form
            if ($(config.fsSelectors.formError, dom.$form).length === 0) {
                dom.$form[0].submit();
            }

        }, 100);
    };
};

new FormstackForm(jQuery).init();
