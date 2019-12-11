

def delete_data(code, min, max, min_value, data):

    data = data.filter(date__gt=min, date__lt=max)

    for d in data:

        values = d.data

        if code in values:
            if values[code] is None:
                continue

            if values[code] < min_value:
                values[code] = None
                d.data = values
                d.save()


def copy_data(src_station, des_station, src_sensor, des_sensor):

    from visualizer.models import StationData

    src_station_data = StationData.objects.filter(station_id=src_station)
    des_station_data = StationData.objects.filter(station_id=des_station)

    count = 0
    existing_count = 0
    new_count = 0
    for record in src_station_data:

        if record.data.has_key(src_sensor):
                
            record_to_change = des_station_data.filter(station_id=des_station, date=record.date)

            if record_to_change.exists():

                changed_record = record_to_change[0]
                record_data = changed_record.data
                record_data.update({des_sensor : record.data[src_sensor]})
                changed_record.data = record_data
                changed_record.save()
                existing_count+=1
            else:

                record.pk = None
                record.station_id = des_station
                record.save()
                new_count+=1

            count+=1

    print('records inserted: ', count)



def serialize_widget(widget):

    w = {}

    w.update({
        'user': widget.user.username,
        'index': widget.index,
        'widget_type': widget.widget_type,
        'dashboard': widget.dashboard.name,
        'expand': widget.expand
        })

    for k, v in widget.widget['data'].items():
        if k in ['title', 'calc', 'range']:
            continue

        if v:
            for i, value in enumerate(v['value']):
                if value:
                    v['value'][i] = value[:1]

    w.update({'widget': widget.widget})

    return w

def serialize_stats(stat):
    return []

def serializer_user_data(username):
    from visualizer.models import Widgets

    data = {
        'charts': [],
    }

    charts = Widgets.objects.filter(widget_type='main-chart', user__username=username)

    for chart in charts:
        data['charts'].append(clone_widget(chart))

    dashboards = Dashboard.objects.filter(user__username=username)

    data['dashboards'] = list(dashboards.values_list('name', flat=True))




