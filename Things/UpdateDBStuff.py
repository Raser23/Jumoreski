def WordChecker(words):
    def oe(likesCount,text):
        for word in words:
            if not str(word) in text:
                return False
        return True
    return oe


def EmptyChecker():
    def oe(likesCount,text):
        return True
    return oe