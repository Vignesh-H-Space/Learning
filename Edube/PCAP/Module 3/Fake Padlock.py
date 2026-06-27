class SecretAgent:
    def __init__(self):
        self.__name = "James Bond"
        self.code = 7
agent = SecretAgent()

agent.__name = "Ethan Hunt"

print(agent._SecretAgent__name)
print(agent.__name)

