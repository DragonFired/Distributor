__author__ = 'arana'

def sudo(command, password=None, prompt="Enter password: "):

    import pexpect

    if not password:
        import getpass
        password = getpass.getpass(prompt)

    command = "/usr/bin/sudo " + command
    child = pexpect.spawn(command)
    result = child.expect(['ssword', pexpect.EOF])
    if result == 0:
        child.sendline(password)
    child.expect(pexpect.EOF)
    child.close()
