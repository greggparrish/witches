import re
from app import db

ethnicities = ("Gael", "English", "Irish", "Italian", "German", "Unknown")
marital_statuses = ("Married", "Widowed", "Single", "Irregular union", "Unknown")
socioeconomic_statuses = ("Lower", "Middling", "Upper", "Landless", "Lairds/Baron", "Very Poor", "Nobility/Chiefs", "Unknown")


class Accused(db.Model):
    __tablename__= 'accused'

    id = db.Column(db.Integer, primary_key=True)
    old_id = db.Column(db.String(128))
    accusations = db.relationship('Accusation', backref='accused', lazy='dynamic')
    family = db.relationship('AccusedFamily', backref='accused', lazy='dynamic')
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    m_first_name = db.Column(db.String(128))
    m_last_name = db.Column(db.String(128))
    alias = db.Column(db.String(128))
    destitle = db.Column(db.String(128))
    sex = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    age_estcareer = db.Column(db.Boolean)
    age_estchild = db.Column(db.Boolean)
    res_settlement = db.Column(db.String(128))
    res_parish = db.Column(db.String(128))
    res_presbytery = db.Column(db.String(128))
    res_county = db.Column(db.String(128))
    res_burgh = db.Column(db.String(128))
    res_ngr_letters = db.Column(db.String(128))
    res_ngr_easting = db.Column(db.Integer)
    res_ngr_northing = db.Column(db.Integer)
    ethnicity = db.Column(db.Enum(*ethnicities, name="ethnicity"))
    marital_status = db.Column(db.Enum(*marital_statuses, name="marital_status"))
    socioeconomic_status = db.Column(db.Enum(*socioeconomic_statuses, name="socioeconomic_status"))
    occupation = db.Column(db.String(128))
    notes = db.Column(db.Text)

    def __repr__(self):
        return 'Accused: {} {}'.format(self.first_name,self.last_name)

class AccusedFamily(db.Model):
    __tablename__= 'accused_family'
    id = db.Column(db.Integer, primary_key=True)
    accused_id = db.Column(db.Integer, db.ForeignKey(Accused.id))
    accused_family_ref = db.Column(db.String(128))
    accused_ref = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    alias = db.Column(db.String(128))
    patronymic = db.Column(db.String(128))
    destitle = db.Column(db.String(128))
    est_birthyear = db.Column(db.String(128))
    age = db.Column(db.Integer)
    age_estcareer = db.Column(db.Integer)
    age_estchild = db.Column(db.Integer)
    occupation = db.Column(db.String(128))
    relationship = db.Column(db.String(128))

    def family_data(self):
        ''' Make list of family member age, occupation if exists '''
        whitelist = ['age', 'occupation']
        return ["{}: {}".format(re.sub('_',' ',key).capitalize(),val) for key, val in self.__dict__.items() if key in whitelist and val != None]


    def __repr__(self):
        return 'Family of accused: {} {}'.format(self.first_name,self.last_name)
