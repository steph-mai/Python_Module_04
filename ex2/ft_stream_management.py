# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 10:46:18 by stmaire         #+#    #+#               #
#  Updated: 2026/02/20 11:45:17 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status: str = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {archivist_id}: "
          f"{status}", file=sys.stdout)
    print("[ALERT] System diagnostic: "
          "Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
