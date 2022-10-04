import socket
import _thread
import sys

def main():    
    server = "10.56.64.165"
    port = 5555

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((server, port))
    except socket.error as e:
        print(str(e))

    sock.listen(2)
    print("Waiting for a connection...server started.")

    pos = [(0, 0), (200, 200)]
    current_player = 0
    while True:
        connection, address = sock.accept()
        print(f"Connected to: {address}")

        _thread.start_new_thread(threaded_client, (connection, pos, current_player))
        current_player += 1


def threaded_client(connection, positions, player):
    connection.send(str.encode(make_pos(positions[player])))
    reply = ""

    while True:
        try:
            data = read_pos(connection.recv(2048).decode())
            positions[player] = data

            if not data:
                print("Disconnected...")
                break
            else:
                if player == 1:
                    reply = positions[0]
                else:
                    reply = positions[1]
                print(f"Received: {data}")
                print(f"Sending: {reply}")

            connection.sendall(str.encode(make_pos(reply)))
        except:
            print("Something bad happened...")
            break

    print("Lost connection...")
    connection.close()


def read_pos(data):
    data = data.split(",")
    return int(data[0]), int(data[1])


def make_pos(position):
    return f"{position[0]},{position[1]}"


if __name__ == "__main__":
    main()