import asyncio

HOST = "sgfl.xyz"
PORT = 2000
OPERATORS = ["+", "-", "*", "/"]


def encode_msg(message):
    operand_1, operator, operand_2 = message.split(" ")
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)

    if operator not in OPERATORS:
        raise ValueError("Invalid operator")

    if operator == "+":
        operator = "plus"
    elif operator == "-":
        operator = "minus"
    elif operator == "*":
        operator = "multiply"
    elif operator == "/":
        operator = "division"

    return f"{operator}|{operand_1}|{operand_2}\n"


async def client_calc(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    line_count = 0

    while line_count != 3:
        message = await reader.readline()
        print(f"Received: {message.decode()!r}")
        line_count += 1

    message = input("Enter expression: ")
    message = encode_msg(message)
    writer.write(message.encode())
    await writer.drain()
    print(f"Send: {message!r}")

    data = await reader.readline()
    print(f"Received: {data.decode().strip()!r}")

    print("Close the connection")
    writer.close()


if __name__ == '__main__':
    asyncio.run(client_calc(HOST, PORT))
