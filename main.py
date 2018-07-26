class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.patients = []
        for x in range(0,capacity):
            self.patients.append(0)
    def add(self, patient):
        for x in range(0, len(self.patients)):
            if self.patients[x] == 0:
                self.patients[x] = patient
                patient.bed_number = x+1
                break
        return self
    def discharge(self, patient_id):
        for x in range(0, len(self.patients)):
            if self.patients[x].id == patient_id:
                self.patients[x] = 0
                break
        return self
    def display(self):
        print self.patients
        for patient in self.patients:
            if patient == 0:
                continue
            else:
                print "patient id: {} name: {} allergies: {} bed: {}".format(patient.id, patient.name, patient.allergies, patient.bed_number)
        return self

p1 = Patient(1111, "will", "pnuts")
p2 = Patient(1112, "bill", "peanuts")
p3 = Patient(1113, "jill", "Weanuts")
p4 = Patient(1114, "Gill", "Teanuts")

hospital1 = Hospital("st jude", 40)
hospital1.add(p1).add(p2).add(p3).discharge(1112).add(p4)
hospital1.display()