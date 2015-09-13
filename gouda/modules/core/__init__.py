import main


META = {
        "commands": {
            # if the key exists in the string, call the value['function'] as a
            # function the parser will only check the first word in the string
            # for a command.
            "modules": {
                "function": main.list_modules,
                "explicit": True
            },
            "commands": {
                "function": main.list_commands,
                "explicit": True
            }
        },
        "context": {
            "function": None,
            "result": main.main
        }
       }
