from django.db.models import Q
from opencivicdata.core.models import Organization
import us


# Metadata for states that are available in the platform
states = sorted(us.STATES + [us.states.PR], key=lambda s: s.name)


def get_legislature_from_state_abbr(state):
    jurisdiction_id_fragment = '/territory:dc' if state == 'pr' else \
        '/district:dc' if state == 'dc' else \
        '/state:{}'.format(state)
    legislature = Organization.objects.get(
        classification='legislature',
        jurisdiction__id__contains=jurisdiction_id_fragment
    )
    return legislature


def get_chambers_from_legislature(legislature):
    chambers = legislature.children.filter(
        Q(classification='lower') |
        Q(classification='upper')
    )
    if chambers:
        return chambers
    else:
        # Unicameral states use their legislature as their chamber
        return [legislature]


def get_chambers_from_state_abbr(state):
    return get_chambers_from_legislature(
        get_legislature_from_state_abbr(state)
    )


def get_legislative_post(person):
    return person.memberships.get(
        Q(organization__classification='legislature') |
        Q(organization__classification='lower') |
        Q(organization__classification='upper')
    ).post
