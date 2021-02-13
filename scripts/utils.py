class Utils:
    def __init__(self, token):
        self.TOKEN = token


    def write_json(self, file, description):
        import json

        if not ".json" in file:
            file += ".json"

        with open(file, "w") as json_file:
     
           json.dump(description, json_file, indent=4)


    def open_json(self, file):
        import json

        if not ".json" in file:
            file += ".json"

        with open(file, "r") as json_file:
            content = json.load(json_file)
        return content


    def ins_prefix(self, prefix, command):
        aliases = []
        for aliase in command:
            aliase = prefix + aliase
            aliases.append(aliase)
        aliases = tuple(aliases)
        return aliases