def getMessage(name):
    message = 'Hello, ' + name + '!'
    return message


def printMessage(message):
    print(message)
    return


msg1 = getMessage('Janis')
msg2 = getMessage("Maris")

printMessage("Hello World!")
printMessage(msg1)
printMessage(getMessage("Anna"))
