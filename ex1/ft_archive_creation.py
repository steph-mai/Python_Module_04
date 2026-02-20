# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 10:05:16 by stmaire         #+#    #+#               #
#  Updated: 2026/02/20 10:56:15 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def data_creation() -> None:
    file_name = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print(f"Initializing new storage unit: {file_name}")
    entry1 = "[ENTRY 001] New quantum algorithm discovered"
    entry2 = "[ENTRY 002] Efficiency increased by 347%"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee"
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data..")

    print(f"{entry1}")
    print(f"{entry2}")
    print(f"{entry3}")

    vault = open(file_name, "w")
    vault.write(entry1 + "\n")
    vault.write(entry2 + "\n")
    vault.write(entry3 + "\n")
    vault.close()

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    data_creation()
