from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ベースクラスの定義
Base = declarative_base()

# ユーザーモデルの定義
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# SQLiteデータベースに接続
engine = create_engine('sqlite:///example.db')

# テーブルの作成
Base.metadata.create_all(engine)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# データの追加
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

new_user = User(name='Toshiyuki Kimura', age=34)
session.add(new_user)
session.commit()
# データのクエリ
user = session.query(User).filter_by(name='Toshiyuki Kimura').first()
print(user)

# データの更新
user.age = 100
session.commit()

# データの削除
'''
session.delete(user)
session.commit()
'''
# セッションを閉じる
session.close()
