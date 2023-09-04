class TextBuffer:
    def __init__(self) -> None:
        self.text = ""
        self.combine_text = ""
        self.count = 0

    def set_text(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text

    def get_combine_fill(self) -> str:
        return self.combine_text

    def clear_combine_fill(self) -> None:
        self.combine_text = ""
        self.count = 0

    def update_combine_fill(self, text: str):
        self.combine_text += text + "\n"
        self.count += 1
