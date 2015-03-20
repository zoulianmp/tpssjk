# coding: utf-8
from sqlalchemy import BINARY, BigInteger, Column, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Unicode, UnicodeText, VARBINARY, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql.base import MONEY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ADT08(Base):
    __tablename__ = 'ADT08'

    ADT08Ser = Column(BigInteger, primary_key=True)
    InternalId = Column(Unicode(32), nullable=False, unique=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    PatientId = Column(Unicode(25), nullable=False, unique=True)
    PatientId2 = Column(Unicode(25))
    SSN = Column(Unicode(64))
    FirstName = Column(Unicode(64))
    MiddleName = Column(Unicode(64))
    LastName = Column(Unicode(64), nullable=False)
    Honorific = Column(Unicode(16))
    DateOfBirth = Column(DateTime)
    Sex = Column(Unicode(16))
    Country = Column(Unicode(64))
    StateOrProvince = Column(Unicode(64))
    CityOrTownship = Column(Unicode(64))
    AddressLine1 = Column(Unicode(64))
    AddressLine2 = Column(Unicode(64))
    PostalCode = Column(Unicode(16))
    WorkPhone = Column(Unicode(64))
    HomePhone = Column(Unicode(64))
    InSyncFlag = Column(Integer)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')


class AccessStatu(Base):
    __tablename__ = 'AccessStatus'

    AccessStatusSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    TimeStamp = Column(DateTime)
    TypeOfTimeStamp = Column(Unicode(32), nullable=False)
    UserName = Column(Unicode(32))
    TaskName = Column(Unicode(32))
    WorkStationName = Column(Unicode(64))
    ExtModified = Column(Integer)
    ExtTaskName = Column(Unicode(32))
    ExtUserName = Column(Unicode(32))
    ExtWorkstation = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))

    Patient = relationship(u'Patient')


class AccountBillingCode(Base):
    __tablename__ = 'AccountBillingCode'

    AccountBillingCodeSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    AccountBillingCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AccountBillingCodeId = Column(Unicode(20), nullable=False)
    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), index=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    BillAccountName = Column(Unicode(254))
    EffDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    ExpiryDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    ObjectStatus = Column(Unicode(16))
    ValidEntryInd = Column(Unicode(1))
    AttendingOncologistSer = Column(ForeignKey(u'Doctor.ResourceSer'), index=True)
    ReferringDoctorSer = Column(ForeignKey(u'Doctor.ResourceSer'), index=True)
    InPatientFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    IntfExternalField1 = Column(Unicode(64))
    IntfExternalField2 = Column(Unicode(64))
    IntfExternalField3 = Column(Unicode(64))
    IntfExternalField4 = Column(Unicode(64))
    IntfExternalField5 = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Doctor = relationship(u'Doctor', primaryjoin='AccountBillingCode.AttendingOncologistSer == Doctor.ResourceSer')
    Department = relationship(u'Department')
    Hospital = relationship(u'Hospital')
    Patient = relationship(u'Patient')
    Doctor1 = relationship(u'Doctor', primaryjoin='AccountBillingCode.ReferringDoctorSer == Doctor.ResourceSer')


class AccountBillingCodeMH(Base):
    __tablename__ = 'AccountBillingCodeMH'

    AccountBillingCodeSer = Column(ForeignKey(u'AccountBillingCode.AccountBillingCodeSer'), primary_key=True, nullable=False)
    AccountBillingCodeRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(BigInteger, nullable=False, index=True)
    AccountBillingCodeId = Column(Unicode(20), nullable=False)
    HospitalSer = Column(BigInteger)
    DepartmentSer = Column(BigInteger)
    BillAccountName = Column(Unicode(254))
    EffDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    ExpiryDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    ObjectStatus = Column(Unicode(16))
    ValidEntryInd = Column(Unicode(1))
    AttendingOncologistSer = Column(BigInteger)
    ReferringDoctorSer = Column(BigInteger)
    InPatientFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    IntfExternalField1 = Column(Unicode(64))
    IntfExternalField2 = Column(Unicode(64))
    IntfExternalField3 = Column(Unicode(64))
    IntfExternalField4 = Column(Unicode(64))
    IntfExternalField5 = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AccountBillingCode = relationship(u'AccountBillingCode')


class ActCaptDiagnosi(Base):
    __tablename__ = 'ActCaptDiagnosis'

    ActCaptDiagnosisSer = Column(BigInteger, primary_key=True)
    ActCaptDiagnosisRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCaptureSer = Column(ForeignKey(u'ActivityCapture.ActivityCaptureSer'), nullable=False, index=True)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    DiagnosisSer = Column(BigInteger, nullable=False)
    LastKnownDiagnosisId = Column(Unicode(16), nullable=False)
    LastKnownDiagnosisTableName = Column(Unicode(64))
    LastKnownDiagnosisCode = Column(Unicode(16))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityCapture = relationship(u'ActivityCapture')


class ActCaptDiagnosisMH(Base):
    __tablename__ = 'ActCaptDiagnosisMH'

    ActCaptDiagnosisSer = Column(ForeignKey(u'ActCaptDiagnosis.ActCaptDiagnosisSer'), primary_key=True, nullable=False)
    ActCaptDiagnosisRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCaptureSer = Column(BigInteger, nullable=False, index=True)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    DiagnosisSer = Column(BigInteger, nullable=False)
    LastKnownDiagnosisId = Column(Unicode(16), nullable=False)
    LastKnownDiagnosisTableName = Column(Unicode(64))
    LastKnownDiagnosisCode = Column(Unicode(16))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActCaptDiagnosi = relationship(u'ActCaptDiagnosi')


class ActCaptTreatment(Base):
    __tablename__ = 'ActCaptTreatment'

    ActCaptTreatmentSer = Column(BigInteger, primary_key=True)
    ActivityCaptureSer = Column(ForeignKey(u'ActivityCapture.ActivityCaptureSer'), nullable=False, index=True)
    RadiationHstrySer = Column(ForeignKey(u'RadiationHstry.RadiationHstrySer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityCapture = relationship(u'ActivityCapture')
    RadiationHstry = relationship(u'RadiationHstry')


class ActInstChecklistItem(Base):
    __tablename__ = 'ActInstChecklistItem'
    __table_args__ = (
        Index('XAK1ActInstChecklistItem', 'ActivityInstanceSer', 'ChecklistItemSer', unique=True),
    )

    ActInstChecklistItemSer = Column(BigInteger, primary_key=True)
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False)
    ChecklistItemSer = Column(ForeignKey(u'ChecklistItem.ChecklistItemSer'), nullable=False, index=True)
    ChecklistItemResponse = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstance = relationship(u'ActivityInstance')
    ChecklistItem = relationship(u'ChecklistItem')


class ActInstProcCode(Base):
    __tablename__ = 'ActInstProcCode'
    __table_args__ = (
        Index('XIE6ActInstProcCode', 'HstryDateTime', 'ProcedureCodeSer'),
    )

    ActInstProcCodeSer = Column(BigInteger, primary_key=True)
    ActInstProcCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ProcedureCodeSer = Column(ForeignKey(u'ProcedureCode.ProcedureCodeSer'), nullable=False)
    ProcedureCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AccountBillingCodeSer = Column(ForeignKey(u'AccountBillingCode.AccountBillingCodeSer'), index=True)
    AccountBillingCodeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ModifierSer = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMdRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier = Column(Unicode(64))
    Modifier2Ser = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMd2RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier2 = Column(Unicode(64))
    Modifier3Ser = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMd3RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier3 = Column(Unicode(64))
    Modifier4Ser = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMd4RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier4 = Column(Unicode(64))
    Modifier5Ser = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMd5RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier5 = Column(Unicode(64))
    Modifier6Ser = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMd6RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier6 = Column(Unicode(64))
    Modifier7Ser = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMd7RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier7 = Column(Unicode(64))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ChargeWaivedBy = Column(Unicode(32))
    FromDateOfService = Column(DateTime)
    ToDateOfService = Column(DateTime)
    CompletedBy = Column(Unicode(32))
    CompletedDateTime = Column(DateTime, index=True)
    MrkdCmpltdBy = Column(Unicode(32))
    MrkdCmpltdDateTime = Column(DateTime, index=True)
    ReviewedBy = Column(Unicode(32))
    ExportedBy = Column(Unicode(32))
    ExportedDateTime = Column(DateTime, index=True)
    ReviewResetBy = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    WeeklyChrgFlag = Column(Integer)
    Comment = Column(Unicode(254))

    AccountBillingCode = relationship(u'AccountBillingCode')
    ActivityInstance = relationship(u'ActivityInstance')
    Department = relationship(u'Department')
    ActivityCodeMd = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.Modifier2Ser == ActivityCodeMd.ModifierSer')
    ActivityCodeMd1 = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.Modifier3Ser == ActivityCodeMd.ModifierSer')
    ActivityCodeMd2 = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.Modifier4Ser == ActivityCodeMd.ModifierSer')
    ActivityCodeMd3 = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.Modifier5Ser == ActivityCodeMd.ModifierSer')
    ActivityCodeMd4 = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.Modifier6Ser == ActivityCodeMd.ModifierSer')
    ActivityCodeMd5 = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.Modifier7Ser == ActivityCodeMd.ModifierSer')
    ActivityCodeMd6 = relationship(u'ActivityCodeMd', primaryjoin='ActInstProcCode.ModifierSer == ActivityCodeMd.ModifierSer')
    ProcedureCode = relationship(u'ProcedureCode')


class ActInstProcCodeMH(Base):
    __tablename__ = 'ActInstProcCodeMH'

    ActInstProcCodeSer = Column(ForeignKey(u'ActInstProcCode.ActInstProcCodeSer'), primary_key=True, nullable=False)
    ActInstProcCodeRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(BigInteger, nullable=False)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ProcedureCodeSer = Column(BigInteger, nullable=False)
    ProcedureCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AccountBillingCodeSer = Column(BigInteger)
    AccountBillingCodeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ModifierSer = Column(BigInteger)
    ActivityCodeMdRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier = Column(Unicode(64))
    Modifier2Ser = Column(BigInteger)
    ActivityCodeMd2RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier2 = Column(Unicode(64))
    Modifier3Ser = Column(BigInteger)
    ActivityCodeMd3RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier3 = Column(Unicode(64))
    Modifier4Ser = Column(BigInteger)
    ActivityCodeMd4RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier4 = Column(Unicode(64))
    Modifier5Ser = Column(BigInteger)
    ActivityCodeMd5RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier5 = Column(Unicode(64))
    Modifier6Ser = Column(BigInteger)
    ActivityCodeMd6RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier6 = Column(Unicode(64))
    Modifier7Ser = Column(BigInteger)
    ActivityCodeMd7RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier7 = Column(Unicode(64))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ChargeWaivedBy = Column(Unicode(32))
    FromDateOfService = Column(DateTime)
    ToDateOfService = Column(DateTime)
    CompletedBy = Column(Unicode(32))
    CompletedDateTime = Column(DateTime)
    MrkdCmpltdBy = Column(Unicode(32))
    MrkdCmpltdDateTime = Column(DateTime)
    ReviewedBy = Column(Unicode(32))
    ExportedBy = Column(Unicode(32))
    ExportedDateTime = Column(DateTime)
    ReviewResetBy = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DepartmentSer = Column(BigInteger)
    WeeklyChrgFlag = Column(Integer)
    Comment = Column(Unicode(254))

    ActInstProcCode = relationship(u'ActInstProcCode')


class Activity(Base):
    __tablename__ = 'Activity'
    __table_args__ = (
        Index('XIE1Activity', 'ActivityCategorySer', 'ActivityCode'),
    )

    ActivitySer = Column(BigInteger, primary_key=True)
    ActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCategorySer = Column(ForeignKey(u'ActivityCategory.ActivityCategorySer'), nullable=False)
    ActivityCode = Column(Unicode(64), nullable=False)
    ActivityType = Column(Unicode(32), nullable=False)
    DerivedFromActivitySer = Column(BigInteger)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ResourceGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), index=True)
    DefaultDuration = Column(Integer)
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NotificationPriorTime = Column(Integer)
    AssignableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Description = Column(Unicode(254))
    ForeGroundColor = Column(BINARY(4))
    Icon = Column(LargeBinary)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), index=True)
    NotificationPriorTimeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    EscalationGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), index=True)
    TreatmentCycleSer = Column(ForeignKey(u'TreatmentCycle.CycleSer'), index=True)
    ReviewFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    UpdCPResourceGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), index=True)
    UpdCPEscalationGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), index=True)
    AutoGenerateFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NoAutoPostFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    ActivityCategory = relationship(u'ActivityCategory')
    DICOMCodeValue = relationship(u'DICOMCodeValue')
    ResourceGroup = relationship(u'ResourceGroup', primaryjoin='Activity.EscalationGroupSer == ResourceGroup.ResourceGroupSer')
    ResourceGroup1 = relationship(u'ResourceGroup', primaryjoin='Activity.ResourceGroupSer == ResourceGroup.ResourceGroupSer')
    TreatmentCycle = relationship(u'TreatmentCycle')
    ResourceGroup2 = relationship(u'ResourceGroup', primaryjoin='Activity.UpdCPEscalationGroupSer == ResourceGroup.ResourceGroupSer')
    ResourceGroup3 = relationship(u'ResourceGroup', primaryjoin='Activity.UpdCPResourceGroupSer == ResourceGroup.ResourceGroupSer')


class ActivityAssociation(Base):
    __tablename__ = 'ActivityAssociation'

    ActivityAssociationSer = Column(BigInteger, primary_key=True)
    NonSchedulableActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), nullable=False, index=True)
    SchedulableActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), nullable=False, index=True)
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DefaultPriorPostDueTime = Column(Integer)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Activity = relationship(u'Activity', primaryjoin='ActivityAssociation.NonSchedulableActivitySer == Activity.ActivitySer')
    Activity1 = relationship(u'Activity', primaryjoin='ActivityAssociation.SchedulableActivitySer == Activity.ActivitySer')


class ActivityAttribute(Base):
    __tablename__ = 'ActivityAttribute'
    __table_args__ = (
        Index('XIE1ActivityAttribute', 'ActivitySer', 'ActivityRevCount', 'UserDefActAttrSer', 'UserDefActAttrRevCount'),
    )

    ActivityAttributeSer = Column(BigInteger, primary_key=True)
    ActivityAttributeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), nullable=False)
    ActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    UserDefActAttrSer = Column(ForeignKey(u'UserDefActAttr.UserDefActAttrSer'), nullable=False, index=True)
    UserDefActAttrRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Activity = relationship(u'Activity')
    UserDefActAttr = relationship(u'UserDefActAttr')


class ActivityAttributeMH(Base):
    __tablename__ = 'ActivityAttributeMH'

    ActivityAttributeSer = Column(ForeignKey(u'ActivityAttribute.ActivityAttributeSer'), primary_key=True, nullable=False)
    ActivityAttributeRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivitySer = Column(BigInteger, nullable=False)
    ActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    UserDefActAttrSer = Column(BigInteger, nullable=False)
    UserDefActAttrRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityAttribute = relationship(u'ActivityAttribute')


class ActivityCapture(Base):
    __tablename__ = 'ActivityCapture'

    ActivityCaptureSer = Column(BigInteger, primary_key=True)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AccountBillingCodeSer = Column(BigInteger)
    AccountBillingCodeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientPayorSer = Column(BigInteger)
    PatientPayorRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PayorSer = Column(ForeignKey(u'Payor.PayorSer'), index=True)
    ResourceSer = Column(ForeignKey(u'Doctor.ResourceSer'), index=True)
    AttendingOncologistSer = Column(ForeignKey(u'Doctor.ResourceSer'), index=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), index=True)
    LastKnownCourseId = Column(Unicode(16))
    InPatientFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PatientStatus = Column(Unicode(32))
    CompletionResetBy = Column(Unicode(32))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstance = relationship(u'ActivityInstance')
    Doctor = relationship(u'Doctor', primaryjoin='ActivityCapture.AttendingOncologistSer == Doctor.ResourceSer')
    Course = relationship(u'Course')
    Department = relationship(u'Department')
    Payor = relationship(u'Payor')
    Doctor1 = relationship(u'Doctor', primaryjoin='ActivityCapture.ResourceSer == Doctor.ResourceSer')


class ActivityCaptureAttribute(Base):
    __tablename__ = 'ActivityCaptureAttribute'

    ActivityCaptureAttributeSer = Column(BigInteger, primary_key=True)
    ActivityCaptureAttrRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCaptureSer = Column(ForeignKey(u'ActivityCapture.ActivityCaptureSer'), nullable=False, index=True)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityAttributeSer = Column(ForeignKey(u'ActivityAttribute.ActivityAttributeSer'), nullable=False, index=True)
    ActivityAttributeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AttributeValue = Column(Unicode(254))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityAttribute = relationship(u'ActivityAttribute')
    ActivityCapture = relationship(u'ActivityCapture')


class ActivityCaptureAttributeMH(Base):
    __tablename__ = 'ActivityCaptureAttributeMH'

    ActivityCaptureAttributeSer = Column(ForeignKey(u'ActivityCaptureAttribute.ActivityCaptureAttributeSer'), primary_key=True, nullable=False)
    ActivityCaptureAttrRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCaptureSer = Column(BigInteger, nullable=False)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityAttributeSer = Column(BigInteger, nullable=False)
    ActivityAttributeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AttributeValue = Column(Unicode(254))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityCaptureAttribute = relationship(u'ActivityCaptureAttribute')


class ActivityCaptureMH(Base):
    __tablename__ = 'ActivityCaptureMH'

    ActivityCaptureSer = Column(ForeignKey(u'ActivityCapture.ActivityCaptureSer'), primary_key=True, nullable=False)
    ActivityCaptureRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(BigInteger, nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AccountBillingCodeSer = Column(BigInteger)
    AccountBillingCodeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientPayorSer = Column(BigInteger)
    PatientPayorRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PayorSer = Column(BigInteger)
    ResourceSer = Column(BigInteger)
    AttendingOncologistSer = Column(BigInteger)
    DepartmentSer = Column(BigInteger)
    CourseSer = Column(BigInteger)
    LastKnownCourseId = Column(Unicode(16))
    InPatientFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PatientStatus = Column(Unicode(32))
    CompletionResetBy = Column(Unicode(32))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityCapture = relationship(u'ActivityCapture')


class ActivityCategory(Base):
    __tablename__ = 'ActivityCategory'
    __table_args__ = (
        Index('XAK1EventType', 'DepartmentSer', 'ActivityCategoryCode', unique=True),
    )

    ActivityCategorySer = Column(BigInteger, primary_key=True)
    ActivityCategoryCode = Column(Unicode(64), nullable=False)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'))
    DerivedFromActCategorySer = Column(BigInteger)
    SchedulableFlag = Column(Integer)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')


class ActivityChecklistItem(Base):
    __tablename__ = 'ActivityChecklistItem'
    __table_args__ = (
        Index('XAK1ActivityChecklistItem', 'ActivitySer', 'ChecklistItemSer', unique=True),
    )

    ActivityChecklistItemSer = Column(BigInteger, primary_key=True)
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), nullable=False)
    ChecklistItemSer = Column(ForeignKey(u'ChecklistItem.ChecklistItemSer'), nullable=False, index=True)
    SortOrder = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Activity = relationship(u'Activity')
    ChecklistItem = relationship(u'ChecklistItem')


class ActivityCodeMd(Base):
    __tablename__ = 'ActivityCodeMd'

    ModifierSer = Column(BigInteger, primary_key=True)
    ActivityCodeMdRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier = Column(Unicode(64), nullable=False)
    MdfrMultiplier = Column(Float(53))
    Description = Column(Unicode(64), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ActivityCodeMdMH(Base):
    __tablename__ = 'ActivityCodeMdMH'

    ModifierSer = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), primary_key=True, nullable=False)
    ActivityCodeMdRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Modifier = Column(Unicode(64), nullable=False)
    MdfrMultiplier = Column(Float(53))
    Description = Column(Unicode(64), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityCodeMd = relationship(u'ActivityCodeMd')


class ActivityInstance(Base):
    __tablename__ = 'ActivityInstance'
    __table_args__ = (
        Index('XIE2ActivityInstance', 'ActivitySer', 'ActivityRevCount'),
    )

    ActivityInstanceSer = Column(BigInteger, primary_key=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    TemplateCycleSer = Column(ForeignKey(u'TemplateCycle.TemplateCycleSer'), index=True)
    TemplateCycleRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), nullable=False)
    ActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    AppointmentInstanceFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    PredecessorSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), index=True)
    AppointmentDependentFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NotificationPriorTime = Column(Integer)
    Duration = Column(Integer)
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ActivityGroup = Column(Integer)
    MinPostDuration = Column(Integer)
    MinTrtmntOccurence = Column(Integer)
    MaxTrtmntOccurence = Column(Integer)
    DefaultTrtmntOccurence = Column(Integer)
    WeekNumber = Column(Integer)
    DayOfWeek = Column(Integer)
    PriorPostDueDurUnits = Column(Integer)
    ActivityNote = Column(Unicode(254))
    ActInstReadOnly = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ActivityInstanceId = Column(Unicode(16))
    StudySer = Column(ForeignKey(u'Study.StudySer'), index=True)
    WorklistType = Column(Unicode(64))
    PlacerOrderNumber = Column(Unicode(64))
    FillerOrderNumber = Column(Unicode(64))
    NotificationPriorTimeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    LastStatusUpdatedByResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    LastStatusUpdatedDate = Column(DateTime)
    LastNoteUpdatedByResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    LastNoteUpdatedDate = Column(DateTime)
    WorkFlowOverrideByResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    WorkFlowOverrideDate = Column(DateTime)
    AnchorActivityFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    AutoAssignOncologistFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Activity = relationship(u'Activity')
    Department = relationship(u'Department')
    Resource = relationship(u'Resource', primaryjoin='ActivityInstance.LastNoteUpdatedByResourceSer == Resource.ResourceSer')
    Resource1 = relationship(u'Resource', primaryjoin='ActivityInstance.LastStatusUpdatedByResourceSer == Resource.ResourceSer')
    parent = relationship(u'ActivityInstance', remote_side=[ActivityInstanceSer])
    Study = relationship(u'Study')
    TemplateCycle = relationship(u'TemplateCycle')
    Resource2 = relationship(u'Resource', primaryjoin='ActivityInstance.WorkFlowOverrideByResourceSer == Resource.ResourceSer')


class ActivityInstanceLink(Base):
    __tablename__ = 'ActivityInstanceLink'

    ActivityInstanceLinkSer = Column(BigInteger, primary_key=True)
    ActivityInstanceLinkRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    PredecessorSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstance = relationship(u'ActivityInstance', primaryjoin='ActivityInstanceLink.ActivityInstanceSer == ActivityInstance.ActivityInstanceSer')
    ActivityInstance1 = relationship(u'ActivityInstance', primaryjoin='ActivityInstanceLink.PredecessorSer == ActivityInstance.ActivityInstanceSer')


class ActivityInstanceLinkMH(Base):
    __tablename__ = 'ActivityInstanceLinkMH'

    ActivityInstanceLinkSer = Column(ForeignKey(u'ActivityInstanceLink.ActivityInstanceLinkSer'), primary_key=True, nullable=False)
    ActivityInstanceLinkRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(BigInteger, nullable=False)
    PredecessorSer = Column(BigInteger, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstanceLink = relationship(u'ActivityInstanceLink')


class ActivityInstanceMH(Base):
    __tablename__ = 'ActivityInstanceMH'
    __table_args__ = (
        Index('XIE1ActivityInstanceMH', 'ActivitySer', 'ActivityRevCount'),
    )

    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), primary_key=True, nullable=False)
    ActivityInstanceRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    TemplateCycleSer = Column(BigInteger)
    TemplateCycleRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivitySer = Column(BigInteger, nullable=False)
    ActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    DepartmentSer = Column(BigInteger)
    AppointmentInstanceFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    PredecessorSer = Column(BigInteger)
    AppointmentDependentFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NotificationPriorTime = Column(Integer)
    Duration = Column(Integer)
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ActivityGroup = Column(Integer)
    MinPostDuration = Column(Integer)
    MinTrtmntOccurence = Column(Integer)
    MaxTrtmntOccurence = Column(Integer)
    DefaultTrtmntOccurence = Column(Integer)
    WeekNumber = Column(Integer)
    DayOfWeek = Column(Integer)
    PriorPostDueDurUnits = Column(Integer)
    ActivityNote = Column(Unicode(254))
    ActInstReadOnly = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ActivityInstanceId = Column(Unicode(16))
    StudySer = Column(BigInteger)
    WorklistType = Column(Unicode(64))
    PlacerOrderNumber = Column(Unicode(64))
    FillerOrderNumber = Column(Unicode(64))
    NotificationPriorTimeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    LastStatusUpdatedByResourceSer = Column(BigInteger)
    LastStatusUpdatedDate = Column(DateTime)
    LastNoteUpdatedByResourceSer = Column(BigInteger)
    LastNoteUpdatedDate = Column(DateTime)
    WorkFlowOverrideByResourceSer = Column(BigInteger)
    WorkFlowOverrideDate = Column(DateTime)
    AnchorActivityFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    AutoAssignOncologistFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    ActivityInstance = relationship(u'ActivityInstance')


class ActivityMH(Base):
    __tablename__ = 'ActivityMH'
    __table_args__ = (
        Index('XAK1ActivityMH', 'ActivityCategorySer', 'ActivityCode', 'ActivityRevCount', unique=True),
    )

    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), primary_key=True, nullable=False)
    ActivityRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCategorySer = Column(BigInteger, nullable=False)
    ActivityCode = Column(Unicode(64), nullable=False)
    ActivityType = Column(Unicode(32), nullable=False)
    DerivedFromActivitySer = Column(BigInteger)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ResourceGroupSer = Column(BigInteger)
    DefaultDuration = Column(Integer)
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NotificationPriorTime = Column(Integer)
    AssignableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Description = Column(Unicode(254))
    ForeGroundColor = Column(BINARY(4))
    Icon = Column(LargeBinary)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DICOMCodeValueSer = Column(BigInteger)
    NotificationPriorTimeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    EscalationGroupSer = Column(BigInteger)
    TreatmentCycleSer = Column(BigInteger)
    ReviewFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    UpdCPResourceGroupSer = Column(BigInteger)
    UpdCPEscalationGroupSer = Column(BigInteger)
    AutoGenerateFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NoAutoPostFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Activity = relationship(u'Activity')


class ActivityPttrn(Base):
    __tablename__ = 'ActivityPttrn'

    ActivityPttrnSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), index=True)
    PatternStartDateTime = Column(DateTime)
    PatternEndDateTime = Column(DateTime)
    WeeksPerCycle = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Activity = relationship(u'Activity')
    Department = relationship(u'Department')


class ActivityPttrnPerCycle(Base):
    __tablename__ = 'ActivityPttrnPerCycle'

    ActivityPttrnPerCycleSer = Column(BigInteger, primary_key=True)
    ActivityPttrnSer = Column(ForeignKey(u'ActivityPttrn.ActivityPttrnSer'), nullable=False, index=True)
    WeekNumber = Column(Integer)
    ActivityDayOfWeek = Column(Integer)
    ActivityStartTime = Column(DateTime)
    ActivityEndTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityPttrn = relationship(u'ActivityPttrn')


class ActivityPttrnResrc(Base):
    __tablename__ = 'ActivityPttrnResrc'

    ActivityPttrnSer = Column(ForeignKey(u'ActivityPttrn.ActivityPttrnSer'), primary_key=True, nullable=False)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True, nullable=False, index=True)
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityPttrn = relationship(u'ActivityPttrn')
    Resource = relationship(u'Resource')


class ActivityPttrnToSchedActivity(Base):
    __tablename__ = 'ActivityPttrnToSchedActivity'

    ScheduledActivitySer = Column(ForeignKey(u'ScheduledActivity.ScheduledActivitySer'), primary_key=True, nullable=False)
    ActivityPttrnPerCycleSer = Column(ForeignKey(u'ActivityPttrnPerCycle.ActivityPttrnPerCycleSer'), primary_key=True, nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityPttrnPerCycle = relationship(u'ActivityPttrnPerCycle')
    ScheduledActivity = relationship(u'ScheduledActivity')


class ActivitySession(Base):
    __tablename__ = 'ActivitySession'

    ScheduledActivitySer = Column(ForeignKey(u'ScheduledActivity.ScheduledActivitySer'), primary_key=True, nullable=False)
    SessionSer = Column(ForeignKey(u'Session.SessionSer'), primary_key=True, nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ScheduledActivity = relationship(u'ScheduledActivity')
    Session = relationship(u'Session')


class ActivityToProcedureCode(Base):
    __tablename__ = 'ActivityToProcedureCode'

    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), primary_key=True, nullable=False)
    ProcedureCodeSer = Column(ForeignKey(u'ProcedureCode.ProcedureCodeSer'), primary_key=True, nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    SortOrder = Column(Integer)
    AutoAssign = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Activity = relationship(u'Activity')
    ProcedureCode = relationship(u'ProcedureCode')


class ActivityToProcedureItem(Base):
    __tablename__ = 'ActivityToProcedureItem'

    ActivityToProcedureItemSer = Column(BigInteger, primary_key=True)
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), nullable=False, index=True)
    ProcedureItemSer = Column(ForeignKey(u'ProcedureItem.ProcedureItemSer'), nullable=False, index=True)
    AutoAssign = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    SortOrder = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Activity = relationship(u'Activity')
    ProcedureItem = relationship(u'ProcedureItem')


class ActtyCatgryResrcType(Base):
    __tablename__ = 'ActtyCatgryResrcType'
    __table_args__ = (
        Index('XAK1EventTypeResourceType', 'ResourceTypeNum', 'ActivityCategorySer', unique=True),
    )

    ActtyCatgryResrcTypeSer = Column(BigInteger, primary_key=True)
    ActivityCategorySer = Column(ForeignKey(u'ActivityCategory.ActivityCategorySer'), nullable=False, index=True)
    ResourceTypeNum = Column(ForeignKey(u'ResourceType.ResourceTypeNum'), nullable=False)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityCategory = relationship(u'ActivityCategory')
    ResourceType = relationship(u'ResourceType')


class AddOn(Base):
    __tablename__ = 'AddOn'
    __table_args__ = (
        Index('XAKAddOn', 'ResourceSer', 'AddOnId', unique=True),
    )

    AddOnSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'ExternalBeam.ResourceSer'), nullable=False)
    AddOnMaterialSer = Column(ForeignKey(u'AddOnMaterial.AddOnMaterialSer'), index=True)
    AddOnId = Column(Unicode(16), nullable=False)
    AddOnName = Column(Unicode(64))
    AddOnType = Column(Unicode(30))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DisplayCode = Column(Unicode(32))
    InternalCode = Column(Integer)
    ExtDeviceVerification = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    OverridePossible = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ValidationDone = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PFVerifyDone = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AddOnMaterial = relationship(u'AddOnMaterial')
    ExternalBeam = relationship(u'ExternalBeam')


class RangeShifter(AddOn):
    __tablename__ = 'RangeShifter'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    IsoRangeShifterDist = Column(Float(53))
    RangeShifterType = Column(Unicode(32), nullable=False)


class Wedge(AddOn):
    __tablename__ = 'Wedge'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    WedgeType = Column(Unicode(30))
    WedgeAngle = Column(Float(53))
    ThinEdgeToX1Flag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ThinEdgeToX2Flag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ThinEdgeToY1Flag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ThinEdgeToY2Flag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    MaxCollX = Column(Float(53))
    MinCollX = Column(Float(53))
    MaxCollY = Column(Float(53))
    MinCollY = Column(Float(53))
    MaxX1 = Column(Float(53))
    MinX1 = Column(Float(53))
    MaxY1 = Column(Float(53))
    MinY1 = Column(Float(53))
    MaxX2 = Column(Float(53))
    MinX2 = Column(Float(53))
    MaxY2 = Column(Float(53))
    MinY2 = Column(Float(53))


class StandardWedge(Wedge):
    __tablename__ = 'StandardWedge'

    AddOnSer = Column(ForeignKey(u'Wedge.AddOnSer'), primary_key=True)
    MotorizedFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    SourceWedgeDist = Column(Float(53))
    OmniWedgeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class DynamicWedge(Wedge):
    __tablename__ = 'DynamicWedge'

    AddOnSer = Column(ForeignKey(u'Wedge.AddOnSer'), primary_key=True)
    EnhancedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    TreatmentFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    BaseFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class ProtonBeamSpot(AddOn):
    __tablename__ = 'ProtonBeamSpot'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)


class RangeModulator(AddOn):
    __tablename__ = 'RangeModulator'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    IsocenterRangeModDist = Column(Float(53))
    RangeModulatorType = Column(Unicode(32), nullable=False)


class MLC(AddOn):
    __tablename__ = 'MLC'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    ManufacturerName = Column(Unicode(254))
    MLCSerialNumber = Column(Unicode(64))
    MLCModel = Column(Unicode(64))
    Rotation = Column(Float(53))
    SupportedFiles = Column(Unicode(64))
    ArcEnableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DoseEnableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    MinDoseDynamicLeafGap = Column(Float(53), nullable=False)
    MinArcDynamicLeafGap = Column(Float(53), nullable=False)
    MaxLeafSpeed = Column(Float(53), nullable=False)
    DoseDynamicLeafTolerance = Column(Float(53), nullable=False)
    ArcDynamicLeafTolerance = Column(Float(53), nullable=False)
    MinStaticLeafGap = Column(Float(53))
    MinSegmentThreshold = Column(Float(53), nullable=False)
    MaxControlPoints = Column(Integer, nullable=False)
    SourceDistance = Column(Float(53))
    ParallelJawSetBack = Column(Float(53))
    PerpendicularJawSetBack = Column(Float(53))
    MaxPerpendicularJawOpening = Column(Float(53))
    NominalLeafLength = Column(Float(53), nullable=False)


class ProtonLateralSpreader(AddOn):
    __tablename__ = 'ProtonLateralSpreader'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    IsoLatSpreadDevDist = Column(Float(53))
    ProtonLatSpreaderType = Column(Unicode(32), nullable=False)


class BeamlineOption(AddOn):
    __tablename__ = 'BeamlineOption'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)


class Tray(AddOn):
    __tablename__ = 'Tray'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    CompensatorDefault = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ProtonWaterEquiThickness = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))


class PrimaryFluenceMode(AddOn):
    __tablename__ = 'PrimaryFluenceMode'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    MaxCollX = Column(Float(53))
    MaxCollY = Column(Float(53))
    MaxX1 = Column(Float(53))
    MaxX2 = Column(Float(53))
    MaxY1 = Column(Float(53))
    MaxY2 = Column(Float(53))
    MinCollX = Column(Float(53))
    MinCollY = Column(Float(53))
    MinX1 = Column(Float(53))
    MinX2 = Column(Float(53))
    MinY1 = Column(Float(53))
    MinY2 = Column(Float(53))


class Applicator(AddOn):
    __tablename__ = 'Applicator'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    AllowInserts = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RectangularFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    FieldSizeX = Column(Float(53))
    FieldSizeY = Column(Float(53))
    ApplicatorLength = Column(Float(53))
    ApplicatorDICOMType = Column(Unicode(16))


class Snout(AddOn):
    __tablename__ = 'Snout'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True)
    MaxRadius = Column(Float(53))
    MaxX = Column(Float(53))
    MaxY = Column(Float(53))
    RectangularFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))


class AddOnMaterial(Base):
    __tablename__ = 'AddOnMaterial'

    AddOnMaterialSer = Column(BigInteger, primary_key=True)
    AddOnMaterialId = Column(Unicode(16), nullable=False)
    AddOnMaterialName = Column(Unicode(64))
    UsageType = Column(Unicode(32))
    Thickness = Column(Float(53))
    BaseplateThickness = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class AddOnValidation(Base):
    __tablename__ = 'AddOnValidation'

    ConfiguredEMTSer = Column(ForeignKey(u'ConfiguredEMT.ConfiguredEMTSer'), primary_key=True, nullable=False)
    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AddOn = relationship(u'AddOn')
    ConfiguredEMT = relationship(u'ConfiguredEMT')


class Addres(Base):
    __tablename__ = 'Address'

    AddressSer = Column(BigInteger, primary_key=True)
    AddressType = Column(Unicode(64), nullable=False)
    Country = Column(Unicode(64))
    StateOrProvince = Column(Unicode(64))
    Location = Column(Unicode(64))
    County = Column(Unicode(64))
    CityOrTownship = Column(Unicode(64))
    AddressLine1 = Column(Unicode(64))
    AddressLine2 = Column(Unicode(64))
    AddressLine3 = Column(Unicode(64))
    PostalCode = Column(Unicode(16))
    OriginationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    TerminationDate = Column(DateTime)
    PhoneNumber1 = Column(Unicode(64))
    PhoneNumber2 = Column(Unicode(64))
    FaxNumber = Column(Unicode(64))
    EMailAddress = Column(Unicode(64))
    PagerNumber = Column(Unicode(64))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


t_AppContext = Table(
    'AppContext', metadata,
    Column('spid', Integer),
    Column('ContextName', String(100, u'Latin1_General_BIN2')),
    Column('AttributeName', String(100, u'Latin1_General_BIN2')),
    Column('AttributeValue', String(100, u'Latin1_General_BIN2')),
    Index('PK_AppContext', 'spid', 'ContextName', 'AttributeName', unique=True)
)


class AppObject(Base):
    __tablename__ = 'AppObject'
    __table_args__ = (
        Index('XAK1ScreenObject', 'ObjectName', 'ObjectGroupName', unique=True),
    )

    AppObjectSer = Column(BigInteger, primary_key=True)
    ObjectName = Column(Unicode(64), nullable=False)
    ObjectGroupName = Column(Unicode(64), nullable=False, index=True)
    Description = Column(Unicode(64))
    AddStatusFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    DeleteStatusFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ApproveStatusFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    AccessStatusFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class AppUser(Base):
    __tablename__ = 'AppUser'

    AppUserSer = Column(BigInteger, primary_key=True)
    UserCUID = Column(Unicode(64), nullable=False, unique=True)
    UserId = Column(Unicode(16), nullable=False, unique=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    LanguageId = Column(ForeignKey(u'LanguageLookup.LanguageId'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    LanguageLookup = relationship(u'LanguageLookup')
    Resource = relationship(u'Resource')


class Application(Base):
    __tablename__ = 'Application'

    ApplicationSer = Column(BigInteger, primary_key=True)
    ApplicationDesc = Column(Unicode(64), nullable=False, unique=True)
    ApplicationNote = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ApplicationAccessLog(Base):
    __tablename__ = 'ApplicationAccessLog'
    __table_args__ = (
        Index('XIE1ApplicationAccessLog', 'HstryDateTime', 'LoginName'),
    )

    ApplicationAccessLogSer = Column(BigInteger, primary_key=True)
    Spid = Column(Integer, nullable=False)
    Suid = Column(Integer, nullable=False)
    LoginName = Column(Unicode(32), nullable=False)
    ApplicationName = Column(Unicode(64), nullable=False)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    ExtraInfo = Column(Unicode(254))


class ApplicationPrintReport(Base):
    __tablename__ = 'ApplicationPrintReport'

    PrintReportSer = Column(ForeignKey(u'PrintReport.PrintReportSer'), primary_key=True, nullable=False)
    ApplicationSer = Column(ForeignKey(u'Application.ApplicationSer'), primary_key=True, nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Application = relationship(u'Application')
    PrintReport = relationship(u'PrintReport')


class ApplicatorJawSize(Base):
    __tablename__ = 'ApplicatorJawSize'
    __table_args__ = (
        Index('XIE1ApplicatorJawSize', 'ApplicatorSer', 'EnergyModeSer'),
    )

    ApplicatorJawSizeSer = Column(BigInteger, primary_key=True)
    ApplicatorSer = Column(ForeignKey(u'Applicator.AddOnSer'), nullable=False)
    EnergyModeSer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), nullable=False, index=True)
    CollX = Column(Float(53))
    CollY = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Applicator = relationship(u'Applicator')
    EnergyMode = relationship(u'EnergyMode')


class Approval(Base):
    __tablename__ = 'Approval'

    ApprovalSer = Column(Numeric(7, 0), primary_key=True)
    ApprovalRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    TypeSer = Column(BigInteger, nullable=False, index=True)
    Type1Ser = Column(BigInteger)
    Type2Ser = Column(BigInteger)
    TypeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Type1RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Type2RevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ApprovalType = Column(Unicode(30), nullable=False)
    Status = Column(Unicode(64), nullable=False)
    StatusUserName = Column(Unicode(32), nullable=False)
    StatusDate = Column(DateTime, nullable=False)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ArchiveLocation(Base):
    __tablename__ = 'ArchiveLocation'

    ArchiveLocationSer = Column(BigInteger, primary_key=True)
    ArchiveLocationPath = Column(Unicode(254), nullable=False)
    ArchiveMediaType = Column(Unicode(64), nullable=False)
    ArchiveMediaStatus = Column(Unicode(64), nullable=False)
    ArchiveMediaLabel = Column(Unicode(254), nullable=False)
    ArchiveMediaId = Column(Unicode(254))
    ArchiveMediaStartDate = Column(DateTime, nullable=False)
    ArchiveMediaCloseDate = Column(DateTime)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ArchiveRestoredFile(Base):
    __tablename__ = 'ArchiveRestoredFile'
    __table_args__ = (
        Index('XAKArchiveRestoredFile', 'PatientSer', 'FileName', unique=True),
    )

    ArchiveRestoredFileSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False)
    FileName = Column(Unicode(64), nullable=False)
    OriginalFileName = Column(Unicode(64))
    DocumentType = Column(Unicode(64), nullable=False)
    ArchiveDate = Column(DateTime)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')


class Attendee(Base):
    __tablename__ = 'Attendee'

    AttendeeSer = Column(BigInteger, primary_key=True)
    AttendeeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    ResourceGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ParticipationRole = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ActivityOwnerFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    ActivityInstance = relationship(u'ActivityInstance')
    ResourceGroup = relationship(u'ResourceGroup')
    Resource = relationship(u'Resource')


class AttendeeMH(Base):
    __tablename__ = 'AttendeeMH'
    __table_args__ = (
        Index('XIE1AttendeeMH', 'ActivityInstanceSer', 'ActivityInstanceRevCount'),
    )

    AttendeeSer = Column(ForeignKey(u'Attendee.AttendeeSer'), primary_key=True, nullable=False)
    AttendeeRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(BigInteger, nullable=False)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ResourceSer = Column(BigInteger)
    ResourceGroupSer = Column(BigInteger)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ParticipationRole = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ActivityOwnerFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Attendee = relationship(u'Attendee')


class AuditLog(Base):
    __tablename__ = 'AuditLog'
    __table_args__ = (
        Index('XIE1AuditLog', 'HstryDateTime', 'LoginName', 'PatientId'),
    )

    AuditLogSer = Column(BigInteger, primary_key=True)
    AuditType = Column(Unicode(32), nullable=False)
    Spid = Column(Integer, nullable=False)
    Suid = Column(Integer, nullable=False)
    LoginName = Column(Unicode(32), nullable=False)
    PatientId = Column(Unicode(25), nullable=False, index=True)
    FirstName = Column(Unicode(64))
    LastName = Column(Unicode(64))
    DiagnosisId = Column(Unicode(16))
    DiagnosisTableName = Column(Unicode(64))
    DiagnosisCode = Column(Unicode(16))
    CourseId = Column(Unicode(16))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    ProcName = Column(Unicode(32), nullable=False)
    ExtraInfo = Column(Unicode(254))


class AvailPrefPttrnDetail(Base):
    __tablename__ = 'AvailPrefPttrnDetails'

    AvailPrefPttrnDetailsSer = Column(BigInteger, primary_key=True)
    AvailPrefWeeklyPttrnSer = Column(ForeignKey(u'AvailPrefWeeklyPttrn.AvailPrefWeeklyPttrnSer'), nullable=False, index=True)
    PatternDayOfWeek = Column(Integer)
    PatternStartTime = Column(DateTime)
    PatternEndTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ActivityCategorySer = Column(ForeignKey(u'ActivityCategory.ActivityCategorySer'), index=True)
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), index=True)

    ActivityCategory = relationship(u'ActivityCategory')
    Activity = relationship(u'Activity')
    AvailPrefWeeklyPttrn = relationship(u'AvailPrefWeeklyPttrn')


class AvailPrefWeeklyPttrn(Base):
    __tablename__ = 'AvailPrefWeeklyPttrn'
    __table_args__ = (
        Index('XIE1AvailPrefWeeklyPttrn', 'ActivitySer', 'ResourceDepartmentSer', 'PrfrPttrnFlag'),
    )

    AvailPrefWeeklyPttrnSer = Column(BigInteger, primary_key=True)
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'))
    ResourceDepartmentSer = Column(ForeignKey(u'ResourceDepartment.ResourceDepartmentSer'), nullable=False, index=True)
    PrfrPttrnFlag = Column(Integer, nullable=False)
    PatternStartDateTime = Column(DateTime)
    PatternEndDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ActivityCategorySer = Column(ForeignKey(u'ActivityCategory.ActivityCategorySer'), index=True)

    ActivityCategory = relationship(u'ActivityCategory')
    Activity = relationship(u'Activity')
    ResourceDepartment = relationship(u'ResourceDepartment')


class BillSysChrgWrk(Base):
    __tablename__ = 'BillSysChrgWrk'

    VarisBillRunSeqId = Column(Integer, primary_key=True, nullable=False)
    ActInstProcCodeSer = Column(ForeignKey(u'ActInstProcCode.ActInstProcCodeSer'), primary_key=True, nullable=False)
    ActInstProcCodeRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ChargeIndicator = Column(Unicode(16), primary_key=True, nullable=False)
    BillSysInstId = Column(Unicode(64), nullable=False)
    BillSysId = Column(Unicode(64), nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    PatientLastName = Column(Unicode(64))
    PatientFirstName = Column(Unicode(64))
    PatientMiddleName = Column(Unicode(64))
    PatientId = Column(Unicode(25))
    PatientId2 = Column(Unicode(25))
    PatientAccountNumberId = Column(Unicode(32))
    PatientAddressType = Column(Unicode(64))
    PatientCountry = Column(Unicode(64))
    PatientStateOrProvince = Column(Unicode(64))
    PatientCounty = Column(Unicode(64))
    PatientCityOrTownship = Column(Unicode(64))
    PatientAddressLine1 = Column(Unicode(64))
    PatientAddressLine2 = Column(Unicode(64))
    PatientPostalCode = Column(Unicode(16))
    PhoneNumberHome1 = Column(Unicode(64))
    PhoneNumberHome2 = Column(Unicode(64))
    PhoneNumberHome3 = Column(Unicode(64))
    PhoneNumberBusiness1 = Column(Unicode(64))
    PhoneNumberBusiness2 = Column(Unicode(64))
    PatientBirthDate = Column(DateTime)
    PatientSSN = Column(Unicode(64))
    PatientRace = Column(Unicode(64))
    PatientMothersMaidenName = Column(Unicode(64))
    PatientSex = Column(Unicode(16))
    PatientStatus = Column(Unicode(32))
    PatientMaritalStatus = Column(Unicode(16))
    PatientLocation = Column(Unicode(16))
    PatientDischargeDate = Column(DateTime)
    PatientAdmissionDate = Column(DateTime)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    DepartmentName = Column(Unicode(64))
    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), index=True)
    HospitalName = Column(Unicode(64))
    CompletedDateTime = Column(DateTime)
    FromDateOfService = Column(DateTime)
    CodeType = Column(Unicode(32))
    ActivityType = Column(Unicode(32))
    BillingCode = Column(Unicode(64))
    MedicareComplexCode = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_CODEVALUE_DEF]
	AS 0"""))
    ProcedureCode = Column(Unicode(64))
    ModifierCode = Column(Unicode(64))
    UserDefinedCode = Column(Unicode(64))
    ProcedureComment = Column(Unicode(254))
    ProcedureShortComment = Column(Unicode(64))
    ModifierDescription = Column(Unicode(64))
    ModifierCode2 = Column(Unicode(64))
    ModifierDescription2 = Column(Unicode(64))
    ModifierCode3 = Column(Unicode(64))
    ModifierDescription3 = Column(Unicode(64))
    ModifierCode4 = Column(Unicode(64))
    ModifierDescription4 = Column(Unicode(64))
    ModifierCode5 = Column(Unicode(64))
    ModifierDescription5 = Column(Unicode(64))
    ModifierCode6 = Column(Unicode(64))
    ModifierDescription6 = Column(Unicode(64))
    ModifierCode7 = Column(Unicode(64))
    ModifierDescription7 = Column(Unicode(64))
    TSAComment = Column(Unicode(254))
    NoChargeFlag = Column(Integer)
    NumberOfCycles = Column(Integer)
    PrmrTechCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PrmrProfessCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PrmrGlblCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OtherGlobalCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OtherProfessionalCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OtherTechnicalCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    TechnicalRVU = Column(Float(53))
    ProfessionalRVU = Column(Float(53))
    GlobalRVU = Column(Float(53))
    AverageActivityCost = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    BillingServiceID = Column(Unicode(16))
    RVUExportCode = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RVUExport = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RVUMultiplier = Column(Float(53))
    ExportType = Column(Unicode(32))
    ExternalBillingCodeExport = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ApprovedBy = Column(Unicode(32))
    CompletedBy = Column(Unicode(32))
    DiagnosisCode = Column(Unicode(16))
    DiagnosisDescription = Column(Unicode(254))
    InsuranceCompanyName1 = Column(Unicode(64))
    InsurancePlanType1 = Column(Unicode(32))
    InsurancePlanNumber1 = Column(Unicode(16))
    AuthorizationDescription1 = Column(Unicode(254))
    InsuranceCompanyName2 = Column(Unicode(64))
    InsurancePlanType2 = Column(Unicode(32))
    InsurancePlanNumber2 = Column(Unicode(16))
    AuthorizationDescription2 = Column(Unicode(254))
    InsuranceCompanyName3 = Column(Unicode(64))
    InsurancePlanType3 = Column(Unicode(32))
    InsurancePlanNumber3 = Column(Unicode(16))
    AuthorizationDescription3 = Column(Unicode(254))
    InsuranceCompanyName4 = Column(Unicode(64))
    InsurancePlanType4 = Column(Unicode(32))
    InsurancePlanNumber4 = Column(Unicode(16))
    AuthorizationDescription4 = Column(Unicode(254))
    RadiationOncologistLastName = Column(Unicode(64))
    RadiationOncologistFirstName = Column(Unicode(64))
    RadiationOncologistID = Column(Unicode(16))
    RadiationOncologistSpecialty = Column(Unicode(64))
    ReferringPhysicianLastName = Column(Unicode(64))
    ReferringPhysicianFirstName = Column(Unicode(64))
    ReferringPhysicianID = Column(Unicode(16))
    ReferringPhysicianSpecialty = Column(Unicode(64))
    ActivitySerialNumber = Column(ForeignKey(u'Activity.ActivitySer'), index=True)
    ChargesControlSerialNumber = Column(ForeignKey(u'ChargesControl.ChargesControlSer'), index=True)
    AccountBillingCodeSer = Column(ForeignKey(u'AccountBillingCode.AccountBillingCodeSer'), index=True)
    AccountBillingCodeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ProcedureCodeSer = Column(ForeignKey(u'ProcedureCode.ProcedureCodeSer'), index=True)
    ProcedureCodeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    InPatientFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ActivityCaptureSer = Column(ForeignKey(u'ActivityCapture.ActivityCaptureSer'), index=True)
    ActivityCaptureRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    TransId = Column(Unicode(16))
    BatchId = Column(Unicode(16))
    FillerRefNo = Column(Unicode(16))
    ExportedBy = Column(Unicode(32))

    AccountBillingCode = relationship(u'AccountBillingCode')
    ActInstProcCode = relationship(u'ActInstProcCode')
    ActivityCapture = relationship(u'ActivityCapture')
    Activity = relationship(u'Activity')
    ChargesControl = relationship(u'ChargesControl')
    Department = relationship(u'Department')
    Hospital = relationship(u'Hospital')
    Patient = relationship(u'Patient')
    ProcedureCode1 = relationship(u'ProcedureCode')


class BillSysHospDeptActivity(Base):
    __tablename__ = 'BillSysHospDeptActivity'

    BillSysHospDeptActivitySer = Column(BigInteger, primary_key=True)
    BillSysInstId = Column(Unicode(64), nullable=False)
    BillSysId = Column(Unicode(64), nullable=False)
    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), nullable=False, index=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), nullable=False, index=True)
    CodeType = Column(Unicode(32), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')
    Hospital = relationship(u'Hospital')


class BillSysSentCharge(Base):
    __tablename__ = 'BillSysSentCharges'
    __table_args__ = (
        Index('XAKBillSysSentCharges', 'TransId', 'ActInstProcCodeSer', 'ActInstProcCodeRevCount', 'ChargeIndicator', 'VoidCharge', unique=True),
    )

    BillSysSentChargesSer = Column(BigInteger, primary_key=True)
    TransId = Column(Unicode(16), nullable=False)
    ActInstProcCodeSer = Column(ForeignKey(u'ActInstProcCode.ActInstProcCodeSer'), nullable=False, index=True)
    ActInstProcCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ChargeIndicator = Column(Unicode(16), nullable=False)
    VoidCharge = Column(Unicode(1), nullable=False)
    BillSysInstId = Column(Unicode(64), nullable=False)
    BillSysId = Column(Unicode(64), nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    MergeFlag = Column(Unicode(1))
    BatchId = Column(Unicode(16))
    Hl7MsgCntlId = Column(Unicode(32))
    Hl7SetId = Column(Integer)
    FillerRefNo = Column(Unicode(16))
    BillEventUnits = Column(Integer)
    BillCdBillPrice = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    BillCdInvId = Column(Unicode(16))
    SendSurpressed = Column(Unicode(1))
    BillChargeStatus = Column(Unicode(1), nullable=False)
    BillChargeStatusTxt = Column(Unicode(254))

    ActInstProcCode = relationship(u'ActInstProcCode')
    Patient = relationship(u'Patient')


class BillingService(Base):
    __tablename__ = 'BillingService'

    BillingServiceSer = Column(BigInteger, primary_key=True)
    BillingServiceID = Column(Unicode(16), nullable=False, unique=True)
    BillingServiceName = Column(Unicode(64), nullable=False)
    Location = Column(Unicode(64))
    AddressLine1 = Column(Unicode(64))
    AddressLine2 = Column(Unicode(64))
    AddressLine3 = Column(Unicode(64))
    CityorTownship = Column(Unicode(64))
    County = Column(Unicode(64))
    StateOrProvince = Column(Unicode(64))
    Country = Column(Unicode(64))
    PostalCode = Column(Unicode(16))
    POCName = Column(Unicode(254))
    POCPhoneNumber = Column(Unicode(64))
    POCFaxNumber = Column(Unicode(64))
    ExtBillingExportFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RVUExportFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class Block(Base):
    __tablename__ = 'Block'

    BlockSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), nullable=False, index=True)
    AddOnMaterialSer = Column(ForeignKey(u'AddOnMaterial.AddOnMaterialSer'), index=True)
    TrayAddOnSer = Column(ForeignKey(u'Tray.AddOnSer'), index=True)
    BlockId = Column(Unicode(64), nullable=False)
    DicomSeqNumber = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DICOMSEQNBR_DEF]
	AS -999999999"""))
    BlockType = Column(Unicode(32))
    AboveTrayFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DivergingFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Coordinates = Column(LargeBinary)
    CoordinatesLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    EllipticalMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    BEVMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    LeftMargin = Column(Float(53))
    RightMargin = Column(Float(53))
    TopMargin = Column(Float(53))
    BottomMargin = Column(Float(53))
    OptimizeCollRtnFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    OptimizeFldSizeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    BlockThickness = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    MillingMachineResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    DrillBitDiameter = Column(Float(53))
    SnoutPositionUsedForMillingCorrection = Column(Float(53))
    MillingCorrectionConfiguredFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    AddOnMaterial = relationship(u'AddOnMaterial')
    Resource = relationship(u'Resource')
    ExternalFieldCommon = relationship(u'ExternalFieldCommon')
    Tray = relationship(u'Tray')


class BrachyApplicator(Base):
    __tablename__ = 'BrachyApplicator'

    BrachyApplicatorSer = Column(BigInteger, primary_key=True)
    BrachyApplicatorId = Column(Unicode(16), nullable=False, unique=True)
    BrachyApplicatorName = Column(Unicode(64))
    BrachyApplicatorTypeInfo = Column(Unicode(16))
    DefaultLength = Column(Float(53))
    ManufacturerName = Column(Unicode(254))
    NoOfShapePoints = Column(Integer)
    Shape = Column(LargeBinary)
    NoOfSourceGeom = Column(Integer)
    SourceGeometry = Column(LargeBinary)
    WallMaterialId = Column(Unicode(16))
    WallNominalTransmission = Column(Float(53))
    Comment = Column(Unicode(254))
    StepSize = Column(Float(53))
    FirstSourcePosition = Column(Float(53))
    LastSourcePosition = Column(Float(53))
    SeparateSources = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DefaultChannelNumber = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))


class BrachySolidApplicator(Base):
    __tablename__ = 'BrachySolidApplicator'

    BrachySolidApplicatorSer = Column(BigInteger, primary_key=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), nullable=False, index=True)
    BrachySolidApplicatorId = Column(Unicode(16), nullable=False)
    BrachySolidApplicatorName = Column(Unicode(64))
    ApplicatorPartUID = Column(Unicode(64), nullable=False)
    ApplicatorPartFileName = Column(Unicode(254), nullable=False)
    Transformation = Column(BINARY(96), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PlanSetup = relationship(u'PlanSetup')


class BreakPoint(Base):
    __tablename__ = 'BreakPoint'
    __table_args__ = (
        Index('XAKBreakPoint', 'RefPointSer', 'BreakPointNum', unique=True),
    )

    BreakPointSer = Column(BigInteger, primary_key=True)
    RefPointSer = Column(ForeignKey(u'RefPoint.RefPointSer'), nullable=False)
    BreakPointNum = Column(Integer, nullable=False)
    BreakPointDose = Column(Float(53))
    BreakPointCondition = Column(Unicode(64), nullable=False)
    AuthorizationName = Column(Unicode(32))
    Note = Column(Unicode(254))
    AuthorizationDate = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    RefPoint = relationship(u'RefPoint')


class Channel(Base):
    __tablename__ = 'Channel'

    ChannelSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'BrachyUnit.ResourceSer'), nullable=False, index=True)
    ChannelId = Column(Unicode(16), nullable=False)
    ChannelName = Column(Unicode(64))
    ChannelNumber = Column(Integer)
    MinLength = Column(Float(53))
    MaxLength = Column(Float(53))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    BrachyUnit = relationship(u'BrachyUnit')


class ChargesControl(Base):
    __tablename__ = 'ChargesControl'

    ChargesControlSer = Column(BigInteger, primary_key=True)
    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), index=True)
    TmpltType = Column(Unicode(32))
    ExtBillCodDisp = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ExtBillCodExport = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ExportType = Column(Unicode(32), nullable=False)
    RVUExport = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RVUMultiplier = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Hospital = relationship(u'Hospital')


class ChartQA(Base):
    __tablename__ = 'ChartQA'

    ChartQASer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    ChartQADateTime = Column(DateTime, nullable=False)
    ChartQABy = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    Comment = Column(Unicode(1024))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstance = relationship(u'ActivityInstance')
    Patient = relationship(u'Patient')


class ChartQATreatment(Base):
    __tablename__ = 'ChartQATreatment'
    __table_args__ = (
        Index('XAK1ChartQATreatment', 'RadiationHstrySer', 'ChartQASer', unique=True),
    )

    ChartQATreatmentSer = Column(BigInteger, primary_key=True)
    RadiationHstrySer = Column(ForeignKey(u'RadiationHstry.RadiationHstrySer'), nullable=False)
    ChartQASer = Column(ForeignKey(u'ChartQA.ChartQASer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ChartQA = relationship(u'ChartQA')
    RadiationHstry = relationship(u'RadiationHstry')


class ChecklistGroup(Base):
    __tablename__ = 'ChecklistGroup'
    __table_args__ = (
        Index('XAK1ChecklistGroup', 'DepartmentSer', 'ChecklistGroupName', unique=True),
    )

    ChecklistGroupSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'))
    ChecklistGroupName = Column(Unicode(254), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')


class ChecklistItem(Base):
    __tablename__ = 'ChecklistItem'
    __table_args__ = (
        Index('XAK1ChecklistItem', 'DepartmentSer', 'ChecklistItemDesc', unique=True),
    )

    ChecklistItemSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'))
    ChecklistItemDesc = Column(Unicode(254), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')


class ChecklistItemGroup(Base):
    __tablename__ = 'ChecklistItemGroup'
    __table_args__ = (
        Index('XAK1ChecklistItemGroup', 'ChecklistGroupSer', 'ChecklistItemSer', unique=True),
    )

    ChecklistItemGroupSer = Column(BigInteger, primary_key=True)
    ChecklistItemSer = Column(ForeignKey(u'ChecklistItem.ChecklistItemSer'), nullable=False, index=True)
    ChecklistGroupSer = Column(ForeignKey(u'ChecklistGroup.ChecklistGroupSer'), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ChecklistGroup = relationship(u'ChecklistGroup')
    ChecklistItem = relationship(u'ChecklistItem')


class ChildMachine(Base):
    __tablename__ = 'ChildMachine'

    ChildResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True, nullable=False)
    ParentResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Machine = relationship(u'Machine', primaryjoin='ChildMachine.ChildResourceSer == Machine.ResourceSer')
    Machine1 = relationship(u'Machine', primaryjoin='ChildMachine.ParentResourceSer == Machine.ResourceSer')


class ChildProcessing(Base):
    __tablename__ = 'ChildProcessing'

    ParentProcessingSer = Column(ForeignKey(u'Processing.ProcessingSer'), primary_key=True, nullable=False)
    ChildProcessingSer = Column(ForeignKey(u'Processing.ProcessingSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    SequenceNumber = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Processing = relationship(u'Processing', primaryjoin='ChildProcessing.ChildProcessingSer == Processing.ProcessingSer')
    Processing1 = relationship(u'Processing', primaryjoin='ChildProcessing.ParentProcessingSer == Processing.ProcessingSer')


class Compensator(Base):
    __tablename__ = 'Compensator'

    CompensatorSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), nullable=False, index=True)
    AddOnMaterialSer = Column(ForeignKey(u'AddOnMaterial.AddOnMaterialSer'), index=True)
    TrayAddOnSer = Column(ForeignKey(u'Tray.AddOnSer'), index=True)
    CompensatorId = Column(Unicode(16), nullable=False)
    CompensatorName = Column(Unicode(64))
    CompensatorType = Column(Unicode(32), nullable=False)
    AboveTrayFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    FieldEdgeMargin = Column(Float(53))
    ColumnOffset = Column(Float(53))
    DivergingFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DicomSeqNumber = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DICOMSEQNBR_DEF]
	AS -999999999"""))
    Comment = Column(Unicode(254))
    Status = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AddOnMaterial = relationship(u'AddOnMaterial')
    ExternalFieldCommon = relationship(u'ExternalFieldCommon')
    Tray = relationship(u'Tray')


class ProtonCompensator(Compensator):
    __tablename__ = 'ProtonCompensator'

    CompensatorSer = Column(ForeignKey(u'Compensator.CompensatorSer'), primary_key=True)
    BolusFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    CompMillingToolDiameter = Column(Float(53))
    CompStoppingPowerRatio = Column(Float(53))
    MillingMachineId = Column(Unicode(16))


class PhotonCompensator(Compensator):
    __tablename__ = 'PhotonCompensator'

    CompensatorSer = Column(ForeignKey(u'Compensator.CompensatorSer'), primary_key=True)
    IsoToPlaneDistance = Column(Float(53))


class ConfigurationGuard(Base):
    __tablename__ = 'ConfigurationGuard'

    HstryTimeStamp = Column(DateTime, primary_key=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False)
    HstryTaskName = Column(Unicode(32), nullable=False)


class ConfigurationItem(Base):
    __tablename__ = 'ConfigurationItem'

    ConfigurationSetSer = Column(ForeignKey(u'ConfigurationSet.ConfigurationSetSer'), primary_key=True, nullable=False)
    ConfigurationItemId = Column(Unicode(16), primary_key=True, nullable=False, index=True)
    ConfigValue = Column(Unicode(254))
    SettingXML = Column(UnicodeText(1073741823))
    SettingXMLLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ConfigurationSet = relationship(u'ConfigurationSet')


class ConfigurationSet(Base):
    __tablename__ = 'ConfigurationSet'

    ConfigurationSetSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    AppUserSer = Column(ForeignKey(u'AppUser.AppUserSer'), index=True)
    ConfigurationSetId = Column(Unicode(16), nullable=False, index=True)
    UserOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    EditFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AppUser = relationship(u'AppUser')
    Department = relationship(u'Department')


class ConfiguredEMT(Base):
    __tablename__ = 'ConfiguredEMT'
    __table_args__ = (
        Index('XAK1ConfiguredEMT', 'TechniqueSer', 'EnergyModeSer', unique=True),
    )

    ConfiguredEMTSer = Column(BigInteger, primary_key=True)
    TechniqueSer = Column(ForeignKey(u'Technique.TechniqueSer'), nullable=False)
    EnergyModeSer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), nullable=False, index=True)
    DefaultVirtualSADX = Column(Float(53))
    DefaultVirtualSADY = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    EnergyMode = relationship(u'EnergyMode')
    Technique = relationship(u'Technique')


class ContrastBolu(Base):
    __tablename__ = 'ContrastBolus'

    ContrastBolusSer = Column(BigInteger, primary_key=True)
    Agent = Column(Unicode(64))
    Route = Column(Unicode(64))
    Volume = Column(Float(53))
    StartTime = Column(DateTime)
    StopTime = Column(DateTime)
    TotalDose = Column(Float(53))
    Ingredient = Column(Unicode(16))
    IngredientConcentration = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), nullable=False, index=True)

    Slouse = relationship(u'Slouse')


class ContrastBolusCode(Base):
    __tablename__ = 'ContrastBolusCode'
    __table_args__ = (
        Index('XAK1ContrastBolusCode', 'ContrastBolusSer', 'CodeIndex', 'CodeType', unique=True),
    )

    ContrastBolusCodeSer = Column(BigInteger, primary_key=True)
    ContrastBolusSer = Column(ForeignKey(u'ContrastBolus.ContrastBolusSer'), nullable=False)
    CodeType = Column(Integer, nullable=False)
    CodeIndex = Column(Integer, nullable=False)
    Value = Column(Unicode(16))
    Designator = Column(Unicode(16))
    Version = Column(Unicode(16))
    Meaning = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ContrastBolu = relationship(u'ContrastBolu')


class ContrastFlow(Base):
    __tablename__ = 'ContrastFlow'
    __table_args__ = (
        Index('XAK1ContrastFlow', 'ContrastBolusSer', 'FlowIndex', unique=True),
    )

    ContrastFlowSer = Column(BigInteger, primary_key=True)
    ContrastBolusSer = Column(ForeignKey(u'ContrastBolus.ContrastBolusSer'), nullable=False)
    FlowIndex = Column(Integer, nullable=False)
    FlowRate = Column(Float(53), nullable=False)
    FlowDuration = Column(Float(53), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ContrastBolu = relationship(u'ContrastBolu')


class ControlPoint(Base):
    __tablename__ = 'ControlPoint'
    __table_args__ = (
        Index('XAK1ControlPoint', 'RadiationSer', 'ControlPointIndex', unique=True),
    )

    ControlPointSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), nullable=False)
    ControlPointIndex = Column(Integer, nullable=False)
    ControlPointType = Column(Unicode(30), nullable=False)
    MetersetWeight = Column(Float(53), nullable=False)
    NominalEnergy = Column(Integer)
    CollX1 = Column(Float(53))
    CollX2 = Column(Float(53))
    CollY1 = Column(Float(53))
    CollY2 = Column(Float(53))
    GantryRtn = Column(Float(53))
    CollRtn = Column(Float(53))
    OffPlaneAngle = Column(Float(53))
    PlanPosLeaf1A = Column(SmallInteger)
    PlanPosLeaf2A = Column(SmallInteger)
    PlanPosLeaf3A = Column(SmallInteger)
    PlanPosLeaf4A = Column(SmallInteger)
    PlanPosLeaf5A = Column(SmallInteger)
    PlanPosLeaf6A = Column(SmallInteger)
    PlanPosLeaf7A = Column(SmallInteger)
    PlanPosLeaf8A = Column(SmallInteger)
    PlanPosLeaf9A = Column(SmallInteger)
    PlanPosLeaf10A = Column(SmallInteger)
    PlanPosLeaf11A = Column(SmallInteger)
    PlanPosLeaf12A = Column(SmallInteger)
    PlanPosLeaf13A = Column(SmallInteger)
    PlanPosLeaf14A = Column(SmallInteger)
    PlanPosLeaf15A = Column(SmallInteger)
    PlanPosLeaf16A = Column(SmallInteger)
    PlanPosLeaf17A = Column(SmallInteger)
    PlanPosLeaf18A = Column(SmallInteger)
    PlanPosLeaf19A = Column(SmallInteger)
    PlanPosLeaf20A = Column(SmallInteger)
    PlanPosLeaf21A = Column(SmallInteger)
    PlanPosLeaf22A = Column(SmallInteger)
    PlanPosLeaf23A = Column(SmallInteger)
    PlanPosLeaf24A = Column(SmallInteger)
    PlanPosLeaf25A = Column(SmallInteger)
    PlanPosLeaf26A = Column(SmallInteger)
    PlanPosLeaf27A = Column(SmallInteger)
    PlanPosLeaf28A = Column(SmallInteger)
    PlanPosLeaf29A = Column(SmallInteger)
    PlanPosLeaf30A = Column(SmallInteger)
    PlanPosLeaf31A = Column(SmallInteger)
    PlanPosLeaf32A = Column(SmallInteger)
    PlanPosLeaf33A = Column(SmallInteger)
    PlanPosLeaf34A = Column(SmallInteger)
    PlanPosLeaf35A = Column(SmallInteger)
    PlanPosLeaf36A = Column(SmallInteger)
    PlanPosLeaf37A = Column(SmallInteger)
    PlanPosLeaf38A = Column(SmallInteger)
    PlanPosLeaf39A = Column(SmallInteger)
    PlanPosLeaf40A = Column(SmallInteger)
    PlanPosLeaf41A = Column(SmallInteger)
    PlanPosLeaf42A = Column(SmallInteger)
    PlanPosLeaf43A = Column(SmallInteger)
    PlanPosLeaf44A = Column(SmallInteger)
    PlanPosLeaf45A = Column(SmallInteger)
    PlanPosLeaf46A = Column(SmallInteger)
    PlanPosLeaf47A = Column(SmallInteger)
    PlanPosLeaf48A = Column(SmallInteger)
    PlanPosLeaf49A = Column(SmallInteger)
    PlanPosLeaf50A = Column(SmallInteger)
    PlanPosLeaf51A = Column(SmallInteger)
    PlanPosLeaf52A = Column(SmallInteger)
    PlanPosLeaf53A = Column(SmallInteger)
    PlanPosLeaf54A = Column(SmallInteger)
    PlanPosLeaf55A = Column(SmallInteger)
    PlanPosLeaf56A = Column(SmallInteger)
    PlanPosLeaf57A = Column(SmallInteger)
    PlanPosLeaf58A = Column(SmallInteger)
    PlanPosLeaf59A = Column(SmallInteger)
    PlanPosLeaf60A = Column(SmallInteger)
    PlanPosLeaf61A = Column(SmallInteger)
    PlanPosLeaf62A = Column(SmallInteger)
    PlanPosLeaf63A = Column(SmallInteger)
    PlanPosLeaf64A = Column(SmallInteger)
    PlanPosLeaf65A = Column(SmallInteger)
    PlanPosLeaf66A = Column(SmallInteger)
    PlanPosLeaf67A = Column(SmallInteger)
    PlanPosLeaf68A = Column(SmallInteger)
    PlanPosLeaf69A = Column(SmallInteger)
    PlanPosLeaf70A = Column(SmallInteger)
    PlanPosLeaf71A = Column(SmallInteger)
    PlanPosLeaf72A = Column(SmallInteger)
    PlanPosLeaf73A = Column(SmallInteger)
    PlanPosLeaf74A = Column(SmallInteger)
    PlanPosLeaf75A = Column(SmallInteger)
    PlanPosLeaf76A = Column(SmallInteger)
    PlanPosLeaf77A = Column(SmallInteger)
    PlanPosLeaf78A = Column(SmallInteger)
    PlanPosLeaf79A = Column(SmallInteger)
    PlanPosLeaf80A = Column(SmallInteger)
    PlanPosLeaf1B = Column(SmallInteger)
    PlanPosLeaf2B = Column(SmallInteger)
    PlanPosLeaf3B = Column(SmallInteger)
    PlanPosLeaf4B = Column(SmallInteger)
    PlanPosLeaf5B = Column(SmallInteger)
    PlanPosLeaf6B = Column(SmallInteger)
    PlanPosLeaf7B = Column(SmallInteger)
    PlanPosLeaf8B = Column(SmallInteger)
    PlanPosLeaf9B = Column(SmallInteger)
    PlanPosLeaf10B = Column(SmallInteger)
    PlanPosLeaf11B = Column(SmallInteger)
    PlanPosLeaf12B = Column(SmallInteger)
    PlanPosLeaf13B = Column(SmallInteger)
    PlanPosLeaf14B = Column(SmallInteger)
    PlanPosLeaf15B = Column(SmallInteger)
    PlanPosLeaf16B = Column(SmallInteger)
    PlanPosLeaf17B = Column(SmallInteger)
    PlanPosLeaf18B = Column(SmallInteger)
    PlanPosLeaf19B = Column(SmallInteger)
    PlanPosLeaf20B = Column(SmallInteger)
    PlanPosLeaf21B = Column(SmallInteger)
    PlanPosLeaf22B = Column(SmallInteger)
    PlanPosLeaf23B = Column(SmallInteger)
    PlanPosLeaf24B = Column(SmallInteger)
    PlanPosLeaf25B = Column(SmallInteger)
    PlanPosLeaf26B = Column(SmallInteger)
    PlanPosLeaf27B = Column(SmallInteger)
    PlanPosLeaf28B = Column(SmallInteger)
    PlanPosLeaf29B = Column(SmallInteger)
    PlanPosLeaf30B = Column(SmallInteger)
    PlanPosLeaf31B = Column(SmallInteger)
    PlanPosLeaf32B = Column(SmallInteger)
    PlanPosLeaf33B = Column(SmallInteger)
    PlanPosLeaf34B = Column(SmallInteger)
    PlanPosLeaf35B = Column(SmallInteger)
    PlanPosLeaf36B = Column(SmallInteger)
    PlanPosLeaf37B = Column(SmallInteger)
    PlanPosLeaf38B = Column(SmallInteger)
    PlanPosLeaf39B = Column(SmallInteger)
    PlanPosLeaf40B = Column(SmallInteger)
    PlanPosLeaf41B = Column(SmallInteger)
    PlanPosLeaf42B = Column(SmallInteger)
    PlanPosLeaf43B = Column(SmallInteger)
    PlanPosLeaf44B = Column(SmallInteger)
    PlanPosLeaf45B = Column(SmallInteger)
    PlanPosLeaf46B = Column(SmallInteger)
    PlanPosLeaf47B = Column(SmallInteger)
    PlanPosLeaf48B = Column(SmallInteger)
    PlanPosLeaf49B = Column(SmallInteger)
    PlanPosLeaf50B = Column(SmallInteger)
    PlanPosLeaf51B = Column(SmallInteger)
    PlanPosLeaf52B = Column(SmallInteger)
    PlanPosLeaf53B = Column(SmallInteger)
    PlanPosLeaf54B = Column(SmallInteger)
    PlanPosLeaf55B = Column(SmallInteger)
    PlanPosLeaf56B = Column(SmallInteger)
    PlanPosLeaf57B = Column(SmallInteger)
    PlanPosLeaf58B = Column(SmallInteger)
    PlanPosLeaf59B = Column(SmallInteger)
    PlanPosLeaf60B = Column(SmallInteger)
    PlanPosLeaf61B = Column(SmallInteger)
    PlanPosLeaf62B = Column(SmallInteger)
    PlanPosLeaf63B = Column(SmallInteger)
    PlanPosLeaf64B = Column(SmallInteger)
    PlanPosLeaf65B = Column(SmallInteger)
    PlanPosLeaf66B = Column(SmallInteger)
    PlanPosLeaf67B = Column(SmallInteger)
    PlanPosLeaf68B = Column(SmallInteger)
    PlanPosLeaf69B = Column(SmallInteger)
    PlanPosLeaf70B = Column(SmallInteger)
    PlanPosLeaf71B = Column(SmallInteger)
    PlanPosLeaf72B = Column(SmallInteger)
    PlanPosLeaf73B = Column(SmallInteger)
    PlanPosLeaf74B = Column(SmallInteger)
    PlanPosLeaf75B = Column(SmallInteger)
    PlanPosLeaf76B = Column(SmallInteger)
    PlanPosLeaf77B = Column(SmallInteger)
    PlanPosLeaf78B = Column(SmallInteger)
    PlanPosLeaf79B = Column(SmallInteger)
    PlanPosLeaf80B = Column(SmallInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PatientSupportAngle = Column(Float(53))
    IsoCenterPositionX = Column(Float(53))
    IsoCenterPositionY = Column(Float(53))
    IsoCenterPositionZ = Column(Float(53))

    ExternalFieldCommon = relationship(u'ExternalFieldCommon')


class ControlPointProton(ControlPoint):
    __tablename__ = 'ControlPointProton'

    ControlPointSer = Column(ForeignKey(u'ControlPoint.ControlPointSer'), primary_key=True)
    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), index=True)
    SnoutPosition = Column(Float(53))
    NozzleEquivalentRange = Column(Float(53))
    PeakRange = Column(Float(53))
    NumberOfSpots = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    NumberOfPaintings = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SpotSizeX = Column(Float(53))
    SpotSizeY = Column(Float(53))
    RangeMod1InterruptStart = Column(Float(53))
    RangeMod1InterruptStop = Column(Float(53))
    RangeMod1WeTStart = Column(Float(53))
    RangeMod1WeTStop = Column(Float(53))
    RangeMod1DicomSeqNumb = Column(Integer)
    RangeMod2InterruptStart = Column(Float(53))
    RangeMod2InterruptStop = Column(Float(53))
    RangeMod2WeTStart = Column(Float(53))
    RangeMod2WeTStop = Column(Float(53))
    RangeMod2DicomSeqNumb = Column(Integer)
    IsocenterToRangeMod1Dist = Column(Float(53))
    IsocenterToRangeMod2Dist = Column(Float(53))
    LateralSpreadDev1Setting = Column(Unicode(64))
    LateralSpreadDev1WeT = Column(Float(53))
    IsoToLatSpreadDev1Dist = Column(Float(53))
    LatSpreadDev1DcmSeqNumb = Column(Integer)
    LateralSpreadDev2Setting = Column(Unicode(64))
    LateralSpreadDev2WeT = Column(Float(53))
    IsoToLatSpreadDev2Dist = Column(Float(53))
    LatSpreadDev2DcmSeqNumb = Column(Integer)
    LateralSpreadDev3Setting = Column(Unicode(64))
    LateralSpreadDev3WeT = Column(Float(53))
    IsoToLatSpreadDev3Dist = Column(Float(53))
    LatSpreadDev3DcmSeqNumb = Column(Integer)
    RangeShifter1Setting = Column(Unicode(64))
    RangeShifter1WeT = Column(Float(53))
    IsoToRangeShifter1Dist = Column(Float(53))
    RangeShifter1DcmSeqNumb = Column(Integer)
    RangeShifter2Setting = Column(Unicode(64))
    RangeShifter2WeT = Column(Float(53))
    IsoToRangeShifter2Dist = Column(Float(53))
    RangeShifter2DcmSeqNumb = Column(Integer)
    RangeShifter3Setting = Column(Unicode(64))
    RangeShifter3WeT = Column(Float(53))
    IsoToRangeShifter3Dist = Column(Float(53))
    RangeShifter3DcmSeqNumb = Column(Integer)
    UserPreselectEnergy = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ApertureShape = Column(LargeBinary)

    AddOn = relationship(u'AddOn')


class Course(Base):
    __tablename__ = 'Course'
    __table_args__ = (
        Index('XIE1Course', 'PatientSer', 'CourseSer'),
        Index('XIE2Course', 'PatientSer', 'CourseId')
    )

    CourseSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False)
    CourseId = Column(Unicode(16), nullable=False)
    StartDateTime = Column(DateTime)
    ClinicalStatus = Column(Unicode(16), nullable=False, server_default=text("""\

CREATE DEFAULT [dbo].[VDT_CLINICALSTATUS_DEF]
	AS 'ACTIVE'"""))
    CompletedByUserName = Column(Unicode(32))
    CompletedDateTime = Column(DateTime)
    Comment = Column(Unicode(254))
    ClinicalProtocolDir = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    TransactionId = Column(String(255, u'Latin1_General_BIN2'))

    Patient = relationship(u'Patient')


class CoursePrintInfo(Course):
    __tablename__ = 'CoursePrintInfo'

    CourseSer = Column(ForeignKey(u'Course.CourseSer'), primary_key=True)
    LastPrintedPageNum = Column(Integer)
    LastPrintedLineNum = Column(Integer)
    SessionsPrintedLineNum = Column(Unicode(254))
    SummaryPrintDate = Column(DateTime)
    PatientHisPrintDate = Column(DateTime)
    ChartFormat = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class CourseDiagnosi(Base):
    __tablename__ = 'CourseDiagnosis'
    __table_args__ = (
        Index('XAKCourseDiagnosis', 'DiagnosisSer', 'CourseSer', unique=True),
    )

    CourseSer = Column(ForeignKey(u'Course.CourseSer'), primary_key=True, nullable=False)
    DiagnosisSer = Column(BigInteger, primary_key=True, nullable=False)
    CacheKeySer = Column(BigInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Course = relationship(u'Course')


class Credit(Base):
    __tablename__ = 'Credit'

    CreditSer = Column(BigInteger, primary_key=True)
    CreditRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCaptureSer = Column(ForeignKey(u'ActivityCapture.ActivityCaptureSer'), nullable=False, index=True)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActInstProcCodeSer = Column(ForeignKey(u'ActInstProcCode.ActInstProcCodeSer'), nullable=False, index=True)
    ActInstProcCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    CreditedBy = Column(Unicode(32))
    CreditedDateTime = Column(DateTime)
    ExportedBy = Column(Unicode(32))
    ExportedDateTime = Column(DateTime)
    Note = Column(Unicode(254))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActInstProcCode = relationship(u'ActInstProcCode')
    ActivityCapture = relationship(u'ActivityCapture')


class CreditMH(Base):
    __tablename__ = 'CreditMH'

    CreditSer = Column(ForeignKey(u'Credit.CreditSer'), primary_key=True, nullable=False)
    CreditRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCaptureSer = Column(BigInteger, nullable=False, index=True)
    ActivityCaptureRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActInstProcCodeSer = Column(BigInteger, nullable=False)
    ActInstProcCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    CreditedBy = Column(Unicode(32))
    CreditedDateTime = Column(DateTime)
    ExportedBy = Column(Unicode(32))
    ExportedDateTime = Column(DateTime)
    Note = Column(Unicode(254))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Credit = relationship(u'Credit')


class DBHistory(Base):
    __tablename__ = 'DBHistory'

    DBHistorySer = Column(BigInteger, primary_key=True)
    EventType = Column(Unicode(32), nullable=False)
    StartingRelease = Column(Unicode(32))
    EndingRelease = Column(Unicode(32))
    Description = Column(Unicode(254))
    UpgrVersion = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))


class DCObjectPointerSery(Base):
    __tablename__ = 'DCObjectPointerSeries'

    DCObjectPointerSeriesSer = Column(BigInteger, primary_key=True)
    DCObjectPointerStudySer = Column(ForeignKey(u'DCObjectPointerStudy.DCObjectPointerStudySer'), nullable=False, index=True)
    Modality = Column(Unicode(16))
    SeriesUID = Column(Unicode(64), nullable=False)

    DCObjectPointerStudy = relationship(u'DCObjectPointerStudy')


class DCObjectPointerStudy(Base):
    __tablename__ = 'DCObjectPointerStudy'

    DCObjectPointerStudySer = Column(BigInteger, primary_key=True)
    StudyUID = Column(Unicode(64), nullable=False)


class DCObjectTrackingInfo(Base):
    __tablename__ = 'DCObjectTrackingInfo'

    DCObjectTrackingInfoSer = Column(BigInteger, primary_key=True)
    ObjectPointerSer = Column(ForeignKey(u'ObjectPointer.ObjectPointerSer'), nullable=False, index=True)
    TrackingInformationSer = Column(ForeignKey(u'TrackingInformation.TrackingInformationSer'), nullable=False, index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ObjectPointer = relationship(u'ObjectPointer')
    TrackingInformation = relationship(u'TrackingInformation')


class DCTransferSyntax(Base):
    __tablename__ = 'DCTransferSyntax'

    DCTransferSyntaxSer = Column(BigInteger, primary_key=True)
    DCTransferSyntaxUID = Column(Unicode(64), nullable=False, unique=True)


class DICOMCodeMeaning(Base):
    __tablename__ = 'DICOMCodeMeaning'
    __table_args__ = (
        Index('XAK1DICOMCodeMeaning', 'DICOMCodeValueSer', 'Meaning', 'LanguageId', unique=True),
    )

    DICOMCodeMeaningSer = Column(BigInteger, primary_key=True)
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), nullable=False)
    Meaning = Column(Unicode(64), nullable=False)
    LanguageId = Column(Unicode(16), nullable=False)

    DICOMCodeValue = relationship(u'DICOMCodeValue')


class DICOMCodeScheme(Base):
    __tablename__ = 'DICOMCodeScheme'
    __table_args__ = (
        Index('XAK1DICOMCodeScheme', 'Designator', 'Version', unique=True),
    )

    DICOMCodeSchemeSer = Column(BigInteger, primary_key=True)
    Designator = Column(Unicode(16), nullable=False)
    Version = Column(Unicode(16))
    Registry = Column(Unicode(64))
    UID = Column(Unicode(64))
    ExternalID = Column(UnicodeText(1073741823))
    CommonName = Column(UnicodeText(1073741823))
    ResponsibleOrganization = Column(UnicodeText(1073741823))


class DICOMCodeValue(Base):
    __tablename__ = 'DICOMCodeValue'
    __table_args__ = (
        Index('XAK1DICOMCodeValue', 'DICOMCodeSchemeSer', 'Value', unique=True),
    )

    DICOMCodeValueSer = Column(BigInteger, primary_key=True)
    DICOMCodeSchemeSer = Column(ForeignKey(u'DICOMCodeScheme.DICOMCodeSchemeSer'), nullable=False)
    Value = Column(Unicode(16), nullable=False)
    Category = Column(Unicode(64))

    DICOMCodeScheme = relationship(u'DICOMCodeScheme')


class DVH(Base):
    __tablename__ = 'DVH'

    DVHSer = Column(BigInteger, primary_key=True)
    PlanSumSer = Column(ForeignKey(u'PlanSum.PlanSumSer'), index=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), index=True)
    Structures = Column(UnicodeText(1073741823))
    StructuresLen = Column(Integer, nullable=False)
    DVHDisplayFlags = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PlanSetup = relationship(u'PlanSetup')
    PlanSum = relationship(u'PlanSum')


class DeliverySetupDevice(Base):
    __tablename__ = 'DeliverySetupDevice'

    DeliverySetupDeviceSer = Column(BigInteger, primary_key=True)
    DeliverySetupDeviceId = Column(Unicode(16), nullable=False)
    DeliverySetupDeviceName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    DeviceType = Column(Unicode(64), nullable=False)
    DeviceCode = Column(Unicode(32))
    DeviceCategory = Column(Unicode(16), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    GeometricDefinition = Column(UnicodeText(1073741823), nullable=False)
    GeometricDefinitionLen = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class DeliverySetupDeviceMachine(Base):
    __tablename__ = 'DeliverySetupDeviceMachine'

    DeliverySetupDeviceSer = Column(ForeignKey(u'DeliverySetupDevice.DeliverySetupDeviceSer'), primary_key=True, nullable=False)
    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger, nullable=False, unique=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    DeliverySetupDevice = relationship(u'DeliverySetupDevice')
    Machine = relationship(u'Machine')


class DemExternalBeam(Base):
    __tablename__ = 'DemExternalBeam'

    DemExternalBeamSer = Column(BigInteger, primary_key=True)
    DemGroupSer = Column(ForeignKey(u'DemGroup.DemGroupSer'), nullable=False, index=True)
    EnergyModeSer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), nullable=False, index=True)
    PrimaryFluenceModeSer = Column(ForeignKey(u'PrimaryFluenceMode.AddOnSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    TechniqueSer = Column(ForeignKey(u'Technique.TechniqueSer'), index=True)

    DemGroup = relationship(u'DemGroup')
    EnergyMode = relationship(u'EnergyMode')
    PrimaryFluenceMode = relationship(u'PrimaryFluenceMode')
    Technique = relationship(u'Technique')


class DemGroup(Base):
    __tablename__ = 'DemGroup'

    DemGroupSer = Column(BigInteger, primary_key=True)
    DemGroupId = Column(Unicode(16), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class Department(Base):
    __tablename__ = 'Department'
    __table_args__ = (
        Index('XAK1Department', 'HospitalSer', 'DepartmentId', unique=True),
    )

    DepartmentSer = Column(BigInteger, primary_key=True)
    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), nullable=False)
    DepartmentId = Column(Unicode(16), nullable=False)
    DepartmentName = Column(Unicode(64))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Hospital = relationship(u'Hospital')


class DepartmentPttrnDetail(Base):
    __tablename__ = 'DepartmentPttrnDetails'

    DeptPttrnDetailSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    PatternDayOfWeek = Column(Integer)
    PatternStartTime = Column(DateTime)
    PatternEndTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')


class DeptGrpAssociation(Base):
    __tablename__ = 'DeptGrpAssociation'
    __table_args__ = (
        Index('XAK1DeptGrpAssociation', 'ResourceGroupSer', 'DepartmentSer', unique=True),
    )

    DeptGrpAssociationSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), nullable=False, index=True)
    ResourceGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')
    ResourceGroup = relationship(u'ResourceGroup')


class DerivedImageCode(Base):
    __tablename__ = 'DerivedImageCode'

    DerivedImageCodeSer = Column(BigInteger, primary_key=True)
    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), nullable=False, index=True)
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), nullable=False, index=True)

    DICOMCodeValue = relationship(u'DICOMCodeValue')
    Slouse = relationship(u'Slouse')


class DerivedInstanceUID(Base):
    __tablename__ = 'DerivedInstanceUID'

    DerivedInstanceUIDSer = Column(BigInteger, primary_key=True)
    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), nullable=False, index=True)
    InstanceUID = Column(Unicode(64), nullable=False, index=True)

    Slouse = relationship(u'Slouse')


class DiagnosisStage(Base):
    __tablename__ = 'DiagnosisStage'
    __table_args__ = (
        Index('XIE1DiagnosisStage', 'DiagnosisTableName', 'DiagnosisCode'),
    )

    DiagnosisStageSer = Column(BigInteger, primary_key=True)
    DiagnosisTableName = Column(Unicode(64), nullable=False)
    DiagnosisCode = Column(Unicode(16), nullable=False)
    DiagnosisStage = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class DicomLocation(Base):
    __tablename__ = 'DicomLocation'

    DicomLocationSer = Column(BigInteger, primary_key=True)
    MediaFileSetID = Column(Unicode(16))
    MediaFileSetUID = Column(Unicode(64))
    AETitle = Column(Unicode(16))


class Directive(Base):
    __tablename__ = 'Directive'

    DirectiveSer = Column(BigInteger, primary_key=True)
    Description = Column(Unicode(254), nullable=False)
    ActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ConfirmFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class DoctorBillingService(Base):
    __tablename__ = 'DoctorBillingService'

    BillingServiceSer = Column(ForeignKey(u'BillingService.BillingServiceSer'), primary_key=True, nullable=False)
    ResourceSer = Column(ForeignKey(u'Doctor.ResourceSer'), primary_key=True, nullable=False, index=True)
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    BillingService = relationship(u'BillingService')
    Doctor = relationship(u'Doctor')


class DoseContribution(Base):
    __tablename__ = 'DoseContribution'

    RTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), primary_key=True, nullable=False)
    RefPointSer = Column(ForeignKey(u'RefPoint.RefPointSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    DosePerFraction = Column(Float(53))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DicomSeqNumber = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DICOMSEQNBR_DEF]
	AS -999999999"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    RTPlan = relationship(u'RTPlan')
    RefPoint = relationship(u'RefPoint')


class DoseCorrectionLog(Base):
    __tablename__ = 'DoseCorrectionLog'

    DoseCorrectionLogSer = Column(BigInteger, primary_key=True)
    CorrectionDateTime = Column(DateTime, nullable=False, index=True)
    CorrectionNote = Column(Unicode(254))
    PrintFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class DoseMatrix(Base):
    __tablename__ = 'DoseMatrix'

    DoseMatrixSer = Column(BigInteger, primary_key=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    DoseMatrixId = Column(Unicode(16), nullable=False)
    DoseMatrixName = Column(Unicode(64))
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    SizeX = Column(Integer)
    SizeY = Column(Integer)
    SizeZ = Column(Integer)
    ResX = Column(Float(53))
    ResY = Column(Float(53))
    ResZ = Column(Float(53))
    Transformation = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    DoseMatrixFile = Column(Unicode(254))
    DoseDistributionType = Column(Unicode(32))
    Unit = Column(Unicode(16))
    Scaler = Column(Float(53))
    Location = Column(Unicode(16))
    Medium = Column(Unicode(32))
    IsodoseLevels = Column(LargeBinary)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    CreationNote = Column(Unicode(254))
    Offset = Column(Integer)
    BitsAllocated = Column(Integer, nullable=False)
    DoseUID = Column(Unicode(64), nullable=False, unique=True)
    DoseComment = Column(Unicode(64))
    EquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), index=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), index=True)
    FieldVariationSer = Column(ForeignKey(u'FieldVariation.FieldVariationSer'), index=True)

    Equipment = relationship(u'Equipment')
    FieldVariation = relationship(u'FieldVariation')
    Patient = relationship(u'Patient')
    PlanSetup = relationship(u'PlanSetup')
    Radiation = relationship(u'Radiation')
    Series = relationship(u'Series')


class DoseRate(Base):
    __tablename__ = 'DoseRate'
    __table_args__ = (
        Index('XAK1DoseRate', 'EnergyModeSer', 'DoseRateValue', 'PrimaryFluenceModeSer', unique=True),
    )

    DoseRateSer = Column(BigInteger, primary_key=True)
    EnergyModeSer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), nullable=False)
    DoseRateValue = Column(Integer, nullable=False)
    RepRate = Column(Integer)
    DefaultFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    PrimaryFluenceModeSer = Column(ForeignKey(u'PrimaryFluenceMode.AddOnSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DefPortalImagingFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    LowPortalImagingFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ConeBeamFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    EnergyMode = relationship(u'EnergyMode')
    PrimaryFluenceMode = relationship(u'PrimaryFluenceMode')


class DoseTemplate(Base):
    __tablename__ = 'DoseTemplate'

    DoseTemplateSer = Column(BigInteger, primary_key=True)
    DoseTemplateId = Column(Unicode(16), nullable=False, unique=True)
    DoseTemplateName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    Comment = Column(Unicode(254))
    IsodoseLevels = Column(LargeBinary)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class DosimetricDatum(Base):
    __tablename__ = 'DosimetricData'
    __table_args__ = (
        Index('XAK1DosimetricData', 'AddOnMaterialSer', 'EnergyModeSer', 'PrimaryFluenceModeSer', unique=True),
    )

    DosimetricDataSer = Column(BigInteger, primary_key=True)
    AddOnMaterialSer = Column(ForeignKey(u'AddOnMaterial.AddOnMaterialSer'), nullable=False)
    EnergyModeSer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), nullable=False, index=True)
    PrimaryFluenceModeSer = Column(ForeignKey(u'PrimaryFluenceMode.AddOnSer'), index=True)
    TransmissionFact = Column(Float(53))
    LinearAttenFact = Column(Float(53))
    WedgeFactor = Column(Float(53))
    DosimetricLeafGap = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AddOnMaterial = relationship(u'AddOnMaterial')
    EnergyMode = relationship(u'EnergyMode')
    PrimaryFluenceMode = relationship(u'PrimaryFluenceMode')


class DrillBit(Base):
    __tablename__ = 'DrillBit'

    DrillBitSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'MillingMachine.ResourceSer'), nullable=False, index=True)
    Diameter = Column(Float(53))
    Description = Column(Unicode(254))
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    MillingMachine = relationship(u'MillingMachine')


class Employer(Base):
    __tablename__ = 'Employer'
    __table_args__ = (
        Index('XIE1Employer', 'EmployerName', 'DivisionName'),
    )

    EmployerSer = Column(BigInteger, primary_key=True)
    AddressSer = Column(ForeignKey(u'Address.AddressSer'), index=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    EmployerId = Column(Unicode(16), nullable=False, unique=True)
    EmployerName = Column(Unicode(64))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    DivisionName = Column(Unicode(64))
    POCName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    SchoolFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Addres = relationship(u'Addres')
    Patient = relationship(u'Patient')


class EnergyMode(Base):
    __tablename__ = 'EnergyMode'
    __table_args__ = (
        Index('XAK1EnergyMode', 'ResourceSer', 'RadiationType', 'Energy', unique=True),
    )

    EnergyModeSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'ExternalBeam.ResourceSer'), nullable=False)
    RadiationType = Column(Unicode(16), nullable=False)
    Energy = Column(Integer, nullable=False)
    MaxEnergy = Column(Integer)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    MinDoseRate = Column(Integer)
    MaxDoseRate = Column(Integer)
    DefaultFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DisplayCode = Column(Unicode(32))
    InternalCode = Column(Integer)
    LevelCode = Column(Integer)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ExternalBeam = relationship(u'ExternalBeam', primaryjoin='EnergyMode.ResourceSer == ExternalBeam.ResourceSer')


class Equipment(Base):
    __tablename__ = 'Equipment'
    __table_args__ = (
        Index('XAK1Equipment', 'Manufacturer', 'InstitutionName', 'StationName', 'DepartmentName', 'ModelName', 'DeviceSerialNumber', 'SoftwareVersion', unique=True),
    )

    EquipmentSer = Column(BigInteger, primary_key=True)
    Manufacturer = Column(Unicode(64))
    InstitutionName = Column(Unicode(64))
    StationName = Column(Unicode(16))
    DepartmentName = Column(Unicode(64))
    ModelName = Column(Unicode(64))
    DeviceSerialNumber = Column(Unicode(64))
    SoftwareVersion = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ErrorMsg(Base):
    __tablename__ = 'ErrorMsg'

    ErrorCode = Column(Integer, primary_key=True, nullable=False)
    LanguageId = Column(ForeignKey(u'LanguageLookup.LanguageId'), primary_key=True, nullable=False, index=True)
    ErrorLabel = Column(Unicode(32), nullable=False, index=True)
    ErrorMessage = Column(Unicode(254), nullable=False)
    ErrorDescription = Column(Unicode(254))

    LanguageLookup = relationship(u'LanguageLookup')


class ExternalIntegration(Base):
    __tablename__ = 'ExternalIntegration'

    ExternalIntegrationSer = Column(BigInteger, primary_key=True)
    VarisType = Column(Unicode(30), nullable=False)
    VarisSer = Column(BigInteger, nullable=False)
    ExternalApplication = Column(Unicode(32), nullable=False)
    ExternalID = Column(Unicode(512), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    AuthenticationID = Column(Unicode(128))
    EffectiveDate = Column(DateTime)
    AdditionalInfo = Column(Unicode(1024))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class FieldAddOn(Base):
    __tablename__ = 'FieldAddOn'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True, nullable=False)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    SlotSer = Column(ForeignKey(u'Slot.SlotSer'), index=True)
    CustomCode = Column(Unicode(64))
    DicomSeqNumber = Column(Integer)
    UserPreselection = Column(SmallInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    AddOn = relationship(u'AddOn')
    ExternalFieldCommon = relationship(u'ExternalFieldCommon')
    Slot = relationship(u'Slot')


class FieldPhoto(Base):
    __tablename__ = 'FieldPhoto'

    PhotoSer = Column(ForeignKey(u'Photo.PhotoSer'), primary_key=True, nullable=False)
    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DisplaySequence = Column(Integer, nullable=False)

    Photo = relationship(u'Photo')
    Radiation = relationship(u'Radiation')


class FieldStructure(Base):
    __tablename__ = 'FieldStructure'
    __table_args__ = (
        Index('XIE3FieldStructure', 'RadiationSer', 'StructureSer'),
    )

    FieldStructureSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), nullable=False)
    StructureSer = Column(ForeignKey(u'Structure.StructureSer'), nullable=False, index=True)
    StructUsageType = Column(Unicode(16))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    BlockSer = Column(ForeignKey(u'Block.BlockSer'), index=True)

    Block = relationship(u'Block')
    ExternalFieldCommon = relationship(u'ExternalFieldCommon')
    Structure = relationship(u'Structure')


class FieldVariation(Base):
    __tablename__ = 'FieldVariation'

    FieldVariationSer = Column(BigInteger, primary_key=True)
    PlanVariationSer = Column(ForeignKey(u'PlanVariation.PlanVariationSer'), nullable=False, index=True)
    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PlanVariation = relationship(u'PlanVariation')
    Radiation = relationship(u'Radiation')


class FileLocation(Base):
    __tablename__ = 'FileLocation'

    FileLocationSer = Column(BigInteger, primary_key=True)
    FileName = Column(Unicode(254), nullable=False, unique=True)
    ServerName = Column(Unicode(254), nullable=False)
    DriveName = Column(Unicode(254), nullable=False)
    FolderName1 = Column(Unicode(254))
    FolderName2 = Column(Unicode(254))
    FolderName3 = Column(Unicode(254))
    FolderName4 = Column(Unicode(254))
    FileExtension = Column(Unicode(16))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))


class GraphicAnnotation(Base):
    __tablename__ = 'GraphicAnnotation'

    GraphicAnnotationSer = Column(BigInteger, primary_key=True)
    GraphicAnnotationTypeSer = Column(ForeignKey(u'GraphicAnnotationType.GraphicAnnotationTypeSer'), nullable=False, index=True)
    ImageSer = Column(ForeignKey(u'Image.ImageSer'), nullable=False, index=True)
    GraphicAnnotationId = Column(Unicode(16), nullable=False)
    GraphicAnnotationName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    MaterialSer = Column(ForeignKey(u'Material.MaterialSer'), index=True)
    FileName = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    GraphicAnnotationType = relationship(u'GraphicAnnotationType')
    Image = relationship(u'Image')
    Material = relationship(u'Material')


class GraphicAnnotationType(Base):
    __tablename__ = 'GraphicAnnotationType'

    GraphicAnnotationTypeSer = Column(BigInteger, primary_key=True)
    GraphicAnnotationTypeIndex = Column(Integer, nullable=False)
    MaterialSer = Column(ForeignKey(u'Material.MaterialSer'), nullable=False, index=True)
    CurveLabel = Column(Unicode(16), nullable=False)
    UserSelectable = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Material = relationship(u'Material')


class GroupResource(Base):
    __tablename__ = 'GroupResource'
    __table_args__ = (
        Index('XAK1GroupResource', 'ResourceSer', 'ResourceGroupSer', unique=True),
    )

    GroupResourceSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), nullable=False)
    ResourceGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ResourceGroup = relationship(u'ResourceGroup')
    Resource = relationship(u'Resource')


class Hospital(Base):
    __tablename__ = 'Hospital'

    HospitalSer = Column(BigInteger, primary_key=True)
    HospitalName = Column(Unicode(64), nullable=False, unique=True)
    AddressSer = Column(ForeignKey(u'Address.AddressSer'), index=True)
    HospitalLocation = Column(Unicode(64), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    Organization = Column(Unicode(64))
    WebAddress = Column(Unicode(64))
    Logo = Column(LargeBinary)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    MailServerAddress = Column(Unicode(64))

    Addres = relationship(u'Addres')


class Image(Base):
    __tablename__ = 'Image'
    __table_args__ = (
        Index('XIE7Image', 'ImageSer', 'PatientSer', 'ImageType', 'Status', 'CreationDate'),
        Index('XIE5Image', 'Image4DSer', 'ImageSer'),
        Index('XIE1Image', 'SeriesSer', 'ImageId'),
        Index('XIE6Image', 'SeriesSer', 'ImageSer')
    )

    ImageSer = Column(BigInteger, primary_key=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False)
    ImageId = Column(Unicode(16), nullable=False)
    ImageName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    StatusDate = Column(DateTime, nullable=False)
    StatusUserName = Column(Unicode(32), nullable=False)
    ImageType = Column(Unicode(30))
    Status = Column(Unicode(64), nullable=False)
    VolumetricPixelOffset = Column(Integer)
    ProcessedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DefaultProcessingSer = Column(ForeignKey(u'Processing.ProcessingSer'), index=True)
    OtherProcessingSer = Column(ForeignKey(u'Processing.ProcessingSer'), index=True)
    GeometricParentSer = Column(ForeignKey(u'Image.ImageSer'), index=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    ImageSizeX = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ImageSizeY = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ImageSizeZ = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ImageResX = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    ImageResY = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    ImageResZ = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    InverseSliceOrder = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    FocusX = Column(Float(53))
    FocusY = Column(Float(53))
    FocusZ = Column(Float(53))
    Comment = Column(Unicode(254))
    PatientOrientation = Column(Unicode(16))
    UsageType = Column(Unicode(64))
    ActWindow = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ActLevel = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    VolumetricPixelSlope = Column(Float(53))
    PixelUnit = Column(Unicode(32))
    ImageNotesLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ImageNotes = Column(UnicodeText(1073741823))
    Transformation = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    VolumeTransformation = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    UserOrigin = Column(BINARY(24))
    UserOriginComment = Column(Unicode(254))
    DisplayTransformation = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ProcessingDefinition = Column(UnicodeText(1073741823))
    ProcessingDefinitionLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    FractionNumber = Column(Integer)
    RefDicomSeqNumber = Column(Integer)
    Image4DSer = Column(ForeignKey(u'Image4D.Image4DSer'))
    Flags4D = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Processing = relationship(u'Processing', primaryjoin='Image.DefaultProcessingSer == Processing.ProcessingSer')
    parent = relationship(u'Image', remote_side=[ImageSer])
    Image4D = relationship(u'Image4D')
    Processing1 = relationship(u'Processing', primaryjoin='Image.OtherProcessingSer == Processing.ProcessingSer')
    Patient = relationship(u'Patient')
    Series = relationship(u'Series')


class Image4D(Base):
    __tablename__ = 'Image4D'
    __table_args__ = (
        Index('XIE1Image4D', 'PatientSer', 'Image4DSer'),
    )

    Image4DSer = Column(BigInteger, primary_key=True)
    Image4DId = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_EMPTYSTRING_DEF]
	AS ''"""))
    Image4DName = Column(Unicode(64), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_EMPTYSTRING_DEF]
	AS ''"""))
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')


class ImageMatchResult(Base):
    __tablename__ = 'ImageMatchResult'

    ImageSer = Column(ForeignKey(u'Image.ImageSer'), primary_key=True, nullable=False)
    MatchResultSer = Column(ForeignKey(u'MatchResult.MatchResultSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    ReferenceFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Image = relationship(u'Image')
    MatchResult = relationship(u'MatchResult')


class ImageSlouse(Base):
    __tablename__ = 'ImageSlice'

    ImageSer = Column(ForeignKey(u'Image.ImageSer'), primary_key=True, nullable=False)
    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Image = relationship(u'Image')
    Slouse = relationship(u'Slouse')


class ImportExportColumn(Base):
    __tablename__ = 'ImportExportColumn'

    TableName = Column(ForeignKey(u'ImportExportTable.TableName'), primary_key=True, nullable=False, index=True)
    ColumnName = Column(Unicode(64), primary_key=True, nullable=False)
    CopyOnExport = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    IncludeInDuplicateCheck = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    IncludeInConflictCheck = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    UseInRowMatching = Column(Unicode(32))
    RenameOnConflict = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    LookupTableListSelector = Column(Unicode(32))
    ValueOnImport = Column(Unicode(64))
    SpecialValue = Column(Unicode(32))
    InsertionParameterName = Column(Unicode(64))

    ImportExportTable = relationship(u'ImportExportTable')


class ImportExportReference(Base):
    __tablename__ = 'ImportExportReference'
    __table_args__ = (
        ForeignKeyConstraint(['ReferencedTable', 'ReferencedColumn'], [u'ImportExportColumn.TableName', u'ImportExportColumn.ColumnName']),
        ForeignKeyConstraint(['ReferencingTable', 'ReferencingColumn'], [u'ImportExportColumn.TableName', u'ImportExportColumn.ColumnName']),
        Index('XIE1ImportExportReference', 'ReferencedTable', 'ReferencedColumn'),
        Index('XIE2ImportExportReference', 'ReferencingTable', 'ReferencingColumn')
    )

    ReferencedTable = Column(Unicode(64), primary_key=True, nullable=False)
    ReferencedColumn = Column(Unicode(64), primary_key=True, nullable=False)
    ReferencingTable = Column(Unicode(64), primary_key=True, nullable=False)
    ReferencingColumn = Column(Unicode(64), primary_key=True, nullable=False)
    Forward = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Reverse = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    ImportExportColumn = relationship(u'ImportExportColumn', primaryjoin='ImportExportReference.ReferencedTable == ImportExportColumn.TableName')
    ImportExportColumn1 = relationship(u'ImportExportColumn', primaryjoin='ImportExportReference.ReferencingTable == ImportExportColumn.TableName')


class ImportExportTable(Base):
    __tablename__ = 'ImportExportTable'

    TableName = Column(Unicode(64), primary_key=True)
    PreprocessingMethodName = Column(Unicode(64))
    PostprocessingMethodName = Column(Unicode(64))
    CheckObjectStatusOnExport = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    InsertionStoredProcedure = Column(Unicode(64))
    ContinueIfInsertFails = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class InVivoDosimetry(Base):
    __tablename__ = 'InVivoDosimetry'

    InVivoDosimetrySer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    InVivoDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    InVivoVendorName = Column(Unicode(64), nullable=False)
    DosimeterType = Column(Unicode(64))
    DosimeterId = Column(Unicode(64), nullable=False)
    DosimeterLocation = Column(Unicode(128), nullable=False)
    FieldId = Column(Unicode(16), nullable=False)
    FieldName = Column(Unicode(64))
    ExpectedDose = Column(Float(53))
    DeliveredDose = Column(Float(53))
    ToleranceValue = Column(Float(53))
    UserName = Column(Unicode(32))
    CreationUserName = Column(Unicode(32), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    PlanUID = Column(Unicode(64))
    FieldGroupNumber = Column(Integer)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')


class IntfTrgr(Base):
    __tablename__ = 'IntfTrgr'

    IntfTrgrSer = Column(BigInteger, primary_key=True)
    FacId = Column(Integer)
    InstId = Column(Unicode(32))
    MsgEvntTyp = Column(Unicode(16))
    MsgTyp = Column(Unicode(16))
    OrderTyp = Column(Unicode(16))
    TrgrStatusInd = Column(Unicode(16))
    IntfAppParmIdNoTrgr = Column(Unicode(16))
    IntfAppParmIdTrgr = Column(Unicode(16))
    UserId = Column(Unicode(16))
    UserInstId = Column(Unicode(32))
    AppCd = Column(Unicode(16))
    KeyName1 = Column(Unicode(64))
    KeyName2 = Column(Unicode(64))
    KeyName3 = Column(Unicode(64))
    KeyName4 = Column(Unicode(64))
    KeyName5 = Column(Unicode(64))
    KeyName6 = Column(Unicode(64))
    KeyName7 = Column(Unicode(64))
    KeyName8 = Column(Unicode(64))
    KeyName9 = Column(Unicode(64))
    KeyName10 = Column(Unicode(64))
    KeyValue1 = Column(Unicode(64))
    KeyValue2 = Column(Unicode(64))
    KeyValue3 = Column(Unicode(64))
    KeyValue4 = Column(Unicode(64))
    KeyValue5 = Column(Unicode(64))
    KeyValue6 = Column(Unicode(64))
    KeyValue7 = Column(Unicode(64))
    KeyValue8 = Column(Unicode(64))
    KeyValue9 = Column(Unicode(64))
    KeyValue10 = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class LTAScheduledTask(Base):
    __tablename__ = 'LTAScheduledTask'

    ScheduledTaskSer = Column(BigInteger, primary_key=True)
    Name = Column(Unicode(64))
    Status = Column(Unicode(32), nullable=False)
    ArchiveLocationSer = Column(ForeignKey(u'ArchiveLocation.ArchiveLocationSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    StatusDescription = Column(Unicode(254))

    ArchiveLocation = relationship(u'ArchiveLocation')


class LTAScheduledTaskPatient(Base):
    __tablename__ = 'LTAScheduledTaskPatient'

    ScheduledTaskSer = Column(ForeignKey(u'LTAScheduledTask.ScheduledTaskSer'), primary_key=True, nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True, nullable=False, index=True)
    Status = Column(Unicode(32), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')
    LTAScheduledTask = relationship(u'LTAScheduledTask')


class LanguageLookup(Base):
    __tablename__ = 'LanguageLookup'

    LanguageId = Column(Unicode(16), primary_key=True)
    LanguageName = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


t_LinkRTTemp = Table(
    'LinkRTTemp', metadata,
    Column('SPID', BigInteger, nullable=False),
    Column('MLCPlanSer', BigInteger),
    Column('IndexValues', Float(53)),
    Column('PointCount', BigInteger),
    Column('LeafNumber', BigInteger),
    Column('DynamicPosTolerance', Float(53)),
    Column('LeftLeafPosition', Float(53)),
    Column('RightLeafPosition', Float(53)),
    Column('UpdateFlag', Unicode(1)),
    Column('LeftLeaf', SmallInteger),
    Column('RightLeaf', SmallInteger),
    Column('AddOnSer', BigInteger),
    Column('AddOnId', Unicode(16)),
    Column('SlotSer', BigInteger),
    Column('SlotNo', BigInteger),
    Column('CacheKey', BigInteger),
    Column('PatientId', Unicode(25)),
    Column('CourseID', Unicode(16)),
    Column('PlanSetupID', Unicode(16)),
    Column('FieldID', Unicode(16)),
    Column('FieldName', Unicode(64)),
    Column('CreationDate', DateTime),
    Column('MachineId', Unicode(16)),
    Column('ToleranceId', Unicode(16)),
    Column('ToleranceTableName', Unicode(64)),
    Column('Scale', Unicode(16)),
    Column('TechniqueId', Unicode(16)),
    Column('EnergyMode', Unicode(16)),
    Column('MLCFlag', Integer),
    Column('SetupNote', Unicode(254)),
    Column('CollMode', Unicode(16)),
    Column('MU', Integer),
    Column('TreatmentTime', Float(53)),
    Column('SSD', Float(53)),
    Column('StopAng', Float(53)),
    Column('StopAngE', Unicode(16)),
    Column('MUdeg', Float(53)),
    Column('CollRtn', Float(53)),
    Column('CollRtnM', Float(53)),
    Column('GantryRtn', Float(53)),
    Column('GantryRtnE', Unicode(16)),
    Column('GantryRtnExt', Unicode(16)),
    Column('CollY1', Float(53)),
    Column('CollY2', Float(53)),
    Column('CollX1', Float(53)),
    Column('CollX2', Float(53)),
    Column('CouchVrt', Float(53)),
    Column('CouchVrtM', Float(53)),
    Column('CouchLng', Float(53)),
    Column('CouchLngM', Float(53)),
    Column('CouchLat', Float(53)),
    Column('CouchLatM', Float(53)),
    Column('CouchRtn', Float(53)),
    Column('CouchRtnM', Float(53)),
    Column('AddOnId1', Unicode(16)),
    Column('AddOnType1', Unicode(30)),
    Column('SlotName1', Unicode(64)),
    Column('AddOnId2', Unicode(16)),
    Column('AddOnType2', Unicode(30)),
    Column('SlotName2', Unicode(64)),
    Column('AddOnId3', Unicode(16)),
    Column('AddOnType3', Unicode(30)),
    Column('SlotName3', Unicode(64)),
    Column('AddOnId4', Unicode(16)),
    Column('AddOnType4', Unicode(30)),
    Column('SlotName4', Unicode(64)),
    Column('AddOnId5', Unicode(16)),
    Column('AddOnType5', Unicode(30)),
    Column('SlotName5', Unicode(64)),
    Column('AddOnId6', Unicode(16)),
    Column('AddOnType6', Unicode(30)),
    Column('SlotName6', Unicode(64)),
    Column('TreatmentFlag', Integer),
    Column('PtTreatedFlag', Integer),
    Column('DoseRate', Integer),
    Column('WedgeDose', Float(53)),
    Column('FieldSer', BigInteger),
    Column('FieldRevCount', BigInteger),
    Column('MUpGy', Float(53)),
    Column('TempDose', Float(53)),
    Column('WDProcessFlag', Integer)
)


class LinkUsage(Base):
    __tablename__ = 'LinkUsage'

    StoredProcedureName = Column(Unicode(254), primary_key=True)
    UsageCount = Column(Integer, nullable=False)
    DateStartedUse = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    LastDateUsed = Column(DateTime, nullable=False)


class LookupMapping(Base):
    __tablename__ = 'LookupMapping'

    LookupMappingSer = Column(BigInteger, primary_key=True)
    ListSelector = Column(Unicode(32), nullable=False)
    ParentLookupValue = Column(Unicode(64), nullable=False)
    ChildLookupValue = Column(Unicode(64), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))


class LookupTable(Base):
    __tablename__ = 'LookupTable'
    __table_args__ = (
        Index('XAKLookupTable', 'ListSelector', 'LanguageId', 'SubSelector', 'LookupValue', unique=True),
    )

    LookupTableSer = Column(BigInteger, primary_key=True)
    ListSelector = Column(Unicode(32), nullable=False)
    SubSelector = Column(BigInteger)
    LanguageId = Column(ForeignKey(u'LanguageLookup.LanguageId'), nullable=False, index=True)
    LookupValue = Column(Unicode(64), nullable=False)
    Expression1 = Column(Unicode(64))
    Expression2 = Column(Unicode(64))
    Expression3 = Column(Unicode(64))
    EditFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    LanguageLookup = relationship(u'LanguageLookup')


class MLCBank(Base):
    __tablename__ = 'MLCBank'
    __table_args__ = (
        Index('XAKMLCBank', 'AddOnSer', 'MLCBankId', unique=True),
    )

    MLCBankSer = Column(BigInteger, primary_key=True)
    MLCBankId = Column(Unicode(16), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    AddOnSer = Column(ForeignKey(u'MLC.AddOnSer'), nullable=False)
    MaxLeafExposure = Column(Float(53))
    MaxLeafSpan = Column(Float(53))

    MLC = relationship(u'MLC')


class MLCLeaf(Base):
    __tablename__ = 'MLCLeaf'
    __table_args__ = (
        Index('XAK1MLCLeaf', 'MLCBankSer', 'LeafNumber', unique=True),
        Index('XAK2MLCLeaf', 'MLCBankSer', 'LeafId', unique=True)
    )

    MLCLeafSer = Column(BigInteger, primary_key=True)
    MLCBankSer = Column(ForeignKey(u'MLCBank.MLCBankSer'), nullable=False)
    LeafId = Column(Unicode(16), nullable=False)
    LeafNumber = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    OffsetY = Column(Float(53))
    MaxRetractPosition = Column(Float(53))
    MaxExtendPosition = Column(Float(53))
    Width = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    MLCBank = relationship(u'MLCBank')


class MLCPlan(Base):
    __tablename__ = 'MLCPlan'
    __table_args__ = (
        Index('XAKMLCPlan', 'RadiationSer', 'MLCPlanId', unique=True),
    )

    MLCPlanSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), nullable=False)
    MLCPlanId = Column(Unicode(16), nullable=False)
    MLCPlanName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    MLCPlanType = Column(Unicode(30), nullable=False)
    IndexParameterType = Column(Unicode(32))
    Comment = Column(Unicode(254))
    IsLockedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    EllipticalMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    BEVMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    LeftMargin = Column(Float(53))
    RightMargin = Column(Float(53))
    TopMargin = Column(Float(53))
    BottomMargin = Column(Float(53))
    ContourMeetPoint = Column(Unicode(32))
    ClosedMeetPoint = Column(Unicode(32))
    OptimizeCollRtnFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    CollimatorJawOptimization = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ExternalFieldCommon = relationship(u'ExternalFieldCommon')


class MatchResult(Base):
    __tablename__ = 'MatchResult'

    MatchResultSer = Column(BigInteger, primary_key=True)
    MatchResultId = Column(Unicode(16), nullable=False)
    MatchAlgorithm = Column(Unicode(64))
    MatchMatrix = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    KindOfMatch = Column(Unicode(64))
    MaxErrorDist = Column(Float(53))
    AverageErrorDist = Column(Float(53))
    ScaleFactor = Column(Float(53))
    ModificationLog = Column(Unicode(254))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class Material(Base):
    __tablename__ = 'Material'

    MaterialSer = Column(BigInteger, primary_key=True)
    MaterialId = Column(Unicode(16), nullable=False, unique=True)
    MaterialName = Column(Unicode(64))
    UseSpecularFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Color2D = Column(BINARY(4))
    Rendering3DModel = Column(Unicode(32))
    Rendering2DModel = Column(Unicode(32))
    ShadowFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Translucency3D = Column(Float(53))
    Translucency2D = Column(Float(53))
    LineThickness = Column(Float(53))
    LinePattern = Column(BINARY(32))
    SpecularColor = Column(BINARY(4))
    DiffuseColor = Column(BINARY(4))
    AmbientColor = Column(BINARY(4))
    SpecularPower = Column(Float(53))
    SpecularAngular = Column(Float(53))
    TransparencyFolding = Column(Float(53))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class Matrix(Base):
    __tablename__ = 'Matrix'

    MatrixSer = Column(BigInteger, primary_key=True)
    MatrixId = Column(Unicode(16), nullable=False)
    MatrixName = Column(Unicode(64))
    MatrixType = Column(Unicode(30), nullable=False)
    MatrixDataType = Column(Unicode(32), nullable=False)
    UsageType = Column(Unicode(64))
    MatrixFileName = Column(Unicode(254))
    SizeX = Column(Integer)
    SizeY = Column(Integer)
    Comment = Column(Unicode(254))
    ContextDetails = Column(Unicode(32))
    GantryCoordinates = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    MLCPlanSer = Column(ForeignKey(u'MLCPlan.MLCPlanSer'), index=True)
    RadiationSer = Column(ForeignKey(u'ExternalField.RadiationSer'), index=True)
    CompensatorSer = Column(ForeignKey(u'Compensator.CompensatorSer'), index=True)

    Compensator = relationship(u'Compensator')
    MLCPlan = relationship(u'MLCPlan')
    ExternalField = relationship(u'ExternalField')


class Message(Base):
    __tablename__ = 'Message'

    MessageSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), nullable=False, index=True)
    MessageText = Column(UnicodeText(1073741823))
    DeletedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    CreationDate = Column(DateTime, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Resource = relationship(u'Resource')


class MobilePhoneProvider(Base):
    __tablename__ = 'MobilePhoneProvider'

    MobilePhoneProviderSer = Column(BigInteger, primary_key=True)
    ProviderName = Column(Unicode(64), nullable=False)
    SMSMsgDomainName = Column(Unicode(64), nullable=False)
    ActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class NextKeyTable(Base):
    __tablename__ = 'NextKeyTable'

    KeyName = Column(Unicode(64), primary_key=True)
    KeyValue = Column(BigInteger, nullable=False)


class NonScheduledActivity(Base):
    __tablename__ = 'NonScheduledActivity'

    NonScheduledActivitySer = Column(BigInteger, primary_key=True)
    NonScheduledActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    CreatedByResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    CreatedByUserName = Column(Unicode(32), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    UID = Column(Unicode(64), nullable=False, unique=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DueDateTime = Column(DateTime, index=True)
    NonScheduledActivityCode = Column(Unicode(64))
    Priority = Column(Unicode(64))
    ActivityNote = Column(Unicode(254))
    RecurrenceRuleSer = Column(ForeignKey(u'RecurrenceRule.RecurrenceRuleSer'), index=True)
    ReadByAppUserName = Column(Unicode(32))
    ReadByDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    WorkFlowActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))

    ActivityInstance = relationship(u'ActivityInstance')
    Resource = relationship(u'Resource')
    Patient = relationship(u'Patient')
    RecurrenceRule = relationship(u'RecurrenceRule')


class NonScheduledActivityMH(Base):
    __tablename__ = 'NonScheduledActivityMH'
    __table_args__ = (
        Index('XIE1NonScheduledActivityMH', 'ActivityInstanceSer', 'ActivityInstanceRevCount'),
    )

    NonScheduledActivitySer = Column(ForeignKey(u'NonScheduledActivity.NonScheduledActivitySer'), primary_key=True, nullable=False)
    NonScheduledActivityRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(BigInteger, nullable=False)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(BigInteger)
    CreatedByResourceSer = Column(BigInteger)
    CreatedByUserName = Column(Unicode(32), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    UID = Column(Unicode(64), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DueDateTime = Column(DateTime)
    NonScheduledActivityCode = Column(Unicode(64))
    Priority = Column(Unicode(64))
    ActivityNote = Column(Unicode(254))
    RecurrenceRuleSer = Column(BigInteger)
    ReadByAppUserName = Column(Unicode(32))
    ReadByDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    WorkFlowActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))

    NonScheduledActivity = relationship(u'NonScheduledActivity')


class ObjectPointer(Base):
    __tablename__ = 'ObjectPointer'

    ObjectPointerSer = Column(BigInteger, primary_key=True)
    ObjectType = Column(Unicode(32), nullable=False)
    ObjectSer = Column(BigInteger)
    DicomLocationSer = Column(ForeignKey(u'DicomLocation.DicomLocationSer'), index=True)
    DCObjectPointerSeriesSer = Column(ForeignKey(u'DCObjectPointerSeries.DCObjectPointerSeriesSer'), index=True)
    SOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), index=True)
    SOPInstanceUID = Column(Unicode(64))

    DCObjectPointerSery = relationship(u'DCObjectPointerSery')
    DicomLocation = relationship(u'DicomLocation')
    SOPClas = relationship(u'SOPClas')
    PerformedProcedure = relationship(u'PerformedProcedure', secondary='PerformedObjectPointer')


class ObsoleteObject(Base):
    __tablename__ = 'ObsoleteObject'

    ObsoleteObjectSer = Column(BigInteger, primary_key=True)
    DirLabel = Column(Unicode(32), nullable=False)
    ObjectPath = Column(Unicode(254), nullable=False)
    ErrorReason = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    LastAccessDate = Column(DateTime)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)

    Patient = relationship(u'Patient')


class OperatingLimit(Base):
    __tablename__ = 'OperatingLimit'
    __table_args__ = (
        Index('XAKOperatingLimit', 'ParameterType', 'ResourceSer', 'TechniqueSer', 'PrimaryFluenceModeSer', unique=True),
    )

    OperatingLimitSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), nullable=False)
    ParameterType = Column(Unicode(32), nullable=False)
    ParameterName = Column(Unicode(64))
    MinValue = Column(Float(53))
    MaxValue = Column(Float(53))
    DefValue = Column(Float(53))
    LimitPrecision = Column(Integer)
    TolerancePossible = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    MotionMode = Column(Unicode(64))
    MaxSpeed = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PrimaryFluenceModeSer = Column(ForeignKey(u'PrimaryFluenceMode.AddOnSer'), index=True)
    TechniqueSer = Column(ForeignKey(u'Technique.TechniqueSer'), index=True)

    PrimaryFluenceMode = relationship(u'PrimaryFluenceMode')
    Machine = relationship(u'Machine')
    Technique = relationship(u'Technique')


class ParameterType(Base):
    __tablename__ = 'ParameterType'

    ParameterTypeSer = Column(BigInteger, primary_key=True)
    ParameterTypeDataType = Column(Unicode(64), nullable=False)


t_PatEdHstryControl = Table(
    'PatEdHstryControl', metadata,
    Column('GroupId', Integer, nullable=False),
    Column('AttribName', Unicode(64), nullable=False),
    Column('OldValue', Unicode(254)),
    Column('NewValue', Unicode(254)),
    Index('XIE1PatEdHstryControl', 'GroupId', 'AttribName', 'OldValue')
)


class PatEdHstryRelevance(Base):
    __tablename__ = 'PatEdHstryRelevance'

    PatEdHstryRelevanceSer = Column(BigInteger, primary_key=True)
    TableName = Column(Unicode(30), nullable=False)
    AttribName = Column(Unicode(64), nullable=False)
    AfterTreatInd = Column(Unicode(1))
    AfterApproveInd = Column(Unicode(1))
    AttribRelevanceInd = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RowRelevanceInd = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    OnInsInd = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    OnUpdInd = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    OnDelInd = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class Patient(Base):
    __tablename__ = 'Patient'
    __table_args__ = (
        Index('XIE3Patient', 'LastName', 'FirstName'),
        Index('XIE1Patient', 'PatientId2', 'MiddleName')
    )

    PatientSer = Column(BigInteger, primary_key=True)
    PatientId = Column(Unicode(25), nullable=False, unique=True)
    PatientId2 = Column(Unicode(25))
    PatientUID = Column(Unicode(64), nullable=False, unique=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_UID_DEF]
	AS '0'"""))
    PatientType = Column(Unicode(30), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    SSN = Column(Unicode(64), index=True)
    FirstName = Column(Unicode(64))
    MiddleName = Column(Unicode(64))
    LastName = Column(Unicode(64), nullable=False)
    NameSuffix = Column(Unicode(16))
    Honorific = Column(Unicode(16))
    DateOfBirth = Column(DateTime)
    Sex = Column(Unicode(16))
    WorkPhone = Column(Unicode(64))
    HomePhone = Column(Unicode(64))
    Citizenship = Column(Unicode(64))
    Race = Column(Unicode(64))
    BirthCountry = Column(Unicode(64))
    BirthState = Column(Unicode(64))
    BirthCounty = Column(Unicode(64))
    BirthCity = Column(Unicode(64))
    PatientIdIssuer = Column(Unicode(32))
    MaidenName = Column(Unicode(64))
    MothersMaidenName = Column(Unicode(64))
    MedRecordLocator = Column(Unicode(64))
    Language = Column(Unicode(16))
    Occupation = Column(Unicode(64))
    SpecialNeeds = Column(Unicode(64))
    ReligiousPreference = Column(Unicode(64))
    ArchiveDate = Column(DateTime)
    ArchiveVolume = Column(Unicode(32))
    Comment = Column(Unicode(254))
    ClinicalTrialFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    FileDataSiteID = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    MobilePhone = Column(Unicode(64))
    Ethnicity = Column(Unicode(64))
    MobilePhoneProviderSer = Column(ForeignKey(u'MobilePhoneProvider.MobilePhoneProviderSer'), index=True)

    MobilePhoneProvider = relationship(u'MobilePhoneProvider')


class PatientActual(Patient):
    __tablename__ = 'PatientActuals'
    __table_args__ = (
        Index('XIE1PatientActuals', 'FirstNameUpper', 'LastNameUpper'),
    )

    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True)
    PatientIdUpper = Column(Unicode(25), nullable=False, index=True)
    PatientId2Upper = Column(Unicode(25), index=True)
    FirstNameUpper = Column(Unicode(64))
    LastNameUpper = Column(Unicode(64), index=True)
    SSN = Column(Unicode(64))
    PatientType = Column(Unicode(30), nullable=False)
    HospitalSer = Column(BigInteger)
    InPatientFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PatientLocation = Column(Unicode(16))
    ArrivalTime = Column(DateTime)
    PatientStatus = Column(Unicode(32))
    SelectionStatus = Column(Integer)
    LastImagePIDate = Column(DateTime)
    LastImageSIDate = Column(DateTime)
    LastOtherImageDate = Column(DateTime)
    DirectiveAskedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class PatientParticular(Patient):
    __tablename__ = 'PatientParticular'

    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True)
    UniversalPatientId = Column(Unicode(32))
    PassportNumber = Column(Unicode(32))
    PatientState = Column(Unicode(64))
    MaritalStatus = Column(Unicode(16))
    PregnancyStatus = Column(Unicode(32))
    MedicalAlerts = Column(Unicode(64))
    ContrastAllergies = Column(Unicode(64))
    LastMenstrualDate = Column(DateTime)
    SmokingStatus = Column(Unicode(16))
    RetireDate = Column(DateTime)
    RetireReason = Column(Unicode(254))
    RetireNote = Column(Unicode(254))
    DeathDate = Column(DateTime)
    DeathCause = Column(Unicode(254))
    AutopsyStatus = Column(Unicode(16))
    AutopsyOutcome = Column(Unicode(254))
    BloodGroup = Column(Unicode(16))
    UserDefAttrib01 = Column(Unicode(16))
    UserDefAttrib02 = Column(Unicode(16))
    UserDefAttrib03 = Column(Unicode(16))
    UserDefAttrib04 = Column(Unicode(16))
    UserDefAttrib05 = Column(Unicode(16))
    UserDefAttrib06 = Column(Unicode(16))
    UserDefAttrib07 = Column(Unicode(16))
    UserDefAttrib08 = Column(Unicode(16))
    UserDefAttrib09 = Column(Unicode(16))
    UserDefAttrib10 = Column(Unicode(16))
    UserDefAttrib11 = Column(Unicode(16))
    UserDefAttrib12 = Column(Unicode(16))
    UserDefAttrib13 = Column(Unicode(16))
    UserDefAttrib14 = Column(Unicode(16))
    UserDefAttrib15 = Column(Unicode(16))
    UserDefAttrib16 = Column(Unicode(16))


class PatientAddres(Base):
    __tablename__ = 'PatientAddress'

    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True, nullable=False)
    AddressSer = Column(ForeignKey(u'Address.AddressSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Addres = relationship(u'Addres')
    Patient = relationship(u'Patient')


class PatientAuthorization(Base):
    __tablename__ = 'PatientAuthorization'
    __table_args__ = (
        Index('XAK1PatientAuthorization', 'PatientPayorSer', 'PatientPayorRevCount', 'AuthorizationDateTime', unique=True),
    )

    PatientAuthorizationSer = Column(BigInteger, primary_key=True)
    PatientPayorSer = Column(ForeignKey(u'PatientPayor.PatientPayorSer'), nullable=False)
    PatientPayorRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AuthorizationId = Column(Unicode(16))
    Comment = Column(Unicode(254))
    AuthorizationDateTime = Column(DateTime, nullable=False)
    AuthorizedBy = Column(Unicode(64))
    AuthorizationPhone = Column(Unicode(64))
    AuthorizationFAX = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PatientPayor = relationship(u'PatientPayor')


class PatientDepartment(Base):
    __tablename__ = 'PatientDepartment'
    __table_args__ = (
        Index('XAKPatientDepartment', 'PatientSer', 'DepartmentSer', unique=True),
    )

    PatientDepartmentSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), nullable=False, index=True)
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')
    Patient = relationship(u'Patient')


class PatientDirective(Base):
    __tablename__ = 'PatientDirective'

    PatientDirectiveSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    DirectiveSer = Column(ForeignKey(u'Directive.DirectiveSer'), nullable=False, index=True)
    Comment = Column(Unicode(254))
    ActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ValidEntryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ErrorReason = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Directive = relationship(u'Directive')
    Patient = relationship(u'Patient')


class PatientDoctor(Base):
    __tablename__ = 'PatientDoctor'

    ResourceSer = Column(ForeignKey(u'Doctor.ResourceSer'), primary_key=True, nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    OncologistFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PrimaryCarePhysicianFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Patient = relationship(u'Patient')
    Doctor = relationship(u'Doctor')


t_PatientEditingLog = Table(
    'PatientEditingLog', metadata,
    Column('PatientEditingLogSer', BigInteger, nullable=False),
    Column('PatientSer', ForeignKey(u'Patient.PatientSer'), nullable=False, index=True),
    Column('TableName', Unicode(30)),
    Column('AttribName', Unicode(32)),
    Column('EventId', Integer),
    Column('Key1', BigInteger),
    Column('Key2', BigInteger),
    Column('Key3', BigInteger),
    Column('TableId', Unicode(16)),
    Column('UID', Unicode(64), index=True),
    Column('OldValue', Unicode(254)),
    Column('NewValue', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()""")),
    Column('HstryDateTime', DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()""")),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Index('XIE4PatientEditingLog', 'PatientEditingLogSer', 'PatientSer'),
    Index('XIE2PatientEditingLog', 'TableName', 'AttribName', 'EventId')
)


class PatientHospital(Base):
    __tablename__ = 'PatientHospital'

    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), primary_key=True, nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    PatientHospitalRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    InPatientFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    PatientLocation = Column(Unicode(16))
    PatientStatus = Column(Unicode(32))
    StartDateTime = Column(DateTime)
    ProjectedEndDate = Column(DateTime)
    EndDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Hospital = relationship(u'Hospital')
    Patient = relationship(u'Patient')


class PatientHospitalMH(Base):
    __tablename__ = 'PatientHospitalMH'
    __table_args__ = (
        ForeignKeyConstraint(['HospitalSer', 'PatientSer'], [u'PatientHospital.HospitalSer', u'PatientHospital.PatientSer']),
        Index('XAK1PatientHospitalMH', 'HospitalSer', 'PatientSer', 'PatientHospitalRevCount', unique=True)
    )

    HospitalSer = Column(BigInteger, primary_key=True, nullable=False)
    PatientSer = Column(BigInteger, primary_key=True, nullable=False)
    PatientHospitalRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    CacheKeySer = Column(BigInteger)
    InPatientFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    PatientLocation = Column(Unicode(16))
    PatientStatus = Column(Unicode(32))
    StartDateTime = Column(DateTime)
    ProjectedEndDate = Column(DateTime)
    EndDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PatientHospital = relationship(u'PatientHospital')


class PatientLocation(Base):
    __tablename__ = 'PatientLocation'

    PatientLocationSer = Column(BigInteger, primary_key=True)
    PatientLocationRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ScheduledActivitySer = Column(ForeignKey(u'ScheduledActivity.ScheduledActivitySer'), nullable=False, index=True)
    ScheduledActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ResourceSer = Column(ForeignKey(u'Venue.ResourceSer'), index=True)
    CheckedInFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ArrivalDateTime = Column(DateTime)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Venue = relationship(u'Venue')
    ScheduledActivity = relationship(u'ScheduledActivity')


class PatientLocationMH(Base):
    __tablename__ = 'PatientLocationMH'
    __table_args__ = (
        Index('XIE1PatientLocationMH', 'ScheduledActivitySer', 'ScheduledActivityRevCount'),
    )

    PatientLocationSer = Column(ForeignKey(u'PatientLocation.PatientLocationSer'), primary_key=True, nullable=False)
    PatientLocationRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ScheduledActivitySer = Column(BigInteger, nullable=False)
    ScheduledActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ResourceSer = Column(BigInteger)
    CheckedInFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ArrivalDateTime = Column(DateTime)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PatientLocation = relationship(u'PatientLocation')


class PatientNote(Base):
    __tablename__ = 'PatientNote'

    PatientNoteSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    Note = Column(Unicode(512))
    PatientNoteCode = Column(Unicode(64))
    DisplayDateTime = Column(DateTime, nullable=False, index=True)
    WrittenByAppUserName = Column(Unicode(32), nullable=False)
    ReadByAppUserName = Column(Unicode(32))
    ReadDateTime = Column(DateTime)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')


class PatientPayor(Base):
    __tablename__ = 'PatientPayor'
    __table_args__ = (
        Index('XIE2PatientPayor', 'PayorSer', 'PrimaryFlag', 'PolicyNumber'),
    )

    PatientPayorSer = Column(BigInteger, primary_key=True)
    PatientPayorRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PayorSer = Column(ForeignKey(u'Payor.PayorSer'), nullable=False)
    PolicyNumber = Column(Unicode(16))
    PrimaryFlag = Column(Integer, nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    PreadmitNumber = Column(Unicode(32))
    AccountNumber = Column(Unicode(32))
    PrcntOfPaymnt = Column(Float(53))
    CoPayment = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    InsrdName = Column(Unicode(64))
    InsrdMdclNmbr = Column(Unicode(32))
    Relationship = Column(Unicode(64))
    InsrdGroupNumber = Column(Unicode(16))
    InsrdGroupName = Column(Unicode(64))
    InsrdGroupEmpId = Column(Unicode(16))
    InsrdGroupEmpName = Column(Unicode(64))
    VerificationDate = Column(DateTime)
    CreatedByHL7 = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')
    Payor = relationship(u'Payor')


class PatientPayorMH(Base):
    __tablename__ = 'PatientPayorMH'

    PatientPayorSer = Column(ForeignKey(u'PatientPayor.PatientPayorSer'), primary_key=True, nullable=False)
    PatientPayorRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PayorSer = Column(BigInteger, nullable=False)
    PolicyNumber = Column(Unicode(16))
    PrimaryFlag = Column(Integer, nullable=False)
    PatientSer = Column(BigInteger, nullable=False)
    PreadmitNumber = Column(Unicode(32))
    AccountNumber = Column(Unicode(32))
    PrcntOfPaymnt = Column(Float(53))
    CoPayment = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    InsrdName = Column(Unicode(64))
    InsrdMdclNmbr = Column(Unicode(32))
    Relationship = Column(Unicode(64))
    InsrdGroupNumber = Column(Unicode(16))
    InsrdGroupName = Column(Unicode(64))
    InsrdGroupEmpId = Column(Unicode(16))
    InsrdGroupEmpName = Column(Unicode(64))
    VerificationDate = Column(DateTime)
    CreatedByHL7 = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PatientPayor = relationship(u'PatientPayor')


t_PatientRTStatus = Table(
    'PatientRTStatus', metadata,
    Column('PatientSer', ForeignKey(u'Patient.PatientSer'), nullable=False),
    Column('StatusType', Unicode(32), nullable=False),
    Column('Status', Unicode(64), nullable=False),
    Column('ObjectType', Unicode(32)),
    Column('LastObjectDate', DateTime),
    Index('XIE1PatientRTStatus', 'PatientSer', 'StatusType'),
    Index('XIE2PatientRTStatus', 'PatientSer', 'LastObjectDate')
)


class PatientStaff(Base):
    __tablename__ = 'PatientStaff'

    ResourceSer = Column(ForeignKey(u'Staff.ResourceSer'), primary_key=True, nullable=False)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), primary_key=True, nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')
    Staff = relationship(u'Staff')


class PatientTransportation(Base):
    __tablename__ = 'PatientTransportation'

    PatientTransportationSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    TransportationSer = Column(ForeignKey(u'Transportation.TransportationSer'), index=True)
    TransportationName = Column(Unicode(64))
    TransportationPhone = Column(Unicode(64))
    TransportationComment = Column(Unicode(254))
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Patient = relationship(u'Patient')
    Transportation = relationship(u'Transportation')


class PatientVolume(Base):
    __tablename__ = 'PatientVolume'

    PatientVolumeSer = Column(BigInteger, primary_key=True)
    VolumeTypeSer = Column(ForeignKey(u'VolumeType.VolumeTypeSer'), nullable=False, index=True)
    VolumeCodeSer = Column(ForeignKey(u'VolumeCode.VolumeCodeSer'), index=True)
    PatientVolumeId = Column(Unicode(16), nullable=False)
    PatientVolumeName = Column(Unicode(64))
    PrescTotalDose = Column(Float(53))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)

    Patient = relationship(u'Patient')
    VolumeCode = relationship(u'VolumeCode')
    VolumeType = relationship(u'VolumeType')


class Payor(Base):
    __tablename__ = 'Payor'
    __table_args__ = (
        Index('XAK1Payor', 'PlanNumber', 'CompanyName', unique=True),
    )

    PayorSer = Column(BigInteger, primary_key=True)
    PlanTypeSer = Column(ForeignKey(u'PlanTypes.PlanTypeSer'), index=True)
    PlanNumber = Column(Unicode(16), nullable=False)
    CompanyName = Column(Unicode(64), nullable=False)
    StreetAddress1 = Column(Unicode(64))
    StreetAddress2 = Column(Unicode(64))
    City = Column(Unicode(64))
    State = Column(Unicode(64))
    PostalCode = Column(Unicode(16))
    Country = Column(Unicode(64))
    PrimaryContactName = Column(Unicode(64))
    Phone = Column(Unicode(64))
    FAX = Column(Unicode(64))
    EmailAddress = Column(Unicode(64))
    EffectiveDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    EndDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    NumOfPlanMmbrs = Column(Integer)
    MnthlyPaymntPerMmbr = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    TotalPaymntPerDiag = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PlanDeductible = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PlanLimitAmount = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PlanLimitDays = Column(Integer)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PlanType = relationship(u'PlanType')


class PayorAuthorization(Base):
    __tablename__ = 'PayorAuthorization'

    PayorAuthorizationSer = Column(BigInteger, primary_key=True)
    PayorSer = Column(ForeignKey(u'Payor.PayorSer'), nullable=False, index=True)
    Description = Column(Unicode(254))
    AuthorizedBy = Column(Unicode(64))
    AuthorizationPhone = Column(Unicode(64))
    AuthorizationFAX = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Payor = relationship(u'Payor')


t_PerformedObjectPointer = Table(
    'PerformedObjectPointer', metadata,
    Column('PerformedProcedureSer', ForeignKey(u'PerformedProcedure.PerformedProcedureSer'), primary_key=True, nullable=False),
    Column('ObjectPointerSer', ForeignKey(u'ObjectPointer.ObjectPointerSer'), primary_key=True, nullable=False, index=True)
)


class PerformedProcedure(Base):
    __tablename__ = 'PerformedProcedure'

    PerformedProcedureSer = Column(BigInteger, primary_key=True)
    PerformedProcedureId = Column(Unicode(16))
    PerformedProcedureUID = Column(Unicode(64))
    StartDateTime = Column(DateTime)
    EndDateTime = Column(DateTime)
    Description = Column(Unicode(64))
    Modality = Column(Unicode(16))
    Operator1 = Column(Unicode(64))
    Operator2 = Column(Unicode(64))
    Operator3 = Column(Unicode(64))
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), index=True)
    DiscReasonCodeMeaning = Column(Unicode(64))
    Status = Column(Unicode(16))
    ProtocolName = Column(Unicode(64))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Progress = Column(Float(53))
    TransactionUID = Column(Unicode(64))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstance = relationship(u'ActivityInstance')
    DICOMCodeValue = relationship(u'DICOMCodeValue')


class Photo(Base):
    __tablename__ = 'Photo'

    PhotoSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    PhotoType = Column(Unicode(32), nullable=False)
    Picture = Column(VARBINARY(-1))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    Thumbnail = Column(VARBINARY(-1))

    Patient = relationship(u'Patient')


class PhysicalMaterial(Base):
    __tablename__ = 'PhysicalMaterial'

    PhysicalMaterialSer = Column(BigInteger, primary_key=True)
    PhysicalMaterialId = Column(Unicode(16), nullable=False)
    DefaultMassDensity = Column(Float(53), nullable=False)
    MinimumMassDensity = Column(Float(53))
    MaximumMassDensity = Column(Float(53))
    LookupFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ReadOnlyFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PhysicalMaterialVersion = Column(Unicode(64), nullable=False)


class PhysicianIntent(Base):
    __tablename__ = 'PhysicianIntent'

    PhysicianIntentSer = Column(BigInteger, primary_key=True)
    PhysicianIntentUID = Column(Unicode(64))
    TreatmentIntentType = Column(Unicode(64), nullable=False)
    DiagnosisSer = Column(BigInteger)
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), nullable=False, index=True)
    CreationDate = Column(DateTime)
    CreationUserName = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    Course = relationship(u'Course')


class PlanConcurrency(Base):
    __tablename__ = 'PlanConcurrency'

    PlanUID = Column(Unicode(64), primary_key=True)
    LastSaveCRC = Column(BINARY(32), nullable=False)
    LastITLoadCRC = Column(BINARY(32))
    CheckSumSource = Column(Integer, nullable=False)
    UserDecidedAbortPartialOnDate = Column(DateTime)


class PlanRelationship(Base):
    __tablename__ = 'PlanRelationship'

    PlanRelationshipSer = Column(BigInteger, primary_key=True)
    RTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), nullable=False, index=True)
    RelatedRTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), index=True)
    RelatedPlanUID = Column(Unicode(64))
    RelatedPlanSOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), index=True)
    RelationshipType = Column(Unicode(16), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    RTPlan = relationship(u'RTPlan', primaryjoin='PlanRelationship.RTPlanSer == RTPlan.RTPlanSer')
    SOPClas = relationship(u'SOPClas')
    RTPlan1 = relationship(u'RTPlan', primaryjoin='PlanRelationship.RelatedRTPlanSer == RTPlan.RTPlanSer')


class PlanSetup(Base):
    __tablename__ = 'PlanSetup'
    __table_args__ = (
        Index('XIE7PlanSetup', 'CourseSer', 'PlanSetupSer', 'Status'),
    )

    PlanSetupSer = Column(BigInteger, primary_key=True)
    PatientSupportDeviceSer = Column(ForeignKey(u'PatientSupportDevice.ResourceSer'), index=True)
    PrescriptionSer = Column(ForeignKey(u'Prescription.PrescriptionSer'), index=True)
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), nullable=False)
    PlanSetupId = Column(Unicode(16), nullable=False)
    PlanSetupName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    Status = Column(Unicode(64), nullable=False)
    StatusUserName = Column(Unicode(32), nullable=False)
    StatusDate = Column(DateTime, nullable=False)
    PlanNormFactor = Column(Float(53))
    PlanNormMethod = Column(Unicode(64))
    Comment = Column(Unicode(254))
    TreatmentTechnique = Column(Unicode(16))
    ApplicationSetupType = Column(Unicode(16))
    ApplicationSetupNumber = Column(Integer)
    TreatmentType = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_TREATMENTTYPE_DEF]
	AS 'Linac'"""))
    CalcModelOptions = Column(UnicodeText(1073741823))
    CalcModelOptionsLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    TreatmentOrientation = Column(Unicode(16))
    PrescribedPercentage = Column(Float(53))
    PrimaryPTVSer = Column(ForeignKey(u'PatientVolume.PatientVolumeSer'), index=True)
    IrregFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    FieldRules = Column(UnicodeText(1073741823))
    FieldRulesLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SkinFlashMargin = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_TWENTY_FLT_DEF]
	AS 20.0"""))
    ProtocolPhaseId = Column(Unicode(64))
    MultiFieldOptFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    CopyOfSer = Column(BigInteger)
    StructureSetSer = Column(ForeignKey(u'StructureSet.StructureSetSer'), index=True)
    EquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    RaySearchPrivateData = Column(LargeBinary)
    RaySearchPrivateDataLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Intent = Column(Unicode(16))
    ViewingPlane = Column(BINARY(96))
    ViewingPlaneULCorner = Column(BINARY(24))
    ViewingPlaneLRCorner = Column(BINARY(24))
    BrachyPdrPulseInterval = Column(Float(53))
    BrachyPdrNoOfPulses = Column(Integer)
    TransactionId = Column(String(255, u'Latin1_General_BIN2'))
    ImageSer = Column(ForeignKey(u'Image.ImageSer'), index=True)

    Course = relationship(u'Course')
    Equipment = relationship(u'Equipment')
    Image = relationship(u'Image')
    PatientSupportDevice = relationship(u'PatientSupportDevice')
    Prescription = relationship(u'Prescription')
    PatientVolume = relationship(u'PatientVolume')
    StructureSet = relationship(u'StructureSet')


class PlanSum(Base):
    __tablename__ = 'PlanSum'

    PlanSumSer = Column(BigInteger, primary_key=True)
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), nullable=False, index=True)
    PlanSumId = Column(Unicode(16), nullable=False)
    PlanSumName = Column(Unicode(64))
    IsodoseLevels = Column(LargeBinary)
    IsodoseLevelsLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    FieldRules = Column(UnicodeText(1073741823))
    FieldRulesLen = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ImageSer = Column(ForeignKey(u'Image.ImageSer'), index=True)

    Course = relationship(u'Course')
    Image = relationship(u'Image')


class PlanSumPlanSetup(Base):
    __tablename__ = 'PlanSumPlanSetup'

    PlanSumSer = Column(ForeignKey(u'PlanSum.PlanSumSer'), primary_key=True, nullable=False)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    Sign = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ONE_INT_DEF]
	AS 1"""))
    RBEFactor = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PlanSetup = relationship(u'PlanSetup')
    PlanSum = relationship(u'PlanSum')


class PlanType(Base):
    __tablename__ = 'PlanTypes'

    PlanTypeSer = Column(BigInteger, primary_key=True)
    PlnTpAbbrvtn = Column(Unicode(32), nullable=False, unique=True)
    Description = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class PlanVariation(Base):
    __tablename__ = 'PlanVariation'

    PlanVariationSer = Column(BigInteger, primary_key=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), nullable=False, index=True)
    PlanVariationId = Column(Unicode(64))
    PlanVariationType = Column(Unicode(32), nullable=False)
    HUConversionError = Column(Float(53))
    IsocenterShiftX = Column(Float(53))
    IsocenterShiftY = Column(Float(53))
    IsocenterShiftZ = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PlanSetup = relationship(u'PlanSetup')


class PointOfContact(Base):
    __tablename__ = 'PointOfContact'

    PointOfContactSer = Column(BigInteger, primary_key=True)
    AddressSer = Column(ForeignKey(u'Address.AddressSer'), index=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    PrimaryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Relationship = Column(Unicode(64))
    Honorific = Column(Unicode(16))
    FirstName = Column(Unicode(64))
    MiddleName = Column(Unicode(64))
    LastName = Column(Unicode(64))
    NameSuffix = Column(Unicode(16))
    FirstNameUpper = Column(Unicode(64))
    LastNameUpper = Column(Unicode(64))
    DateOfBirth = Column(DateTime)
    Sex = Column(Unicode(16))
    WorkPhone = Column(Unicode(64))
    HomePhone = Column(Unicode(64))
    Comment = Column(Unicode(254))
    CreatedByHL7 = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    MobilePhone = Column(Unicode(64))
    EntrustedContactFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))

    Addres = relationship(u'Addres')
    Patient = relationship(u'Patient')


class PortalDoseAnalysi(Base):
    __tablename__ = 'PortalDoseAnalysis'

    PortalDoseAnalysisSer = Column(BigInteger, primary_key=True)
    CreationUserName = Column(Unicode(32))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    Comment = Column(Unicode(254))
    XMLPortalDoseAnalysis = Column(UnicodeText(1073741823), nullable=False)
    XMLPortalDoseAnalysisLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class Prescription(Base):
    __tablename__ = 'Prescription'

    PrescriptionSer = Column(BigInteger, primary_key=True)
    PrescriptionName = Column(Unicode(64), nullable=False)
    TreatmentPhaseSer = Column(ForeignKey(u'TreatmentPhase.TreatmentPhaseSer'), nullable=False, index=True)
    PredecessorPrescriptionSer = Column(ForeignKey(u'Prescription.PrescriptionSer'), index=True)
    PhaseType = Column(Unicode(16))
    Gating = Column(Unicode(32))
    SimulationNeeded = Column(Integer)
    BolusFrequency = Column(Unicode(64))
    BolusThickness = Column(Unicode(64))
    Notes = Column(Unicode(1024))
    Status = Column(Unicode(64), nullable=False)
    NumberOfFractions = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Technique = Column(Unicode(64))
    Site = Column(Unicode(64))
    PrescriptionTemplateSer = Column(ForeignKey(u'PrescriptionTemplate.PrescriptionTemplateSer'), index=True)
    CreationDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    parent = relationship(u'Prescription', remote_side=[PrescriptionSer])
    PrescriptionTemplate = relationship(u'PrescriptionTemplate')
    TreatmentPhase = relationship(u'TreatmentPhase')


class PrescriptionAnatomy(Base):
    __tablename__ = 'PrescriptionAnatomy'

    PrescriptionAnatomySer = Column(BigInteger, primary_key=True)
    PrescriptionSer = Column(ForeignKey(u'Prescription.PrescriptionSer'), nullable=False, index=True)
    AnatomyRole = Column(SmallInteger, nullable=False)
    AnatomyName = Column(Unicode(256), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    Prescription = relationship(u'Prescription')


class PrescriptionAnatomyItem(Base):
    __tablename__ = 'PrescriptionAnatomyItem'

    PrescriptionAnatomyItemSer = Column(BigInteger, primary_key=True)
    PrescriptionAnatomySer = Column(ForeignKey(u'PrescriptionAnatomy.PrescriptionAnatomySer'), nullable=False, index=True)
    ItemType = Column(Unicode(64), nullable=False)
    ItemValue = Column(Unicode(64), nullable=False)
    ItemValueUnit = Column(Unicode(16))
    Param1Value = Column(Unicode(64))
    Param1ValueUnit = Column(Unicode(16))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PrescriptionAnatomy = relationship(u'PrescriptionAnatomy')


class PrescriptionProperty(Base):
    __tablename__ = 'PrescriptionProperty'

    PrescriptionPropertySer = Column(BigInteger, primary_key=True)
    PrescriptionSer = Column(ForeignKey(u'Prescription.PrescriptionSer'), nullable=False, index=True)
    PropertyType = Column(SmallInteger, nullable=False)
    PropertyValue = Column(Unicode(64), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    Prescription = relationship(u'Prescription')


class PrescriptionPropertyItem(Base):
    __tablename__ = 'PrescriptionPropertyItem'

    PrescriptionPropertyItemSer = Column(BigInteger, primary_key=True)
    PrescriptionPropertySer = Column(ForeignKey(u'PrescriptionProperty.PrescriptionPropertySer'), nullable=False, index=True)
    ItemType = Column(SmallInteger, nullable=False)
    ItemValue = Column(Unicode(64), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PrescriptionProperty = relationship(u'PrescriptionProperty')


class PrescriptionTemplate(Base):
    __tablename__ = 'PrescriptionTemplate'

    PrescriptionTemplateSer = Column(BigInteger, primary_key=True)
    PrescriptionTemplateName = Column(Unicode(64), nullable=False)
    PrescriptionName = Column(Unicode(64), nullable=False)
    Intent = Column(Unicode(64))
    UserCUID = Column(Unicode(64))
    Gating = Column(Unicode(32))
    SimulationNeeded = Column(Integer)
    BolusFrequency = Column(Unicode(64))
    BolusThickness = Column(Unicode(64))
    Notes = Column(Unicode(1024))
    Status = Column(Unicode(32), nullable=False)
    PhaseType = Column(Unicode(16))
    NumberOfFractions = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Technique = Column(Unicode(64))
    Site = Column(Unicode(64))
    CreationDate = Column(DateTime, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))


class PrescriptionTemplateAnatomy(Base):
    __tablename__ = 'PrescriptionTemplateAnatomy'

    PrescriptionTemplateAnatomySer = Column(BigInteger, primary_key=True)
    PrescriptionAnatomyTemplateName = Column(Unicode(64))
    PrescriptionTemplateSer = Column(ForeignKey(u'PrescriptionTemplate.PrescriptionTemplateSer'), index=True)
    AnatomyRole = Column(SmallInteger)
    AnatomyName = Column(Unicode(256))
    UserCUID = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PrescriptionTemplate = relationship(u'PrescriptionTemplate')


class PrescriptionTemplateAnatomyItem(Base):
    __tablename__ = 'PrescriptionTemplateAnatomyItem'

    PrescriptionTemplateAnatomyItemSer = Column(BigInteger, primary_key=True)
    PrescriptionTemplateAnatomySer = Column(ForeignKey(u'PrescriptionTemplateAnatomy.PrescriptionTemplateAnatomySer'), nullable=False, index=True)
    ItemType = Column(Unicode(64), nullable=False)
    ItemValue = Column(Unicode(64), nullable=False)
    ItemValueUnit = Column(Unicode(16))
    Param1Value = Column(Unicode(64))
    Param1ValueUnit = Column(Unicode(16))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PrescriptionTemplateAnatomy = relationship(u'PrescriptionTemplateAnatomy')


class PrescriptionTemplateProperty(Base):
    __tablename__ = 'PrescriptionTemplateProperty'

    PrescriptionTemplatePropertySer = Column(BigInteger, primary_key=True)
    PrescriptionPropertyTemplateName = Column(Unicode(64))
    PrescriptionTemplateSer = Column(ForeignKey(u'PrescriptionTemplate.PrescriptionTemplateSer'), index=True)
    PropertyType = Column(SmallInteger, nullable=False)
    PropertyValue = Column(Unicode(64), nullable=False)
    UserCUID = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PrescriptionTemplate = relationship(u'PrescriptionTemplate')


class PrescriptionTemplatePropertyItem(Base):
    __tablename__ = 'PrescriptionTemplatePropertyItem'

    PrescriptionTemplatePropertyItemSer = Column(BigInteger, primary_key=True)
    PrescriptionTemplatePropertySer = Column(ForeignKey(u'PrescriptionTemplateProperty.PrescriptionTemplatePropertySer'), nullable=False, index=True)
    ItemType = Column(SmallInteger, nullable=False)
    ItemValue = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PrescriptionTemplateProperty = relationship(u'PrescriptionTemplateProperty')


class PrintReport(Base):
    __tablename__ = 'PrintReport'

    PrintReportSer = Column(BigInteger, primary_key=True)
    PrintReportID = Column(Unicode(64), nullable=False)
    PrintReportDesc = Column(Unicode(254), nullable=False)
    PrintReportTemplate = Column(Unicode(254), nullable=False)
    PrintReportSP = Column(Unicode(64), nullable=False)
    PrintReportArg = Column(Unicode(254))
    PrintReportBind1 = Column(Unicode(254), nullable=False)
    PrintReportBind2 = Column(Unicode(254))
    ModeDialog1 = Column(Integer, nullable=False)
    ModeDialog2 = Column(Integer, nullable=False)
    ModeDialog3 = Column(Integer, nullable=False)
    ModeDialog4 = Column(Integer, nullable=False)
    PrintModeFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ProcedureCode(Base):
    __tablename__ = 'ProcedureCode'
    __table_args__ = (
        Index('XIE1ProcedureCode', 'ActivityCategorySer', 'ProcedureCode', 'BillingCode'),
    )

    ProcedureCodeSer = Column(BigInteger, primary_key=True)
    ProcedureCodeRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ModifierSer = Column(ForeignKey(u'ActivityCodeMd.ModifierSer'), index=True)
    ActivityCodeMdRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCategorySer = Column(ForeignKey(u'ActivityCategory.ActivityCategorySer'), nullable=False)
    ProcedureCode = Column(Unicode(64), nullable=False)
    CodeType = Column(Unicode(32), nullable=False)
    BillingCode = Column(Unicode(64))
    DerivedFromProcedureCodeSer = Column(BigInteger)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    UserDefinedCode = Column(Unicode(64))
    PrmrProfessCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PrmrTechCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PrmrGlblCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ProfessionalRVU = Column(Float(53))
    TechnicalRVU = Column(Float(53))
    GlobalRVU = Column(Float(53))
    OthrProfessCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OthrTechCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OthrGlblCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ComplexityCode = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_CODEVALUE_DEF]
	AS 0"""))
    ActivityCost = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    Comment = Column(Unicode(254), nullable=False)
    ShortComment = Column(Unicode(64), nullable=False)
    WorkUnit = Column(Float(53))
    ChargeForecast = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ActualCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ExportableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)

    ActivityCategory = relationship(u'ActivityCategory')
    Department = relationship(u'Department')
    ActivityCodeMd = relationship(u'ActivityCodeMd')


class ProcedureCodeMH(Base):
    __tablename__ = 'ProcedureCodeMH'

    ProcedureCodeSer = Column(ForeignKey(u'ProcedureCode.ProcedureCodeSer'), primary_key=True, nullable=False)
    ProcedureCodeRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ModifierSer = Column(BigInteger)
    ActivityCodeMdRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityCategorySer = Column(BigInteger, nullable=False)
    ProcedureCode = Column(Unicode(64), nullable=False)
    CodeType = Column(Unicode(32), nullable=False)
    BillingCode = Column(Unicode(64))
    DerivedFromProcedureCodeSer = Column(BigInteger)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    UserDefinedCode = Column(Unicode(64))
    PrmrProfessCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PrmrTechCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    PrmrGlblCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ProfessionalRVU = Column(Float(53))
    TechnicalRVU = Column(Float(53))
    GlobalRVU = Column(Float(53))
    OthrProfessCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OthrTechCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    OthrGlblCharge = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ComplexityCode = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_CODEVALUE_DEF]
	AS 0"""))
    ActivityCost = Column(MONEY, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    Comment = Column(Unicode(254), nullable=False)
    ShortComment = Column(Unicode(64), nullable=False)
    WorkUnit = Column(Float(53))
    ChargeForecast = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ActualCharge = Column(MONEY, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_MONEY_DEF]
	AS 0"""))
    ExportableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DepartmentSer = Column(BigInteger)

    ProcedureCode1 = relationship(u'ProcedureCode')


class ProcedureItem(Base):
    __tablename__ = 'ProcedureItem'

    ProcedureItemSer = Column(BigInteger, primary_key=True)
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), nullable=False, index=True)
    Duration = Column(Integer)
    Comment = Column(Unicode(254))
    ProcedureItemType = Column(Unicode(16), nullable=False)
    NoEditFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ProcedureItemLabel = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    DICOMCodeValue = relationship(u'DICOMCodeValue')


class ProcedureItemResource(Base):
    __tablename__ = 'ProcedureItemResource'

    ProcedureItemResourceSer = Column(BigInteger, primary_key=True)
    ProcedureItemSer = Column(ForeignKey(u'ProcedureItem.ProcedureItemSer'), nullable=False, index=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    ResourceGroupSer = Column(ForeignKey(u'ResourceGroup.ResourceGroupSer'), index=True)
    Modality = Column(Unicode(16))
    NoEditFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ProcedureItem = relationship(u'ProcedureItem')
    ResourceGroup = relationship(u'ResourceGroup')
    Resource = relationship(u'Resource')


class ProcedureItemSOPClas(Base):
    __tablename__ = 'ProcedureItemSOPClass'

    ProcedureItemSOPClassSer = Column(BigInteger, primary_key=True)
    ProcedureItemSer = Column(ForeignKey(u'ProcedureItem.ProcedureItemSer'), nullable=False, index=True)
    SOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), index=True)
    TableName = Column(Unicode(30))
    Type = Column(Unicode(32), nullable=False)
    InputTemplateSer = Column(BigInteger)
    RequiredFlag = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ProcedureItem = relationship(u'ProcedureItem')
    SOPClas = relationship(u'SOPClas')


class Processing(Base):
    __tablename__ = 'Processing'

    ProcessingSer = Column(BigInteger, primary_key=True)
    ProcessingId = Column(Unicode(16), nullable=False)
    ProcessingName = Column(Unicode(64))
    RootFlag = Column(Integer)
    FunctionName = Column(Unicode(64))
    ProcessingStatus = Column(Integer)
    ImageTypes = Column(Unicode(254))
    ParameterList = Column(LargeBinary)
    ParameterListLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class PttrnRelatedNonSchActivity(Base):
    __tablename__ = 'PttrnRelatedNonSchActivity'

    ActivityPttrnPerCycleSer = Column(ForeignKey(u'ActivityPttrnPerCycle.ActivityPttrnPerCycleSer'), primary_key=True, nullable=False)
    ActivitySer = Column(ForeignKey(u'Activity.ActivitySer'), primary_key=True, nullable=False, index=True)
    PriorPostDueTime = Column(Integer)
    ResourceAssignedBySer = Column(BigInteger, nullable=False)
    GroupAssignedToSer = Column(BigInteger, nullable=False)
    ResourceAssignedToSer = Column(BigInteger, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityPttrnPerCycle = relationship(u'ActivityPttrnPerCycle')
    Activity = relationship(u'Activity')


t_PurgePatientTemp = Table(
    'PurgePatientTemp', metadata,
    Column('Tablename', Unicode(30), nullable=False),
    Column('Serialnumber1', BigInteger),
    Column('Serialnumber2', BigInteger),
    Column('Serialnumber3', BigInteger),
    Column('Revisioncount1', Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0""")),
    Column('Revisioncount2', Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0""")),
    Column('Uid1', Unicode(64)),
    Column('Int1', Integer),
    Column('String16_1', Unicode(16)),
    Column('Numeric1', Numeric(7, 0)),
    Index('XIE1PurgePatientTemp', 'Tablename', 'Serialnumber1', 'String16_1')
)


class RTPlan(Base):
    __tablename__ = 'RTPlan'

    RTPlanSer = Column(BigInteger, primary_key=True)
    PlanSOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), nullable=False, index=True)
    PlanUID = Column(Unicode(64), nullable=False, unique=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), nullable=False, index=True)
    RTPlanId = Column(Unicode(16), nullable=False)
    RTPlanName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    NoFractions = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    StartDelay = Column(Integer)
    DicomSeqNumber = Column(Integer, nullable=False)
    Comment = Column(Unicode(254))
    InterfaceStamp = Column(Integer)
    PrescribedDose = Column(Float(53))
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    PlanIntegrityHash = Column(BINARY(32))
    PlanHashVersion = Column(Integer)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    TreatmentOrder = Column(Integer)
    FileName = Column(Unicode(254))
    FractionPatternDigitsPerDay = Column(Integer)
    FractionPattern = Column(Unicode(64))

    SOPClas = relationship(u'SOPClas')
    PlanSetup = relationship(u'PlanSetup')
    Series = relationship(u'Series')


class Radiation(Base):
    __tablename__ = 'Radiation'
    __table_args__ = (
        Index('XIE2Radiation', 'PlanSetupSer', 'RadiationSer'),
    )

    RadiationSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), index=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), nullable=False)
    RadiationId = Column(Unicode(16), nullable=False)
    RadiationName = Column(Unicode(64))
    RadiationType = Column(Unicode(32), nullable=False)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    RadiationNumber = Column(Integer, nullable=False)
    TechniqueLabel = Column(Unicode(64))
    RadiationOrder = Column(Integer)
    RefImageSer = Column(ForeignKey(u'Image.ImageSer'), index=True)
    SetupNote = Column(Unicode(254))
    RefImageUID = Column(Unicode(64))
    RefImageSOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), index=True)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))

    PlanSetup = relationship(u'PlanSetup')
    SOPClas = relationship(u'SOPClas')
    Image = relationship(u'Image')
    RadiationDevice = relationship(u'RadiationDevice')


class BrachyField(Radiation):
    __tablename__ = 'BrachyField'

    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), primary_key=True)
    ChannelSer = Column(ForeignKey(u'Channel.ChannelSer'), index=True)
    BrachyApplicatorSer = Column(ForeignKey(u'BrachyApplicator.BrachyApplicatorSer'), index=True)
    BrachyFieldTypeInfo = Column(Unicode(32))
    ApplicatorLength = Column(Float(53))
    PlannedTreatmDateTime = Column(DateTime)
    StepSize = Column(Float(53))
    FirstSourcePosition = Column(Float(53))
    LastSourcePosition = Column(Float(53))
    AutomaticPosFlag = Column(Integer)
    BrachySolidApplicatorSer = Column(ForeignKey(u'BrachySolidApplicator.BrachySolidApplicatorSer'), index=True)
    ApplicatorPartChannelUID = Column(Integer)

    BrachyApplicator = relationship(u'BrachyApplicator')
    BrachySolidApplicator = relationship(u'BrachySolidApplicator')
    Channel = relationship(u'Channel')


class ExternalFieldCommon(Radiation):
    __tablename__ = 'ExternalFieldCommon'

    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), primary_key=True)
    Meterset = Column(Float(53))
    MetersetPerGy = Column(Float(53))
    TreatmentTime = Column(Float(53))
    SetupFieldFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    MotionCompSource = Column(Unicode(254))
    MotionCompTechnique = Column(Unicode(254))
    SetupTechnique = Column(Unicode(16))
    SSD = Column(Float(53))
    SourceFieldEntryDistance = Column(Float(53))
    CouchLat = Column(Float(53))
    CouchLatDelta = Column(Float(53))
    CouchLng = Column(Float(53))
    CouchLngDelta = Column(Float(53))
    CouchVrt = Column(Float(53))
    CouchVrtDelta = Column(Float(53))
    PatientSupportAngle = Column(Float(53))
    TableTopPitchAngle = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    TableTopRollAngle = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    IDUPosLat = Column(Float(53))
    IDUPosLng = Column(Float(53))
    IDUPosVrt = Column(Float(53))
    IDURtn = Column(Float(53))
    IsoCenterPositionX = Column(Float(53))
    IsoCenterPositionY = Column(Float(53))
    IsoCenterPositionZ = Column(Float(53))
    TechniqueSer = Column(ForeignKey(u'Technique.TechniqueSer'), index=True)
    EnergyModeSer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), index=True)
    ToleranceSer = Column(ForeignKey(u'Tolerance.ToleranceSer'), index=True)

    EnergyMode = relationship(u'EnergyMode')
    Technique = relationship(u'Technique')
    Tolerance = relationship(u'Tolerance')


class ExternalField(ExternalFieldCommon):
    __tablename__ = 'ExternalField'

    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), primary_key=True)
    GantryRtn = Column(Float(53))
    CollRtn = Column(Float(53))
    CollMode = Column(Unicode(16))
    CollX1 = Column(Float(53))
    CollY1 = Column(Float(53))
    CollX2 = Column(Float(53))
    CollY2 = Column(Float(53))
    TimepGy = Column(Float(53))
    GantryRtnDirection = Column(Unicode(16))
    GantryRtnExt = Column(Unicode(16))
    DoseRate = Column(Integer)
    StopAngle = Column(Float(53))
    WedgeDose = Column(Float(53))
    BEVMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    CollMarginBottom = Column(Float(53))
    CalculationLog = Column(UnicodeText(1073741823))
    CalculationLogLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    DirectionPointDistance = Column(Float(53))
    EllipticalMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    FldNormFactor = Column(Float(53))
    FldNormMethod = Column(Unicode(64))
    CollMarginLeft = Column(Float(53))
    MUCoeff = Column(Float(53))
    MUCoeffMWOpen = Column(Float(53))
    MUCoeffMWWedged = Column(Float(53))
    MUCoeffMWVirtual = Column(Float(53))
    OptimizeCollRtnFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    SkinFlashFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DRRTemplateFileName = Column(Unicode(254))
    RefDose = Column(Float(53))
    RefDoseMWOpen = Column(Float(53))
    RefDoseMWWedged = Column(Float(53))
    RefDoseMWVirtual = Column(Float(53))
    CollMarginRight = Column(Float(53))
    CollMarginTop = Column(Float(53))
    WedgeWeightFactor = Column(Float(53))
    WeightFactor = Column(Float(53))
    TrackingSer = Column(ForeignKey(u'Tracking.TrackingSer'), index=True)
    DesiredDoseAtIsocenter = Column(Float(53))
    MuCoeffUnit = Column(Unicode(16))

    Tracking = relationship(u'Tracking')


class FieldProton(ExternalField):
    __tablename__ = 'FieldProton'

    RadiationSer = Column(ForeignKey(u'ExternalField.RadiationSer'), primary_key=True)
    AirGap = Column(Float(53))
    FieldModifiersSet = Column(Unicode(64))
    DistalEndDistance = Column(Float(53))
    DistalEndEnergy = Column(Float(53))
    IsocenterMarginFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PrimaryRadiationSer = Column(ForeignKey(u'FieldProton.RadiationSer'), index=True)
    ProximalEndDistance = Column(Float(53))
    SnoutPositionInputFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    TargetUncertaintyMarginX1 = Column(Float(53))
    TargetUncertaintyMarginX2 = Column(Float(53))
    TargetUncertaintyMarginY1 = Column(Float(53))
    TargetUncertaintyMarginY2 = Column(Float(53))
    VirtualSADX = Column(Float(53), nullable=False)
    VirtualSADY = Column(Float(53), nullable=False)
    BeamCurrModulationId = Column(Unicode(16))
    BeamlineDataTableVers = Column(Unicode(16))
    BeamlineSettingsId = Column(Unicode(64))
    SOBPWidth = Column(Float(53))
    HeadFixationAngle = Column(Float(53))
    FixLightPolarPos = Column(Float(53))
    FixLightAzimuthAngle = Column(Float(53))
    WedgeOrientation = Column(Float(53))
    WedgeThinEdgePos = Column(Float(53))
    Status = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SnoutFitPosition = Column(Float(53))
    UserPreselectedSOBP = Column(SmallInteger)
    UserPreselectedRange = Column(SmallInteger)
    SpotListFile = Column(Unicode(254))
    ScanningTechnique = Column(SmallInteger)

    parent = relationship(u'FieldProton', remote_side=[RadiationSer])


class RadiationDeliverySetupDevice(Base):
    __tablename__ = 'RadiationDeliverySetupDevice'

    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), primary_key=True, nullable=False)
    DeliverySetupDeviceSer = Column(ForeignKey(u'DeliverySetupDevice.DeliverySetupDeviceSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger, nullable=False, unique=True)
    CustomCode = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    DeliverySetupDevice = relationship(u'DeliverySetupDevice')
    Radiation = relationship(u'Radiation')


class RadiationHstry(Base):
    __tablename__ = 'RadiationHstry'

    RadiationHstrySer = Column(BigInteger, primary_key=True)
    TreatmentRecordSer = Column(ForeignKey(u'TreatmentRecord.TreatmentRecordSer'), nullable=False, index=True)
    RadiationHstryType = Column(Unicode(32), nullable=False)
    TreatmentDeliveryType = Column(Unicode(16))
    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), nullable=False, index=True)
    RadiationId = Column(Unicode(16), nullable=False)
    RadiationName = Column(Unicode(64))
    RadiationNumber = Column(Integer)
    TechniqueLabel = Column(Unicode(64))
    RadiationType = Column(Unicode(16))
    TreatmentStartTime = Column(DateTime, nullable=False, index=True)
    TreatmentEndTime = Column(DateTime, nullable=False, index=True)
    TreatmentTime = Column(Float(53))
    TreatmentTimeOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    TerminationStatus = Column(Unicode(16), nullable=False)
    FractionNumber = Column(Integer, nullable=False)
    ApprovalDate = Column(DateTime)
    ApprovalUserName = Column(Unicode(32))
    UserName1 = Column(Unicode(64))
    UserName2 = Column(Unicode(32))
    UserName3 = Column(Unicode(32))
    OverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NoOfImage = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    PrintFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RVFlag = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    HistoryNote = Column(Unicode)
    MachineNote = Column(Unicode)
    FieldSetupNote = Column(Unicode)
    BeamOffCode = Column(Unicode(64))

    Radiation = relationship(u'Radiation')
    TreatmentRecord = relationship(u'TreatmentRecord')


class ExternalFieldCommonHstry(RadiationHstry):
    __tablename__ = 'ExternalFieldCommonHstry'

    RadiationHstrySer = Column(ForeignKey(u'RadiationHstry.RadiationHstrySer'), primary_key=True)
    PlannedMeterset = Column(Float(53))
    ActualMeterset = Column(Float(53))
    MetersetOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SSD = Column(Float(53))
    CouchCorrectionLat = Column(Float(53))
    CouchCorrectionLng = Column(Float(53))
    CouchCorrectionVrt = Column(Float(53))
    CouchLat = Column(Float(53))
    CouchLatOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CouchLatPlanned = Column(Float(53))
    CouchLng = Column(Float(53))
    CouchLngOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CouchLngPlanned = Column(Float(53))
    CouchVrt = Column(Float(53))
    CouchVrtOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CouchVrtPlanned = Column(Float(53))
    TableTopEccAngleOverFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    TableTopEccentricAngle = Column(Float(53))
    PatientSupportAngle = Column(Float(53))
    PatientSupportAngleOverFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    PatSupPitchOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    PatSupportPitchAngle = Column(Float(53))
    PatSupportRollAngle = Column(Float(53))
    PatSupRollOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    PFFlag = Column(String(1, u'Latin1_General_BIN2'))
    PFMUSubFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    PIFlag = Column(String(1, u'Latin1_General_BIN2'))
    ToleranceSer = Column(ForeignKey(u'Tolerance.ToleranceSer'), index=True)
    NominalEnergy = Column(Integer)
    EnergyModeOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SSDOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))

    Tolerance = relationship(u'Tolerance')


class ExternalFieldHstry(ExternalFieldCommonHstry):
    __tablename__ = 'ExternalFieldHstry'

    RadiationHstrySer = Column(ForeignKey(u'ExternalFieldCommonHstry.RadiationHstrySer'), primary_key=True)
    ResourceSer = Column(ForeignKey(u'ExternalBeam.ResourceSer'), index=True)
    IntendedNumOfPaintings = Column(Integer)
    NumOfPaintOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Technique = Column(Unicode(16))
    GantryRtn = Column(Float(53))
    GantryRtnOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CollRtn = Column(Float(53))
    CollRtnOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CollMode = Column(Unicode(16))
    CollX1 = Column(Float(53))
    CollX1OverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CollY1 = Column(Float(53))
    CollY1OverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CollX2 = Column(Float(53))
    CollX2OverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    CollY2 = Column(Float(53))
    CollY2OverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    PSACorrection = Column(Float(53))
    OffPlaneAngle = Column(Float(53))
    WedgeAngle = Column(Float(53))
    WedgeDirection = Column(Float(53))
    DoseRate = Column(Integer)
    DoseRateOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    WedgeDose = Column(Float(53))
    WedgeDoseOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    StopAngle = Column(Float(53))
    MUpDeg = Column(Float(53))
    MUpDegOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SnoutPosition = Column(Float(53))
    SnoutPosOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    FixLightPolarPos = Column(Float(53))
    FixLightAzimuthAngle = Column(Float(53))
    GantryRtnDirection = Column(Unicode(16))
    GantryRtnExt = Column(Unicode(16))
    DistalEndEnergy = Column(Float(53))
    SOBPWidth = Column(Float(53))
    BeamModifiersSet = Column(Unicode(64))
    WedgeNumber1 = Column(Integer)
    WedgeNumber2 = Column(Integer)
    WedgeAngle2 = Column(Float(53))
    WedgeDirection2 = Column(Float(53))
    BeamCurrentModulationId = Column(Unicode(16))

    ExternalBeam = relationship(u'ExternalBeam')


class BrachyFieldHstry(RadiationHstry):
    __tablename__ = 'BrachyFieldHstry'

    RadiationHstrySer = Column(ForeignKey(u'RadiationHstry.RadiationHstrySer'), primary_key=True)
    BrachyTreatmentType = Column(Unicode(16), nullable=False)
    ChannelNumber = Column(Integer, nullable=False)
    ChannelLength = Column(Float(53), nullable=False)
    SpecifiedChannelTotalTime = Column(Float(53), nullable=False)
    ChannelReferenceAirKerma = Column(Float(53), nullable=False)
    DeliveredChannelTotalTime = Column(Float(53), nullable=False)
    SpecifiedNumberOfPulses = Column(Integer)
    DeliveredNumberOfPulses = Column(Integer)
    SpecifiedPulseRepetitionInterval = Column(Float(53))
    DeliveredPulseRepetitionInterval = Column(Float(53))
    SourceSerialNumber = Column(Unicode(64))
    SourceIsotopeName = Column(Unicode(64), nullable=False)
    ReferenceAirKermaRate = Column(Float(53), nullable=False)
    SourceStrengthReferenceDateTime = Column(DateTime, nullable=False)
    NumberOfSourcePositions = Column(Integer, nullable=False)


class RadiationRefPoint(Base):
    __tablename__ = 'RadiationRefPoint'

    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), primary_key=True, nullable=False)
    RefPointSer = Column(ForeignKey(u'RefPoint.RefPointSer'), primary_key=True, nullable=False, index=True)
    RTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    FieldDose = Column(Float(53))
    DoseSpecificationFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Depth = Column(Float(53))
    PSSD = Column(Float(53))
    DominantFieldFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    NominalFlag = Column(Integer, nullable=False)

    RTPlan = relationship(u'RTPlan')
    Radiation = relationship(u'Radiation')
    RefPoint = relationship(u'RefPoint')


class RadioactiveSource(Base):
    __tablename__ = 'RadioactiveSource'

    RadioactiveSourceSer = Column(BigInteger, primary_key=True)
    RadioactiveSourceModelSer = Column(ForeignKey(u'RadioactiveSourceModel.RadioactiveSourceModelSer'), nullable=False, index=True)
    ResourceSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), index=True)
    RadioactiveSourceId = Column(Unicode(16), nullable=False)
    RadioactiveSourceName = Column(Unicode(64))
    SourceNumber = Column(Integer)
    SourceSerialNo = Column(Unicode(64))
    SourceStrength = Column(Float(53))
    CalibrationDate = Column(DateTime)
    Comment = Column(Unicode(254))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    RadioactiveSourceModel = relationship(u'RadioactiveSourceModel')
    RadiationDevice = relationship(u'RadiationDevice')


class RadioactiveSourceModel(Base):
    __tablename__ = 'RadioactiveSourceModel'

    RadioactiveSourceModelSer = Column(BigInteger, primary_key=True)
    RadioactiveSourceModelId = Column(Unicode(16), nullable=False)
    RadioactiveSourceModelName = Column(Unicode(64))
    RadioIsotopType = Column(Unicode(64))
    HalfTime = Column(Float(53))
    ManufacturerName = Column(Unicode(64))
    SourceType = Column(Unicode(16))
    ActivityConversionFact = Column(Float(53))
    DoseRateConstant = Column(Float(53))
    ActiveSize = Column(BINARY(24))
    TotalSize = Column(BINARY(24))
    AnisotropyTable = Column(Unicode(254))
    DoseCalcModel = Column(Unicode(16))
    RadDoseFunctionType = Column(Unicode(32))
    RadDoseFunctionNoOfValues = Column(Integer)
    RadDoseFunctionValuesX = Column(VARBINARY(240))
    RadDoseFunctionValuesY = Column(VARBINARY(240))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))


class Recipient(Base):
    __tablename__ = 'Recipient'

    MessageSer = Column(ForeignKey(u'Message.MessageSer'), primary_key=True, nullable=False)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True, nullable=False, index=True)
    ReadFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DeletedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RepliedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Message = relationship(u'Message')
    Resource = relationship(u'Resource')


class RecurrenceElement(Base):
    __tablename__ = 'RecurrenceElement'

    RecurrenceElementSer = Column(BigInteger, primary_key=True)
    RecurrenceRuleSer = Column(ForeignKey(u'RecurrenceRule.RecurrenceRuleSer'), nullable=False, index=True)
    ElementType = Column(Integer, nullable=False)
    ElementValue = Column(Integer, nullable=False)

    RecurrenceRule = relationship(u'RecurrenceRule')


class RecurrenceRule(Base):
    __tablename__ = 'RecurrenceRule'

    RecurrenceRuleSer = Column(BigInteger, primary_key=True)
    Frequency = Column(Integer, nullable=False)
    EndCondition = Column(Integer, nullable=False)
    NoOfRecurrences = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Interval = Column(Integer)
    StartDateTime = Column(DateTime, nullable=False)
    EndDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class RefPoint(Base):
    __tablename__ = 'RefPoint'
    __table_args__ = (
        Index('XAK1RefPoint', 'PatientSer', 'RefPointId', unique=True),
        Index('XAKRefPoint', 'PatientVolumeSer', 'RefPointId', unique=True)
    )

    RefPointSer = Column(BigInteger, primary_key=True)
    PatientVolumeSer = Column(ForeignKey(u'PatientVolume.PatientVolumeSer'), nullable=False)
    PatientSer = Column(BigInteger, nullable=False)
    RefPointId = Column(Unicode(16), nullable=False)
    RefPointName = Column(Unicode(64))
    RefPointUID = Column(Unicode(64), nullable=False, unique=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_UID_DEF]
	AS '0'"""))
    RefPointType = Column(Unicode(16))
    TotalDoseLimit = Column(Float(53))
    DailyDoseLimit = Column(Float(53))
    SessionDoseLimit = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    PatientVolume = relationship(u'PatientVolume')


t_RefPointDeliveredDose = Table(
    'RefPointDeliveredDose', metadata,
    Column('RefPointSer', BigInteger, nullable=False),
    Column('TotDeliveredDose', Float(53))
)


class RefPointHstry(Base):
    __tablename__ = 'RefPointHstry'
    __table_args__ = (
        Index('XAK1RefPointHstry', 'RefPointSer', 'RadiationHstrySer', unique=True),
    )

    RefPointHstrySer = Column(BigInteger, primary_key=True)
    RadiationHstrySer = Column(ForeignKey(u'RadiationHstry.RadiationHstrySer'), nullable=False, index=True)
    RefPointSer = Column(ForeignKey(u'RefPoint.RefPointSer'), nullable=False)
    ActualDose = Column(Float(53))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    RadiationHstry = relationship(u'RadiationHstry')
    RefPoint = relationship(u'RefPoint')


class RefPointLocation(Base):
    __tablename__ = 'RefPointLocation'

    ImageSer = Column(ForeignKey(u'Image.ImageSer'), primary_key=True, nullable=False)
    RefPointSer = Column(ForeignKey(u'RefPoint.RefPointSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    RefPointLocationType = Column(Unicode(32))
    Location = Column(BINARY(24))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Image = relationship(u'Image')
    RefPoint = relationship(u'RefPoint')


class RefPointLog(Base):
    __tablename__ = 'RefPointLog'

    RefPointLogSer = Column(BigInteger, primary_key=True)
    DoseCorrectionLogSer = Column(ForeignKey(u'DoseCorrectionLog.DoseCorrectionLogSer'), index=True)
    RefPointSer = Column(ForeignKey(u'RefPoint.RefPointSer'), nullable=False, index=True)
    ModificationType = Column(Unicode(32), nullable=False)
    ModificationDate = Column(DateTime, nullable=False)
    DoseDelta = Column(Float(53))
    OvrdAuthorizedName = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    DoseCorrectionLog = relationship(u'DoseCorrectionLog')
    RefPoint = relationship(u'RefPoint')


class RefWaveformField(Base):
    __tablename__ = 'RefWaveformField'

    RefWaveformRelationSer = Column(ForeignKey(u'RefWaveformRelation.RefWaveformRelationSer'), primary_key=True, nullable=False)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ExternalFieldCommon = relationship(u'ExternalFieldCommon')
    RefWaveformRelation = relationship(u'RefWaveformRelation')


class RefWaveformRelation(Base):
    __tablename__ = 'RefWaveformRelation'

    RefWaveformRelationSer = Column(BigInteger, primary_key=True)
    TrackingSer = Column(ForeignKey(u'Tracking.TrackingSer'), nullable=False, index=True)
    ReferenceWaveformSer = Column(ForeignKey(u'Tracking.TrackingSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Tracking = relationship(u'Tracking', primaryjoin='RefWaveformRelation.ReferenceWaveformSer == Tracking.TrackingSer')
    Tracking1 = relationship(u'Tracking', primaryjoin='RefWaveformRelation.TrackingSer == Tracking.TrackingSer')


class ReminderAck(Base):
    __tablename__ = 'ReminderAck'

    ReminderAckSer = Column(BigInteger, primary_key=True)
    AttendeeSer = Column(ForeignKey(u'Attendee.AttendeeSer'), nullable=False, index=True)
    ReminderAckFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ReminderAckDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False)
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Attendee = relationship(u'Attendee')


class Report(Base):
    __tablename__ = 'Report'

    ReportSer = Column(BigInteger, primary_key=True)
    AppUserSer = Column(ForeignKey(u'AppUser.AppUserSer'), nullable=False, index=True)
    ReportName = Column(Unicode(254), nullable=False)
    DerivedFromReportSer = Column(ForeignKey(u'Report.ReportSer'), index=True)
    ProcedureName = Column(Unicode(64), nullable=False)
    Description = Column(Unicode(254))
    ReportCategory = Column(Unicode(64))
    ReportAccess = Column(Unicode(64), nullable=False)
    ReportType = Column(Unicode(64), nullable=False)
    FSRptFileName = Column(Unicode(254), nullable=False)
    FSSchFileName = Column(Unicode(254), nullable=False)
    SchemaName = Column(Unicode(64), nullable=False)
    ReportFileName = Column(Unicode(64), nullable=False)
    LanguageId = Column(Unicode(16), nullable=False)
    EditFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    EnabledFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ReportVersion = Column(Unicode(16), nullable=False)
    SchemaVersion = Column(Unicode(16), nullable=False)
    ReportValidation = Column(Unicode(16), nullable=False)
    DerivedFromReportVersion = Column(Unicode(16))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ProcedureDatabaseType = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_CODEVALUE_DEF]
	AS 0"""))

    AppUser = relationship(u'AppUser')
    parent = relationship(u'Report', remote_side=[ReportSer])


class ReportLinkage(Base):
    __tablename__ = 'ReportLinkage'

    ReportLinkageSer = Column(BigInteger, primary_key=True)
    ReportSer = Column(ForeignKey(u'Report.ReportSer'), nullable=False, index=True)
    SubReportSer = Column(ForeignKey(u'Report.ReportSer'), nullable=False, index=True)
    EnabledFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Report = relationship(u'Report', primaryjoin='ReportLinkage.ReportSer == Report.ReportSer')
    Report1 = relationship(u'Report', primaryjoin='ReportLinkage.SubReportSer == Report.ReportSer')


class ReportParameter(Base):
    __tablename__ = 'ReportParameter'

    ReportParameterSer = Column(BigInteger, primary_key=True)
    ReportSer = Column(ForeignKey(u'Report.ReportSer'), nullable=False, index=True)
    ParameterTypeSer = Column(ForeignKey(u'ParameterType.ParameterTypeSer'), nullable=False, index=True)
    EnabledStatus = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    EnabledDefaultFlag = Column(Integer)
    ReportColumn = Column(Unicode(64), nullable=False)
    ParameterName1 = Column(Unicode(64), nullable=False)
    ParameterName2 = Column(Unicode(64))
    ParameterName3 = Column(Unicode(64))
    ParameterName4 = Column(Unicode(64))
    ParameterName5 = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ParameterType = relationship(u'ParameterType')
    Report = relationship(u'Report')


class Resource(Base):
    __tablename__ = 'Resource'

    ResourceSer = Column(BigInteger, primary_key=True)
    ResourceTypeNum = Column(ForeignKey(u'ResourceType.ResourceTypeNum'), nullable=False, index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ResourceType = Column(Unicode(30), nullable=False)
    SchedulableFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), index=True)
    WorklistType = Column(Unicode(64))
    AETitle = Column(Unicode(16))
    MultiProtocolFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))

    DICOMCodeValue = relationship(u'DICOMCodeValue')
    ResourceType1 = relationship(u'ResourceType')


class Doctor(Resource):
    __tablename__ = 'Doctor'
    __table_args__ = (
        Index('XIE1Doctor', 'LastName', 'FirstName', 'MiddleName', 'OncologistFlag'),
        Index('XIE2Doctor', 'OncologistFlag', 'LastName', 'FirstName', 'MiddleName')
    )

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True)
    DoctorId = Column(Unicode(16), nullable=False, unique=True)
    Honorific = Column(Unicode(16))
    FirstName = Column(Unicode(64), nullable=False)
    MiddleName = Column(Unicode(64))
    LastName = Column(Unicode(64), nullable=False)
    NameSuffix = Column(Unicode(16))
    AliasName = Column(Unicode(64), nullable=False, unique=True)
    Specialty = Column(Unicode(64))
    Institution = Column(Unicode(64))
    OncologistFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))


class Staff(Resource):
    __tablename__ = 'Staff'
    __table_args__ = (
        Index('XIE1Staff', 'LastName', 'FirstName', 'MiddleName'),
    )

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True)
    StaffId = Column(Unicode(16), nullable=False, unique=True)
    Honorific = Column(Unicode(16))
    FirstName = Column(Unicode(64), nullable=False)
    MiddleName = Column(Unicode(64))
    LastName = Column(Unicode(64), nullable=False)
    NameSuffix = Column(Unicode(16))
    AliasName = Column(Unicode(64), nullable=False, unique=True)
    Profession = Column(Unicode(64))
    Comment = Column(Unicode(254))
    AdvancedPractitionerFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class Venue(Resource):
    __tablename__ = 'Venue'

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True)
    VenueId = Column(Unicode(16), nullable=False, unique=True)
    VenueType = Column(Unicode(64))
    VenueName = Column(Unicode(64))
    VenueDirections = Column(UnicodeText(1073741823))
    RoomNumber = Column(Unicode(16))
    ScheduleFlag = Column(Integer)
    EquipmentList = Column(UnicodeText(1073741823))
    Comment = Column(Unicode(254))


class Auxiliary(Resource):
    __tablename__ = 'Auxiliary'

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True)
    AuxiliaryId = Column(Unicode(16), nullable=False, unique=True)
    AuxiliaryName = Column(Unicode(64))
    AuxiliaryCode = Column(Unicode(64))


class Machine(Resource):
    __tablename__ = 'Machine'

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True)
    WorkstationSer = Column(ForeignKey(u'Workstation.WorkstationSer'), index=True)
    MachineId = Column(Unicode(16), nullable=False, unique=True)
    MachineName = Column(Unicode(64))
    MachineType = Column(Unicode(30), nullable=False)
    MachineModel = Column(Unicode(64), nullable=False)
    MachineInterface = Column(Unicode(64))
    MachineScale = Column(Unicode(16))
    ManufacturerName = Column(Unicode(254), nullable=False)
    MachineSerialNo = Column(Unicode(64))
    ServiceContact = Column(Unicode(128))
    DateInstalled = Column(DateTime)
    DateLastService = Column(DateTime)
    DateNextService = Column(DateTime)
    OperationStatus = Column(Unicode(32))
    SoftwareVersion = Column(Unicode(32))
    HardwareVersion = Column(Unicode(32))
    Description = Column(Unicode(64))

    Workstation = relationship(u'Workstation')


class RadiationDevice(Machine):
    __tablename__ = 'RadiationDevice'

    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True)
    RadiationDeviceType = Column(Unicode(30), nullable=False)
    Features = Column(Unicode(64))
    CompletelyModelled = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class BrachyUnit(RadiationDevice):
    __tablename__ = 'BrachyUnit'

    ResourceSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), primary_key=True)
    MaxDwellTimePerChannel = Column(Float(53))
    MaxDwellTimePerPos = Column(Float(53))
    MaxDwellTimePerTreatment = Column(Float(53))
    TimeResolution = Column(Float(53))
    SourceMovementType = Column(Unicode(16))
    MinStepSize = Column(Float(53))
    MaxStepSize = Column(Float(53))
    NumOfDwellPosPerChannel = Column(Integer)
    StepSizeResolution = Column(Float(53))
    PosToSourceDist = Column(Float(53))
    DoseRateMode = Column(Unicode(16))
    ExportDirectory = Column(Unicode(254))
    ExportPostProcessor = Column(Unicode(254))


class Simulator(RadiationDevice):
    __tablename__ = 'Simulator'

    ResourceSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), primary_key=True)
    CollMode = Column(Unicode(16))
    BeamTime = Column(Float(53))
    XRayUnit = Column(Unicode(64))


class ExternalBeam(RadiationDevice):
    __tablename__ = 'ExternalBeam'

    ResourceSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), primary_key=True)
    ExternalBeamType = Column(Unicode(30))
    CobaltFlag = Column(Integer, nullable=False)
    BeamAngle = Column(Float(53))
    StopAngle = Column(Float(53))
    CollMode = Column(Unicode(16))
    SAD = Column(Float(53))
    SPD = Column(Float(53))
    PFDefaultEnergySer = Column(ForeignKey(u'EnergyMode.EnergyModeSer'), index=True)
    PFMaxMuAllow = Column(Integer)
    FixedBeamFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ImagerAutoCorrFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ImagerAutoCorrTolerance = Column(Float(53))
    UserPreselectableBeamLine = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DefPortalImagingEnergySer = Column(BigInteger)
    LowPortalImagingEnergySer = Column(BigInteger)
    ConeBeamEnergySer = Column(BigInteger)
    PrimaryDosimeterUnit = Column(Unicode(16), nullable=False)
    ShutterError = Column(Float(53))

    EnergyMode = relationship(u'EnergyMode', primaryjoin='ExternalBeam.PFDefaultEnergySer == EnergyMode.EnergyModeSer')


class PatientSupportDevice(Machine):
    __tablename__ = 'PatientSupportDevice'

    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True)
    PatSupportType = Column(Unicode(16), nullable=False)
    PatientSupportDeviceId = Column(Unicode(16))
    PatientSupportDeviceName = Column(Unicode(64))
    AccessoryCode = Column(Unicode(64))


class MillingMachine(Machine):
    __tablename__ = 'MillingMachine'

    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True)
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class PlanningSystem(Machine):
    __tablename__ = 'PlanningSystem'

    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ImagingDevice(Machine):
    __tablename__ = 'ImagingDevice'

    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), primary_key=True)
    ImagingDeviceType = Column(Unicode(30), nullable=False, index=True)
    ImageModality = Column(Unicode(16), nullable=False)
    Comment = Column(Unicode(254))
    ConeBeamFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class VideoDigitizer(ImagingDevice):
    __tablename__ = 'VideoDigitizer'

    ResourceSer = Column(ForeignKey(u'ImagingDevice.ResourceSer'), primary_key=True)
    DefStorageRes = Column(Integer)
    XYAspectRatio = Column(Float(53))
    VideoBoard = Column(Unicode(64))


class CTScanner(ImagingDevice):
    __tablename__ = 'CTScanner'

    ResourceSer = Column(ForeignKey(u'ImagingDevice.ResourceSer'), primary_key=True)
    CalibrationFile = Column(Unicode(254))
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


class CTSimulator(ImagingDevice):
    __tablename__ = 'CTSimulator'

    ResourceSer = Column(ForeignKey(u'ImagingDevice.ResourceSer'), primary_key=True)
    SimulatorResourceSer = Column(ForeignKey(u'Simulator.ResourceSer'), nullable=False, index=True)
    CalibrationDate = Column(DateTime)
    CollimatorType = Column(Unicode(64))
    MaterialType = Column(Unicode(64))

    Simulator = relationship(u'Simulator')


class PortImager(ImagingDevice):
    __tablename__ = 'PortImager'

    ResourceSer = Column(ForeignKey(u'ImagingDevice.ResourceSer'), primary_key=True)
    ExtBeamResourceSer = Column(ForeignKey(u'ExternalBeam.ResourceSer'), nullable=False, index=True)
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    SAD = Column(Float(53))
    Gantry = Column(Float(53))
    GantryPitch = Column(Float(53))
    RadSourceGantryDelta = Column(Float(53))

    ExternalBeam = relationship(u'ExternalBeam')


class SimulationImager(ImagingDevice):
    __tablename__ = 'SimulationImager'

    ResourceSer = Column(ForeignKey(u'ImagingDevice.ResourceSer'), primary_key=True)
    SimulatorResourceSer = Column(ForeignKey(u'Simulator.ResourceSer'), nullable=False, unique=True)
    CalibrationAccuracy = Column(Unicode(32))
    CalibrationDate = Column(DateTime)
    ExposureTime = Column(Float(53))
    VideoBoard = Column(Unicode(64))
    NoOfXLines = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    NoOfYLines = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ResolutionX = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    ResolutionY = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))

    Simulator = relationship(u'Simulator')


class LocalizationJig(ImagingDevice):
    __tablename__ = 'LocalizationJig'

    ResourceSer = Column(ForeignKey(u'ImagingDevice.ResourceSer'), primary_key=True)
    ImagingGeometry = Column(Unicode(32))
    Beam1Label = Column(Unicode(64))
    Beam1FocusToFilmDist = Column(Float(53))
    Beam1IsocenterToFilmDist = Column(Float(53))
    Beam1Angle = Column(Float(53))
    Beam1FilmToJigDist = Column(Float(53))
    Beam1JigSize = Column(Float(53))
    Beam1JigCrossSize = Column(Float(53))
    Beam1JigCrossAngle = Column(Float(53))
    Beam1JigCrossShift = Column(Float(53))
    Beam2Label = Column(Unicode(64))
    Beam2FocusToFilmDist = Column(Float(53))
    Beam2IsocenterToFilmDist = Column(Float(53))
    Beam2Angle = Column(Float(53))
    Beam2FilmToJigDist = Column(Float(53))
    Beam2JigSize = Column(Float(53))
    Beam2JigCrossSize = Column(Float(53))
    Beam2JigCrossAngle = Column(Float(53))
    Beam2JigCrossShift = Column(Float(53))
    Plane = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    Beam1FocusToFilmDistFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Beam2FocusToFilmDistFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))


class Workspace(Resource):
    __tablename__ = 'Workspace'

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True)
    WorkspaceId = Column(Unicode(32), nullable=False)
    VarianWorkspaceFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))


t_ResourceActivity = Table(
    'ResourceActivity', metadata,
    Column('ScheduledActivitySer', BigInteger, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('ExclusiveFlag', Integer, nullable=False),
    Column('PrimaryFlag', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


class ResourceAddres(Base):
    __tablename__ = 'ResourceAddress'

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True, nullable=False)
    AddressSer = Column(ForeignKey(u'Address.AddressSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    POCName = Column(Unicode(254))
    PrimaryFlag = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Addres = relationship(u'Addres')
    Resource = relationship(u'Resource')


class ResourceDepartment(Base):
    __tablename__ = 'ResourceDepartment'
    __table_args__ = (
        Index('XAK1ResourceDepartment', 'ResourceSer', 'DepartmentSer', unique=True),
    )

    ResourceDepartmentSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), nullable=False, index=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), nullable=False)
    DefaultDepartment = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    AssignedToDepartment = Column(Integer, nullable=False)
    AccessRights = Column(Unicode(32), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')
    Resource = relationship(u'Resource')


class ResourceGroup(Base):
    __tablename__ = 'ResourceGroup'
    __table_args__ = (
        Index('XAK1ResourceGroup', 'ResourceGroupCode', 'DepartmentSer', unique=True),
    )

    ResourceGroupSer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    ResourceGroupCode = Column(Unicode(64), nullable=False)
    GroupType = Column(Unicode(32), nullable=False)
    DerivedFromResourceGroupSer = Column(BigInteger)
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    DICOMCodeValueSer = Column(ForeignKey(u'DICOMCodeValue.DICOMCodeValueSer'), index=True)
    WorklistType = Column(Unicode(64))

    DICOMCodeValue = relationship(u'DICOMCodeValue')
    Department = relationship(u'Department')


class ResourceIdentifier(Base):
    __tablename__ = 'ResourceIdentifier'

    ResourceIdentifierSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), nullable=False, index=True)
    ResourceIdentifierTypeSer = Column(ForeignKey(u'ResourceIdentifierType.ResourceIdentifierTypeSer'), nullable=False, index=True)
    KeyValue = Column(Unicode(30), nullable=False)
    UpperKeyValue = Column(Unicode(30), nullable=False)
    CurValueFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    ValidEntryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    EffDate = Column(DateTime, nullable=False)
    ExpiryDate = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ResourceIdentifierType = relationship(u'ResourceIdentifierType')
    Resource = relationship(u'Resource')


class ResourceIdentifierType(Base):
    __tablename__ = 'ResourceIdentifierType'

    ResourceIdentifierTypeSer = Column(BigInteger, primary_key=True)
    ResourceTypeNum = Column(ForeignKey(u'ResourceType.ResourceTypeNum'), nullable=False, index=True)
    ResourceDescription = Column(Unicode(100), nullable=False)
    ActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    RequiredFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    UniqueFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    UniqueHistoryFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    CodeType = Column(Integer)
    SSCodeValue = Column(Unicode(6))

    ResourceType = relationship(u'ResourceType')


class ResourceType(Base):
    __tablename__ = 'ResourceType'

    ResourceTypeNum = Column(Integer, primary_key=True)
    ResourceTypeCode = Column(Unicode(64), nullable=False, unique=True)
    ExclusiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    NoEditFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ResourceVenue(Base):
    __tablename__ = 'ResourceVenue'

    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), primary_key=True, nullable=False)
    VenueResourceSer = Column(ForeignKey(u'Venue.ResourceSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    HstryTimeStamp = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Resource = relationship(u'Resource')
    Venue = relationship(u'Venue')


class SOPClas(Base):
    __tablename__ = 'SOPClass'

    SOPClassSer = Column(BigInteger, primary_key=True)
    SOPClassUID = Column(Unicode(64), nullable=False)
    Name = Column(Unicode(128))
    Category = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class STTFile(Base):
    __tablename__ = 'STTFile'
    __table_args__ = (
        Index('XAKSTTFile', 'AddOnSer', 'FileId', unique=True),
    )

    STTFileSer = Column(BigInteger, primary_key=True)
    AddOnSer = Column(ForeignKey(u'DynamicWedge.AddOnSer'), nullable=False)
    FileId = Column(Unicode(16), nullable=False)
    FileName = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    DynamicWedge = relationship(u'DynamicWedge')


class ScheduleHoliday(Base):
    __tablename__ = 'ScheduleHoliday'
    __table_args__ = (
        Index('XAK1ScheduleHoliday', 'HolidayId', 'DepartmentSer', unique=True),
    )

    HolidaySer = Column(BigInteger, primary_key=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    HolidayId = Column(Unicode(16), nullable=False)
    HolidayName = Column(Unicode(32), nullable=False)
    StartDateTime = Column(DateTime, nullable=False, index=True)
    EndDateTime = Column(DateTime, nullable=False)
    RecurrenceRuleSer = Column(ForeignKey(u'RecurrenceRule.RecurrenceRuleSer'), nullable=False, index=True)
    HsptlBusShutdown = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Department = relationship(u'Department')
    RecurrenceRule = relationship(u'RecurrenceRule')


class ScheduledActivity(Base):
    __tablename__ = 'ScheduledActivity'
    __table_args__ = (
        Index('XIE8ScheduledActivity', 'ScheduledActivityCode', 'ObjectStatus'),
        Index('XIE2Event', 'ScheduledStartTime', 'ScheduledEndTime')
    )

    ScheduledActivitySer = Column(BigInteger, primary_key=True)
    ScheduledActivityRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    CreatedByResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    CreatedByUserName = Column(Unicode(32), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreatedByHL7 = Column(Unicode(32))
    UID = Column(Unicode(64), nullable=False, unique=True)
    ScheduledStartTime = Column(DateTime, index=True)
    ScheduledEndTime = Column(DateTime)
    ActualStartDate = Column(DateTime)
    ActualEndDate = Column(DateTime)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ScheduledActivityCode = Column(Unicode(64))
    Priority = Column(Unicode(64))
    WaitListedFlag = Column(Integer, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ActivityNote = Column(Unicode(254))
    RecurrenceRuleSer = Column(ForeignKey(u'RecurrenceRule.RecurrenceRuleSer'), index=True)
    ReadByAppUserName = Column(Unicode(32))
    ReadByDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PreMedication = Column(Unicode(64))
    ContrastAgent = Column(Unicode(64))
    WorkFlowActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))

    ActivityInstance = relationship(u'ActivityInstance')
    Resource = relationship(u'Resource')
    Patient = relationship(u'Patient')
    RecurrenceRule = relationship(u'RecurrenceRule')


class ScheduledActivityMH(Base):
    __tablename__ = 'ScheduledActivityMH'
    __table_args__ = (
        Index('XIE1ScheduledActivityMH', 'ActivityInstanceSer', 'ActivityInstanceRevCount'),
    )

    ScheduledActivitySer = Column(ForeignKey(u'ScheduledActivity.ScheduledActivitySer'), primary_key=True, nullable=False)
    ScheduledActivityRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ActivityInstanceSer = Column(BigInteger, nullable=False)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(BigInteger)
    CreatedByResourceSer = Column(BigInteger)
    CreatedByUserName = Column(Unicode(32), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreatedByHL7 = Column(Unicode(32))
    UID = Column(Unicode(64), nullable=False)
    ScheduledStartTime = Column(DateTime)
    ScheduledEndTime = Column(DateTime)
    ActualStartDate = Column(DateTime)
    ActualEndDate = Column(DateTime)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    ScheduledActivityCode = Column(Unicode(64))
    Priority = Column(Unicode(64))
    WaitListedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ActivityNote = Column(Unicode(254))
    RecurrenceRuleSer = Column(BigInteger)
    ReadByAppUserName = Column(Unicode(32))
    ReadByDateTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PreMedication = Column(Unicode(64))
    ContrastAgent = Column(Unicode(64))
    WorkFlowActiveFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))

    ScheduledActivity = relationship(u'ScheduledActivity')


class ScheduledObjectPointer(Base):
    __tablename__ = 'ScheduledObjectPointer'

    ScheduledProcedureSer = Column(ForeignKey(u'ScheduledProcedure.ScheduledProcedureSer'), primary_key=True, nullable=False)
    ObjectPointerSer = Column(ForeignKey(u'ObjectPointer.ObjectPointerSer'), primary_key=True, nullable=False, index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ObjectPointer = relationship(u'ObjectPointer')
    ScheduledProcedure = relationship(u'ScheduledProcedure')


class ScheduledPerformedProcedure(Base):
    __tablename__ = 'ScheduledPerformedProcedure'

    ScheduledProcedureSer = Column(ForeignKey(u'ScheduledProcedure.ScheduledProcedureSer'), primary_key=True, nullable=False)
    PerformedProcedureSer = Column(ForeignKey(u'PerformedProcedure.PerformedProcedureSer'), primary_key=True, nullable=False, index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PerformedProcedure = relationship(u'PerformedProcedure')
    ScheduledProcedure = relationship(u'ScheduledProcedure')


class ScheduledProcedure(Base):
    __tablename__ = 'ScheduledProcedure'

    ScheduledProcedureSer = Column(BigInteger, primary_key=True)
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    ActivityInstanceRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AttendeeSer = Column(ForeignKey(u'Attendee.AttendeeSer'), index=True)
    AttendeeRevCount = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    Status = Column(Unicode(16))
    ScheduledProcedureUID = Column(Unicode(64), nullable=False)
    ScheduledProcedureId = Column(Unicode(16), nullable=False)
    ScheduledStartDateTime = Column(DateTime)
    ScheduledEndDateTime = Column(DateTime)
    ExportedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Priority = Column(Unicode(16))
    InputAvailability = Column(Unicode(16))
    ProcedureStepLabel = Column(Unicode(64), nullable=False)
    WorklistLabel = Column(Unicode(64))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActivityInstance = relationship(u'ActivityInstance')
    Attendee = relationship(u'Attendee')


class ScheduledProcedureItem(Base):
    __tablename__ = 'ScheduledProcedureItem'

    ScheduledProcedureItemSer = Column(BigInteger, primary_key=True)
    ScheduledProcedureSer = Column(ForeignKey(u'ScheduledProcedure.ScheduledProcedureSer'), nullable=False, index=True)
    ProcedureItemSer = Column(ForeignKey(u'ProcedureItem.ProcedureItemSer'), nullable=False, index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ProcedureItem = relationship(u'ProcedureItem')
    ScheduledProcedure = relationship(u'ScheduledProcedure')


class Series(Base):
    __tablename__ = 'Series'
    __table_args__ = (
        Index('XIE3Series', 'StudySer', 'SeriesSer'),
        Index('XIE2Series', 'FrameOfReferenceUID', 'SeriesSer')
    )

    SeriesSer = Column(BigInteger, primary_key=True)
    StudySer = Column(ForeignKey(u'Study.StudySer'))
    SeriesId = Column(Unicode(16), nullable=False)
    SeriesName = Column(Unicode(64))
    SeriesNumber = Column(Integer)
    SeriesUID = Column(Unicode(64), nullable=False, unique=True)
    SeriesType = Column(Unicode(30), nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    BodyPartExamined = Column(Unicode(32))
    PatientOrientation = Column(Unicode(32))
    SeriesModality = Column(Unicode(16), nullable=False)
    AcquisitionType = Column(Unicode(32))
    Comment = Column(Unicode(254))
    ReconstructionType4D = Column(Unicode(64), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_EMPTYSTRING_DEF]
	AS ''"""))
    ReconstructionPhase4D = Column(Float(53))
    PositionReferenceIndicator = Column(Unicode(64))
    FrameOfReferenceUID = Column(Unicode(64))
    ResampledSeriesFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), index=True)
    RelatedCourseSer = Column(ForeignKey(u'Course.CourseSer'), index=True)
    RelatedPlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), index=True)
    RelatedRadiationSer = Column(ForeignKey(u'ExternalField.RadiationSer'), index=True)
    RelatedDiagnosisSer = Column(BigInteger)

    Course = relationship(u'Course')
    PlanSetup = relationship(u'PlanSetup')
    ExternalField = relationship(u'ExternalField')
    Machine = relationship(u'Machine')
    Study = relationship(u'Study')


class ServiceControl(Base):
    __tablename__ = 'ServiceControl'

    ActivityName = Column(Unicode(64), primary_key=True, nullable=False)
    ActivityDateTime = Column(DateTime, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    Object = Column(Unicode(32))
    ObjectName = Column(Unicode(64))
    DeviceName = Column(Unicode(64))
    BeforeSize = Column(Integer)
    AfterSize = Column(Integer)
    BeforeTime = Column(DateTime)
    AfterTime = Column(DateTime)
    ErrorCode = Column(Integer)
    ErrorDescription = Column(Unicode(254))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class Session(Base):
    __tablename__ = 'Session'
    __table_args__ = (
        Index('XIE1Session', 'CourseSer', 'SessionNum', unique=True),
    )

    SessionSer = Column(BigInteger, primary_key=True)
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), nullable=False)
    SessionNum = Column(Integer, nullable=False)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Course = relationship(u'Course')


class SessionProcedure(Base):
    __tablename__ = 'SessionProcedure'
    __table_args__ = (
        Index('XIE1SessionProcedure', 'Status', 'SessionSer'),
    )

    SessionProcedureSer = Column(BigInteger, primary_key=True)
    SessionSer = Column(ForeignKey(u'Session.SessionSer'), nullable=False, index=True)
    SequenceNumber = Column(Integer)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    ProcedureItemSer = Column(ForeignKey(u'ProcedureItem.ProcedureItemSer'), index=True)
    ProcedureInstanceUID = Column(Unicode(64))
    SessionProcedureTemplateId = Column(Unicode(16), nullable=False)
    Status = Column(Unicode(16), nullable=False)
    ProgressIndicator = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    ProcedureItem = relationship(u'ProcedureItem')
    Series = relationship(u'Series')
    Session = relationship(u'Session')


class SessionProcedurePart(Base):
    __tablename__ = 'SessionProcedurePart'
    __table_args__ = (
        Index('XAK1SessionProcedurePart', 'SessionProcedureSer', 'SequenceNumber', unique=True),
    )

    SessionProcedurePartSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), index=True)
    ImageType = Column(Unicode(32))
    SequenceNumber = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    AcqAdjustment = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    AutoSave = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DoseAccumulation = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Continuous = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    BeamOff = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DeviationImage = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DevEnergy = Column(Integer)
    DevDoseRate = Column(Integer)
    DevGeometry = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    JawState = Column(Float(53))
    DevCollX1 = Column(Float(53))
    DevCollX2 = Column(Float(53))
    DevCollY1 = Column(Float(53))
    DevCollY2 = Column(Float(53))
    MUSubtraction = Column(Integer)
    AcquisitionMode = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    SessionProcedureSer = Column(ForeignKey(u'SessionProcedure.SessionProcedureSer'), nullable=False)
    ImageModality = Column(Unicode(16), nullable=False)
    RTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), index=True)

    RTPlan = relationship(u'RTPlan')
    Radiation = relationship(u'Radiation')
    SessionProcedure = relationship(u'SessionProcedure')


class SessionProcedureTemplate(Base):
    __tablename__ = 'SessionProcedureTemplate'

    SessionProcedureTemplateSer = Column(BigInteger, primary_key=True)
    SessionProcedureTemplateId = Column(Unicode(16), nullable=False)
    SessionProcedureTemplateName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUser = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class SessionProcedureTemplatePart(Base):
    __tablename__ = 'SessionProcedureTemplatePart'
    __table_args__ = (
        Index('XAKSessionProcedureTemplatePart', 'SessionProcedureTemplateSer', 'SequenceNumber', unique=True),
    )

    SessionProcedureTemplatePartSer = Column(BigInteger, primary_key=True)
    SessionProcedureTemplateSer = Column(ForeignKey(u'SessionProcedureTemplate.SessionProcedureTemplateSer'), nullable=False)
    SequenceNumber = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    AcqAdjustment = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    ImageType = Column(Unicode(32))
    AutoSave = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DoseAccumulation = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))
    Continuous = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    BeamOff = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DeviationImage = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DevEnergy = Column(Integer)
    DevDoseRate = Column(Integer)
    DevGeometry = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    JawState = Column(Float(53))
    MUSubtraction = Column(Integer)
    AcquisitionMode = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ImageModality = Column(Unicode(16), nullable=False)

    SessionProcedureTemplate = relationship(u'SessionProcedureTemplate')


class SessionRTPlan(Base):
    __tablename__ = 'SessionRTPlan'
    __table_args__ = (
        Index('XAK1SessionPlan', 'SessionSer', 'SessionRTPlanSer', unique=True),
        Index('XIE1SessionRTPlan', 'Status', 'SessionSer')
    )

    SessionRTPlanSer = Column(BigInteger, primary_key=True)
    RTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), nullable=False, index=True)
    SessionSer = Column(ForeignKey(u'Session.SessionSer'), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    Status = Column(Unicode(16), nullable=False)

    RTPlan = relationship(u'RTPlan')
    Session = relationship(u'Session')


class Slouse(Base):
    __tablename__ = 'Slice'
    __table_args__ = (
        Index('XAK2Slice', 'SliceFormat', 'IsLockedFlag', 'SliceSer', unique=True),
        Index('XIE2Slice', 'SliceSer', 'SliceType', 'SliceModality', 'SliceFormat', 'SliceCharacteristics')
    )

    SliceSer = Column(BigInteger, primary_key=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    SliceUID = Column(Unicode(64), nullable=False, unique=True)
    CreationDate = Column(DateTime)
    CreationUserName = Column(Unicode(32))
    SliceNumber = Column(Integer)
    Position = Column(Float(53))
    FileName = Column(Unicode(254))
    SliceType = Column(Unicode(30))
    SliceModality = Column(Unicode(16), nullable=False)
    ResourceSer = Column(ForeignKey(u'Machine.ResourceSer'), index=True)
    SliceFormat = Column(Unicode(32))
    HeaderSize = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SizeX = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SizeY = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    AcqWindow = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    AcqLevel = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ResolutionX = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    ResolutionY = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_FLT_DEF]
	AS 0.0"""))
    CalibratedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    PixelOffset = Column(Integer)
    PixelSlope = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ONE_FLT_DEF]
	AS 1.0"""))
    Transformation = Column(BINARY(96), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    SliceCharacteristics = Column(Unicode(254))
    PhotometricInterpretation = Column(Unicode(16))
    BitsAllocated = Column(Integer, nullable=False)
    BitsStored = Column(Integer)
    CouchVrt = Column(Float(53))
    CouchLng = Column(Float(53))
    CouchLat = Column(Float(53))
    PatientSupportAngle = Column(Float(53))
    TableTopEccentricAngle = Column(Float(53))
    ConversionType = Column(Unicode(16))
    HighBit = Column(Integer, nullable=False)
    PatSupportPitchAngle = Column(Float(53))
    PatSupportRollAngle = Column(Float(53))
    Thickness = Column(Float(53))
    EquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    NumberOfFrames = Column(Integer)
    DCTransferSyntaxSer = Column(ForeignKey(u'DCTransferSyntax.DCTransferSyntaxSer'), index=True)
    IsLockedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    PixelIntensityRel = Column(Integer)
    PixelIntensitySign = Column(Integer)
    PixelRepresentation = Column(Integer, nullable=False)
    TransactionId = Column(String(255, u'Latin1_General_BIN2'))
    ActualPatientWeight = Column(Float(53))
    ActualPatientHeight = Column(Float(53))
    ContributingEquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    SOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), nullable=False, index=True)
    AcquisitionDateTime = Column(DateTime)
    IrradiationEventUID = Column(Unicode(64))

    Equipment = relationship(u'Equipment', primaryjoin='Slouse.ContributingEquipmentSer == Equipment.EquipmentSer')
    DCTransferSyntax = relationship(u'DCTransferSyntax')
    Equipment1 = relationship(u'Equipment', primaryjoin='Slouse.EquipmentSer == Equipment.EquipmentSer')
    Machine = relationship(u'Machine')
    SOPClas = relationship(u'SOPClas')
    Series = relationship(u'Series')


class SliceMR(Slouse):
    __tablename__ = 'SliceMR'

    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), primary_key=True)
    ScanningSequence = Column(Unicode(16), nullable=False)
    SequenceVariant = Column(Unicode(16), nullable=False)


class SliceCT(Slouse):
    __tablename__ = 'SliceCT'

    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), primary_key=True)
    RescaleIntercept = Column(Float(53))
    RescaleSlope = Column(Float(53))
    KVP = Column(Float(53))
    AcquisitionNumber = Column(Integer)
    ScanOptions = Column(Unicode(64))
    DataCollectionDiameter = Column(Float(53))
    ReconstructionDiameter = Column(Float(53))
    SourceDetectorDist = Column(Float(53))
    SourcePatientDist = Column(Float(53))
    GantryTilt = Column(Float(53))
    RotationDirection = Column(Unicode(16))
    ExposureTime = Column(Integer)
    XRayTubeCurrent = Column(Integer)
    Exposure = Column(Integer)
    FilterType = Column(Unicode(32))
    GeneratorPower = Column(Integer)
    FocalSpot = Column(Float(53))
    ConvolutionKernel = Column(Unicode(32))
    Mode = Column(Unicode(254))
    Norm = Column(Unicode(254))


class SliceRT(Slouse):
    __tablename__ = 'SliceRT'

    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), primary_key=True)
    DoubleExposureSer = Column(ForeignKey(u'Image.ImageSer'), index=True)
    ReportedValuesOrigin = Column(Unicode(16))
    IDUPosLat = Column(Float(53))
    IDUPosLng = Column(Float(53))
    IDUSID = Column(Float(53))
    IDURtn = Column(Float(53))
    Energy = Column(Integer)
    SAD = Column(Float(53))
    PrimaryDosimeterUnit = Column(Unicode(16))
    MetersetExposure = Column(Float(53))
    ExposureTime = Column(Integer)
    CollX1 = Column(Float(53))
    CollX2 = Column(Float(53))
    CollY1 = Column(Float(53))
    CollY2 = Column(Float(53))
    SliceRTType = Column(Unicode(30), nullable=False)
    OpenField = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DoseRate = Column(Integer)
    StartCumulativeMeterset = Column(Float(53))
    EndCumulativeMeterset = Column(Float(53))
    AcqNote = Column(Unicode(254))
    GantryAngle = Column(Float(53))
    CollRtn = Column(Float(53))
    BladeX1 = Column(Float(53))
    BladeX2 = Column(Float(53))
    BladeY1 = Column(Float(53))
    BladeY2 = Column(Float(53))
    IDUCorrectionLat = Column(Float(53))
    IDUCorrectionLng = Column(Float(53))
    XRayTubeCurrent = Column(Integer)
    RTImagePositionX = Column(Float(53))
    RTImagePositionY = Column(Float(53))
    OffPlaneAngle = Column(Float(53))
    IsoCenterPositionX = Column(Float(53))
    IsoCenterPositionY = Column(Float(53))
    IsoCenterPositionZ = Column(Float(53))
    PrimaryFluenceModeId = Column(Unicode(16))
    RadiationSer = Column(ForeignKey(u'Radiation.RadiationSer'), index=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), index=True)
    UpdateOnBeamChange = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    ReferenceImage = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    RadiationMachineName = Column(Unicode(16))

    Image = relationship(u'Image')
    PlanSetup = relationship(u'PlanSetup')
    Radiation = relationship(u'Radiation')


class SlicePortalDoseAnalysi(Base):
    __tablename__ = 'SlicePortalDoseAnalysis'

    SlicePortalDoseAnalysisSer = Column(BigInteger, primary_key=True)
    PortalDoseAnalysisSer = Column(ForeignKey(u'PortalDoseAnalysis.PortalDoseAnalysisSer'), nullable=False, index=True)
    SliceSer = Column(ForeignKey(u'Slice.SliceSer'), nullable=False, index=True)
    DoseImageRole = Column(Integer, nullable=False)

    PortalDoseAnalysi = relationship(u'PortalDoseAnalysi')
    Slouse = relationship(u'Slouse')


class Slot(Base):
    __tablename__ = 'Slot'
    __table_args__ = (
        Index('XAK1Slot', 'ResourceSer', 'SlotNumber', unique=True),
    )

    SlotSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), nullable=False)
    SlotNumber = Column(Integer, nullable=False)
    SlotName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    InternalCode = Column(Integer)
    SourceSlotDist = Column(Float(53))
    MaxCompThickness = Column(Float(53))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    RadiationDevice = relationship(u'RadiationDevice')


class SlotAddOn(Base):
    __tablename__ = 'SlotAddOn'

    AddOnSer = Column(ForeignKey(u'AddOn.AddOnSer'), primary_key=True, nullable=False)
    SlotSer = Column(ForeignKey(u'Slot.SlotSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    AddOn = relationship(u'AddOn')
    Slot = relationship(u'Slot')


class SourcePosition(Base):
    __tablename__ = 'SourcePosition'
    __table_args__ = (
        Index('XIE1SourcePosition', 'RadiationSer', 'RadioactiveSourceSer'),
    )

    SourcePositionSer = Column(BigInteger, primary_key=True)
    RadiationSer = Column(ForeignKey(u'BrachyField.RadiationSer'), nullable=False)
    RadioactiveSourceSer = Column(ForeignKey(u'RadioactiveSource.RadioactiveSourceSer'), index=True)
    SourcePositionId = Column(Unicode(16), nullable=False)
    SourcePositionName = Column(Unicode(64))
    DwellPosition = Column(Float(53))
    DwellTime = Column(Float(53))
    StructureSer = Column(ForeignKey(u'Structure.StructureSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    DwellTimeLockedFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DwellTimeMaxLimit = Column(Float(53))
    DwellTimeMinLimit = Column(Float(53))

    BrachyField = relationship(u'BrachyField')
    RadioactiveSource = relationship(u'RadioactiveSource')
    Structure = relationship(u'Structure')


class SpatialRegistration(Base):
    __tablename__ = 'SpatialRegistration'

    SpatialRegistrationSer = Column(BigInteger, primary_key=True)
    SpatialRegistrationIODSer = Column(ForeignKey(u'SpatialRegistrationIOD.SpatialRegistrationIODSer'), nullable=False, index=True)
    FrameOfReferenceUID = Column(Unicode(64), index=True)
    Comment = Column(Unicode(254))
    RegTypeCodeValue = Column(Unicode(16))
    RegTypeCodeMeaning = Column(Unicode(64))
    RegTypeCodeDesignator = Column(Unicode(16))
    RegTypeCodeVersion = Column(Unicode(16))
    RegSubType = Column(Unicode(64))
    Transformation = Column(BINARY(96), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    AverageErrorDist = Column(Float(53))
    MaxErrorDist = Column(Float(53))
    MatchAlgorithm = Column(Unicode(64))
    Status = Column(Unicode(64), nullable=False)
    StatusDate = Column(DateTime, nullable=False)
    StatusUserName = Column(Unicode(32), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    SpatialRegistrationIOD = relationship(u'SpatialRegistrationIOD')


class SpatialRegistrationIOD(Base):
    __tablename__ = 'SpatialRegistrationIOD'

    SpatialRegistrationIODSer = Column(BigInteger, primary_key=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    SpatialRegistrationIODId = Column(Unicode(16), nullable=False)
    SpatialRegistrationUID = Column(Unicode(64), nullable=False, unique=True)
    InstanceNumber = Column(Integer, nullable=False)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    Comment = Column(Unicode(254))
    EquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    RegistrationType = Column(Unicode(32), nullable=False)
    FileName = Column(Unicode(254))

    Equipment = relationship(u'Equipment')
    Series = relationship(u'Series')


class SpatialRegistrationImage(Base):
    __tablename__ = 'SpatialRegistrationImage'
    __table_args__ = (
        Index('XIE1SpatialRegistrationImage', 'ImageSer', 'SpatialRegistrationSer'),
    )

    SpatialRegistrationImageSer = Column(BigInteger, primary_key=True)
    SpatialRegistrationSer = Column(ForeignKey(u'SpatialRegistration.SpatialRegistrationSer'), nullable=False, index=True)
    ImageSer = Column(ForeignKey(u'Image.ImageSer'))
    ImageClassUID = Column(Unicode(64), nullable=False)
    ImageInstanceUID = Column(Unicode(64), nullable=False, index=True)
    StudyUID = Column(Unicode(64))
    SeriesUID = Column(Unicode(64))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Image = relationship(u'Image')
    SpatialRegistration = relationship(u'SpatialRegistration')


class Structure(Base):
    __tablename__ = 'Structure'

    StructureSer = Column(BigInteger, primary_key=True)
    StructureSetSer = Column(ForeignKey(u'StructureSet.StructureSetSer'), nullable=False, index=True)
    PatientVolumeSer = Column(ForeignKey(u'PatientVolume.PatientVolumeSer'), index=True)
    StructureTypeSer = Column(ForeignKey(u'StructureType.StructureTypeSer'), nullable=False, index=True)
    StructureId = Column(Unicode(16), nullable=False)
    StructureName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    ROINumber = Column(Integer, nullable=False)
    ROIObservationNumber = Column(Integer, nullable=False)
    GenerationAlgorithm = Column(Unicode(16))
    GenAlgoComment = Column(Unicode(64))
    DVHLineColor = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    DVHLineStyle = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    DVHLineWidth = Column(Float(53), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ONE_FLT_DEF]
	AS 1.0"""))
    FirstSlice = Column(Integer)
    LastSlice = Column(Integer)
    MaterialCTValue = Column(Float(53))
    MaterialSer = Column(ForeignKey(u'Material.MaterialSer'), index=True)
    ROIPhysicalProperty = Column(Unicode(254))
    ROIPhysicalPropertyValue = Column(Unicode(254))
    SearchCTHigh = Column(Float(53))
    SearchCTLow = Column(Float(53))
    EUDAlpha = Column(Float(53))
    TCPAlpha = Column(Float(53))
    TCPBeta = Column(Float(53))
    TCPGamma = Column(Float(53))
    ThicknessCm = Column(Float(53))
    FileName = Column(Unicode(254))
    Interpreter = Column(Unicode(64))
    ROIObservationId = Column(Unicode(16))
    ROIMaterialId = Column(Unicode(16))
    VolumeCodeDesignator = Column(Unicode(16))
    VolumeCodeVersion = Column(Unicode(16))
    VolumeCodeValue = Column(Unicode(16))
    VolumeCodeMeaning = Column(Unicode(64))
    Status = Column(Unicode(64), nullable=False)
    StatusDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    StatusUserName = Column(Unicode(32), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    IsVisible = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_TRUE_DEF]
	AS 1"""))

    Material = relationship(u'Material')
    PatientVolume = relationship(u'PatientVolume')
    StructureSet = relationship(u'StructureSet')
    StructureType = relationship(u'StructureType')


class StructureSet(Base):
    __tablename__ = 'StructureSet'
    __table_args__ = (
        Index('XIE1StructureSet', 'SeriesSer', 'StructureSetSer'),
    )

    StructureSetSer = Column(BigInteger, primary_key=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False)
    ImageSer = Column(ForeignKey(u'Image.ImageSer'), nullable=False, index=True)
    StructureSetUID = Column(Unicode(64), nullable=False, unique=True)
    StructureSetId = Column(Unicode(16), nullable=False)
    StructureSetName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    ModifiedDateTime = Column(DateTime)
    InstanceNumber = Column(Integer)
    EquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ROIMaterialVersion = Column(Unicode(64))

    Equipment = relationship(u'Equipment')
    Image = relationship(u'Image')
    Series = relationship(u'Series')


class StructureType(Base):
    __tablename__ = 'StructureType'

    StructureTypeSer = Column(BigInteger, primary_key=True)
    MaterialSer = Column(ForeignKey(u'Material.MaterialSer'), index=True)
    StructureTypeIndex = Column(Integer)
    DicomType = Column(Unicode(16), nullable=False)
    SubType = Column(Unicode(16))
    UserSelectable = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Material = relationship(u'Material')


class Study(Base):
    __tablename__ = 'Study'
    __table_args__ = (
        Index('XIE1Study', 'PatientSer', 'StudyId'),
        Index('XIE3Study', 'PatientSer', 'StudySer')
    )

    StudySer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False)
    StudyId = Column(Unicode(16), nullable=False)
    StudyName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    ReferringPhysicianName = Column(Unicode(64))
    StudyUID = Column(Unicode(64), nullable=False, unique=True)
    AccessionNumber = Column(Unicode(16))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    RelatedCourseSer = Column(ForeignKey(u'Course.CourseSer'), index=True)
    RelatedDiagnosisSer = Column(BigInteger)

    Patient = relationship(u'Patient')
    Course = relationship(u'Course')


class SystemRoot(Base):
    __tablename__ = 'SystemRoot'

    SystemRootSer = Column(BigInteger, primary_key=True)
    InstallationDate = Column(DateTime)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class TFHAddOn(Base):
    __tablename__ = 'TFHAddOn'

    RadiationHstrySer = Column(ForeignKey(u'ExternalFieldCommonHstry.RadiationHstrySer'), primary_key=True, nullable=False)
    AddOnNumber = Column(Integer, primary_key=True, nullable=False)
    AddOnId = Column(Unicode(16), nullable=False)
    AddOnType = Column(Unicode(30), nullable=False)
    AddOnSubType = Column(Unicode(64))

    ExternalFieldCommonHstry = relationship(u'ExternalFieldCommonHstry')


class Technique(Base):
    __tablename__ = 'Technique'
    __table_args__ = (
        Index('XAK1Technique', 'ResourceSer', 'TechniqueId', unique=True),
    )

    TechniqueSer = Column(BigInteger, primary_key=True)
    ResourceSer = Column(ForeignKey(u'ExternalBeam.ResourceSer'), nullable=False)
    TechniqueId = Column(Unicode(16), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DefaultFlag = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    DisplayCode = Column(Unicode(32))
    InternalCode = Column(Integer)
    LevelCode = Column(Integer)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ExternalBeam = relationship(u'ExternalBeam')


class Template(Base):
    __tablename__ = 'Template'

    TemplateSer = Column(BigInteger, primary_key=True)
    TemplateRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), index=True)
    DiagnosisStageSer = Column(ForeignKey(u'DiagnosisStage.DiagnosisStageSer'), index=True)
    PayorSer = Column(ForeignKey(u'Payor.PayorSer'), index=True)
    ResourceSer = Column(ForeignKey(u'Resource.ResourceSer'), index=True)
    DepartmentSer = Column(ForeignKey(u'Department.DepartmentSer'), index=True)
    DerivedFromSer = Column(ForeignKey(u'Template.TemplateSer'), index=True)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    TemplateID = Column(Unicode(64))
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), index=True)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Course = relationship(u'Course')
    Department = relationship(u'Department')
    parent = relationship(u'Template', remote_side=[TemplateSer])
    DiagnosisStage = relationship(u'DiagnosisStage')
    Patient = relationship(u'Patient')
    Payor = relationship(u'Payor')
    Resource = relationship(u'Resource')


class TemplateCycle(Base):
    __tablename__ = 'TemplateCycle'

    TemplateCycleSer = Column(BigInteger, primary_key=True)
    TemplateCycleRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    TemplateSer = Column(ForeignKey(u'Template.TemplateSer'), nullable=False, index=True)
    TemplateRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    CycleSer = Column(ForeignKey(u'TreatmentCycle.CycleSer'), nullable=False, index=True)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    TreatmentCycle = relationship(u'TreatmentCycle')
    Template = relationship(u'Template')


class TemplateCycleMH(Base):
    __tablename__ = 'TemplateCycleMH'

    TemplateCycleSer = Column(ForeignKey(u'TemplateCycle.TemplateCycleSer'), primary_key=True, nullable=False)
    TemplateCycleRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    TemplateSer = Column(BigInteger, nullable=False)
    TemplateRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    CycleSer = Column(BigInteger, nullable=False)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    TemplateCycle = relationship(u'TemplateCycle')


class TemplateDiagnosi(Base):
    __tablename__ = 'TemplateDiagnosis'

    TemplateDiagnosisSer = Column(BigInteger, primary_key=True)
    TemplateSer = Column(ForeignKey(u'Template.TemplateSer'), nullable=False, index=True)
    DiagnosisSer = Column(BigInteger, nullable=False, index=True)
    TemplateRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Template = relationship(u'Template')


class TemplateMH(Base):
    __tablename__ = 'TemplateMH'

    TemplateSer = Column(ForeignKey(u'Template.TemplateSer'), primary_key=True, nullable=False)
    TemplateRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    PatientSer = Column(BigInteger, index=True)
    DiagnosisStageSer = Column(BigInteger)
    PayorSer = Column(BigInteger)
    ResourceSer = Column(BigInteger)
    DepartmentSer = Column(BigInteger)
    DerivedFromSer = Column(BigInteger)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    TemplateID = Column(Unicode(64))
    CourseSer = Column(BigInteger)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DefaultFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Template = relationship(u'Template')


class TickerChannel(Base):
    __tablename__ = 'TickerChannel'

    TickerChannelSer = Column(BigInteger, primary_key=True)
    ChannelName = Column(Unicode(254), nullable=False)
    ChannelUID = Column(Unicode(254), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class TickerMessage(Base):
    __tablename__ = 'TickerMessage'

    TickerMessageSer = Column(BigInteger, primary_key=True)
    FromMachine = Column(Unicode(254), nullable=False)
    MessageType = Column(Unicode(254), nullable=False)
    MsgUID = Column(Unicode(254), nullable=False)
    CreationTime = Column(DateTime, nullable=False)
    ExpirationTime = Column(DateTime, nullable=False)
    Message = Column(UnicodeText(1073741823), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class TickerMessageChannel(Base):
    __tablename__ = 'TickerMessageChannel'

    TickerMessageChannelSer = Column(BigInteger, primary_key=True)
    TickerMessageSer = Column(ForeignKey(u'TickerMessage.TickerMessageSer'), nullable=False, index=True)
    TickerChannelSer = Column(ForeignKey(u'TickerChannel.TickerChannelSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    TickerChannel = relationship(u'TickerChannel')
    TickerMessage = relationship(u'TickerMessage')


class Tolerance(Base):
    __tablename__ = 'Tolerance'

    ToleranceSer = Column(BigInteger, primary_key=True)
    ToleranceId = Column(Unicode(16), nullable=False, unique=True)
    ToleranceName = Column(Unicode(64))
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    CreationUserName = Column(Unicode(32))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class ToleranceLimit(Base):
    __tablename__ = 'ToleranceLimit'
    __table_args__ = (
        Index('XAKToleranceLimit', 'ToleranceSer', 'ParameterType', unique=True),
    )

    ToleranceLimitSer = Column(BigInteger, primary_key=True)
    ToleranceSer = Column(ForeignKey(u'Tolerance.ToleranceSer'), nullable=False)
    ParameterType = Column(Unicode(32), nullable=False)
    ToleranceValue = Column(Float(53))
    AutoSetupLevel = Column(Unicode(32))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Tolerance = relationship(u'Tolerance')


class Tracking(Base):
    __tablename__ = 'Tracking'

    TrackingSer = Column(BigInteger, primary_key=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), index=True)
    TrackingId = Column(Unicode(16), nullable=False)
    TrackingName = Column(Unicode(64))
    TrackingUID = Column(Unicode(64), nullable=False, unique=True)
    CreationDate = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    Comment = Column(Unicode(254))
    FileName = Column(Unicode(254))
    TrackingType = Column(SmallInteger, nullable=False)
    EquipmentSer = Column(ForeignKey(u'Equipment.EquipmentSer'), index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Equipment = relationship(u'Equipment')
    PlanSetup = relationship(u'PlanSetup')
    Series = relationship(u'Series')


class TrackingField(Base):
    __tablename__ = 'TrackingField'

    TrackingSer = Column(ForeignKey(u'Tracking.TrackingSer'), primary_key=True, nullable=False)
    RadiationSer = Column(ForeignKey(u'ExternalFieldCommon.RadiationSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ExternalFieldCommon = relationship(u'ExternalFieldCommon')
    Tracking = relationship(u'Tracking')


class TrackingImage(Base):
    __tablename__ = 'TrackingImage'

    TrackingSer = Column(ForeignKey(u'Tracking.TrackingSer'), primary_key=True, nullable=False)
    ImageSer = Column(ForeignKey(u'Image.ImageSer'), primary_key=True, nullable=False, index=True)
    CacheKeySer = Column(BigInteger)
    ImageAcquisitionTime = Column(DateTime)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Image = relationship(u'Image')
    Tracking = relationship(u'Tracking')


class TrackingInformation(Base):
    __tablename__ = 'TrackingInformation'

    TrackingInformationSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    ArchiveLocationSer = Column(ForeignKey(u'ArchiveLocation.ArchiveLocationSer'), nullable=False, index=True)
    ArchiveDate = Column(DateTime)
    ArchiveUser = Column(Unicode(32))
    ArchiveNote = Column(Unicode(254))
    PurgeDate = Column(DateTime)
    PurgeUser = Column(Unicode(32))
    RestoreDate = Column(DateTime)
    RestoreUser = Column(Unicode(32))
    RestoreNote = Column(Unicode(254))
    RemoveDate = Column(DateTime)
    RemoveUser = Column(Unicode(32))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    LTArchiveVersion = Column(Unicode(32), nullable=False)
    DocDeleteStatus = Column(Unicode(64))
    SchChrgDeleteStatus = Column(Unicode(64))
    TrackingStatus = Column(Unicode(64), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_TRACKINGSTATUS_DEF]
	AS 'UNKNOWN'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ArchiveLocation = relationship(u'ArchiveLocation')
    Patient = relationship(u'Patient')


class Transportation(Base):
    __tablename__ = 'Transportation'

    TransportationSer = Column(BigInteger, primary_key=True)
    HospitalSer = Column(ForeignKey(u'Hospital.HospitalSer'), nullable=False, index=True)
    TransportationName = Column(Unicode(64), nullable=False)
    TransportationPhone = Column(Unicode(64), nullable=False)
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Hospital = relationship(u'Hospital')


class TreatmentCycle(Base):
    __tablename__ = 'TreatmentCycle'

    CycleSer = Column(BigInteger, primary_key=True)
    TreatmentCycle = Column(Unicode(32), nullable=False)
    NoEditFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    SortOrder = Column(Integer, nullable=False)


class TreatmentPhase(Base):
    __tablename__ = 'TreatmentPhase'

    TreatmentPhaseSer = Column(BigInteger, primary_key=True)
    CourseSer = Column(ForeignKey(u'Course.CourseSer'), nullable=False, index=True)
    RelTreatmentPhaseSer = Column(ForeignKey(u'TreatmentPhase.TreatmentPhaseSer'), index=True)
    TimeGapType = Column(Unicode(32))
    PhaseGapNumberOfDays = Column(Integer)
    OtherInfo = Column(Unicode(256))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    Course = relationship(u'Course')
    parent = relationship(u'TreatmentPhase', remote_side=[TreatmentPhaseSer])


class TreatmentRecord(Base):
    __tablename__ = 'TreatmentRecord'

    TreatmentRecordSer = Column(BigInteger, primary_key=True)
    PatientSer = Column(ForeignKey(u'Patient.PatientSer'), nullable=False, index=True)
    SeriesSer = Column(ForeignKey(u'Series.SeriesSer'), nullable=False, index=True)
    RTPlanSer = Column(ForeignKey(u'RTPlan.RTPlanSer'), index=True)
    PlanSOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), nullable=False, index=True)
    TreatmentRecordSOPClassSer = Column(ForeignKey(u'SOPClass.SOPClassSer'), nullable=False, index=True)
    PlanUID = Column(Unicode(64), nullable=False, index=True)
    TreatmentRecordUID = Column(Unicode(64), nullable=False, unique=True)
    FileName = Column(Unicode(254))
    ActualMachineSer = Column(ForeignKey(u'RadiationDevice.ResourceSer'), index=True)
    ActualMachineAuthorization = Column(Unicode(64))
    MachOverrideFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, index=True, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))
    StructureSetUID = Column(Unicode(64))
    TreatmentRecordDateTime = Column(DateTime, index=True)
    NoOfFractions = Column(Integer, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))

    RadiationDevice = relationship(u'RadiationDevice')
    Patient = relationship(u'Patient')
    SOPClas = relationship(u'SOPClas', primaryjoin='TreatmentRecord.PlanSOPClassSer == SOPClas.SOPClassSer')
    RTPlan = relationship(u'RTPlan')
    Series = relationship(u'Series')
    SOPClas1 = relationship(u'SOPClas', primaryjoin='TreatmentRecord.TreatmentRecordSOPClassSer == SOPClas.SOPClassSer')


class UserDefActAttr(Base):
    __tablename__ = 'UserDefActAttr'

    UserDefActAttrSer = Column(BigInteger, primary_key=True)
    UserDefActAttrRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    UserDefActAttrId = Column(Unicode(16), nullable=False)
    Description = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


class UserDefActAttrMH(Base):
    __tablename__ = 'UserDefActAttrMH'

    UserDefActAttrSer = Column(ForeignKey(u'UserDefActAttr.UserDefActAttrSer'), primary_key=True, nullable=False)
    UserDefActAttrRevCount = Column(Integer, primary_key=True, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    UserDefActAttrId = Column(Unicode(16), nullable=False)
    Description = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    UserDefActAttr = relationship(u'UserDefActAttr')


class UserDefActAttrValue(Base):
    __tablename__ = 'UserDefActAttrValue'

    UserDefActAttrValueSer = Column(BigInteger, primary_key=True)
    UserDefActAttrSer = Column(ForeignKey(u'UserDefActAttr.UserDefActAttrSer'), nullable=False, index=True)
    UserDefActAttrRevCount = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_REVISIONCOUNT_DEF]
	AS 0"""))
    AttributeValue = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    UserDefActAttr = relationship(u'UserDefActAttr')


class VolOptConstraint(Base):
    __tablename__ = 'VolOptConstraints'

    VolOptConstraintsSer = Column(BigInteger, primary_key=True)
    PlanSetupSer = Column(ForeignKey(u'PlanSetup.PlanSetupSer'), nullable=False, index=True)
    VolOptConstraintsId = Column(Unicode(16), nullable=False)
    VolOptConstraintsName = Column(Unicode(64))
    Comment = Column(Unicode(254))
    Parameters = Column(UnicodeText(1073741823))
    ParametersLen = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ZERO_INT_DEF]
	AS 0"""))
    ConstraintsType = Column(Unicode(32), nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    PlanSetup = relationship(u'PlanSetup')


class VolOptStruct(Base):
    __tablename__ = 'VolOptStruct'

    VolOptStructSer = Column(BigInteger, primary_key=True)
    VolOptConstraintsSer = Column(ForeignKey(u'VolOptConstraints.VolOptConstraintsSer'), nullable=False, index=True)
    StructureSer = Column(ForeignKey(u'Structure.StructureSer'), nullable=False, index=True)
    VolOptStructId = Column(Unicode(16), nullable=False)
    VolOptStructName = Column(Unicode(64))
    Parameters = Column(UnicodeText(1073741823))
    ParametersLen = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    Structure = relationship(u'Structure')
    VolOptConstraint = relationship(u'VolOptConstraint')


class VolOptStructCstr(Base):
    __tablename__ = 'VolOptStructCstr'

    VolOptStructCstrSer = Column(BigInteger, primary_key=True)
    VolOptStructSer = Column(ForeignKey(u'VolOptStruct.VolOptStructSer'), nullable=False, index=True)
    VolOptStructCstrId = Column(Unicode(16), nullable=False)
    VolOptStructCstrName = Column(Unicode(64))
    Parameters = Column(UnicodeText(1073741823))
    ParametersLen = Column(Integer, nullable=False)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    VolOptStruct = relationship(u'VolOptStruct')


class VolumeCode(Base):
    __tablename__ = 'VolumeCode'
    __table_args__ = (
        Index('XAKVolumeCode', 'LanguageId', 'VolumeCode', 'VolumeCodeTable', unique=True),
    )

    VolumeCodeSer = Column(BigInteger, primary_key=True)
    LanguageId = Column(ForeignKey(u'LanguageLookup.LanguageId'), nullable=False)
    VolumeCode = Column(Unicode(16), nullable=False)
    VolumeCodeTable = Column(Unicode(32), nullable=False)
    MaterialSer = Column(ForeignKey(u'Material.MaterialSer'), index=True)
    Description = Column(Unicode(254))
    SearchCTLow = Column(Float(53))
    SearchCTHigh = Column(Float(53))
    SegmentLimit = Column(Float(53))
    SurfaceTension = Column(Float(53))
    RelativeSize = Column(Float(53))
    IsletSize = Column(Integer)
    DetectionAlgorithm = Column(Unicode(32))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    EUDAlpha = Column(Float(53))
    TCPAlpha = Column(Float(53))
    TCPBeta = Column(Float(53))
    TCPGamma = Column(Float(53))
    DefaultRBEProton = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ONE_DOT_ONE_FLT_DEF]
	AS 1.1"""))
    DefaultRBEBrachy = Column(Float(53), server_default=text("""\
CREATE DEFAULT [dbo].[VDT_ONE_FLT_DEF]
	AS 1.0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    LanguageLookup = relationship(u'LanguageLookup')
    Material = relationship(u'Material')


class VolumeType(Base):
    __tablename__ = 'VolumeType'

    VolumeTypeSer = Column(BigInteger, primary_key=True)
    VolumeType = Column(Unicode(32), nullable=False, unique=True)
    MaterialSer = Column(ForeignKey(u'Material.MaterialSer'), index=True)
    Description = Column(Unicode(64))
    ObjectStatus = Column(Unicode(16), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_OBJECTSTATUS_DEF]
	AS 'Active'"""))
    DicomType = Column(Unicode(16))
    OverlapFlag = Column(Integer, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_FLAG_FALSE_DEF]
	AS 0"""))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTimeStamp = Column(DateTime)
    HstryTaskName = Column(Unicode(32))

    Material = relationship(u'Material')


class WeeklyChargeLink(Base):
    __tablename__ = 'WeeklyChargeLink'
    __table_args__ = (
        Index('XAKWeeklyChargeLink', 'ActInstProcCodeSer', 'ActivityInstanceSer', unique=True),
    )

    WeeklyChargeLinkSer = Column(BigInteger, primary_key=True)
    ActInstProcCodeSer = Column(ForeignKey(u'ActInstProcCode.ActInstProcCodeSer'), nullable=False)
    ActivityInstanceSer = Column(ForeignKey(u'ActivityInstance.ActivityInstanceSer'), nullable=False, index=True)
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))

    ActInstProcCode = relationship(u'ActInstProcCode')
    ActivityInstance = relationship(u'ActivityInstance')


class Workstation(Base):
    __tablename__ = 'Workstation'

    WorkstationSer = Column(BigInteger, primary_key=True)
    WorkstationId = Column(Unicode(16), nullable=False, unique=True)
    WorkstationName = Column(Unicode(64))
    Location = Column(Unicode(64))
    ComputerName = Column(Unicode(64))
    DefaultTask = Column(Unicode(32))
    QueueSelected = Column(BigInteger)
    Comment = Column(Unicode(254))
    HstryUserName = Column(Unicode(32), nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_USERNAME_DEF]
	AS suser_name()"""))
    HstryTimeStamp = Column(DateTime)
    HstryDateTime = Column(DateTime, nullable=False, server_default=text("""\
CREATE DEFAULT [dbo].[VDT_DATETIME_DEF]
	AS getdate()"""))
    HstryTaskName = Column(Unicode(32))


t_lv_LinkRTTempFldAddon = Table(
    'lv_LinkRTTempFldAddon', metadata,
    Column('SPID', BigInteger, nullable=False),
    Column('AddOnSer', BigInteger),
    Column('SlotSer', BigInteger),
    Column('CacheKey', BigInteger)
)


t_lv_LinkRTTempMLCSegment = Table(
    'lv_LinkRTTempMLCSegment', metadata,
    Column('SPID', BigInteger, nullable=False),
    Column('LeafNumber', BigInteger),
    Column('LeftLeaf', SmallInteger),
    Column('RightLeaf', SmallInteger)
)


t_lv_LinkRTTempTFA = Table(
    'lv_LinkRTTempTFA', metadata,
    Column('SPID', BigInteger, nullable=False),
    Column('AddOnSer', BigInteger),
    Column('AddOnId', Unicode(16)),
    Column('SlotSer', BigInteger),
    Column('SlotNo', BigInteger)
)


t_lv_LinkRTTempTable1 = Table(
    'lv_LinkRTTempTable1', metadata,
    Column('SPID', BigInteger, nullable=False),
    Column('MLCPlanSer', BigInteger),
    Column('IndexValues', Float(53)),
    Column('PointCount', BigInteger),
    Column('LeafNumber', BigInteger),
    Column('DynamicPosTolerance', Float(53)),
    Column('LeftLeafPosition', Float(53)),
    Column('RightLeafPosition', Float(53)),
    Column('UpdateFlag', Unicode(1))
)


t_lv_LinkRTTempTrtmntFld = Table(
    'lv_LinkRTTempTrtmntFld', metadata,
    Column('SPID', BigInteger, nullable=False),
    Column('PatientId', Unicode(25)),
    Column('CourseID', Unicode(16)),
    Column('PlanSetupID', Unicode(16)),
    Column('FieldID', Unicode(16)),
    Column('FieldName', Unicode(64)),
    Column('CreationDate', DateTime),
    Column('MachineId', Unicode(16)),
    Column('ToleranceId', Unicode(16)),
    Column('ToleranceTableName', Unicode(64)),
    Column('Scale', Unicode(16)),
    Column('TechniqueId', Unicode(16)),
    Column('EnergyMode', Unicode(16)),
    Column('MLCFlag', Integer),
    Column('SetupNote', Unicode(254)),
    Column('CollMode', Unicode(16)),
    Column('MU', Integer),
    Column('TreatmentTime', Float(53)),
    Column('SSD', Float(53)),
    Column('StopAng', Float(53)),
    Column('StopAngE', Unicode(16)),
    Column('MUdeg', Float(53)),
    Column('CollRtn', Float(53)),
    Column('CollRtnM', Float(53)),
    Column('GantryRtn', Float(53)),
    Column('GantryRtnE', Unicode(16)),
    Column('GantryRtnExt', Unicode(16)),
    Column('CollY1', Float(53)),
    Column('CollY2', Float(53)),
    Column('CollX1', Float(53)),
    Column('CollX2', Float(53)),
    Column('CouchVrt', Float(53)),
    Column('CouchVrtM', Float(53)),
    Column('CouchLng', Float(53)),
    Column('CouchLngM', Float(53)),
    Column('CouchLat', Float(53)),
    Column('CouchLatM', Float(53)),
    Column('CouchRtn', Float(53)),
    Column('CouchRtnM', Float(53)),
    Column('AddOnId1', Unicode(16)),
    Column('AddOnType1', Unicode(30)),
    Column('SlotName1', Unicode(64)),
    Column('AddOnId2', Unicode(16)),
    Column('AddOnType2', Unicode(30)),
    Column('SlotName2', Unicode(64)),
    Column('AddOnId3', Unicode(16)),
    Column('AddOnType3', Unicode(30)),
    Column('SlotName3', Unicode(64)),
    Column('AddOnId4', Unicode(16)),
    Column('AddOnType4', Unicode(30)),
    Column('SlotName4', Unicode(64)),
    Column('AddOnId5', Unicode(16)),
    Column('AddOnType5', Unicode(30)),
    Column('SlotName5', Unicode(64)),
    Column('AddOnId6', Unicode(16)),
    Column('AddOnType6', Unicode(30)),
    Column('SlotName6', Unicode(64)),
    Column('TreatmentFlag', Integer),
    Column('PtTreatedFlag', Integer),
    Column('DoseRate', Integer),
    Column('WedgeDose', Float(53)),
    Column('FieldSer', BigInteger),
    Column('FieldRevCount', BigInteger),
    Column('MUpGy', Float(53)),
    Column('TempDose', Float(53)),
    Column('WDProcessFlag', Integer)
)


t_vv_Activity = Table(
    'vv_Activity', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_ActivityCategory = Table(
    'vv_ActivityCategory', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_ActivityCategoryLng = Table(
    'vv_ActivityCategoryLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_ActivityInstance = Table(
    'vv_ActivityInstance', metadata,
    Column('ActivityInstanceSer', BigInteger, nullable=False),
    Column('ActivityInstanceRevCount', Integer, nullable=False),
    Column('TemplateCycleSer', BigInteger),
    Column('TemplateCycleRevCount', Integer),
    Column('ActivitySer', BigInteger, nullable=False),
    Column('ActivityRevCount', Integer, nullable=False),
    Column('DepartmentSer', BigInteger),
    Column('AppointmentInstanceFlag', Integer, nullable=False),
    Column('ObjectStatus', Unicode(16), nullable=False),
    Column('PredecessorSer', BigInteger),
    Column('AppointmentDependentFlag', Integer, nullable=False),
    Column('NotificationPriorTime', Integer),
    Column('Duration', Integer),
    Column('ExclusiveFlag', Integer, nullable=False),
    Column('ActivityGroup', Integer),
    Column('MinPostDuration', Integer),
    Column('MinTrtmntOccurence', Integer),
    Column('MaxTrtmntOccurence', Integer),
    Column('DefaultTrtmntOccurence', Integer),
    Column('WeekNumber', Integer),
    Column('DayOfWeek', Integer),
    Column('PriorPostDueDurUnits', Integer),
    Column('ActivityNote', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('ActInstReadOnly', Integer, nullable=False),
    Column('StudySer', BigInteger),
    Column('ActivityInstanceId', Unicode(16)),
    Column('PlacerOrderNumber', Unicode(64)),
    Column('FillerOrderNumber', Unicode(64)),
    Column('WorklistType', Unicode(64)),
    Column('NotificationPriorTimeFlag', Integer, nullable=False),
    Column('LastStatusUpdatedByResourceSer', BigInteger),
    Column('LastStatusUpdatedDate', DateTime),
    Column('LastNoteUpdatedByResourceSer', BigInteger),
    Column('LastNoteUpdatedDate', DateTime),
    Column('WorkFlowOverrideByResourceSer', BigInteger),
    Column('WorkFlowOverrideDate', DateTime),
    Column('AnchorActivityFlag', Integer, nullable=False),
    Column('AutoAssignOncologistFlag', Integer, nullable=False)
)


t_vv_ActivityLng = Table(
    'vv_ActivityLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_AppointmentTaskPriority = Table(
    'vv_AppointmentTaskPriority', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_AppointmentTaskPriorityLng = Table(
    'vv_AppointmentTaskPriorityLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ArchiveDeleteStatus = Table(
    'vv_ArchiveDeleteStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ArchiveDeleteStatusLng = Table(
    'vv_ArchiveDeleteStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ArchiveMediaStatus = Table(
    'vv_ArchiveMediaStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ArchiveMediaStatusLng = Table(
    'vv_ArchiveMediaStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ArchiveMediaType = Table(
    'vv_ArchiveMediaType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ArchiveMediaTypeLng = Table(
    'vv_ArchiveMediaTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Attendee = Table(
    'vv_Attendee', metadata,
    Column('AttendeeSer', BigInteger, nullable=False),
    Column('AttendeeRevCount', Integer, nullable=False),
    Column('ActivityInstanceSer', BigInteger, nullable=False),
    Column('ActivityInstanceRevCount', Integer, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('ResourceGroupSer', BigInteger),
    Column('ObjectStatus', Unicode(16), nullable=False),
    Column('ExclusiveFlag', Integer, nullable=False),
    Column('PrimaryFlag', Integer, nullable=False),
    Column('ParticipationRole', Unicode(32)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('ActivityOwnerFlag', Integer, nullable=False)
)


t_vv_AutoSetupLevel = Table(
    'vv_AutoSetupLevel', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_AutoSetupLevelLng = Table(
    'vv_AutoSetupLevelLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Auxiliary = Table(
    'vv_Auxiliary', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_AuxiliaryLng = Table(
    'vv_AuxiliaryLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_BloodGroup = Table(
    'vv_BloodGroup', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_BloodGroupLng = Table(
    'vv_BloodGroupLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_BodySystemName = Table(
    'vv_BodySystemName', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_BodySystemNameLng = Table(
    'vv_BodySystemNameLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_BrachyFieldHstry = Table(
    'vv_BrachyFieldHstry', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('BrachyTreatmentType', Unicode(16), nullable=False),
    Column('ChannelNumber', Integer, nullable=False),
    Column('ChannelLength', Float(53), nullable=False),
    Column('SpecifiedChannelTotalTime', Float(53), nullable=False),
    Column('ChannelReferenceAirKerma', Float(53), nullable=False),
    Column('DeliveredChannelTotalTime', Float(53), nullable=False),
    Column('SpecifiedNumberOfPulses', Integer),
    Column('DeliveredNumberOfPulses', Integer),
    Column('SpecifiedPulseRepetitionInterval', Float(53)),
    Column('DeliveredPulseRepetitionInterval', Float(53)),
    Column('SourceSerialNumber', Unicode(64)),
    Column('SourceIsotopeName', Unicode(64), nullable=False),
    Column('ReferenceAirKermaRate', Float(53), nullable=False),
    Column('SourceStrengthReferenceDateTime', DateTime, nullable=False),
    Column('NumberOfSourcePositions', Integer, nullable=False)
)


t_vv_ChecklistResponse = Table(
    'vv_ChecklistResponse', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ChecklistResponseLng = Table(
    'vv_ChecklistResponseLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ClinicalStatus = Table(
    'vv_ClinicalStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ClinicalStatusLng = Table(
    'vv_ClinicalStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Country = Table(
    'vv_Country', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_CountryLng = Table(
    'vv_CountryLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Course = Table(
    'vv_Course', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('StartDateTime', DateTime),
    Column('ClinicalStatus', Unicode(16), nullable=False),
    Column('CompletedByUserName', Unicode(32)),
    Column('CompletedDateTime', DateTime),
    Column('Comment', Unicode(254)),
    Column('ClinicalProtocolDir', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('TransactionId', String(255, u'Latin1_General_BIN2'))
)


t_vv_CourseIntent = Table(
    'vv_CourseIntent', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_CourseIntentLng = Table(
    'vv_CourseIntentLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DBHistory = Table(
    'vv_DBHistory', metadata,
    Column('DBHistorySer', BigInteger, nullable=False),
    Column('EventType', Unicode(32), nullable=False),
    Column('Release', String(16, u'Latin1_General_BIN2')),
    Column('UpgrVersion', String(12, u'Latin1_General_BIN2')),
    Column('HstryUserName', Unicode(32)),
    Column('HstryDateTime', DateTime),
    Column('Description', Unicode(254))
)


t_vv_DerivedImageCode = Table(
    'vv_DerivedImageCode', metadata,
    Column('DerivedImageCodeSer', BigInteger, nullable=False),
    Column('SliceSer', BigInteger, nullable=False),
    Column('Value', Unicode(16), nullable=False),
    Column('Designator', Unicode(16), nullable=False),
    Column('Version', Unicode(16)),
    Column('Meaning', Unicode(64)),
    Column('Registry', Unicode(64)),
    Column('UID', Unicode(64)),
    Column('ExternalID', UnicodeText(1073741823)),
    Column('CommonName', UnicodeText(1073741823)),
    Column('ResponsibleOrganization', UnicodeText(1073741823))
)


t_vv_DiagnosisCodeDesc = Table(
    'vv_DiagnosisCodeDesc', metadata,
    Column('DiagnosisTableName', Unicode(64)),
    Column('DiagnosisCode', Unicode(16), nullable=False),
    Column('LanguageId', Unicode(16)),
    Column('Description', Unicode(254))
)


t_vv_DiagnosisCodeDescLng = Table(
    'vv_DiagnosisCodeDescLng', metadata,
    Column('DiagnosisTableName', Unicode(64)),
    Column('DiagnosisCode', Unicode(16), nullable=False),
    Column('LanguageId', Unicode(16)),
    Column('Description', Unicode(254))
)


t_vv_DiagnosisStagingMethod = Table(
    'vv_DiagnosisStagingMethod', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DiagnosisStagingMethodLng = Table(
    'vv_DiagnosisStagingMethodLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DiagnosisTableStandardLng = Table(
    'vv_DiagnosisTableStandardLng', metadata,
    Column('LookupValue', Unicode(64)),
    Column('Expression1', Unicode(64)),
    Column('DefaultFlag', Integer, nullable=False)
)


t_vv_DiagnosisType = Table(
    'vv_DiagnosisType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DiagnosisTypeLng = Table(
    'vv_DiagnosisTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DocumentTypes = Table(
    'vv_DocumentTypes', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DocumentTypesLng = Table(
    'vv_DocumentTypesLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_DoseContribution = Table(
    'vv_DoseContribution', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('PlanUID', Unicode(64), nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('RefPointId', Unicode(16), nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RefPointSer', BigInteger, nullable=False),
    Column('CacheKeySer', BigInteger),
    Column('DosePerFraction', Float(53)),
    Column('PrimaryFlag', Integer, nullable=False),
    Column('DicomSeqNumber', Integer, nullable=False),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32))
)


t_vv_DoseOverrideView = Table(
    'vv_DoseOverrideView', metadata,
    Column('LastName', Unicode(64), nullable=False),
    Column('FirstName', Unicode(64)),
    Column('PatientId', Unicode(25), nullable=False),
    Column('SiteId', Unicode(16), nullable=False),
    Column('SiteName', Unicode(64)),
    Column('TotalDose', Float(53)),
    Column('DailyDose', Float(53)),
    Column('DoseOverDateTime', DateTime, nullable=False),
    Column('DoseOverType', Unicode(32), nullable=False),
    Column('DoseOverAuthName', Unicode(32)),
    Column('DoseUnits', Unicode(254))
)


t_vv_Ethnicity = Table(
    'vv_Ethnicity', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_EthnicityLng = Table(
    'vv_EthnicityLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ExternalField = Table(
    'vv_ExternalField', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationId', Unicode(16), nullable=False),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('GantryRtn', Float(53)),
    Column('CollRtn', Float(53)),
    Column('CollMode', Unicode(16)),
    Column('CollX1', Float(53)),
    Column('CollY1', Float(53)),
    Column('CollX2', Float(53)),
    Column('CollY2', Float(53)),
    Column('TimepGy', Float(53)),
    Column('GantryRtnDirection', Unicode(16)),
    Column('GantryRtnExt', Unicode(16)),
    Column('DoseRate', Integer),
    Column('StopAngle', Float(53)),
    Column('WedgeDose', Float(53)),
    Column('BEVMarginFlag', Integer, nullable=False),
    Column('CollMarginBottom', Float(53)),
    Column('CalculationLog', UnicodeText(1073741823)),
    Column('CalculationLogLen', Integer, nullable=False),
    Column('DirectionPointDistance', Float(53)),
    Column('EllipticalMarginFlag', Integer, nullable=False),
    Column('FldNormFactor', Float(53)),
    Column('FldNormMethod', Unicode(64)),
    Column('CollMarginLeft', Float(53)),
    Column('MUCoeff', Float(53)),
    Column('MUCoeffMWOpen', Float(53)),
    Column('MUCoeffMWWedged', Float(53)),
    Column('MUCoeffMWVirtual', Float(53)),
    Column('OptimizeCollRtnFlag', Integer, nullable=False),
    Column('SkinFlashFlag', Integer, nullable=False),
    Column('DRRTemplateFileName', Unicode(254)),
    Column('RefDose', Float(53)),
    Column('RefDoseMWOpen', Float(53)),
    Column('RefDoseMWWedged', Float(53)),
    Column('RefDoseMWVirtual', Float(53)),
    Column('CollMarginRight', Float(53)),
    Column('CollMarginTop', Float(53)),
    Column('WedgeWeightFactor', Float(53)),
    Column('WeightFactor', Float(53)),
    Column('TrackingSer', BigInteger),
    Column('DesiredDoseAtIsocenter', Float(53)),
    Column('MuCoeffUnit', Unicode(16))
)


t_vv_ExternalFieldCommon = Table(
    'vv_ExternalFieldCommon', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationId', Unicode(16), nullable=False),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('Meterset', Float(53)),
    Column('MetersetPerGy', Float(53)),
    Column('TreatmentTime', Float(53)),
    Column('SetupFieldFlag', Integer, nullable=False),
    Column('MotionCompSource', Unicode(254)),
    Column('MotionCompTechnique', Unicode(254)),
    Column('SetupTechnique', Unicode(16)),
    Column('SSD', Float(53)),
    Column('SourceFieldEntryDistance', Float(53)),
    Column('CouchLat', Float(53)),
    Column('CouchLatDelta', Float(53)),
    Column('CouchLng', Float(53)),
    Column('CouchLngDelta', Float(53)),
    Column('CouchVrt', Float(53)),
    Column('CouchVrtDelta', Float(53)),
    Column('PatientSupportAngle', Float(53)),
    Column('TableTopPitchAngle', Float(53), nullable=False),
    Column('TableTopRollAngle', Float(53), nullable=False),
    Column('IDUPosLat', Float(53)),
    Column('IDUPosLng', Float(53)),
    Column('IDUPosVrt', Float(53)),
    Column('IDURtn', Float(53)),
    Column('IsoCenterPositionX', Float(53)),
    Column('IsoCenterPositionY', Float(53)),
    Column('IsoCenterPositionZ', Float(53)),
    Column('TechniqueSer', BigInteger),
    Column('EnergyModeSer', BigInteger),
    Column('ToleranceSer', BigInteger)
)


t_vv_ExternalFieldCommonHstry = Table(
    'vv_ExternalFieldCommonHstry', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('PlannedMeterset', Float(53)),
    Column('ActualMeterset', Float(53)),
    Column('MetersetOverrideFlag', Integer, nullable=False),
    Column('SSD', Float(53)),
    Column('CouchCorrectionLat', Float(53)),
    Column('CouchCorrectionLng', Float(53)),
    Column('CouchCorrectionVrt', Float(53)),
    Column('CouchLat', Float(53)),
    Column('CouchLatOverrideFlag', Integer, nullable=False),
    Column('CouchLatPlanned', Float(53)),
    Column('CouchLng', Float(53)),
    Column('CouchLngOverrideFlag', Integer, nullable=False),
    Column('CouchLngPlanned', Float(53)),
    Column('CouchVrt', Float(53)),
    Column('CouchVrtOverrideFlag', Integer, nullable=False),
    Column('CouchVrtPlanned', Float(53)),
    Column('TableTopEccAngleOverFlag', Integer, nullable=False),
    Column('TableTopEccentricAngle', Float(53)),
    Column('PatientSupportAngle', Float(53)),
    Column('PatientSupportAngleOverFlag', Integer, nullable=False),
    Column('PatSupPitchOverrideFlag', Integer, nullable=False),
    Column('PatSupportPitchAngle', Float(53)),
    Column('PatSupportRollAngle', Float(53)),
    Column('PatSupRollOverrideFlag', Integer, nullable=False),
    Column('PFFlag', String(1, u'Latin1_General_BIN2')),
    Column('PFMUSubFlag', Integer, nullable=False),
    Column('PIFlag', String(1, u'Latin1_General_BIN2')),
    Column('ToleranceSer', BigInteger),
    Column('NominalEnergy', Integer),
    Column('EnergyModeOverrideFlag', Integer, nullable=False),
    Column('SSDOverrideFlag', Integer, nullable=False)
)


t_vv_ExternalFieldHstry = Table(
    'vv_ExternalFieldHstry', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('IntendedNumOfPaintings', Integer),
    Column('NumOfPaintOverrideFlag', Integer, nullable=False),
    Column('Technique', Unicode(16)),
    Column('GantryRtn', Float(53)),
    Column('GantryRtnOverrideFlag', Integer, nullable=False),
    Column('CollRtn', Float(53)),
    Column('CollRtnOverrideFlag', Integer, nullable=False),
    Column('CollMode', Unicode(16)),
    Column('CollX1', Float(53)),
    Column('CollX1OverrideFlag', Integer, nullable=False),
    Column('CollY1', Float(53)),
    Column('CollY1OverrideFlag', Integer, nullable=False),
    Column('CollX2', Float(53)),
    Column('CollX2OverrideFlag', Integer, nullable=False),
    Column('CollY2', Float(53)),
    Column('CollY2OverrideFlag', Integer, nullable=False),
    Column('PSACorrection', Float(53)),
    Column('OffPlaneAngle', Float(53)),
    Column('WedgeAngle', Float(53)),
    Column('WedgeDirection', Float(53)),
    Column('DoseRate', Integer),
    Column('DoseRateOverrideFlag', Integer, nullable=False),
    Column('WedgeDose', Float(53)),
    Column('WedgeDoseOverrideFlag', Integer, nullable=False),
    Column('StopAngle', Float(53)),
    Column('MUpDeg', Float(53)),
    Column('MUpDegOverrideFlag', Integer, nullable=False),
    Column('SnoutPosition', Float(53)),
    Column('SnoutPosOverrideFlag', Integer, nullable=False),
    Column('FixLightPolarPos', Float(53)),
    Column('FixLightAzimuthAngle', Float(53)),
    Column('GantryRtnDirection', Unicode(16)),
    Column('GantryRtnExt', Unicode(16)),
    Column('DistalEndEnergy', Float(53)),
    Column('SOBPWidth', Float(53)),
    Column('BeamModifiersSet', Unicode(64)),
    Column('WedgeNumber1', Integer),
    Column('WedgeNumber2', Integer),
    Column('WedgeAngle2', Float(53)),
    Column('WedgeDirection2', Float(53)),
    Column('BeamCurrentModulationId', Unicode(16))
)


t_vv_HistologyCodeDesc = Table(
    'vv_HistologyCodeDesc', metadata,
    Column('HistologyTableName', Unicode(64)),
    Column('HistologyCode', Unicode(16), nullable=False),
    Column('LanguageId', Unicode(16)),
    Column('Description', Unicode(254))
)


t_vv_HistologyCodeDescLng = Table(
    'vv_HistologyCodeDescLng', metadata,
    Column('HistologyTableName', Unicode(64)),
    Column('HistologyCode', Unicode(16), nullable=False),
    Column('LanguageId', Unicode(16)),
    Column('Description', Unicode(254))
)


t_vv_HistologyTableStandard = Table(
    'vv_HistologyTableStandard', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_HistologyTableStandardLng = Table(
    'vv_HistologyTableStandardLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Image = Table(
    'vv_Image', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientId', Unicode(25), nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('StudySer', BigInteger, nullable=False),
    Column('StudyUID', Unicode(64), nullable=False),
    Column('SeriesId', Unicode(16), nullable=False),
    Column('SeriesUID', Unicode(64), nullable=False),
    Column('SeriesModality', Unicode(16), nullable=False),
    Column('ImageSer', BigInteger, nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('ImageId', Unicode(16), nullable=False),
    Column('ImageName', Unicode(64)),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('StatusDate', DateTime, nullable=False),
    Column('StatusUserName', Unicode(32), nullable=False),
    Column('ImageType', Unicode(30)),
    Column('Status', Unicode(64), nullable=False),
    Column('VolumetricPixelOffset', Integer),
    Column('ProcessedFlag', Integer, nullable=False),
    Column('DefaultProcessingSer', BigInteger),
    Column('OtherProcessingSer', BigInteger),
    Column('GeometricParentSer', BigInteger),
    Column('ImageSizeX', Integer, nullable=False),
    Column('ImageSizeY', Integer, nullable=False),
    Column('ImageSizeZ', Integer, nullable=False),
    Column('ImageResX', Float(53), nullable=False),
    Column('ImageResY', Float(53), nullable=False),
    Column('ImageResZ', Float(53), nullable=False),
    Column('InverseSliceOrder', Integer, nullable=False),
    Column('FocusX', Float(53)),
    Column('FocusY', Float(53)),
    Column('FocusZ', Float(53)),
    Column('Comment', Unicode(254)),
    Column('PatientOrientation', Unicode(16)),
    Column('UsageType', Unicode(64)),
    Column('ActWindow', Integer),
    Column('ActLevel', Integer),
    Column('VolumetricPixelSlope', Float(53)),
    Column('PixelUnit', Unicode(32)),
    Column('ImageNotesLen', Integer, nullable=False),
    Column('ImageNotes', UnicodeText(1073741823)),
    Column('Transformation', BINARY(96)),
    Column('VolumeTransformation', BINARY(96)),
    Column('UserOrigin', BINARY(24)),
    Column('UserOriginComment', Unicode(254)),
    Column('DisplayTransformation', BINARY(96)),
    Column('ProcessingDefinition', UnicodeText(1073741823)),
    Column('ProcessingDefinitionLen', Integer, nullable=False),
    Column('FractionNumber', Integer),
    Column('RefDicomSeqNumber', Integer),
    Column('Image4DSer', BigInteger),
    Column('Flags4D', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_ImageRadiation = Table(
    'vv_ImageRadiation', metadata,
    Column('ImageSer', BigInteger, nullable=False),
    Column('RadiationSer', BigInteger),
    Column('ReferenceImage', Integer, nullable=False),
    Column('SliceCharacteristics', Unicode(254))
)


t_vv_LatestApproval = Table(
    'vv_LatestApproval', metadata,
    Column('ApprovalSer', Numeric(7, 0), nullable=False),
    Column('ApprovalRevCount', Integer, nullable=False),
    Column('TypeSer', BigInteger, nullable=False),
    Column('Type1Ser', BigInteger),
    Column('Type2Ser', BigInteger),
    Column('TypeRevCount', Integer),
    Column('Type1RevCount', Integer),
    Column('Type2RevCount', Integer),
    Column('ApprovalType', Unicode(30), nullable=False),
    Column('Status', Unicode(64), nullable=False),
    Column('StatusUserName', Unicode(32), nullable=False),
    Column('StatusDate', DateTime, nullable=False),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_MachineType = Table(
    'vv_MachineType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_MachineTypeLng = Table(
    'vv_MachineTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_MaritalStatus = Table(
    'vv_MaritalStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_MaritalStatusLng = Table(
    'vv_MaritalStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_NonScheduledActivity = Table(
    'vv_NonScheduledActivity', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_NonScheduledActivityActive = Table(
    'vv_NonScheduledActivityActive', metadata,
    Column('NonScheduledActivitySer', BigInteger, nullable=False),
    Column('NonScheduledActivityRevCount', Integer, nullable=False),
    Column('ActivityInstanceSer', BigInteger, nullable=False),
    Column('ActivityInstanceRevCount', Integer, nullable=False),
    Column('PatientSer', BigInteger),
    Column('CreatedByResourceSer', BigInteger),
    Column('CreatedByUserName', Unicode(32), nullable=False),
    Column('CreationDate', DateTime, nullable=False),
    Column('UID', Unicode(64), nullable=False),
    Column('ObjectStatus', Unicode(16), nullable=False),
    Column('DueDateTime', DateTime),
    Column('WorkFlowActiveFlag', Integer, nullable=False),
    Column('NonScheduledActivityCode', Unicode(64)),
    Column('Priority', Unicode(64)),
    Column('ActivityNote', Unicode(254)),
    Column('RecurrenceRuleSer', BigInteger),
    Column('ReadByAppUserName', Unicode(32)),
    Column('ReadByDateTime', DateTime),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_NonScheduledActivityLng = Table(
    'vv_NonScheduledActivityLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ObjectStatus = Table(
    'vv_ObjectStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ObjectStatusLng = Table(
    'vv_ObjectStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_OpLimit = Table(
    'vv_OpLimit', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('Expression3', Unicode(64))
)


t_vv_OpLimitLng = Table(
    'vv_OpLimitLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('Expression3', Unicode(64))
)


t_vv_OpLimitParameterName = Table(
    'vv_OpLimitParameterName', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('Expression3', Unicode(64))
)


t_vv_OpLimitParameterNameLng = Table(
    'vv_OpLimitParameterNameLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('Expression3', Unicode(64))
)


t_vv_OperationStatus = Table(
    'vv_OperationStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_OperationStatusLng = Table(
    'vv_OperationStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PIModel = Table(
    'vv_PIModel', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PIModelLng = Table(
    'vv_PIModelLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PatientDepartmentbyCUID = Table(
    'vv_PatientDepartmentbyCUID', metadata,
    Column('PatientDepartmentSer', BigInteger, nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('UserCUID', Unicode(64), nullable=False),
    Column('PatientId', Unicode(25), nullable=False)
)


t_vv_PatientDoctor = Table(
    'vv_PatientDoctor', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('PrimaryFlag', Integer),
    Column('OncologistFlag', Integer)
)


t_vv_PatientNote = Table(
    'vv_PatientNote', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PatientNoteLng = Table(
    'vv_PatientNoteLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PatientStatus = Table(
    'vv_PatientStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PatientStatusLng = Table(
    'vv_PatientStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PatientType = Table(
    'vv_PatientType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PatientTypeLng = Table(
    'vv_PatientTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_PlanSetup = Table(
    'vv_PlanSetup', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('PatientSupportDeviceSer', BigInteger),
    Column('PrescriptionSer', BigInteger),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupName', Unicode(64)),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('Status', Unicode(64), nullable=False),
    Column('StatusUserName', Unicode(32), nullable=False),
    Column('StatusDate', DateTime, nullable=False),
    Column('PlanNormFactor', Float(53)),
    Column('PlanNormMethod', Unicode(64)),
    Column('Comment', Unicode(254)),
    Column('TreatmentTechnique', Unicode(16)),
    Column('ApplicationSetupType', Unicode(16)),
    Column('ApplicationSetupNumber', Integer),
    Column('TreatmentType', Unicode(16), nullable=False),
    Column('CalcModelOptions', UnicodeText(1073741823)),
    Column('CalcModelOptionsLen', Integer, nullable=False),
    Column('TreatmentOrientation', Unicode(16)),
    Column('PrescribedPercentage', Float(53)),
    Column('PrimaryPTVSer', BigInteger),
    Column('IrregFlag', Integer, nullable=False),
    Column('FieldRules', UnicodeText(1073741823)),
    Column('FieldRulesLen', Integer, nullable=False),
    Column('SkinFlashMargin', Float(53)),
    Column('ProtocolPhaseId', Unicode(64)),
    Column('MultiFieldOptFlag', Integer, nullable=False),
    Column('CopyOfSer', BigInteger),
    Column('StructureSetSer', BigInteger),
    Column('EquipmentSer', BigInteger),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('RaySearchPrivateData', LargeBinary),
    Column('RaySearchPrivateDataLen', Integer, nullable=False),
    Column('Intent', Unicode(16)),
    Column('ViewingPlane', BINARY(96)),
    Column('ViewingPlaneULCorner', BINARY(24)),
    Column('ViewingPlaneLRCorner', BINARY(24)),
    Column('BrachyPdrPulseInterval', Float(53)),
    Column('BrachyPdrNoOfPulses', Integer),
    Column('TransactionId', String(255, u'Latin1_General_BIN2')),
    Column('ImageSer', BigInteger)
)


t_vv_PortalImages = Table(
    'vv_PortalImages', metadata,
    Column('ImageSer', BigInteger, nullable=False),
    Column('RadiationSer', BigInteger),
    Column('ReferenceImage', Integer, nullable=False),
    Column('SliceCharacteristics', Unicode(254))
)


t_vv_ProcedureItem = Table(
    'vv_ProcedureItem', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_ProcedureItemLng = Table(
    'vv_ProcedureItemLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_RTPlan = Table(
    'vv_RTPlan', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('PlanSOPClassSer', BigInteger, nullable=False),
    Column('PlanUID', Unicode(64), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('RTPlanName', Unicode(64)),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('NoFractions', Integer),
    Column('StartDelay', Integer),
    Column('DicomSeqNumber', Integer, nullable=False),
    Column('Comment', Unicode(254)),
    Column('InterfaceStamp', Integer),
    Column('PrescribedDose', Float(53)),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('PlanIntegrityHash', BINARY(32)),
    Column('PlanHashVersion', Integer),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('TreatmentOrder', Integer),
    Column('FileName', Unicode(254)),
    Column('FractionPatternDigitsPerDay', Integer),
    Column('FractionPattern', Unicode(64))
)


t_vv_Race = Table(
    'vv_Race', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_RaceLng = Table(
    'vv_RaceLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Radiation = Table(
    'vv_Radiation', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationId', Unicode(16), nullable=False),
    Column('RadiationName', Unicode(64)),
    Column('RadiationType', Unicode(32), nullable=False),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('RadiationNumber', Integer, nullable=False),
    Column('TechniqueLabel', Unicode(64)),
    Column('RadiationOrder', Integer),
    Column('RefImageSer', BigInteger),
    Column('SetupNote', Unicode(254)),
    Column('RefImageUID', Unicode(64)),
    Column('RefImageSOPClassSer', BigInteger),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32))
)


t_vv_RadiationHstry = Table(
    'vv_RadiationHstry', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('TreatmentRecordSer', BigInteger, nullable=False),
    Column('RadiationHstryType', Unicode(32), nullable=False),
    Column('TreatmentDeliveryType', Unicode(16)),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('RadiationId', Unicode(16), nullable=False),
    Column('RadiationName', Unicode(64)),
    Column('RadiationNumber', Integer),
    Column('TechniqueLabel', Unicode(64)),
    Column('RadiationType', Unicode(16)),
    Column('TreatmentStartTime', DateTime, nullable=False),
    Column('TreatmentEndTime', DateTime, nullable=False),
    Column('TreatmentTime', Float(53)),
    Column('TreatmentTimeOverrideFlag', Integer, nullable=False),
    Column('TerminationStatus', Unicode(16), nullable=False),
    Column('FractionNumber', Integer, nullable=False),
    Column('ApprovalDate', DateTime),
    Column('ApprovalUserName', Unicode(32)),
    Column('UserName1', Unicode(64)),
    Column('UserName2', Unicode(32)),
    Column('UserName3', Unicode(32)),
    Column('OverrideFlag', Integer, nullable=False),
    Column('NoOfImage', Integer),
    Column('PrintFlag', Integer, nullable=False),
    Column('RVFlag', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('HistoryNote', Unicode),
    Column('MachineNote', Unicode),
    Column('FieldSetupNote', Unicode),
    Column('BeamOffCode', Unicode(64))
)


t_vv_RadiationRefPoint = Table(
    'vv_RadiationRefPoint', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RadiationId', Unicode(16), nullable=False),
    Column('RefPointId', Unicode(16), nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('RefPointSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('CacheKeySer', BigInteger),
    Column('FieldDose', Float(53)),
    Column('DoseSpecificationFlag', Integer, nullable=False),
    Column('Depth', Float(53)),
    Column('PSSD', Float(53)),
    Column('DominantFieldFlag', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('NominalFlag', Integer, nullable=False)
)


t_vv_RefIndex = Table(
    'vv_RefIndex', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_RefPoint = Table(
    'vv_RefPoint', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('PatientVolumeId', Unicode(16), nullable=False),
    Column('RefPointSer', BigInteger, nullable=False),
    Column('PatientVolumeSer', BigInteger, nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('RefPointId', Unicode(16), nullable=False),
    Column('RefPointName', Unicode(64)),
    Column('RefPointUID', Unicode(64), nullable=False),
    Column('RefPointType', Unicode(16)),
    Column('TotalDoseLimit', Float(53)),
    Column('DailyDoseLimit', Float(53)),
    Column('SessionDoseLimit', Float(53)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32))
)


t_vv_ReferenceImages = Table(
    'vv_ReferenceImages', metadata,
    Column('ImageSer', BigInteger, nullable=False),
    Column('RadiationSer', BigInteger)
)


t_vv_Religion = Table(
    'vv_Religion', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ReligionLng = Table(
    'vv_ReligionLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ResourceGroup = Table(
    'vv_ResourceGroup', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_ResourceGroupLng = Table(
    'vv_ResourceGroupLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('SubSelector', BigInteger)
)


t_vv_ResourceName = Table(
    'vv_ResourceName', metadata,
    Column('ResourceSer', BigInteger, nullable=False),
    Column('ResourceName', Unicode(208), nullable=False)
)


t_vv_ResourceType = Table(
    'vv_ResourceType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ResourceTypeLng = Table(
    'vv_ResourceTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ScheduledActivity = Table(
    'vv_ScheduledActivity', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ScheduledActivityActive = Table(
    'vv_ScheduledActivityActive', metadata,
    Column('ScheduledActivitySer', BigInteger, nullable=False),
    Column('ScheduledActivityRevCount', Integer, nullable=False),
    Column('ActivityInstanceSer', BigInteger, nullable=False),
    Column('ActivityInstanceRevCount', Integer, nullable=False),
    Column('PatientSer', BigInteger),
    Column('CreatedByResourceSer', BigInteger),
    Column('CreatedByUserName', Unicode(32), nullable=False),
    Column('CreationDate', DateTime, nullable=False),
    Column('UID', Unicode(64), nullable=False),
    Column('ScheduledStartTime', DateTime),
    Column('ScheduledEndTime', DateTime),
    Column('ActualStartDate', DateTime),
    Column('ActualEndDate', DateTime),
    Column('ObjectStatus', Unicode(16), nullable=False),
    Column('ScheduledActivityCode', Unicode(64)),
    Column('Priority', Unicode(64)),
    Column('WaitListedFlag', Integer, nullable=False),
    Column('ActivityNote', Unicode(254)),
    Column('RecurrenceRuleSer', BigInteger),
    Column('ReadByAppUserName', Unicode(32)),
    Column('ReadByDateTime', DateTime),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('PreMedication', Unicode(64)),
    Column('ContrastAgent', Unicode(64)),
    Column('WorkFlowActiveFlag', Integer, nullable=False)
)


t_vv_ScheduledActivityLng = Table(
    'vv_ScheduledActivityLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Series = Table(
    'vv_Series', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('StudySer', BigInteger),
    Column('SeriesId', Unicode(16), nullable=False),
    Column('SeriesName', Unicode(64)),
    Column('SeriesNumber', Integer),
    Column('SeriesUID', Unicode(64), nullable=False),
    Column('SeriesType', Unicode(30), nullable=False),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('BodyPartExamined', Unicode(32)),
    Column('PatientOrientation', Unicode(32)),
    Column('SeriesModality', Unicode(16), nullable=False),
    Column('AcquisitionType', Unicode(32)),
    Column('Comment', Unicode(254)),
    Column('ReconstructionType4D', Unicode(64)),
    Column('ReconstructionPhase4D', Float(53)),
    Column('PositionReferenceIndicator', Unicode(64)),
    Column('FrameOfReferenceUID', Unicode(64)),
    Column('ResampledSeriesFlag', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('ResourceSer', BigInteger),
    Column('RelatedCourseSer', BigInteger),
    Column('RelatedPlanSetupSer', BigInteger),
    Column('RelatedRadiationSer', BigInteger),
    Column('RelatedDiagnosisSer', BigInteger)
)


t_vv_Session = Table(
    'vv_Session', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('SessionNum', Integer, nullable=False),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_SessionProcedure = Table(
    'vv_SessionProcedure', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('SessionNum', Integer, nullable=False),
    Column('SessionProcedureSer', BigInteger, nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('SequenceNumber', Integer),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('ProcedureItemSer', BigInteger),
    Column('ProcedureInstanceUID', Unicode(64)),
    Column('SessionProcedureTemplateId', Unicode(16), nullable=False),
    Column('Status', Unicode(16), nullable=False),
    Column('ProgressIndicator', Float(53), nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32))
)


t_vv_SessionProcedurePart = Table(
    'vv_SessionProcedurePart', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('SessionNum', Integer, nullable=False),
    Column('SessionProcedureTemplateId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger),
    Column('PlanSetupId', Unicode(16)),
    Column('RadiationId', Unicode(16)),
    Column('SessionProcedurePartSer', BigInteger, nullable=False),
    Column('RadiationSer', BigInteger),
    Column('ImageType', Unicode(32)),
    Column('SequenceNumber', Integer, nullable=False),
    Column('AcqAdjustment', Float(53)),
    Column('AutoSave', Integer, nullable=False),
    Column('DoseAccumulation', Integer, nullable=False),
    Column('Continuous', Integer, nullable=False),
    Column('BeamOff', Integer, nullable=False),
    Column('DeviationImage', Integer, nullable=False),
    Column('DevEnergy', Integer),
    Column('DevDoseRate', Integer),
    Column('DevGeometry', Integer),
    Column('JawState', Float(53)),
    Column('DevCollX1', Float(53)),
    Column('DevCollX2', Float(53)),
    Column('DevCollY1', Float(53)),
    Column('DevCollY2', Float(53)),
    Column('MUSubtraction', Integer),
    Column('AcquisitionMode', Unicode(64)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('SessionProcedureSer', BigInteger, nullable=False),
    Column('ImageModality', Unicode(16), nullable=False),
    Column('RTPlanSer', BigInteger)
)


t_vv_SessionRTPlan = Table(
    'vv_SessionRTPlan', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('SessionNum', Integer, nullable=False),
    Column('SessionRTPlanSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('Status', Unicode(16), nullable=False)
)


t_vv_SessionStatus = Table(
    'vv_SessionStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_SessionStatusLng = Table(
    'vv_SessionStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Sex = Table(
    'vv_Sex', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_SexLng = Table(
    'vv_SexLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Slice = Table(
    'vv_Slice', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('StudySer', BigInteger, nullable=False),
    Column('StudyUID', Unicode(64), nullable=False),
    Column('SeriesId', Unicode(16), nullable=False),
    Column('SeriesUID', Unicode(64), nullable=False),
    Column('SeriesModality', Unicode(16), nullable=False),
    Column('SliceSer', BigInteger, nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('SliceUID', Unicode(64), nullable=False),
    Column('CreationDate', DateTime),
    Column('CreationUserName', Unicode(32)),
    Column('SliceNumber', Integer),
    Column('Position', Float(53)),
    Column('FileName', Unicode(254)),
    Column('SliceType', Unicode(30)),
    Column('SliceModality', Unicode(16), nullable=False),
    Column('ResourceSer', BigInteger),
    Column('SliceFormat', Unicode(32)),
    Column('HeaderSize', Integer, nullable=False),
    Column('SizeX', Integer, nullable=False),
    Column('SizeY', Integer, nullable=False),
    Column('AcqWindow', Integer),
    Column('AcqLevel', Integer),
    Column('ResolutionX', Float(53), nullable=False),
    Column('ResolutionY', Float(53), nullable=False),
    Column('CalibratedFlag', Integer, nullable=False),
    Column('PixelOffset', Integer),
    Column('PixelSlope', Float(53)),
    Column('Transformation', BINARY(96)),
    Column('SliceCharacteristics', Unicode(254)),
    Column('PhotometricInterpretation', Unicode(16)),
    Column('BitsAllocated', Integer, nullable=False),
    Column('BitsStored', Integer),
    Column('CouchVrt', Float(53)),
    Column('CouchLng', Float(53)),
    Column('CouchLat', Float(53)),
    Column('PatientSupportAngle', Float(53)),
    Column('TableTopEccentricAngle', Float(53)),
    Column('ConversionType', Unicode(16)),
    Column('HighBit', Integer, nullable=False),
    Column('PatSupportPitchAngle', Float(53)),
    Column('PatSupportRollAngle', Float(53)),
    Column('Thickness', Float(53)),
    Column('EquipmentSer', BigInteger),
    Column('NumberOfFrames', Integer),
    Column('DCTransferSyntaxSer', BigInteger),
    Column('IsLockedFlag', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('PixelIntensityRel', Integer),
    Column('PixelIntensitySign', Integer),
    Column('PixelRepresentation', Integer, nullable=False),
    Column('TransactionId', String(255, u'Latin1_General_BIN2')),
    Column('ActualPatientWeight', Float(53)),
    Column('ActualPatientHeight', Float(53)),
    Column('ContributingEquipmentSer', BigInteger),
    Column('SOPClassSer', BigInteger, nullable=False),
    Column('AcquisitionDateTime', DateTime),
    Column('IrradiationEventUID', Unicode(64))
)


t_vv_Slot = Table(
    'vv_Slot', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64)),
    Column('Expression3', Unicode(64))
)


t_vv_SlotLng = Table(
    'vv_SlotLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_SmokingStatus = Table(
    'vv_SmokingStatus', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_SmokingStatusLng = Table(
    'vv_SmokingStatusLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_SpatialRegistration = Table(
    'vv_SpatialRegistration', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('StudySer', BigInteger, nullable=False),
    Column('StudyUID', Unicode(64), nullable=False),
    Column('SeriesId', Unicode(16), nullable=False),
    Column('SeriesUID', Unicode(64), nullable=False),
    Column('SeriesModality', Unicode(16), nullable=False),
    Column('SpatialRegistrationIODId', Unicode(16), nullable=False),
    Column('SpatialRegistrationUID', Unicode(64), nullable=False),
    Column('SpatialRegistrationSer', BigInteger, nullable=False),
    Column('SpatialRegistrationIODSer', BigInteger, nullable=False),
    Column('FrameOfReferenceUID', Unicode(64)),
    Column('Comment', Unicode(254)),
    Column('RegTypeCodeValue', Unicode(16)),
    Column('RegTypeCodeMeaning', Unicode(64)),
    Column('RegTypeCodeDesignator', Unicode(16)),
    Column('RegTypeCodeVersion', Unicode(16)),
    Column('RegSubType', Unicode(64)),
    Column('Transformation', BINARY(96), nullable=False),
    Column('AverageErrorDist', Float(53)),
    Column('MaxErrorDist', Float(53)),
    Column('MatchAlgorithm', Unicode(64)),
    Column('Status', Unicode(64), nullable=False),
    Column('StatusDate', DateTime, nullable=False),
    Column('StatusUserName', Unicode(32), nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_SpatialRegistrationIOD = Table(
    'vv_SpatialRegistrationIOD', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('StudySer', BigInteger, nullable=False),
    Column('StudyUID', Unicode(64), nullable=False),
    Column('SeriesId', Unicode(16), nullable=False),
    Column('SeriesUID', Unicode(64), nullable=False),
    Column('SeriesModality', Unicode(16), nullable=False),
    Column('SpatialRegistrationIODSer', BigInteger, nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('SpatialRegistrationIODId', Unicode(16), nullable=False),
    Column('SpatialRegistrationUID', Unicode(64), nullable=False),
    Column('InstanceNumber', Integer, nullable=False),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('Comment', Unicode(254)),
    Column('EquipmentSer', BigInteger),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('RegistrationType', Unicode(32), nullable=False),
    Column('FileName', Unicode(254))
)


t_vv_SpatialRegistrationImage = Table(
    'vv_SpatialRegistrationImage', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('StudySer', BigInteger, nullable=False),
    Column('StudyUID', Unicode(64), nullable=False),
    Column('SeriesId', Unicode(16), nullable=False),
    Column('SeriesUID', Unicode(64), nullable=False),
    Column('SeriesModality', Unicode(16), nullable=False),
    Column('SpatialRegistrationIODId', Unicode(16), nullable=False),
    Column('SpatialRegistrationUID', Unicode(64), nullable=False),
    Column('SpatialRegistrationSer', BigInteger, nullable=False),
    Column('SpatialRegistrationIODSer', BigInteger, nullable=False),
    Column('FrameOfReferenceUID', Unicode(64)),
    Column('Comment', Unicode(254)),
    Column('RegTypeCodeValue', Unicode(16)),
    Column('RegTypeCodeMeaning', Unicode(64)),
    Column('RegTypeCodeDesignator', Unicode(16)),
    Column('RegTypeCodeVersion', Unicode(16)),
    Column('RegSubType', Unicode(64)),
    Column('Transformation', BINARY(96), nullable=False),
    Column('AverageErrorDist', Float(53)),
    Column('MaxErrorDist', Float(53)),
    Column('MatchAlgorithm', Unicode(64)),
    Column('Status', Unicode(64), nullable=False),
    Column('StatusDate', DateTime, nullable=False),
    Column('StatusUserName', Unicode(32), nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_Study = Table(
    'vv_Study', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('StudySer', BigInteger, nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('StudyId', Unicode(16), nullable=False),
    Column('StudyName', Unicode(64)),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('ReferringPhysicianName', Unicode(64)),
    Column('StudyUID', Unicode(64), nullable=False),
    Column('AccessionNumber', Unicode(16)),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('RelatedCourseSer', BigInteger),
    Column('RelatedDiagnosisSer', BigInteger)
)


t_vv_Technique = Table(
    'vv_Technique', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_TechniqueLng = Table(
    'vv_TechniqueLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_Template = Table(
    'vv_Template', metadata,
    Column('TemplateSer', BigInteger, nullable=False),
    Column('TemplateRevCount', Integer, nullable=False),
    Column('PatientSer', BigInteger),
    Column('DepartmentSer', BigInteger),
    Column('DerivedFromSer', BigInteger),
    Column('CreationDate', DateTime, nullable=False),
    Column('TemplateID', Unicode(64)),
    Column('ObjectStatus', Unicode(16), nullable=False),
    Column('DefaultFlag', Integer, nullable=False),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('DiagnosisStageSer', BigInteger),
    Column('PayorSer', BigInteger),
    Column('ResourceSer', BigInteger),
    Column('CourseSer', BigInteger)
)


t_vv_TemplateCycle = Table(
    'vv_TemplateCycle', metadata,
    Column('TemplateCycleSer', BigInteger, nullable=False),
    Column('TemplateCycleRevCount', Integer, nullable=False),
    Column('TemplateSer', BigInteger, nullable=False),
    Column('TemplateRevCount', Integer, nullable=False),
    Column('ObjectStatus', Unicode(16), nullable=False),
    Column('CycleSer', BigInteger, nullable=False),
    Column('Comment', Unicode(254)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_ToxicMaterialType = Table(
    'vv_ToxicMaterialType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ToxicMaterialTypeLng = Table(
    'vv_ToxicMaterialTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ToxicUsageType = Table(
    'vv_ToxicUsageType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_ToxicUsageTypeLng = Table(
    'vv_ToxicUsageTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_TreatmentRecord = Table(
    'vv_TreatmentRecord', metadata,
    Column('PatientId', Unicode(25), nullable=False),
    Column('PatientType', Unicode(30), nullable=False),
    Column('CourseId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('TreatmentRecordSer', BigInteger, nullable=False),
    Column('PatientSer', BigInteger, nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger),
    Column('PlanSOPClassSer', BigInteger, nullable=False),
    Column('TreatmentRecordSOPClassSer', BigInteger, nullable=False),
    Column('PlanUID', Unicode(64), nullable=False),
    Column('TreatmentRecordUID', Unicode(64), nullable=False),
    Column('FileName', Unicode(254)),
    Column('ActualMachineSer', BigInteger),
    Column('ActualMachineAuthorization', Unicode(64)),
    Column('MachOverrideFlag', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryTaskName', Unicode(32)),
    Column('StructureSetUID', Unicode(64)),
    Column('TreatmentRecordDateTime', DateTime),
    Column('NoOfFractions', Integer)
)


t_vv_UserLanguage = Table(
    'vv_UserLanguage', metadata,
    Column('LanguageId', Unicode(16))
)


t_vv_VenueType = Table(
    'vv_VenueType', metadata,
    Column('ListSelector', Unicode(32), nullable=False),
    Column('LanguageId', Unicode(16), nullable=False),
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_VenueTypeLng = Table(
    'vv_VenueTypeLng', metadata,
    Column('LookupValue', Unicode(64), nullable=False),
    Column('Expression1', Unicode(64))
)


t_vv_digit = Table(
    'vv_digit', metadata,
    Column('n', Integer, nullable=False)
)


t_vv_rpTfhCourse = Table(
    'vv_rpTfhCourse', metadata,
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RTPlanId', Unicode(16), nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('PlanSetupId', Unicode(16), nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('CourseId', Unicode(16), nullable=False)
)


t_vv_syActiveImagingSession = Table(
    'vv_syActiveImagingSession', metadata,
    Column('CourseSer', BigInteger, nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('SessionNum', Integer, nullable=False)
)


t_vv_syActiveSession = Table(
    'vv_syActiveSession', metadata,
    Column('CourseSer', BigInteger, nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('SessionNum', Integer, nullable=False)
)


t_vv_syDoseFiguresApp = Table(
    'vv_syDoseFiguresApp', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('FirstRTPlanSer', BigInteger, nullable=False),
    Column('RefPointSer', BigInteger),
    Column('PrimaryFlag', Integer),
    Column('FractionsDelivered', Integer, nullable=False),
    Column('FractionsPlanned', Integer, nullable=False),
    Column('FractionsRemaining', Integer, nullable=False),
    Column('DosePerFraction', Float(53)),
    Column('DoseDelivered', Float(53)),
    Column('DoseRemainingInFraction', Float(53)),
    Column('RunningPartial', Integer),
    Column('DoseRemainingMax', Float(53)),
    Column('DoseRemainingMin', Float(53)),
    Column('DoseRemaining', Float(53)),
    Column('DosePredictedMax', Float(53)),
    Column('DosePredictedMin', Float(53)),
    Column('DosePredicted', Float(53))
)


t_vv_syDoseFiguresAppSum = Table(
    'vv_syDoseFiguresAppSum', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RefPointSer', BigInteger),
    Column('PrimaryFlag', Integer),
    Column('FractionsDelivered', Integer, nullable=False),
    Column('FractionsPlanned', Integer, nullable=False),
    Column('FractionsRemaining', Integer, nullable=False),
    Column('DosePerFraction', Float(53)),
    Column('DoseDelivered', Float(53)),
    Column('DoseRemainingInFraction', Float(53)),
    Column('RunningPartial', Integer),
    Column('DoseRemainingMax', Float(53)),
    Column('DoseRemainingMin', Float(53)),
    Column('DoseRemaining', Float(53)),
    Column('DosePredictedMax', Float(53)),
    Column('DosePredictedMin', Float(53)),
    Column('DosePredicted', Float(53))
)


t_vv_syExternalFieldHstryAddOn = Table(
    'vv_syExternalFieldHstryAddOn', metadata,
    Column('BeamCurrentModulationId', Unicode(16)),
    Column('BeamModifiersSet', Unicode(64)),
    Column('CollMode', Unicode(16)),
    Column('CollRtn', Float(53)),
    Column('CollRtnOverrideFlag', Integer, nullable=False),
    Column('CollX1', Float(53)),
    Column('CollX1OverrideFlag', Integer, nullable=False),
    Column('CollX2', Float(53)),
    Column('CollX2OverrideFlag', Integer, nullable=False),
    Column('CollY1', Float(53)),
    Column('CollY1OverrideFlag', Integer, nullable=False),
    Column('CollY2', Float(53)),
    Column('CollY2OverrideFlag', Integer, nullable=False),
    Column('DistalEndEnergy', Float(53)),
    Column('DoseRate', Integer),
    Column('DoseRateOverrideFlag', Integer, nullable=False),
    Column('FixLightAzimuthAngle', Float(53)),
    Column('FixLightPolarPos', Float(53)),
    Column('GantryRtn', Float(53)),
    Column('GantryRtnDirection', Unicode(16)),
    Column('GantryRtnExt', Unicode(16)),
    Column('GantryRtnOverrideFlag', Integer, nullable=False),
    Column('IntendedNumOfPaintings', Integer),
    Column('MUpDeg', Float(53)),
    Column('MUpDegOverrideFlag', Integer, nullable=False),
    Column('NumOfPaintOverrideFlag', Integer, nullable=False),
    Column('OffPlaneAngle', Float(53)),
    Column('PSACorrection', Float(53)),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('SOBPWidth', Float(53)),
    Column('SnoutPosOverrideFlag', Integer, nullable=False),
    Column('SnoutPosition', Float(53)),
    Column('StopAngle', Float(53)),
    Column('Technique', Unicode(16)),
    Column('WedgeAngle', Float(53)),
    Column('WedgeAngle2', Float(53)),
    Column('WedgeDirection', Float(53)),
    Column('WedgeDirection2', Float(53)),
    Column('WedgeDose', Float(53)),
    Column('WedgeDoseOverrideFlag', Integer, nullable=False),
    Column('WedgeNumber1', Integer),
    Column('WedgeNumber2', Integer),
    Column('AddOnId1', Unicode(16)),
    Column('AddOnId2', Unicode(16)),
    Column('AddOnId3', Unicode(16)),
    Column('AddOnId4', Unicode(16)),
    Column('AddOnId5', Unicode(16)),
    Column('AddOnId6', Unicode(16)),
    Column('AddOnId7', Unicode(16)),
    Column('AddOnId8', Unicode(16)),
    Column('AddOnId9', Unicode(16)),
    Column('AddOnId10', Unicode(16)),
    Column('AddOnType1', Unicode(30)),
    Column('AddOnType2', Unicode(30)),
    Column('AddOnType3', Unicode(30)),
    Column('AddOnType4', Unicode(30)),
    Column('AddOnType5', Unicode(30)),
    Column('AddOnType6', Unicode(30)),
    Column('AddOnType7', Unicode(30)),
    Column('AddOnType8', Unicode(30)),
    Column('AddOnType9', Unicode(30)),
    Column('AddOnType10', Unicode(30)),
    Column('AddOnSubType1', Unicode(64)),
    Column('AddOnSubType2', Unicode(64)),
    Column('AddOnSubType3', Unicode(64)),
    Column('AddOnSubType4', Unicode(64)),
    Column('AddOnSubType5', Unicode(64)),
    Column('AddOnSubType6', Unicode(64)),
    Column('AddOnSubType7', Unicode(64)),
    Column('AddOnSubType8', Unicode(64)),
    Column('AddOnSubType9', Unicode(64)),
    Column('AddOnSubType10', Unicode(64))
)


t_vv_syFieldMU = Table(
    'vv_syFieldMU', metadata,
    Column('RadiationSer', BigInteger, nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('MU', Float(53)),
    Column('MURounded', Numeric(18, 4))
)


t_vv_syFieldMUNative = Table(
    'vv_syFieldMUNative', metadata,
    Column('RadiationSer', BigInteger, nullable=False),
    Column('PlanSetupSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('MU', Float(53)),
    Column('ResourceSer', BigInteger),
    Column('TechniqueLabel', Unicode(64))
)


t_vv_syLastTreatedImagedSession = Table(
    'vv_syLastTreatedImagedSession', metadata,
    Column('CourseSer', BigInteger, nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('SessionNum', Integer, nullable=False)
)


t_vv_syLastTreatedSession = Table(
    'vv_syLastTreatedSession', metadata,
    Column('CourseSer', BigInteger, nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('SessionNum', Integer, nullable=False)
)


t_vv_syPatientRTStatusCBCT = Table(
    'vv_syPatientRTStatusCBCT', metadata,
    Column('PatientSer', BigInteger),
    Column('StatusType', String(12, u'Latin1_General_BIN2'), nullable=False),
    Column('Status', Unicode(64), nullable=False),
    Column('ObjectType', String(12, u'Latin1_General_BIN2'), nullable=False),
    Column('LastObjectDate', DateTime)
)


t_vv_syPatientRTStatusCourses = Table(
    'vv_syPatientRTStatusCourses', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('StatusType', String(13, u'Latin1_General_BIN2'), nullable=False),
    Column('Status', Unicode(16), nullable=False),
    Column('ObjectType', String(30, u'Latin1_General_BIN2')),
    Column('LastObjectDate', DateTime)
)


t_vv_syPatientRTStatusImages = Table(
    'vv_syPatientRTStatusImages', metadata,
    Column('PatientSer', BigInteger),
    Column('StatusType', String(12, u'Latin1_General_BIN2'), nullable=False),
    Column('Status', Unicode(64), nullable=False),
    Column('ObjectType', Unicode(30)),
    Column('LastObjectDate', DateTime)
)


t_vv_syPatientRTStatusPlans = Table(
    'vv_syPatientRTStatusPlans', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('StatusType', String(11, u'Latin1_General_BIN2'), nullable=False),
    Column('Status', Unicode(64), nullable=False),
    Column('ObjectType', String(30, u'Latin1_General_BIN2')),
    Column('LastObjectDate', DateTime)
)


t_vv_syPatientRTStatusTrackings = Table(
    'vv_syPatientRTStatusTrackings', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('StatusType', String(15, u'Latin1_General_BIN2'), nullable=False),
    Column('Status', String(6, u'Latin1_General_BIN2'), nullable=False),
    Column('ObjectType', String(30, u'Latin1_General_BIN2')),
    Column('LastObjectDate', DateTime)
)


t_vv_syPredecessorPlanRelationship = Table(
    'vv_syPredecessorPlanRelationship', metadata,
    Column('PlanRelationshipSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RelatedRTPlanSer', BigInteger),
    Column('RelatedPlanUID', Unicode(64)),
    Column('RelatedPlanSOPClassSer', BigInteger)
)


t_vv_sySessionProcedureRTPlan = Table(
    'vv_sySessionProcedureRTPlan', metadata,
    Column('SessionProcedureSer', BigInteger, nullable=False),
    Column('Status', Unicode(16), nullable=False),
    Column('SessionSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger)
)


t_vv_sySessionsWithScheduledPlans = Table(
    'vv_sySessionsWithScheduledPlans', metadata,
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('LastTreatedSessionSer', BigInteger),
    Column('FirstActiveSessionSer', BigInteger),
    Column('LastTreatedImagedSessionSer', BigInteger),
    Column('FirstActiveImagingSessionSer', BigInteger)
)


t_vv_syTFHFull = Table(
    'vv_syTFHFull', metadata,
    Column('ActualMachineAuthorization', Unicode(64)),
    Column('ActualMachineSer', BigInteger),
    Column('FileName', Unicode(254)),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('HstryTimeStamp', DateTime),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('MachOverrideFlag', Integer, nullable=False),
    Column('NoOfFractions', Integer),
    Column('PatientSer', BigInteger, nullable=False),
    Column('PlanSOPClassSer', BigInteger, nullable=False),
    Column('PlanUID', Unicode(64), nullable=False),
    Column('RTPlanSer', BigInteger),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('StructureSetUID', Unicode(64)),
    Column('TreatmentRecordDateTime', DateTime),
    Column('TreatmentRecordSOPClassSer', BigInteger, nullable=False),
    Column('TreatmentRecordSer', BigInteger, nullable=False),
    Column('TreatmentRecordUID', Unicode(64), nullable=False),
    Column('ApprovalDate', DateTime),
    Column('ApprovalUserName', Unicode(32)),
    Column('BeamOffCode', Unicode(64)),
    Column('FieldSetupNote', Unicode),
    Column('FractionNumber', Integer, nullable=False),
    Column('HistoryNote', Unicode),
    Column('MachineNote', Unicode),
    Column('NoOfImage', Integer),
    Column('OverrideFlag', Integer, nullable=False),
    Column('PrintFlag', Integer, nullable=False),
    Column('RVFlag', Integer, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('RadiationHstryType', Unicode(32), nullable=False),
    Column('RadiationId', Unicode(16), nullable=False),
    Column('RadiationName', Unicode(64)),
    Column('RadiationNumber', Integer),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('RadiationType', Unicode(16)),
    Column('TechniqueLabel', Unicode(64)),
    Column('TerminationStatus', Unicode(16), nullable=False),
    Column('TreatmentDeliveryType', Unicode(16)),
    Column('TreatmentEndTime', DateTime, nullable=False),
    Column('TreatmentStartTime', DateTime, nullable=False),
    Column('TreatmentTime', Float(53)),
    Column('TreatmentTimeOverrideFlag', Integer, nullable=False),
    Column('UserName1', Unicode(64)),
    Column('UserName2', Unicode(32)),
    Column('UserName3', Unicode(32)),
    Column('ActualMeterset', Float(53)),
    Column('CouchCorrectionLat', Float(53)),
    Column('CouchCorrectionLng', Float(53)),
    Column('CouchCorrectionVrt', Float(53)),
    Column('CouchLat', Float(53)),
    Column('CouchLatOverrideFlag', Integer, nullable=False),
    Column('CouchLatPlanned', Float(53)),
    Column('CouchLng', Float(53)),
    Column('CouchLngOverrideFlag', Integer, nullable=False),
    Column('CouchLngPlanned', Float(53)),
    Column('CouchVrt', Float(53)),
    Column('CouchVrtOverrideFlag', Integer, nullable=False),
    Column('CouchVrtPlanned', Float(53)),
    Column('EnergyModeOverrideFlag', Integer, nullable=False),
    Column('MetersetOverrideFlag', Integer, nullable=False),
    Column('NominalEnergy', Integer),
    Column('PFFlag', String(1, u'Latin1_General_BIN2')),
    Column('PFMUSubFlag', Integer, nullable=False),
    Column('PIFlag', String(1, u'Latin1_General_BIN2')),
    Column('PatSupPitchOverrideFlag', Integer, nullable=False),
    Column('PatSupRollOverrideFlag', Integer, nullable=False),
    Column('PatSupportPitchAngle', Float(53)),
    Column('PatSupportRollAngle', Float(53)),
    Column('PatientSupportAngle', Float(53)),
    Column('PatientSupportAngleOverFlag', Integer, nullable=False),
    Column('PlannedMeterset', Float(53)),
    Column('SSD', Float(53)),
    Column('SSDOverrideFlag', Integer, nullable=False),
    Column('TableTopEccAngleOverFlag', Integer, nullable=False),
    Column('TableTopEccentricAngle', Float(53)),
    Column('ToleranceSer', BigInteger),
    Column('AddOnId1', Unicode(16)),
    Column('AddOnId10', Unicode(16)),
    Column('AddOnId2', Unicode(16)),
    Column('AddOnId3', Unicode(16)),
    Column('AddOnId4', Unicode(16)),
    Column('AddOnId5', Unicode(16)),
    Column('AddOnId6', Unicode(16)),
    Column('AddOnId7', Unicode(16)),
    Column('AddOnId8', Unicode(16)),
    Column('AddOnId9', Unicode(16)),
    Column('AddOnSubType1', Unicode(64)),
    Column('AddOnSubType10', Unicode(64)),
    Column('AddOnSubType2', Unicode(64)),
    Column('AddOnSubType3', Unicode(64)),
    Column('AddOnSubType4', Unicode(64)),
    Column('AddOnSubType5', Unicode(64)),
    Column('AddOnSubType6', Unicode(64)),
    Column('AddOnSubType7', Unicode(64)),
    Column('AddOnSubType8', Unicode(64)),
    Column('AddOnSubType9', Unicode(64)),
    Column('AddOnType1', Unicode(30)),
    Column('AddOnType10', Unicode(30)),
    Column('AddOnType2', Unicode(30)),
    Column('AddOnType3', Unicode(30)),
    Column('AddOnType4', Unicode(30)),
    Column('AddOnType5', Unicode(30)),
    Column('AddOnType6', Unicode(30)),
    Column('AddOnType7', Unicode(30)),
    Column('AddOnType8', Unicode(30)),
    Column('AddOnType9', Unicode(30)),
    Column('BeamCurrentModulationId', Unicode(16)),
    Column('BeamModifiersSet', Unicode(64)),
    Column('CollMode', Unicode(16)),
    Column('CollRtn', Float(53)),
    Column('CollRtnOverrideFlag', Integer, nullable=False),
    Column('CollX1', Float(53)),
    Column('CollX1OverrideFlag', Integer, nullable=False),
    Column('CollX2', Float(53)),
    Column('CollX2OverrideFlag', Integer, nullable=False),
    Column('CollY1', Float(53)),
    Column('CollY1OverrideFlag', Integer, nullable=False),
    Column('CollY2', Float(53)),
    Column('CollY2OverrideFlag', Integer, nullable=False),
    Column('DistalEndEnergy', Float(53)),
    Column('DoseRate', Integer),
    Column('DoseRateOverrideFlag', Integer, nullable=False),
    Column('FixLightAzimuthAngle', Float(53)),
    Column('FixLightPolarPos', Float(53)),
    Column('GantryRtn', Float(53)),
    Column('GantryRtnDirection', Unicode(16)),
    Column('GantryRtnExt', Unicode(16)),
    Column('GantryRtnOverrideFlag', Integer, nullable=False),
    Column('IntendedNumOfPaintings', Integer),
    Column('MUpDeg', Float(53)),
    Column('MUpDegOverrideFlag', Integer, nullable=False),
    Column('NumOfPaintOverrideFlag', Integer, nullable=False),
    Column('OffPlaneAngle', Float(53)),
    Column('PSACorrection', Float(53)),
    Column('ResourceSer', BigInteger),
    Column('SOBPWidth', Float(53)),
    Column('SnoutPosOverrideFlag', Integer, nullable=False),
    Column('SnoutPosition', Float(53)),
    Column('StopAngle', Float(53)),
    Column('Technique', Unicode(16)),
    Column('WedgeAngle', Float(53)),
    Column('WedgeAngle2', Float(53)),
    Column('WedgeDirection', Float(53)),
    Column('WedgeDirection2', Float(53)),
    Column('WedgeDose', Float(53)),
    Column('WedgeDoseOverrideFlag', Integer, nullable=False),
    Column('WedgeNumber1', Integer),
    Column('WedgeNumber2', Integer)
)


t_vv_syTRTEvents = Table(
    'vv_syTRTEvents', metadata,
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('TreatmentStartTime', DateTime),
    Column('FractionNumber', Integer),
    Column('FractionNumberCalc', Integer),
    Column('EventNumber', Integer),
    Column('LastFractionNumber', Integer),
    Column('LastFractionNumberCalc', Integer),
    Column('LastEventNumber', Integer),
    Column('PatientSer', BigInteger, nullable=False),
    Column('TreatmentStartTimeFirst', DateTime),
    Column('TreatmentStartTimeLast', DateTime)
)


t_vv_syTRTEventsCorrelated = Table(
    'vv_syTRTEventsCorrelated', metadata,
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('TreatmentStartTime', DateTime),
    Column('IsImage', Integer),
    Column('FractionNumber', Integer),
    Column('FractionNumberCalc', Integer),
    Column('EventNumber', Integer),
    Column('CorrelatedEventNumber', Integer),
    Column('LastFractionNumber', Integer),
    Column('LastFractionNumberCalc', Integer),
    Column('LastEventNumber', Integer),
    Column('LastCorrelatedEventNumber', Integer),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('FirstRTPlanSer', BigInteger, nullable=False),
    Column('PatientSer', BigInteger, nullable=False)
)


t_vv_syTRTHistoryRecords = Table(
    'vv_syTRTHistoryRecords', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('TreatmentStartTime', DateTime),
    Column('FractionNumber', Integer),
    Column('RecordMUActual', Float(53)),
    Column('FieldMUActual', Float(53)),
    Column('FieldMUPlanned', Float(53)),
    Column('RecordStatus', Unicode(16)),
    Column('FieldStatus', Unicode(16)),
    Column('TreatmentDeliveryType', Unicode(16)),
    Column('TreatmentStartTimeFirst', DateTime),
    Column('TreatmentStartTimeLast', DateTime)
)


t_vv_syTRTHistoryRecordsDose = Table(
    'vv_syTRTHistoryRecordsDose', metadata,
    Column('PatientSer', BigInteger, nullable=False),
    Column('CourseSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RadiationSer', BigInteger, nullable=False),
    Column('RadiationHstrySer', BigInteger, nullable=False),
    Column('TreatmentStartTime', DateTime),
    Column('FractionNumber', Integer),
    Column('RecordMUActual', Float(53)),
    Column('FieldMUActual', Float(53)),
    Column('FieldMUPlanned', Float(53)),
    Column('RecordStatus', Unicode(16)),
    Column('FieldStatus', Unicode(16)),
    Column('TreatmentDeliveryType', Unicode(16)),
    Column('TreatmentStartTimeFirst', DateTime),
    Column('TreatmentStartTimeLast', DateTime),
    Column('RefPointSer', BigInteger),
    Column('PrimaryFlag', Integer),
    Column('FieldDoseDelivered', Float(53), nullable=False),
    Column('FieldDosePlanned', Float(53), nullable=False)
)


t_vv_syVerificationPlanRelationship = Table(
    'vv_syVerificationPlanRelationship', metadata,
    Column('PlanRelationshipSer', BigInteger, nullable=False),
    Column('RTPlanSer', BigInteger, nullable=False),
    Column('RelatedRTPlanSer', BigInteger),
    Column('RelatedPlanUID', Unicode(64)),
    Column('RelatedPlanSOPClassSer', BigInteger)
)


t_vv_vaAddOnValidation = Table(
    'vv_vaAddOnValidation', metadata,
    Column('ConfiguredEMTSer', BigInteger, nullable=False),
    Column('AddOnSer', BigInteger, nullable=False),
    Column('CacheKeySer', BigInteger),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('ResourceSer', BigInteger, nullable=False),
    Column('TechniqueId', Unicode(16), nullable=False),
    Column('Energy', Integer, nullable=False),
    Column('RadiationType', Unicode(16), nullable=False)
)


t_vv_vaConfiguredEMT = Table(
    'vv_vaConfiguredEMT', metadata,
    Column('ConfiguredEMTSer', BigInteger, nullable=False),
    Column('TechniqueSer', BigInteger, nullable=False),
    Column('EnergyModeSer', BigInteger, nullable=False),
    Column('DefaultVirtualSADX', Float(53)),
    Column('DefaultVirtualSADY', Float(53)),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32)),
    Column('ResourceSer', BigInteger, nullable=False),
    Column('TechniqueId', Unicode(16), nullable=False),
    Column('Energy', Integer, nullable=False),
    Column('RadiationType', Unicode(16), nullable=False)
)


t_vv_vaMLCLeafWide = Table(
    'vv_vaMLCLeafWide', metadata,
    Column('AddOnSer', BigInteger, nullable=False),
    Column('LeafCount', Integer),
    Column('WidthA01', Float(53)),
    Column('WidthA02', Float(53)),
    Column('WidthA03', Float(53)),
    Column('WidthA04', Float(53)),
    Column('WidthA05', Float(53)),
    Column('WidthA06', Float(53)),
    Column('WidthA07', Float(53)),
    Column('WidthA08', Float(53)),
    Column('WidthA09', Float(53)),
    Column('WidthA10', Float(53)),
    Column('WidthA11', Float(53)),
    Column('WidthA12', Float(53)),
    Column('WidthA13', Float(53)),
    Column('WidthA14', Float(53)),
    Column('WidthA15', Float(53)),
    Column('WidthA16', Float(53)),
    Column('WidthA17', Float(53)),
    Column('WidthA18', Float(53)),
    Column('WidthA19', Float(53)),
    Column('WidthA20', Float(53)),
    Column('WidthA21', Float(53)),
    Column('WidthA22', Float(53)),
    Column('WidthA23', Float(53)),
    Column('WidthA24', Float(53)),
    Column('WidthA25', Float(53)),
    Column('WidthA26', Float(53)),
    Column('WidthA27', Float(53)),
    Column('WidthA28', Float(53)),
    Column('WidthA29', Float(53)),
    Column('WidthA30', Float(53)),
    Column('WidthA31', Float(53)),
    Column('WidthA32', Float(53)),
    Column('WidthA33', Float(53)),
    Column('WidthA34', Float(53)),
    Column('WidthA35', Float(53)),
    Column('WidthA36', Float(53)),
    Column('WidthA37', Float(53)),
    Column('WidthA38', Float(53)),
    Column('WidthA39', Float(53)),
    Column('WidthA40', Float(53)),
    Column('WidthA41', Float(53)),
    Column('WidthA42', Float(53)),
    Column('WidthA43', Float(53)),
    Column('WidthA44', Float(53)),
    Column('WidthA45', Float(53)),
    Column('WidthA46', Float(53)),
    Column('WidthA47', Float(53)),
    Column('WidthA48', Float(53)),
    Column('WidthA49', Float(53)),
    Column('WidthA50', Float(53)),
    Column('WidthA51', Float(53)),
    Column('WidthA52', Float(53)),
    Column('WidthA53', Float(53)),
    Column('WidthA54', Float(53)),
    Column('WidthA55', Float(53)),
    Column('WidthA56', Float(53)),
    Column('WidthA57', Float(53)),
    Column('WidthA58', Float(53)),
    Column('WidthA59', Float(53)),
    Column('WidthA60', Float(53)),
    Column('WidthA61', Float(53)),
    Column('WidthA62', Float(53)),
    Column('WidthA63', Float(53)),
    Column('WidthA64', Float(53)),
    Column('WidthA65', Float(53)),
    Column('WidthA66', Float(53)),
    Column('WidthA67', Float(53)),
    Column('WidthA68', Float(53)),
    Column('WidthA69', Float(53)),
    Column('WidthA70', Float(53)),
    Column('WidthA71', Float(53)),
    Column('WidthA72', Float(53)),
    Column('WidthA73', Float(53)),
    Column('WidthA74', Float(53)),
    Column('WidthA75', Float(53)),
    Column('WidthA76', Float(53)),
    Column('WidthA77', Float(53)),
    Column('WidthA78', Float(53)),
    Column('WidthA79', Float(53)),
    Column('WidthA80', Float(53)),
    Column('WidthB01', Float(53)),
    Column('WidthB02', Float(53)),
    Column('WidthB03', Float(53)),
    Column('WidthB04', Float(53)),
    Column('WidthB05', Float(53)),
    Column('WidthB06', Float(53)),
    Column('WidthB07', Float(53)),
    Column('WidthB08', Float(53)),
    Column('WidthB09', Float(53)),
    Column('WidthB10', Float(53)),
    Column('WidthB11', Float(53)),
    Column('WidthB12', Float(53)),
    Column('WidthB13', Float(53)),
    Column('WidthB14', Float(53)),
    Column('WidthB15', Float(53)),
    Column('WidthB16', Float(53)),
    Column('WidthB17', Float(53)),
    Column('WidthB18', Float(53)),
    Column('WidthB19', Float(53)),
    Column('WidthB20', Float(53)),
    Column('WidthB21', Float(53)),
    Column('WidthB22', Float(53)),
    Column('WidthB23', Float(53)),
    Column('WidthB24', Float(53)),
    Column('WidthB25', Float(53)),
    Column('WidthB26', Float(53)),
    Column('WidthB27', Float(53)),
    Column('WidthB28', Float(53)),
    Column('WidthB29', Float(53)),
    Column('WidthB30', Float(53)),
    Column('WidthB31', Float(53)),
    Column('WidthB32', Float(53)),
    Column('WidthB33', Float(53)),
    Column('WidthB34', Float(53)),
    Column('WidthB35', Float(53)),
    Column('WidthB36', Float(53)),
    Column('WidthB37', Float(53)),
    Column('WidthB38', Float(53)),
    Column('WidthB39', Float(53)),
    Column('WidthB40', Float(53)),
    Column('WidthB41', Float(53)),
    Column('WidthB42', Float(53)),
    Column('WidthB43', Float(53)),
    Column('WidthB44', Float(53)),
    Column('WidthB45', Float(53)),
    Column('WidthB46', Float(53)),
    Column('WidthB47', Float(53)),
    Column('WidthB48', Float(53)),
    Column('WidthB49', Float(53)),
    Column('WidthB50', Float(53)),
    Column('WidthB51', Float(53)),
    Column('WidthB52', Float(53)),
    Column('WidthB53', Float(53)),
    Column('WidthB54', Float(53)),
    Column('WidthB55', Float(53)),
    Column('WidthB56', Float(53)),
    Column('WidthB57', Float(53)),
    Column('WidthB58', Float(53)),
    Column('WidthB59', Float(53)),
    Column('WidthB60', Float(53)),
    Column('WidthB61', Float(53)),
    Column('WidthB62', Float(53)),
    Column('WidthB63', Float(53)),
    Column('WidthB64', Float(53)),
    Column('WidthB65', Float(53)),
    Column('WidthB66', Float(53)),
    Column('WidthB67', Float(53)),
    Column('WidthB68', Float(53)),
    Column('WidthB69', Float(53)),
    Column('WidthB70', Float(53)),
    Column('WidthB71', Float(53)),
    Column('WidthB72', Float(53)),
    Column('WidthB73', Float(53)),
    Column('WidthB74', Float(53)),
    Column('WidthB75', Float(53)),
    Column('WidthB76', Float(53)),
    Column('WidthB77', Float(53)),
    Column('WidthB78', Float(53)),
    Column('WidthB79', Float(53)),
    Column('WidthB80', Float(53))
)


t_vv_vaRegisteredVolImage = Table(
    'vv_vaRegisteredVolImage', metadata,
    Column('ReferenceImageSer', BigInteger, nullable=False),
    Column('ReferenceImageFOR', Unicode(64)),
    Column('RegisteredImageSer', BigInteger, nullable=False),
    Column('RegisteredImageFOR', Unicode(64)),
    Column('SpatialRegistrationSer', BigInteger, nullable=False),
    Column('SpatialRegistrationIODSer', BigInteger, nullable=False),
    Column('FrameOfReferenceUID', Unicode(64)),
    Column('ImageFOR', Unicode(64)),
    Column('ImageSer', BigInteger, nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('ImageId', Unicode(16), nullable=False),
    Column('ImageName', Unicode(64)),
    Column('CreationDate', DateTime, nullable=False),
    Column('CreationUserName', Unicode(32)),
    Column('StatusDate', DateTime, nullable=False),
    Column('StatusUserName', Unicode(32), nullable=False),
    Column('ImageType', Unicode(30)),
    Column('Status', Unicode(64), nullable=False),
    Column('VolumetricPixelOffset', Integer),
    Column('ProcessedFlag', Integer, nullable=False),
    Column('DefaultProcessingSer', BigInteger),
    Column('OtherProcessingSer', BigInteger),
    Column('GeometricParentSer', BigInteger),
    Column('PatientSer', BigInteger),
    Column('ImageSizeX', Integer, nullable=False),
    Column('ImageSizeY', Integer, nullable=False),
    Column('ImageSizeZ', Integer, nullable=False),
    Column('ImageResX', Float(53), nullable=False),
    Column('ImageResY', Float(53), nullable=False),
    Column('ImageResZ', Float(53), nullable=False),
    Column('InverseSliceOrder', Integer, nullable=False),
    Column('FocusX', Float(53)),
    Column('FocusY', Float(53)),
    Column('FocusZ', Float(53)),
    Column('Comment', Unicode(254)),
    Column('PatientOrientation', Unicode(16)),
    Column('UsageType', Unicode(64)),
    Column('ActWindow', Integer),
    Column('ActLevel', Integer),
    Column('VolumetricPixelSlope', Float(53)),
    Column('PixelUnit', Unicode(32)),
    Column('Transformation', BINARY(96)),
    Column('VolumeTransformation', BINARY(96)),
    Column('UserOrigin', BINARY(24)),
    Column('UserOriginComment', Unicode(254)),
    Column('DisplayTransformation', BINARY(96)),
    Column('FractionNumber', Integer),
    Column('RefDicomSeqNumber', Integer),
    Column('Image4DSer', BigInteger),
    Column('Flags4D', Integer, nullable=False),
    Column('HstryUserName', Unicode(32), nullable=False),
    Column('HstryTimeStamp', DateTime),
    Column('HstryDateTime', DateTime, nullable=False),
    Column('HstryTaskName', Unicode(32))
)


t_vv_vaSliceCBCT = Table(
    'vv_vaSliceCBCT', metadata,
    Column('SliceSer', BigInteger, nullable=False),
    Column('SeriesSer', BigInteger, nullable=False),
    Column('ResourceSer', BigInteger),
    Column('DCTransferSyntaxSer', BigInteger),
    Column('EquipmentSer', BigInteger),
    Column('SliceUID', Unicode(64), nullable=False)
)


t_vv_vaWedge = Table(
    'vv_vaWedge', metadata,
    Column('AddOnSer', BigInteger, nullable=False),
    Column('WedgeType', Unicode(30)),
    Column('WedgeAngle', Float(53)),
    Column('ThinEdgeToX1Flag', Integer, nullable=False),
    Column('ThinEdgeToX2Flag', Integer, nullable=False),
    Column('ThinEdgeToY1Flag', Integer, nullable=False),
    Column('ThinEdgeToY2Flag', Integer, nullable=False),
    Column('MaxCollX', Float(53)),
    Column('MinCollX', Float(53)),
    Column('MaxCollY', Float(53)),
    Column('MinCollY', Float(53)),
    Column('MaxX1', Float(53)),
    Column('MinX1', Float(53)),
    Column('MaxY1', Float(53)),
    Column('MinY1', Float(53)),
    Column('MaxX2', Float(53)),
    Column('MinX2', Float(53)),
    Column('MaxY2', Float(53)),
    Column('MinY2', Float(53)),
    Column('WedgeDirection', Float(53))
)
