# classify_species_dao.py

from DAO.BaseDAO import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import text

from model.classify import ClassifySpecies
from vo.SpecieVO import SpecieVO


class SpeciesDAO(BaseDAO):

    def add_species(self, species_name, species_alias, genus_id, growth_env, province, city, country):
        sql = text("INSERT INTO classify_species "
                   "(species_name, species_alias, genus_id, growth_env, province, city, country) "
                   "VALUES (:species_name, :species_alias, :genus_id, :growth_env, :province, :city, :country)")
        parameters = {
            "species_name": species_name,
            "species_alias": species_alias,
            "genus_id": genus_id,
            "growth_env": growth_env,
            "province": province,
            "city": city,
            "country": country
        }
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {
            "species_name": species_name,
            "species_alias": species_alias,
            "genus_id": genus_id,
            "growth_env": growth_env,
            "province": province,
            "city": city,
            "country": country
        }

    def get_all_species(self):
        sql = text("SELECT * FROM classify_species")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [self._map_result_to_species(row) for row in result]

    def get_species_by_id(self, species_id):
        sql = text("SELECT * FROM classify_species WHERE species_id = :species_id")
        parameters = {"species_id": species_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return self._map_result_to_species(result)

    def update_species(self, species_id, new_species_name, new_species_alias, new_genus_id, new_growth_env,
                       new_province, new_city, new_country):
        sql = text("UPDATE classify_species SET species_name = :new_species_name, "
                   "species_alias = :new_species_alias, genus_id = :new_genus_id, "
                   "growth_env = :new_growth_env, province = :new_province, "
                   "city = :new_city, country = :new_country "
                   "WHERE species_id = :species_id")
        parameters = {
            "new_species_name": new_species_name,
            "new_species_alias": new_species_alias,
            "new_genus_id": new_genus_id,
            "new_growth_env": new_growth_env,
            "new_province": new_province,
            "new_city": new_city,
            "new_country": new_country,
            "species_id": species_id
        }
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {
            "species_id": species_id,
            "species_name": new_species_name,
            "species_alias": new_species_alias,
            "genus_id": new_genus_id,
            "growth_env": new_growth_env,
            "province": new_province,
            "city": new_city,
            "country": new_country
        }

    def delete_species(self, species_id):
        sql = text("DELETE FROM classify_species WHERE species_id = :species_id")
        parameters = {"species_id": species_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return True

    def _map_result_to_species(self, result):
        if result:
            return ClassifySpecies(
                species_id=result[0],
                genus_id=result[1],
                species_name=result[2],
                species_alias=result[3],
                growth_env=result[4],
                province=result[5],
                city=result[6],
                country=result[7]
            )
        return None

    def get_species_by_genus_id(self, genus_id):
        sql = text("SELECT * FROM classify_species WHERE genus_id = :genus_id")
        parameters = {"genus_id": genus_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchall()
        return [self._map_result_to_species(row) for row in result]

    # 通过视图获取所有物种信息
    def get_all_species_view(self):
        sql = text("SELECT * FROM species_view")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [SpecieVO(*row) for row in result]

    def get_species_view_by_growth_env(self, growth_env):
        sql = text("SELECT * FROM species_view WHERE growth_env like :growth_env")
        parameters = {"growth_env": f"%{growth_env}%"}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchall()
        return [SpecieVO(*row) for row in result]

    def get_species_view_by_family(self, family_name):
        sql = text("SELECT * FROM species_view WHERE family_name like :family_name")
        parameters = {"family_name": f"%{family_name}%"}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchall()
        return [SpecieVO(*row) for row in result]

    def get_species_view_by_genus(self, genus_name):
        sql = text("SELECT * FROM species_view WHERE genus_name like :genus_name")
        parameters = {"genus_name": f"%{genus_name}%"}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchall()
        return [SpecieVO(*row) for row in result]

