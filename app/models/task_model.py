from database import db

# Define la clase Task que hereda de db.Model
class Task(db.Model):
    __tablename__ = "tasks"
    
    # Define las columnas de la tabla 'candies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
    assigned_to = db.Column(db.String, nullable=False)
    
    def __init__(self, title, description, status, created_at, assigned_to):
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.assigned_to = assigned_to
    
    # Guarda los datos
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Task.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Task.query.get(id)
    
    def update(self, title=None, description=None, status=None, created_at=None, assigned_to=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if assigned_to is not None:
            self.assigned_to = assigned_to
        db.session.commit()
    
    # Elimina un dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()