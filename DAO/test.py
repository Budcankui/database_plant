from peewee import Model, CharField, Proxy
from playhouse.pool import PooledDatabase
import pyodbc

db_params = {
    'host': 'rm-bp1a117z150cwqt0lqo.sqlserver.rds.aliyuncs.com',
    'user': 'pubuser',
    'password': '123456@abc',
    'database': 'plant',
    'port': 3433,  # 注意：将端口改为整数类型
}

# 创建 PooledDatabase 连接池的代理
db_proxy = Proxy()

# 创建 PooledDatabase 连接池
pooled_db = PooledDatabase(
    'pyodbc',
    max_connections=10,
    stale_timeout=300,
    database_params={
        'driver': 'ODBC Driver 17 for SQL Server',
        'host': db_params['host'],
        'user': db_params['user'],
        'password': db_params['password'],
        'database': db_params['database'],
        'port': db_params['port'],
        'autocommit': True,
    }
)

# 将代理与连接池关联
db_proxy.initialize(pooled_db)

# 定义 Peewee 模型
class User(Model):
    username = CharField()

    class Meta:
        database = db_proxy

# 创建表
db_proxy.connect()
db_proxy.create_tables([User])
db_proxy.close()

# 使用连接池进行查询
with db_proxy.connection():
    user = User.create(username='example_user')
    retrieved_user = User.get(User.username == 'example_user')
    print(retrieved_user.username)
