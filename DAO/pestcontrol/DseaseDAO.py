from sqlalchemy import text

from DAO.BaseDAO import BaseDAO
from model.pest_control import Disease


class DiseaseDAO(BaseDAO):

    def add_disease(self, disease_name, method, drug, dosage, time):
        sql = text("INSERT INTO pest_control_disease (disease_name, method, drug, dosage, time) "
                   "VALUES (:disease_name, :method, :drug, :dosage, :time)")
        parameters = {"disease_name": disease_name, "method": method, "drug": drug, "dosage": dosage, "time": time}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"disease_name": disease_name, "method": method, "drug": drug, "dosage": dosage, "time": time}

    def get_all_diseases(self):
        sql = text("SELECT * FROM pest_control_disease")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [self._map_result_to_disease(row) for row in result]

    def get_disease_by_id(self, disease_id):
        sql = text("SELECT * FROM pest_control_disease WHERE disease_id = :disease_id")
        parameters = {"disease_id": disease_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return self._map_result_to_disease(result)

    def update_disease(self, disease_id, disease_name, method, drug, dosage,
                       time):
        sql = text("UPDATE pest_control_disease SET "
                   "disease_name = :disease_name, method = :method, "
                   "drug = :drug, dosage = :dosage, time = :time "
                   "WHERE disease_id = :disease_id")
        parameters = {
            "disease_id": disease_id,
            "disease_name": disease_name,
            "method": method,
            "drug": drug,
            "dosage": dosage,
            "time": time
        }
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"disease_id": disease_id, "disease_name": disease_name,
                "method": method, "drug": drug, "dosage": dosage, "time": time}

    def delete_disease(self, disease_id):
        sql = text("DELETE FROM pest_control_disease WHERE disease_id = :disease_id")
        parameters = {"disease_id": disease_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return True

    def _map_result_to_disease(self, result):
        if result:
            return Disease(
                disease_id=result[0],
                disease_name=result[1],
                method=result[2],
                drug=result[3],
                dosage=result[4],
                time=result[5]
            )
        return None
