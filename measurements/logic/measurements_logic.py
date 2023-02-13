from ..models import Measurement

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.value = new_mea["value"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(var["id"],var["variable"], value=var["value"], unit = var["unit"], place=var["place"])
    measurement.save()
    return measurement
    