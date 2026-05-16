def secure_archive(file_name: str, action: str, string: str = "") -> \
        tuple[bool, str]:
    action = action.lower()
    try:
        with open(f"{file_name}", "+a") as file:
            if action == "read":
                print(file.read())
            elif action == "write":
                file.write(string)
    except ValueError as e:
        print(f"{e}")


def main() -> None:
    secure_archive("ola.txt", "write", "ola meu mundo")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{e}")
