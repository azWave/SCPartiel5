from datetime import datetime
from models.patient import Patient
from models.protocole import Protocole
from models.stock import Stock
from rules import Rule801, Rule327, Rule666
from models.prescription_validator import PrescriptionValidator


patient = Patient(1800, 2020, ['Y', 'Z'], ['BRCA1'])
protocole = Protocole('Gamma')
stock = Stock({'W': 10})
rules = [Rule801(), Rule327(), Rule666()]
validator = PrescriptionValidator(rules)
date_test = datetime(2025, 2, 21)

print(validator.validate_prescription(patient, protocole, stock, 'X', 1, date_test))  
print(validator.validate_prescription(patient, protocole, stock, 'Y', 1, date_test))  
print(validator.validate_prescription(patient, protocole, stock, 'W', 2, date_test)) 