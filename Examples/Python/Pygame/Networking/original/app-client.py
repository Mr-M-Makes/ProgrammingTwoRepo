import socket
import selectors
import traceback
import pygame

import libclient
from client_network import Network


def main():
    pygame.init()
    pygame.display.set_caption("Client")

    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    network = Network()
    start_position = (100, 100)

    try:
        while True:
            events = network.sel.select(timeout=1)
            for key, mask in events:
                position = key.data
                try:
                    start_position = position.process_events(mask)
                except Exception:
                    print(
                        "main: error: exception for",
                        f"{position.addr}:\n{traceback.format_exc()}",
                    )
                    position.close()
            # Check for a socket being monitored to continue.
            if not network.sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        network.sel.close()


if __name__ == "__main__":
    main()
