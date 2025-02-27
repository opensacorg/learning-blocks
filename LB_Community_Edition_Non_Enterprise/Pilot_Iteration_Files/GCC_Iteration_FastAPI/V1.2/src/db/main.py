from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import text, SQLModel
from src.config import settings  # Ensure correct settings import
# Access the DATABASE_URL from settings
DATABASE_URL = settings.DATABASE_URL

# Create an asynchronous engine for database connection
async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True
)

# Function to initialize the database connection
async def init_db():
    async with async_engine.begin() as conn:
        from .models import \
                            AcademicTotalData,\
                            AcademicChangeData, \
                            AcademicDenominator, \
                            AcademicNumerator, \
                            AcademicPerformanceLevelorColor, \
                            CCPerformanceLevelorColorData, \
                            class_section,\
                            InterventionCategories,\
                            InterventionSession,\
                            PeopleInDB, \
                            CCReadinessStatusData, \
                            CCReadinessNumerator, \
                            CCReadinessDenominatorData, \
                            CCReadinessChangeData, \
                            CCReadinessTotalData, \
                            RoleEnum ,\
                            StudentSectionAssociation, \
                            SchoolsInDB, \
                            StudentInDB, \
                            SectionsInDB, \
                            TeacherInDB, \
                            Vendor
                     
        await conn.run_sync(SQLModel.metadata.create_all)


