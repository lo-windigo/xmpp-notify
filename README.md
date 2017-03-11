Unnamed XMPP Notification Daemon
===

This is a daemon that checks an XMPP account, and displays any messages received
as system notifications.

Installation
===

This application is designed to run in a virtualenv; here are some quick
instructions for getting it set up, and getting the repository:

    virtualenv -p python3 ./xmpp-notices
	cd xmpp-notices
    git clone <this repository> src
	bin/activate

We need to install some system requirements as well. You can run the shell
script included, or just read what it's installing and do it manually.

	sudo src/system-requirements.sh
	pip install -r src/requirements.txt

We need to copy the configuration file and set up accounts to watch as well.

	mkdir ~/.config/xmpp-notices/
	cp src/accounts.ini-example ~/.config/xmpp-notices/accounts.ini
	editor ~/.config/xmpp-notices/accounts.ini

Once that's all set, you should be able to start the utility!

    python src/xmpp_notices.py

