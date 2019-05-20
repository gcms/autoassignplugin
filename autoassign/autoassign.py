"""
Autoassign:
mark the ticket as assigned when created with an owner
"""


from trac.core import *
from trac.ticket.api import ITicketManipulator

class Autoassign(Component):
    implements(ITicketManipulator)

    ### methods for ITicketManipulator
    def prepare_ticket(self, req, ticket, fields, actions):
        pass

    def validate_ticket(self, req, ticket):
        if ticket['owner'] and ticket['status'] == 'new':
            ticket['status'] = 'assigned'

        return []
