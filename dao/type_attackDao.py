from dao import db_connection


class TypeAttackDao():
    def find_id_by_label(self, attack_name: str):
        "Méthode pour retourner l'id d'un type d'attaque à partir du label"
    # Récupération de la connexion
        with DBConnection().connection as conn :
            with conn.cursor()  as cursor :
                cursor.execute(
                    "SELECT id_attack"
                    "\n \tFROM attack"
                    "\n \t WHERE attack_name=%(attack_name)s"
                        ,{"attack_name": attack_name}
                )
                # On récupère le résultat de la requête
                res = cursor.fetchone()

        return res

