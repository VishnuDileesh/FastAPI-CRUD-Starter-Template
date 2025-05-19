from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def get_by_title(self, db: Session, *, title: str) -> Optional[Task]:
        stmt = select(Task).where(Task.title == title)
        return db.execute(stmt).scalar_one_or_none()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Task]:
        stmt = select(Task).offset(skip).limit(limit)
        return list(db.execute(stmt).scalars().all())


task = CRUDTask(Task)
