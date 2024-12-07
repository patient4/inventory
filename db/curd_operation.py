from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from Model.Product import Product
from db.connection import connect_to_mysql, Base


class Database:
    def __init__(self):
        self.session, self.engine = connect_to_mysql()

    def add(self, obj):
        try:
            self.session.add(obj)  # Add the object to the session
            self.session.commit()  # Commit to the database
            return True, f"{obj.__class__.__name__} added successfully!"
        except SQLAlchemyError as e:
            self.session.rollback()  # Rollback in case of error
            return False, f"Error: {str(e)}"

    def get(self, model, id):
        try:
            result = self.session.query(model).filter(model.id == id).first()
            if result:
                return True, result
            else:
                return False, f"{model.__name__} with ID {id} not found."
        except SQLAlchemyError as e:
            return False, f"Error: {str(e)}"


    def update(self, model, id, **kwargs):
        try:
            # Print received details
            print(f"Received in update: model={model.id}, id={id}, kwargs={kwargs}")
            # Query the record by the provided ID
            record = self.session.query(model).filter(model.id == id).first()
            print(f"Record found: {record}")

            if record:
                # Update the attributes of the record
                for key, value in kwargs.items():
                    setattr(record, key, value)  # Update each attribute dynamically
                self.session.commit()  # Commit to the database
                return True, f"{model.__name__} with ID {id} updated successfully!"
            else:
                return False, f"{model.__name__} with ID {id} not found."
        except SQLAlchemyError as e:
            self.session.rollback()  # Rollback in case of error
            print(f"Error: {str(e)}")
            return False, f"Error: {str(e)}"

    def delete(self, model, id):
        try:
            record = self.session.query(model).filter(model.id == id).first()
            if record:
                self.session.delete(record)  # Delete the record
                self.session.commit()  # Commit to the database
                return True, f"{model.__name__} with ID {id} deleted successfully!"
            else:
                return False, f"{model.__name__} with ID {id} not found."
        except SQLAlchemyError as e:
            self.session.rollback()  # Rollback in case of error
            return False, f"Error: {str(e)}"

    def get_all(self, model):
        try:
            records = self.session.query(model).all()
            if records:
                return True, records
            else:
                return False, f"No records found for {model.__name__}."
        except SQLAlchemyError as e:
            return False, f"Error: {str(e)}"
