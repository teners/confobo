from unittest.mock import Mock

import pytest

from confobo.models import event, user
from confobo.controllers import schedule, subscriptions, voting
from confobo import persistence


@pytest.fixture(scope='module')
def fixture_user():
    return user.User(1)


@pytest.fixture(scope='module')
def fixture_event():
    return event.Event(1)


def test_vote(fixture_user, fixture_event):
    persistence.voting.save_vote = Mock(return_value=True)
    vote_acceptable = 4
    vote_unacceptable = 6

    assert voting.vote(fixture_user, vote_acceptable, fixture_event) is True
    with pytest.raises(voting.BadVoteValueError):
        voting.vote(fixture_user, vote_unacceptable, fixture_event)


def test_remove_subs(fixture_user):
    persistence.subscriptions.remove_all = Mock(return_value=True)

    assert subscriptions.unsubscribe_user(fixture_user) is True


def test_schedule():
    assert schedule.get_schedule('2017-06-01') == 'Schedule for 2017-06-01'
    with pytest.raises(schedule.NoSuchDayError):
        schedule.get_schedule('2020-06-04')
