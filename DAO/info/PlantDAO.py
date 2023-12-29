from DAO.BaseDAO import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import text, func

from model.info import Plant
from model.maintenance import Task
from vo.PlantVo import PlantVO


class PlantDAO(BaseDAO):

    def add_plant(self, species_id, disease_id, plant_desc, plant_value, plant_tip, image_path,
                  image_desc, image_location,  create_by):
        sql = text("""
            INSERT INTO info_plant (species_id, disease_id, plant_desc, plant_value, plant_tip, image_path,
                                    image_desc, image_location,  create_by)
            VALUES (:species_id, :disease_id, :plant_desc, :plant_value, :plant_tip, :image_path,
                    :image_desc, :image_location,  :create_by)
        """)
        parameters = {
            "species_id": species_id,
            "disease_id": disease_id,
            "plant_desc": plant_desc,
            "plant_value": plant_value,
            "plant_tip": plant_tip,
            "image_path": image_path,
            "image_desc": image_desc,
            "image_location": image_location,
            "create_by": create_by
        }

        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()

    def get_all_plants(self):
        sql = text("SELECT * FROM info_plant")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [self._map_result_to_plant(row) for row in result]

    def get_plant_by_id(self, plant_id):
        sql = text("SELECT * FROM info_plant WHERE plant_id = :plant_id")
        parameters = {"plant_id": plant_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return self._map_result_to_plant(result)

    def update_plant(self, plant_id, new_values):
        set_clause = ", ".join([f"{key} = :{key}" for key in new_values.keys()])
        sql = text(f"UPDATE info_plant SET {set_clause} WHERE plant_id = :plant_id")
        parameters = {**new_values, "plant_id": plant_id}

        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()

    def delete_plant(self, plant_id):
        sql = text("DELETE FROM info_plant WHERE plant_id = :plant_id")
        parameters = {"plant_id": plant_id}

        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()

    def _map_result_to_plant(self, result):
        if result:
            return Plant(
                plant_id=result[0],
                species_id=result[1],
                disease_id=result[2],
                plant_desc=result[3],
                plant_value=result[4],
                plant_tip=result[5],
                image_path=result[6],
                image_desc=result[7],
                image_location=result[8],
                create_by=result[9],
                create_time=result[10],
                update_time=result[11]
            )
        return None

    def query_plant_detail_view(self):
        with self.get_session() as session:
            return session.query(PlantVO).all()

    def query_plant_count_by_family(self):
        with self.get_session() as session:
             return session.query(PlantVO.family_name,func.count(PlantVO.plant_id)).group_by(PlantVO.family_name).all()

    def query_plant_by_like_attribute(self, filter_conditions):
        with self.get_session() as session:
            # 构建模糊匹配的过滤条件
            query = session.query(PlantVO)
            for column, value in filter_conditions.items():
                query=query.filter(getattr(PlantVO, column).like(f'%{value}%'))
            return query.all()

    def query_plant_join_maintenance_classfiy(self):
        # 养护信息、分类信息、基本信息联合查询
        with self.get_session() as session:
            return session.query(PlantVO,Task).join(Task, Task.plant_id==PlantVO.plant_id).all()

