from model.User import User


class UserDAO:
    def __init__(self, data_source):
        self.data_source = data_source

    def get_user_by_id(self, user_id):
        with self.data_source.get_session() as session:
            return session.query(User).filter(User.user_id == user_id).first()

    def get_user_by_username(self, username):
        with self.data_source.get_session() as session:
            return session.query(User).filter(User.username == username).first()

    def get_all_users(self):
        with self.data_source.get_session() as session:
            return session.query(User).all()

    def create_user(self, username, password, role):
        with self.data_source.get_session() as session:
            new_user = User(username=username, password=password, role=role)
            session.add(new_user)
            session.commit()
            return new_user

    def update_user(self, user_id, new_username):
        with self.data_source.get_session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user:
                user.username = new_username
                session.commit()
                return user
            else:
                raise ValueError(f"User with user_id {user_id} not found.")

    def delete_user(self, user_id):
        with self.data_source.get_session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            else:
                return False
