
from DAO.BaseDAO import BaseDAO
from entity.classify.Distribution import Distribution


class DistributionDao(BaseDAO):
    def __init__(self):
        BaseDAO.__init__(self)

    def get_distribution_by_id(self, distribution_id):
        distribution = None

        try:
            self.open_connection()
            sql = "SELECT * FROM distribution WHERE distributionID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (distribution_id,))
                result = cursor.fetchone()


                if result:  # If a record is found
                    print(*result)
                    distribution = Distribution(**result)

        # except Exception as e:
        #     print(e)

        finally:
            self.close_connection()

        return distribution

    def get_distribution_by_plant_id(self, plant_id):
        distribution = None

        try:
            self.open_connection()

            # First step: Get distributionId from plant_classify table
            sql = "SELECT distributionID FROM plant_classify WHERE plantID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (plant_id,))
                result = cursor.fetchone()

                distribution_id = result[0] if result else 0

            # Second step: Use distributionId to get Distribution information from distribution table
            if distribution_id != 0:
                sql = "SELECT * FROM distribution WHERE distributionID = %s"
                with self.connection.cursor() as cursor:
                    cursor.execute(sql, (distribution_id,))
                    result = cursor.fetchone()

                    if result:
                        distribution = Distribution(*result)

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return distribution

    def add_distribution(self, distribution, add_parent):
        result = False

        try:
            self.open_connection()
            sql = "INSERT INTO distribution (distributionID, parentID, name, level) VALUES (%s, %s, %s, %s)"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (distribution.distributionId, distribution.parentDistributionId if add_parent else None,
                                     distribution.name, distribution.level))

            self.connection.commit()
            result = True

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return result

    def update_distribution(self, distribution):
        result = False

        try:
            self.open_connection()
            sql = "UPDATE distribution SET parentID = %s, name = %s, level = %s WHERE distributionID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (distribution.parentDistributionId, distribution.name, distribution.level,
                                     distribution.distributionId))

            self.connection.commit()
            result = True

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return result

    def delete_distribution(self, distribution_id):
        result = False

        try:
            self.open_connection()
            sql = "DELETE FROM distribution WHERE distributionID = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (distribution_id,))

            self.connection.commit()
            result = True

        except Exception as e:
            print(e)

        finally:
            self.close_connection()

        return result

if __name__ == '__main__':
    dao = DistributionDao()
    distribution = dao.get_distribution_by_id(1)
    print(distribution)
    distribution = dao.get_distribution_by_plant_id(1)
    print(distribution)
    # distribution = Distribution(2, 1, "Distribution 2", 2)
    # print(dao.add_distribution(distribution, True))
    # distribution = Distribution(2, 1, "Distribution 2", 3)
    # print(dao.update_distribution(distribution))
    # print(dao.delete_distribution(2))