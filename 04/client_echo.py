import asyncio

HOST = "sgfl.xyz"
PORT = 2001


def encode_msg(message):
    return f"{message}\n"


async def client_echo(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    init_msg = await reader.readline()
    print(f"Received: {init_msg.decode()!r}")

    message = input("Enter message: ")
    message = encode_msg(message)
    writer.write(message.encode())
    await writer.drain()

    data = await reader.readline()
    print(f"Received: {data.decode().strip()!r}")

    print("Close the connection")
    writer.close


if __name__ == '__main__':
    asyncio.run(client_echo(HOST, PORT))
