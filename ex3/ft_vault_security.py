# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 12:03:15 by stmaire         #+#    #+#               #
#  Updated: 2026/02/20 12:47:16 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", "r") as vault:
        print(vault.read())

    print("\nSECURE PRESERVATION:")
    with open("classified_data.txt", "a") as vault:
        new = "[CLASSIFIED] New security protocols archived"
        print(f"{new}")
        vault.write("\n" + new)
    print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security()
