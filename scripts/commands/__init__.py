''' Usage:
    etl ls {{conf|ds|db}} [key]
    etl add {{conf|ds|db}} key value
    etl rm {{conf|ds|db}} key
    etl up {{co|cm|fm|pm}} yyyymmdd
    etl chk {{co|cm}} later_date earlier_date
    etl exec path

commands:
    ls    list configuration of either general, data source, database.
    add   add an item into one of those configurations.
    rm    remote an item from one of those configurations.
    up    update either CO, CM, FM, or PM data of some date.
    chk   check either CO or CM data between some date to another date.
    exec  execute some SQL script.

alias:
    ls    list
    rm    remove
    up    update
    chk   check
    exec  execute
    conf  cfg, config, configuration
    ds    datasource
    db    database
    co    common_object
    cm    configuration_management
    fm    alarm, fx_alarm
    pm    performance, performance_measurement
'''
