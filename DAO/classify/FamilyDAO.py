# classify_family_dao.py

from DAO.BaseDAO import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import text

from model.classify import ClassifyFamily


class FamilyDAO(BaseDAO):

    def add_family(self, family_name):
        sql = text("INSERT INTO classify_family (family_name) VALUES (:family_name)")
        parameters = {"family_name": family_name}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"family_name": family_name}

    def get_all_families(self):
        sql = text("SELECT * FROM classify_family")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [self._map_result_to_family(row) for row in result]

    def get_family_by_id(self, family_id):
        sql = text("SELECT * FROM classify_family WHERE family_id = :family_id")
        parameters = {"family_id": family_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return self._map_result_to_family(result)

    def update_family(self, family_id, new_family_name):
        sql = text("UPDATE classify_family SET family_name = :new_family_name WHERE family_id = :family_id")
        parameters = {"new_family_name": new_family_name, "family_id": family_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"family_id": family_id, "family_name": new_family_name}

    def delete_family(self, family_id):
        sql = text("DELETE FROM classify_family WHERE family_id = :family_id")
        parameters = {"family_id": family_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return True

    def _map_result_to_family(self, result):
        if result:
            return ClassifyFamily(
                family_id=result[0],
                family_name=result[1]
            )
        return None
