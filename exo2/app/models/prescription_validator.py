from typing import List, Optional
from datetime import datetime
from models.patient import Patient
from models.protocole import Protocole
from models.stock import Stock
from rules import Rule

class PrescriptionValidator:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
    
    def validate_prescription(self, patient: Patient, protocole: Optional[Protocole], stock: Stock, medication: str, doses: int, date: datetime) -> bool:
        return all(rule.is_valid(patient, protocole, stock, medication, doses, date) for rule in self.rules)