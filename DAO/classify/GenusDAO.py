# classify_genus_dao.py

from DAO.BaseDAO import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import text

from model.classify import ClassifyGenus


class GenusDAO(BaseDAO):

    def add_genus(self, genus_name, family_id):
        sql = text("INSERT INTO classify_genus (genus_name, family_id) VALUES (:genus_name, :family_id)")
        parameters = {"genus_name": genus_name, "family_id": family_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"genus_name": genus_name, "family_id": family_id}

    def get_all_genera(self):
        sql = text("SELECT * FROM classify_genus")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [self._map_result_to_genus(row) for row in result]

    def get_genus_by_id(self, genus_id):
        sql = text("SELECT * FROM classify_genus WHERE genus_id = :genus_id")
        parameters = {"genus_id": genus_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return self._map_result_to_genus(result)

    def update_genus(self, genus_id, new_genus_name):
        sql = text("UPDATE classify_genus SET genus_name = :new_genus_name "
                   "WHERE genus_id = :genus_id")
        parameters = {"new_genus_name": new_genus_name,  "genus_id": genus_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"genus_id": genus_id, "genus_name": new_genus_name}

    def delete_genus(self, genus_id):
        sql = text("DELETE FROM classify_genus WHERE genus_id = :genus_id")
        parameters = {"genus_id": genus_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return True

    def _map_result_to_genus(self, result):
        if result:
            return ClassifyGenus(
                genus_id=result[0],
                genus_name=result[1],
                family_id=result[2]
            )
        return None

    def get_genera_by_family_id(self, family_id):
        sql = text("SELECT * FROM classify_genus WHERE family_id = :family_id")
        parameters = {"family_id": family_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchall()
        return [self._map_result_to_genus(row) for row in result]
