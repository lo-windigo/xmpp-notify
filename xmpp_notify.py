import aioxmpp, asyncio, notify2

def raise_notification(msg):
    """
    Take an XMPP message and raise it as a desktop notification
    """

    # We can't raise a notification without a message, can we?
    if not msg.body:
       return 

    notify2.init("XMPP Notifications")

    notification = notify2.Notification(
        str(msg.from_),
        str(msg.body[None])
    )

    notification.show()


async def watch_for_messages(xmpp_id, password):
    """
    Monitor an XMPP account, and raise any messages received as desktop
    notifications
    """
    client = aioxmpp.PresenceManagedClient(
        xmpp_id,
        aioxmpp.make_security_layer(password)
    )

    # Whenever we receive a message, raise it as a notification
    client.stream.register_message_callback(
	aioxmpp.MessageType.CHAT,
	None,
	raise_notification,
    )

    async with client.connected():
        while True:
            await asyncio.sleep(5)


if __name__ == "__main__":

    from os import path
    import configparser

    # Pull the accounts from the configuration files
    config_path = 'xmpp-notices/accounts.ini'
    system_config_path = path.join('/etc', config_path)
    user_config_path = path.join(path.expanduser('~/.config'), config_path)
    config = configparser.ConfigParser()

    if path.exists(user_config_path):
        config.read(user_config_path)
    elif path.exists(system_config_path):
        config.read(system_config_path)
    else:
        raise Exception('No configuration file found!')

    #TODO: handle multiple accounts
    account = config.sections()[0]

    xmpp_user = aioxmpp.JID.fromstr(config[account].get('XMPPUser'))
    xmpp_password = config[account].get('Password')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(watch_for_messages(xmpp_user, xmpp_password))
    loop.close()

