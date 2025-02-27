from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlmodel import Session, select
from src.db.session import get_session 
from src.db.models import (
    AcademicTotalData,
    AcademicChangeData,
    AcademicDenominator,
    AcademicNumerator,
    AcademicPerformanceLevelorColor,
    CCPerformanceLevelorColorData,
    class_section,
    InterventionCategories,
    InterventionSession,
    PeopleInDB,
    CCReadinessStatusData,
    CCReadinessNumerator,
    CCReadinessDenominatorData,
    CCReadinessChangeData,
    CCReadinessTotalData,
    RoleEnum,
    StudentSectionAssociation,
    SchoolsInDB,
    StudentInDB,
    SectionsInDB,
    TeacherInDB,
    Vendor
)
from src.db.enums import (
    RoleEnum,
    LocationEnum,
    CCIEnum,
    HigherGroupEnum,
    SubgroupEnum,
    GenderSubgroupEnum,
    EconomicStatusEnum,
    ColorEnum
)

app = APIRouter()

