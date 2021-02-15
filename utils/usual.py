class Utils:
    def __init__(self, token=None):
        self.TOKEN = token


    def write_json(self, file, description, encoding="utf-8"):
        """
        create and/or write in a .json file
        file:          file name
        description:   the value to be saved in the file
        encoding:      encoding wich will be used
        """
        import json

        if not ".json" in file:
            file += ".json"

        with open(file, "w", encoding=encoding) as json_file:
     
           json.dump(description, json_file, indent=4)


    def open_json(self, file, encoding="utf-8"):
        """
        open a .json file
        file:     file name 
        encoding: encoding wich will be used
        return returns a variable with the contents of the file
        """
        import json

        if not ".json" in file:
            file += ".json"

        with open(file, "r", encoding=encoding) as json_file:
            content = json.load(json_file)
        return content


    def ins_prefix(self, prefix, command):
        """
        inserts the prefix in each alias of a command
        prefix:     inserts the prefix in each alias of a command
        command:    command alias list
        return alias list with the prefix
        """
        aliases = []
        for aliase in command:
            aliase = prefix + aliase
            aliases.append(aliase)
        aliases = tuple(aliases)
        return aliases