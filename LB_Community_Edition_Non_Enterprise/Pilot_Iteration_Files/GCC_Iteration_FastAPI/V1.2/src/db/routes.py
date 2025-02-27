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

router = APIRouter()

# Get teacher info based on intervention session in an Intervention Session
@router.get("/intervention_session/{intervention_session_id}/teachers", response_model=List[TeacherInDB])
async def get_teachers_in_intervention_session(intervention_session_id: int, session: Session = Depends(get_session)):
    stmt = select(TeacherInDB).join(InterventionSession).where(InterventionSession.InterventionSessionID == intervention_session_id)
    teachers = session.exec(stmt).all()
    return teachers


@router.get("/intervention_sessions/teacher_ids", response_model=List[int])
async def get_all_teacher_ids_in_intervention_sessions(session: Session = Depends(get_session)):
    stmt = select(TeacherInDB.TeacherID).join(InterventionSession).distinct()
    teacher_ids = session.exec(stmt).all()
    return teacher_ids

@router.get("/intervention_sessions/teacher_emails", response_model=List[str])
async def get_all_teacher_emails_in_intervention_sessions(session: Session = Depends(get_session)):
    # Assuming TeacherInDB has a field named "Email"
    stmt = select(TeacherInDB.TeacherEmail).join(InterventionSession).distinct()
    teacher_emails = session.exec(stmt).all()
    return teacher_emails

@router.get("/intervention_sessions/session_ids", response_model=List[int])
async def get_all_session_ids(session: Session = Depends(get_session)):
    stmt = select(InterventionSession.InterventionSessionID).distinct()
    session_ids = session.exec(stmt).all()
    return session_ids