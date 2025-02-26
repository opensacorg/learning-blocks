from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import String, Enum as SQLMEnum
from sqlalchemy.dialects.postgresql import JSON
from typing import List, Optional, Dict
from enum import Enum
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import declared_attr
from pydantic import BaseModel
from sqlmodel import Field
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Integer, String, Enum as SQLAlchemyEnum, DateTime
from uuid import uuid4
from .enums import RoleEnum, LocationEnum, CCIEnum, HigherGroupEnum, SubgroupEnum, GenderSubgroupEnum, EconomicStatusEnum, ColorEnum, LevelEnum, TrueFalseEnum, InterventionTiersEnum


# Polymorphic model for teachers
def validate_stu_associated(data: Dict[str, Dict[str, Optional[str]]]) -> bool:
    """Validate the structure of StuAssociated data."""
    for _, value in data.items():
        if not isinstance(value, dict):
            return False
        if "Start_Date" not in value or "End_Date" not in value:
            return False
        if not isinstance(value["Start_Date"], (str, type(None))) or not isinstance(value["End_Date"], (str, type(None))):
            return False
    return True


class TimestampMixin:
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(datetime.timezone.utc)})

class BaseWithPolymorphism(SQLModel):
    """
    Base class that handles the polymorphic setup.
    This abstracts the common setup for polymorphic behavior.
    """
    
    @declared_attr
    def __mapper_args__(cls):
        return {
            "polymorphic_on": cls.__table__.c.role,
            "polymorphic_identity": cls.__name__.lower(),
        }

class AcademicData:
    AcademicID: int = Field(default=None, primary_key=True, index=True)
    AcademicYear: str = Field(nullable=False, index=True)
    AcademicSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicGradeLevel: str = Field(nullable=False, index=True)
    AcdemicLocation: LocationEnum = Field(nullable=False, index=True)
    AcademicHighergroup: HigherGroupEnum = Field(nullable=False, index=True)
    AcademicSubgroup: SubgroupEnum = Field(nullable=False, index=True)
    AcademicGenderSubgroup: GenderSubgroupEnum = Field(nullable=False, index=True)
    AcademicEconomicStatus: EconomicStatusEnum = Field(nullable=False, index=True)
    AcademicCurrent: TrueFalseEnum = Field(nullable=False, index=True)
    AcademicAllStu: TrueFalseEnum = Field(nullable=False, index=True)


class AcademicTotalData(AcademicData, SQLModel, table=True):
    __tablename__ = "Academic_total_data"
    AcademicTotalID: int = Field(default=None, primary_key=True, index=True)
    AcademicTotalStu: int = Field(nullable=False)
    AcademicTotalSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicTotalStudents: List["StudentInDB"] = Relationship(back_populates="AcademicTotalData")

class AcademicNumerator(AcademicData, SQLModel, table=True):
    __tablename__ = "academic_numerator"
    AcademicNumeratorID: int = Field(default=None, primary_key=True, index=True)
    AcademicNumeratorTotal: int = Field(unique=True, nullable=False)
    AcademicNumeratorSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicNumeratorStudents: List["StudentInDB"] = Relationship(back_populates="AcademicNumerator")

class AcademicDenominator(AcademicData, SQLModel, table=True):
    __tablename__ = "academic_Denominator"
    AcademicDenominatorID: int = Field(default=None, primary_key=True, index=True)
    AcademicDenominatorTotal: int = Field(unique=True, nullable=False)
    AcademicDenominatorSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicDenominatorStudents: List["StudentInDB"] = Relationship(back_populates="AcademicDenominator")


class AcademicColorData(AcademicData, SQLModel, table=True):
    __tablename__ = "Academic_color_data"
    AcademicColorlID: int = Field(default=None, primary_key=True, index=True)
    AcademicColor: ColorEnum = Field(default="NA" , index = True, nullable=False)
    AcademicColorSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicColorStudents: List["StudentInDB"] = Relationship(back_populates="AcademicColorData")


class AcademicStatusData(AcademicData, SQLModel, table=True):
    __tablename__ = "Academic_status_data"
    AcademicStatusID: int = Field(default=None, primary_key=True, index=True)
    AcademicStatusRate: str = Field(nullable=False)
    AcademicSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicStatusStudents: List["StudentInDB"] = Relationship(back_populates="AcademicStatusData")


class AcademicChangeData(AcademicData, SQLModel, table=True):
    __tablename__ = "Academic_change_data"
    AcademicChangeID: int = Field(default=None, primary_key=True, index=True)
    AcademicChangeRate: str = Field( nullable=False)
    AcademicSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicChangeStudents: List["StudentInDB"] = Relationship(back_populates="AcademicStatusData")


class AcademicPerformanceLevelorColor(AcademicData, SQLModel, table=True):
    __tablename__ = "academic_performance_color_data"
    AcademicPerformanceID: int = Field(default=None, primary_key=True, index=True)
    AcademicPerformColor: ColorEnum = Field(default="NA" , index = True, nullable=False)
    AcademicPerformLevel: LevelEnum = Field(default="no_performance_level", index = True, nullable=False)    
    AcademicSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    AcademicStudents: List["StudentInDB"] = Relationship(back_populates="AcademicPerformanceLevelorColor")
























class CCReadinessData:
  

    CCID: int = Field(default=None, primary_key=True, index=True)
    CCAcademicYear: str = Field(nullable=False, index=True)
    CCReadinessLocation: LocationEnum = Field(nullable=False, index=True) 
    CCReadinessCCI: CCIEnum = Field(  nullable=False, index=True)
    CCeadinessHighergroup: HigherGroupEnum = Field( nullable=False, index=True)
    CCReadinessSubgroup: SubgroupEnum = Field( nullable=False, index=True)
    CCGenderSubgroup: GenderSubgroupEnum = Field( nullable=False, index=True)     
    CCEconomicStatus: EconomicStatusEnum = Field( nullable=False, index=True)
    CCCurrent: TrueFalseEnum = Field(nullable=False, index=True) 
    CCAllStu: TrueFalseEnum = Field(nullable=False, index=True)

class CCStuRelateData(CCReadinessData, SQLModel, table=True):
    __tablename__ = "CC_stu_relate_data"
    CCStuRelateSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    CCStuRelateStudents: List["StudentInDB"] = Relationship(back_populates="CCStuRelateData")


class CCReadinessTotalData(CCReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_total_data"
    CCReadinessTotalID: int = Field(default=None, primary_key=True, index=True, unique=True)
    CCReadinessTotalStu: int = Field(nullable=False)
    CCReadinessTotalSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    CCReadinessTotalStudents: List["StudentInDB"] = Relationship(back_populates="ReadinessTotalData")




class CCReadinessNumerator(CCReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_numerator"
    CCReadinessNumeratorID: int = Field(default=None, primary_key=True, index=True, unique=True)
    CCReadinessNumeratorTotal: int = Field(unique=True, nullable=False)
    CCReadinessSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    CCReadinessStudents: List["StudentInDB"] = Relationship(back_populates="ReadinessNumerator")



class CCPerformanceLevelorColorData(CCReadinessData, SQLModel, table=True):
    __tablename__ = "cc_performance_color_data"
    CCReadinessPerformanceID: int = Field(default=None, primary_key=True, index=True)
    CCReadinesPerformColor: ColorEnum = Field(default="NA" , index = True, nullable=False)
    CCReadinesPerformLevel: LevelEnum = Field(default="no_performance_level", index = True, nullable=False)    
    CCReadinesSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    CCReadinesStudents: List["StudentInDB"] = Relationship(back_populates="ReadinessNumerator")


class CCReadinessStatusData(CCReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_status_data"
    CCReadinesStatusID: int = Field(default=None, primary_key=True, unique= True ,index=True)
    CCReadinesStatusRate: str = Field(nullable=False)
    CCReadinesSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)


class CCReadinessDenominatorData(CCReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_denominator_data"
    CCReadinesDenominatorID: int = Field(default=None, primary_key=True, index=True, unique=True)
    CCReadinesDenominatorRate: str = Field( nullable=False)
    CCReadinesSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)

class CCReadinessChangeData(CCReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_change_data"
    CCReadinesChangeID: int = Field(default=None, primary_key=True, index=True)
    CCReadinesChangeRate: str = Field( nullable=False)
    CCReadinesSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)


class StudentSectionAssociation(TimestampMixin, SQLModel, table=True):
    __tablename__ = "student_section_association"

    school_id: int = Field(foreign_key="schools.SchoolID", primary_key=True)
    student_id: int = Field(foreign_key="students.StudentID", primary_key=True)
    section_id: int = Field(foreign_key="sections.SectionID", primary_key=True)
    teacher_id: int = Field(foreign_key="teachers.TeacherID", primary_key=True)
 
class SchoolsInDB(TimestampMixin, SQLModel, table=True):
    __tablename__ = "schools"

    SchoolID: int = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(unique=True, nullable=False)
    SchoolName: str = Field(nullable=False)
    GradeLevels: Optional[str] = Field(default=None)
    Address: Optional[str] = Field(default=None)
    City: Optional[str] = Field(default=None)
    State: Optional[str] = Field(default=None)
    ZipCode: Optional[str] = Field(default=None)
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
 
    school_readiness_status_data: List["CCReadinessStatusData"] = Relationship(back_populates="school")
    school_performance_color_data: List["CCPerformanceLevelorColorData"] = Relationship(back_populates="school")
    school_readiness_change_data: List["CCReadinessChangeData"] = Relationship(back_populates="school")
    school_readiness_total_data: List["CCReadinessTotalData"] = Relationship(back_populates="school")
    school_readiness_numerator: List["CCReadinessNumerator"] = Relationship(back_populates="school")
    school_readiness_denominator_data: List["CCReadinessDenominatorData"] = Relationship(back_populates="school")
    
    school_academic_status_data: List["AcademicStatusData"] = Relationship(back_populates="school")
    school_academic_change_data: List["AcademicChangeData"] = Relationship(back_populates="school")
    school_academic_total_data: List["AcademicTotalData"] = Relationship(back_populates="school")


    # Add relationship to SectionsInDB
    sections: List["SectionsInDB"] = Relationship(back_populates="school")




class SectionsInDB(TimestampMixin,SQLModel, table=True):
    __tablename__ = "sections"

    SectionID: int = Field(default=None, primary_key=True, index=True)
    CourseName: str = Field(nullable=False)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    students: List["StudentInDB"] = Relationship(back_populates="sections")
 


class PeopleInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "people"

    PeopleID: int = Field(default=None, primary_key=True, index=True)
    FirstName: str = Field(index=True)
    LastName: str = Field(index=True)

    Role: RoleEnum = Field(sa_column=Column(SQLMEnum(RoleEnum), nullable=False))

    SourcedID: str = Field(unique=True, nullable=False, index=True)
    EnabledUser: Optional[str] = Field(default=None, index=True)
    DateLastModified: Optional[str] = Field(default=None, index=True)
    SchoolCode: Optional[str] = Field(default=None, foreign_key="schools.SchoolCode", index=True)
    AnonymizedStudentID: Optional[str] = Field(default=None)
    AnonymizedStudentNumber: Optional[str] = Field(default=None)
    AnonymizedTeacherID: Optional[str] = Field(default=None, unique=True)
 
    # Relationship field
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")

    __mapper_args__ = {
        "polymorphic_identity": "people",
    }

    class Config:
        arbitrary_types_allowed = True


class StudentInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "students"

    # Regular fields
    StudentID: int = Field(default=None, primary_key=True, foreign_key="people.PeopleID", index=True)
    AnonymizedStudentID: str = Field(nullable=False)
    AnonymizedStudentNumber: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    sections: List["SectionsInDB"] = Relationship(back_populates="students")   
    Interventions: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))    
    ReadinessTotalID: Optional[int] = Field(default=None, foreign_key="readiness_total_data.CCReadinessTotalID")
    ReadinessNumeratorID: Optional[int] = Field(default=None, foreign_key="readiness_numerator.CCReadinessNumeratorID", index=True)    
    ReadinessDenominatorID: Optional[int] = Field(default=None, foreign_key="readiness_denominator_data.CCReadinesDenominatorID", index=True)
    # Define the relationships with ReadinessStatusData and PerformanceColorData
    student_readiness_status_data: List["CCReadinessStatusData"] = Relationship(back_populates="students")
    student_performance_color_data: List["CCPerformanceLevelorColorData"] = Relationship(back_populates="students")
    student_readiness_change_data: List["CCReadinessChangeData"] = Relationship(back_populates="students")
    student_readiness_total_data: List["CCReadinessTotalData"] = Relationship(back_populates="students")
    student_readiness_numerator: List["CCReadinessNumerator"] = Relationship(back_populates="students")
    student_readiness_denominator_data: List["CCReadinessDenominatorData"] = Relationship(back_populates="students")
    
    __mapper_args__ = {
        "polymorphic_identity": "student",
    }


class TeacherInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "teachers"

    # Regular fields
    TeacherID: int = Field(default=None, primary_key=True, foreign_key="people.PeopleID", index=True)
    AnonymizedTeacherID: str = Field(nullable=False, unique=True)
    TeacherEmail: Optional[str] = Field(default=None, index=True)
    StuAssociated: Optional[Dict[str, Dict[str, Optional[str]]]] = Field(
        default=None, sa_column=Column(JSON)
    )
    Credentials: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    Subjects: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    GradeLevels: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    sections: List["SectionsInDB"] = Relationship(back_populates="teachers")
 
    # Relationships and additional methods
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
    
    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }
    def set_stu_associated(self, data: Optional[Dict[str, Dict[str, Optional[str]]]]):
        """Sets the StuAssociated field after validation."""
        if data and validate_stu_associated(data):
            self.StuAssociated = data
        else:
            raise ValueError("Invalid structure for StuAssociated")

    def get_stu_associated(self) -> Optional[Dict[str, Dict[str, Optional[str]]]]:
        """Returns the StuAssociated field as a dictionary."""
        return self.StuAssociated
    
class class_section(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "class_section"

    # Regular fields
    ClassSectionID: int = Field(default=None, primary_key=True, index=True)
    SectionName: str = Field(nullable=False)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
 
    __mapper_args__ = {
        "polymorphic_identity": "class_section",
    }
class VendorSchoolLink(SQLModel, table=True):
    vendor_id: int = Field(foreign_key="vendor.VendorID", primary_key=True)
    school_code: str = Field(foreign_key="schools.SchoolCode", primary_key=True)


class Vendor(TimestampMixin, BaseWithPolymorphism, SQLModel, table=True):
    __tablename__ = "vendor"

    # Regular fields
    VendorID: int = Field(default=None, primary_key=True, foreign_key="people.PeopleID", index=True)
    VendorName: str = Field(nullable=False)
    VendorURL: str = Field(nullable=False)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))

    # Many-to-many relationship: Vendor can have multiple Schools
    schools: List["SchoolsInDB"] = Relationship(
        back_populates="vendors", 
        link_model=VendorSchoolLink
    )
    __mapper_args__ = {
        "polymorphic_identity": "vendor",
    }


# Back-populating the relationship on SchoolsInDB
SchoolsInDB.vendors = Relationship(back_populates="schools", link_model=VendorSchoolLink)

class InterventionCategories(TimestampMixin, BaseWithPolymorphism, table=True):
        __tablename__ = "intervention_categories"

        # Regular fields
        InterventionCategoriesID: int = Field(default=None, primary_key=True, index=True)
        CategoryName: str = Field(nullable=False)
        MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))

        # Relationships
        school: Optional["SchoolsInDB"] = Relationship(back_populates="people")

        __mapper_args__ = {
            "polymorphic_identity": "intervention_categories",
        }
class InterventionSession(TimestampMixin, BaseWithPolymorphism, table=True):
        __tablename__ = "interventionSession"

        # Regular fields
        InterventionSessionID: int = Field(default=None, primary_key=True, index=True)
        Intervention_Category: Optional[int] = Field(default=None, foreign_key="intervention_categories.InterventionCategoriesID", primary_key=True, index=True)
        InterventionSessionName: str = Field(nullable=False, index=True)
        Tier: InterventionTiersEnum = Field(nullable=False, index=True)
        StartDate: datetime = Field(nullable=False, index=True)
        EndDate: datetime = Field(nullable=False, index=True)
        StartTime: datetime = Field(nullable=False, index=True)
        EndTime: datetime = Field(nullable=False, index=True)
        MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
        Vendor: Optional[int] = Field(nullable=False, foreign_key="vendor.VendorID", index=True)
        Teacher: Optional[int] = Field(nullable=False, foreign_key="teachers.TeacherID", index=True)   
        Students: Optional[List[int]] = Field(default=None, sa_column=Column(pg.ARRAY(Integer)))
        school: Optional["SchoolsInDB"] = Relationship(back_populates="school")
        created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), index=True)
        updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(datetime.timezone.utc), "index": True})

        __mapper_args__ = {
            "polymorphic_identity": "interventions",
        }

