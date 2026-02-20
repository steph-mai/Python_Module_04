# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 08:51:21 by stmaire         #+#    #+#               #
#  Updated: 2026/02/20 10:01:56 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
def data_recovery() -> None:
    file_name = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        vault = open(file_name, "r")
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(vault.read())
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    data_recovery()
