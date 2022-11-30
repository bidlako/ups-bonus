import asyncio

HOST = "sgfl.xyz"
PORT = 2002


def encode_msg(message):
    return f"{message}\n"


async def client_reverse(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    init_msg = await reader.readline()
    print(f"Received: {init_msg.decode()!r}")

    cookie = await reader.readline()
    print(f"Received: {cookie.decode()!r}")
    cookie = cookie.decode().strip()[::-1]
    msg = encode_msg(cookie)

    writer.write(msg.encode())
    await writer.drain()

    data = await reader.readline()
    print(f"Received: {data.decode().strip()!r}")

    writer.close()


if __name__ == '__main__':
    asyncio.run(client_reverse(HOST, PORT))
