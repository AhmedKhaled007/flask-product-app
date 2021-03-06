def get_or_create(db, model, defaults=None, **kwargs):
    instance = model.query.filter_by(**kwargs).one_or_none()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        try:
            db.session.add(instance)
            db.session.commit()
        except Exception:
            db.session.rollback()
            instance = model.query.filter_by(**kwargs).one()
            return instance
        else:
            return instance
