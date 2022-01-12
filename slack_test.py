from cts_pro.utils.slack_config import send_slack_message


def test_send_slack_message():
    channel = "# 테스팅"
    msg = "## pytest ##"
    res = send_slack_message(channel=channel, message=msg)
    assert res["message"]["text"] == msg
