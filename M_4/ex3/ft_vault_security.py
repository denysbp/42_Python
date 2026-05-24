def secure_archive(file_name: str, action: str, string: str = "") -> \
        tuple[bool, str]:
    action = action.lower()
    try:
        if action == "read":
            with open(f"{file_name}", "r") as file:
                data = file.read()
                return (True, data)
        elif action == "write":
            if not string:
                return (False, "[STDERR]: Invalid content")
            with open(f"{file_name}", "w") as file:
                file.write(string)
                return (True, "Write successfully")
        else:
            return (False, "[STDERR]: Invalid action")
    except FileNotFoundError:
        return (False, f"[STDERR]: File {file_name} not found ")
    except PermissionError as e:
        return (False, f"[STDERR]: Permission: {e}")
    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print("==== Teste 1 ====")
    data = secure_archive("ola.txt", "wreite", "ola meu mundo$")
    print(data)

    print("\n--------")
    print("==== Teste 2 ====")
    data = secure_archive("ola.txt", "write", "something to passs")
    print(data)

    print("\n--------")
    print("==== Teste 3 ====")
    data = secure_archive("ex0/ft_ancient_text.py", "read")
    print(data)

    print("\n--------")
    print("==== Teste 3 ====")
    data = secure_archive("ex0/ft_ancient_text.py", "write", None)
    print(data)


if __name__ == '__main__':
    main()
