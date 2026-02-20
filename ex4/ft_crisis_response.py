# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 13:42:21 by stmaire         #+#    #+#               #
#  Updated: 2026/02/20 15:43:30 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def archive_handle(file: str) -> None:
    try:
        with open(file) as f:
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
            print("SUCCESS: Archive recovered - ''", end="")
            print(f.read() + "''")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access "
              f"to '{file}'...", file=sys.stderr)
        print("RESPONSE: Archive not found "
              "in storage matrix", file=sys.stderr)
        print("STATUS: Crisis handled, system stable\n", file=sys.stderr)

    except PermissionError:
        print(f"CRISIS ALERT: Attempting "
              f"access to '{file}'...", file=sys.stderr)
        print("RESPONSE: Security protocols deny access", file=sys.stderr)
        print("STATUS: Crisis handled, security maintained\n", file=sys.stderr)

    except Exception as e:
        print(f"CRISIS ALERT: Unexpected error - {e}", file=sys.stderr)
        print("RESPONSE: Emergency protocol started", file=sys.stderr)
        print("STATUS: System under investigation\n", file=sys.stderr)


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    archive_handle("lost_archive.txt")
    archive_handle("classified_vault.txt")
    archive_handle("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
