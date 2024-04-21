from plone.supermodel import model
from z3c.form import form, button
from plone.z3cform.layout import wrap_form
from zope.interface import Interface

class IWorkDetail(model.Schema):
    # Fields defined as per the XML schema above

class WorkDetailForm(form.SchemaForm):
    schema = IWorkDetail
    label = "Enter Work Details"
    description = "Fill in the details of the work performed."

    @button.buttonAndHandler(u'Save')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # Save logic for the form data

WorkDetailView = wrap_form(WorkDetailForm)
