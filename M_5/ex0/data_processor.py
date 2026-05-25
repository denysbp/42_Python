from abc import ABC, abstractmethod
from typing import List, Any, Tuple


class DataProcessor(ABC):
    def __init__(self):
        self.storage: List = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        if len(self.storage) == 0:
            raise IndexError("There nothing to output")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for num in data:
                if not isinstance(num, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid data for NumericProcessor")
        if isinstance(data, list):
            for num in data:
                self.storage.append((self.rank, str(num)))
                self.rank += 1
        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for letras in data:
                if not isinstance(letras, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid Data for TextProcessor")
        if isinstance(data, list):
            for letras in data:
                self.storage.append((self.rank, letras))
                self.rank += 1
        if isinstance(data, str):
            self.storage.append((self.rank, data))
            self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False

                for key, value in item.items():
                    if not isinstance(key, str) or not isinstance(
                            value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid data for LogPorcessor")
        if isinstance(data, dict):
            for key, value in data.items():
                message: str = f"{key} : {value}"
                self.storage.append((self.rank, str(message)))
                self.rank += 1
        if isinstance(data, list):
            for item in data:
                for key, value in item.items():
                    message: str = f"{key} : {value}"
                    self.storage.append((self.rank, str(message)))
                    self.rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n\n")
    print("Testing Numeric Processor")
    numeric: NumericProcessor = NumericProcessor()
    print(f"Trying to validate input 42: {numeric.validate(42)}")
    print(f"Trying to validate input HELLO: {numeric.validate('HELLO')}")
    print("Trying invalid ingestion of foo:", end=" ")
    try:
        numeric.ingest("foo")
    except TypeError as e:
        print(f"{e}")
    print("Processing data: [5, 4, 3, 2, 1]")
    numeric.ingest([5, 4, 3, 2, 1])
    print("Extrating 3 valuess..")
    for i in range(0, 3):
        output: Tuple[int, str] = numeric.output()
        print(f"Numeric value {output[0]}: {output[1]}")
    print("\n\n")

    print("Testing Text Processor")
    text: TextProcessor = TextProcessor()
    print(f"Trying to validate input 42: {text.validate(42)}")
    print("Processing data ['data', 'resultado', 'hello']")
    try:
        text.ingest(["data", "resultado", "hello"])
    except TypeError as e:
        print(f"{e}")
    print("Extrating 3 valuess..")
    for c in range(0, 3):
        output_text: Tuple[int, str] = text.output()
        print(f"Text value {output_text[0]}: {output_text[1]}")
    print("\n\n")

    print("Testing Log Processor")
    log: LogProcessor = LogProcessor()
    print(f"Trying to validate input Hello: {log.validate('HELLO')}")
    print("Processing data: [{'NOTICE': 'Connection to a server'}, ", end="")
    print("{'ERROR': 'server is DOWN!'}]")
    try:
        log.ingest(
            [{'NOTICE': 'Connection to a server'},
                {'ERROR': 'server is DOWN!'}])
    except TypeError as e:
        print(f"{e}")
    print("Extracting 2 logs")
    for c in range(0, 2):
        log_out: Tuple[int, str] = log.output()
        print(f"Text value {log_out[0]} : {log_out[1]}")


if __name__ == '__main__':
    main()
