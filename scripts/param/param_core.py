import re, datetime

##
## Get Help Page
##

param_spec = """
usage:
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
             """

def show_cfg(key):
    if key is None:
        pass
    else:
        pass

def show_ds_cfg(key):
    if key is None:
        pass
    else:
        pass

def show_db_cfg(key):
    if key is None:
        pass
    else:
        pass

def add_cfg(kv):
    pass

def add_ds_cfg(kv):
    pass

def add_db_cfg(kv):
    pass

def rm_cfg(key):
    pass

def rm_ds_cfg(key):
    pass

def rm_db_cfg(key):
    pass

def update_co(date):
    pass

def update_cm(date):
    pass

def update_fm(date):
    pass

def update_pm(date):
    pass

def chk_co(two_dates):
    pass

def chk_cm(two_dates):
    pass

def exe_sql_sc(path):
    pass

##
## Strategy
##
## When you find some value which is not dict() deep in the nested `cmd_all', it's a valid command,
## else not.
##
def meet(args):
    if type(args) is list:
        cmd, target, key, path, value = args[1] if len(args) > 1 else None, \
                                        args[2] if len(args) > 2 else None, \
                                        args[3] if len(args) > 3 else None, \
                                        args[3] if len(args) > 3 else None, \
                                        args[4] if len(args) > 4 else None
        ls = set(['ls', 'list'])
        conf = set(['conf', 'cfg', 'config', 'configuration'])
        ds = set(['ds', 'datasource'])
        db = set(['db', 'database'])
        add = set(['add'])
        rm = set(['rm', 'remove'])
        up = set(['up', 'update'])
        chk = set(['chk', 'check'])
        ex = set(['exec', 'execute'])
        co = set(['co', 'CO', 'common_object'])
        cm = set(['cm', 'CM', 'configuration_management'])
        fm = set(['fm', 'FM', 'alarm', 'fx_alarm'])
        pm = set(['pm', 'PM', 'performance', 'performance_measurement'])
        is_date = re.compile(r'^\d\d\d\d\d\d\d\d$')
        if cmd in ls:
            if target in conf:
                return show_cfg, key
            elif target in ds:
                return show_ds_cfg, key
            elif target in db:
                return show_db_cfg, key
        elif cmd in add:
            if key is not None and value is not None:
                if target in conf:
                    return add_cfg, (key, value)
                elif target in ds:
                    return add_ds_cfg, (key, value)
                elif target in db:
                    return add_db_cfg, (key, value)
        elif cmd in rm:
            if key is not None:
                if target in conf:
                    return rm_cfg, key
                elif target in ds:
                    return rm_ds_cfg, key
                elif target in db:
                    return rm_db_cfg, key
        elif cmd in up:
            if target in co or target in cm or target in fm or target in pm:
                key = Util.conv_date(key)
                if type(key) is datetime.date:
                    if target in co:
                        return update_co, key
                    elif target in cm:
                        return update_cm, key
                    elif target in fm:
                        return update_fm, key
                    elif target in pm:
                        return update_pm, key
        elif cmd in chk:
            if target in co or target in cm:
                key = Util.conv_date(key)
                value = Util.conv_date(value)
                if type(key) is datetime.date and type(value) is datetime.date:
                    if target in co:
                        return chk_co, (key, value)
                    elif target in cm:
                        return chk_cm, (key, value)
        elif cmd in ex:
            if target is not None:
                return exe_sql_sc, target
