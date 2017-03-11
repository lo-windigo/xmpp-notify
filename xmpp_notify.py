import notify2


# Initialize the notification system
notify2.init("XMPP Notifications")


def raise_notice(msg):
    """
    Take an XMPP message and raise it as a desktop notification
    """
    notification = notify2.Notification.new("Hi")
    notification.show()


def xmpp_watcher():
    pass

