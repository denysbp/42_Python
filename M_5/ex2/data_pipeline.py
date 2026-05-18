from abc import ABC, abstractmethod
from typing import List, Any, Protocol


class DataProcessor(ABC):
    def __init__(self):
        self.storage: List = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self, nb: int = 1) -> list[tuple[int, str]]:
        if len(self.storage) == 0:
            raise IndexError("There nothing to output")
        data = self.storage[:nb]
        self.storage = self.storage[nb:]
        return data

    def stats(self) -> tuple[int, int]:
        return (self.rank, len(self.storage))


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

    def ingest(self, data: Any) -> None:
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

    def ingest(self, data: Any) -> None:
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

    def ingest(self, data: Any) -> None:
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV output: ")
        for item_id, value in data:
            print(f"{item_id}, {value}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("[")
        for i, (item_id, value) in enumerate(data):
            coma = "," if i < len(data) - 1 else ""
            print(f'  {{"id": {item_id}, "value": "{value}"}}{coma}')
        print("]")


class DataStream:
    def __init__(self):
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for dados in stream:
            exits: bool = False
            for proc in self._processors:
                if proc.validate(dados):
                    proc.ingest(dados)
                    exits = True
                    break
            if not exits:
                print("Data error, Invalid type of data")

    def print_processors_stats(self) -> None:
        if (len(self._processors) == 0):
            print("None Process was found")
            return
        for proc in self._processors:
            total, remain = proc.stats()
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}, total: {total}", end=" ")
            print(f"Remain: {remain}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        output_data: list[tuple[int, str]] = []
        for processor in self._processors:
            output_data.extend(processor.output(nb))
        plugin.process_output(output_data)


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialized DataStream")
    stream: DataStream = DataStream()
    stream.print_processors_stats()
    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    dados = [
            'Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING', 'log_message': 'Telnet access!'},
                {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42,
            54,
            ['Hi', 'five'],
            ['Ola', 'Mundo'],
            '42 Gang'
    ]
    print(f"Sending the first bacth of Data stream {dados}")
    stream.process_stream(dados)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("Updating stats...")
    numeric = stream._processors[0]
    text = stream._processors[1]
    log = stream._processors[2]
    try:
        print("Consuming Numeric one time")
        numeric.output()
        print("Consuming Text one time")
        text.output()
        print("Consuming Log one time")
        log.output()
    except IndexError as e:
        print(f"{e}")
        return
    stream.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())


if __name__ == '__main__':
    main()
