from datetime import datetime

import pytest

from . import models


@pytest.mark.django_db
def test_create_board():
    cre = models.Board.objects.create(
        title="test",
        sub_title="sub_test",
        read_cnt=1,
        writer="user",
        created_at=datetime.now(),
        context="",
    )
    assert cre


@pytest.mark.django_db
def test_search_board():
    bo = models.Board.objects.all()
    res = True if bo.count() == 0 else False
    assert res == True
