import pymysql
from DAO.BaseDAO import BaseDAO
from entity.classify import PlantClassify

class PlantClassifyDao(BaseDAO):
    def __init__(self):
        BaseDAO.__init__(self)

    def get_plant_classify_by_id(self, plant_id):
        plant_classify = None

        try:
            self.open_connection()
            sql = "SELECT * FROM plant_classify WHERE plantID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (plant_id,))
                result = cursor.fetchone()

                if result:  # If a record is found
                    plant_classify = PlantClassify(*result)

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return plant_classify

    def get_all_plant_classifies(self):
        plant_classify_list = []

        try:
            self.open_connection()
            sql = "SELECT * FROM plant_classify"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()

                for result in results:
                    plant_classify = PlantClassify(*result)
                    plant_classify_list.append(plant_classify)

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return plant_classify_list

    def add_plant_classify(self, plant):
        result = False

        try:
            self.open_connection()
            sql = "INSERT INTO plant_classify (plantID, commonName, growthEnvironment, taxonomyID, distributionID, creator, createTime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (plant.plantId, plant.commonName, plant.growthEnvironment,
                                     plant.taxonomyId, plant.distributionId, plant.creator,
                                     plant.createTime))

            self.connection.commit()
            result = True

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return result

    def update_plant_classify(self, plant):
        result = False

        try:
            self.open_connection()
            sql = "UPDATE plant_classify SET commonName = %s, growthEnvironment = %s, taxonomyID = %s, distributionID = %s, creator = %s, updateTime = %s WHERE plantID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (plant.commonName, plant.growthEnvironment, plant.taxonomyId,
                                     plant.distributionId, plant.creator, plant.updateTime,
                                     plant.plantId))

            self.connection.commit()
            result = True

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return result

    def delete_plant_classify(self, plant_id):
        result = False

        try:
            self.open_connection()
            sql = "DELETE FROM plant_classify WHERE plantID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (plant_id,))

            self.connection.commit()
            result = True

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return result

    def query_by_growth_environment(self, growth_environment):
        plant_classifies = []

        try:
            self.open_connection()
            sql = "SELECT * FROM plant_classify WHERE growthEnvironment LIKE %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, ('%' + growth_environment + '%',))

                results = cursor.fetchall()

                for result in results:
                    plant_classify = PlantClassify(*result)
                    plant_classifies.append(plant_classify)

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return plant_classifies

    def get_plant_ids_by_taxonomy(self, taxonomy_name):
        plant_ids = []

        try:
            self.open_connection()
            sql = "SELECT pc.PlantID " \
                  "FROM Plant_Classify pc " \
                  "JOIN Taxonomy_Classify tc ON pc.TaxonomyID = tc.TaxonomyID " \
                  "JOIN Taxonomy_Classify tc_genus ON tc.ParentID = tc_genus.TaxonomyID " \
                  "JOIN Taxonomy_Classify tc_family ON tc_genus.ParentID = tc_family.TaxonomyID " \
                  "WHERE tc.Name = %s OR tc_genus.Name = %s OR tc_family.Name = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (taxonomy_name, taxonomy_name, taxonomy_name))

                results = cursor.fetchall()

                for result in results:
                    plant_ids.append(result[0])

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return plant_ids
