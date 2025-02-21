from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from models.patient import Patient
from models.protocole import Protocole
from models.stock import Stock


class Rule(ABC):
    @abstractmethod
    def is_valid(self, patient: Patient, protocole: Optional[Protocole], stock: Stock, medication: str, doses: int, date: datetime) -> bool:
        pass

class Rule801(Rule):
    def is_valid(self, patient: Patient, protocole: Optional[Protocole], stock: Stock, medication: str, doses: int, date: datetime) -> bool:
        if medication != 'X':
            return True
        if patient.taux_globules_blancs > 2000:
            return True
        if protocole and protocole.nom == 'Gamma' and patient.taux_globules_blancs > 1500:
            return True
        return not (patient.rechute and patient.rechute > 2019)

class Rule327(Rule):
    def is_valid(self, patient: Patient, protocole: Optional[Protocole], stock: Stock, medication: str, doses: int, date: datetime) -> bool:
        if medication not in ['Y', 'Z']:
            return True
        if 'Y' in patient.medications and 'Z' in patient.medications:
            return 'BRCA1' in patient.dossier_genetique or date.weekday() == 2
        return True

class Rule666(Rule):
    def is_valid(self, patient: Patient, protocole: Optional[Protocole], stock: Stock, medication: str, doses: int, date: datetime) -> bool:
        if medication != 'W':
            return True
        return stock.has_sufficient_stock(medication, doses, date.weekday() >= 5)