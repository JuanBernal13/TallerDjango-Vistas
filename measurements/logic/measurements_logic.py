from ..models import Measurement

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.name = new_mea["name"]
    measurement.save()
    return measurement

def create_measurement(mea):
    measurement = measurement(name=mea["name"])
    measurement.save()
    return measurement