class Functions:

    @staticmethod
    def value_or_zero(value: int):
        return value if value >= 0 else 0

    @staticmethod
    def get_average_value(ls: list[int]) -> int:
        return sum(ls) // len(ls)

    @staticmethod
    def get_list_dicts_data(data: list[dict],
                 key: str, sort_it=False) -> list[int | str]:
        ls = [line[key] for line in data]
        return sorted(ls) if sort_it else ls

    @staticmethod
    def no_duplicates(ls: list) -> list:
        return list(dict.fromkeys(ls))

