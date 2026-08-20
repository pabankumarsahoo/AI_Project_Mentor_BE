from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProjectBase(BaseModel):
	project_name: str = Field(min_length=1, max_length=150)
	description: str
	technology_stack: str = Field(min_length=1, max_length=300)


class ProjectCreate(ProjectBase):
	pass


class ProjectUpdate(ProjectBase):
	pass


class ProjectResponse(ProjectBase):
	model_config = ConfigDict(from_attributes=True)

	project_id: int
	created_at: datetime
