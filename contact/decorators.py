from django.utils.html import escape

def add_control_label_tag(f):
    """ Adds the Bootstrap 'control-label' CSS class to field labels. """
    def control_label_tag(self, contents=None, attrs=None):
        attrs_new = {'class': 'control-label'}
        if attrs is not None:
            attrs_new.update(attrs)
        return f(self, contents, attrs_new)
    return control_label_tag

def decorate_bound_field():
    from django.forms.forms import BoundField
    BoundField.label_tag = add_control_label_tag(BoundField.label_tag)

##
# Courtesy of http://www.thebitguru.com/blog/view/299-Adding%20%2a%20to%20required%20fields
#
# from django.utils.html import escape
# 
# def add_required_label_tag(original_function):
#   """Adds the 'required' CSS class and an asterisks to required field labels."""
#   def required_label_tag(self, contents=None, attrs=None):
#     contents = contents or escape(self.label)
#     if self.field.required:
#       if not self.label.endswith(" *"):
#         self.label += " *"
#         contents += " *"
#       attrs = {'class': 'required'}
#     return original_function(self, contents, attrs)
#   return required_label_tag
# 
# def decorate_bound_field():
#   from django.forms.forms import BoundField
#   BoundField.label_tag = add_required_label_tag(BoundField.label_tag)
#
# from project.forms import decorate_bound_field
# decorate_bound_field()

