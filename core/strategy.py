class Strategy:

    def place_token(self, token, board):
        raise NotImplementedError("Implement this method in your subclass.")

    def __str__(self):
        return self.__class__.__name__
