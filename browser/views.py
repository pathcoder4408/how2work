from plone import api
from Products.Five.browser import BrowserView

class ListWorkOrdersView(BrowserView):
    def __call__(self):
        # This view could list all work orders, potentially with filtering options
        catalog = api.portal.get_tool(name='portal_catalog')
        results = catalog.searchResults(portal_type='WorkOrder')
        return results
