import argparse

# Applying arguments in sequence to the following dict(),
# and if None is met, it's a complete command with valid arguments.
cmd_set = {
    'cmd': {
        'ls':   'List some configuration',
        'add':  'Add a configuration in key-value format',
        'rm':   'Remove a configuration in key-value format',
        'up':   'Perform CO/CM/FM/PM update',
        'chk':  'Perform CO/CM update and check',
        'exec': 'Run some SQL script'
    },
    'cmd alias': {
        'list':    'ls',
        'remove':  'rm',
        'update':  'up',
        'check':   'chk',
        'execute': 'exec'
    },
    'ls': {
        'cmd': {
            'conf':   'List general configuration',
            'ds':     'List data source configuration',
            'db':     'List database configuration'
        },
        'cmd alias': {
            'cfg': 'conf',
            'config': 'conf',
            'configuration': 'conf',
            'datasource': 'ds',
            'data': 'ds',
            'database': 'db'
        },
        'conf': None, # adding dict() dynamically
        'ds': None,   # adding dict() dynamically
        'db': None    # adding dict() dynamically
    },
    'add': {
        'cmd': {
            'conf': 'Add configuration in key-value format'
        },
        'cmd alias': {
            'cfg': 'conf',
            'config': 'conf',
            'configuration': 'conf'
        },
        'config': dict()
    },
    'rm': {
        'cmd': {
            'conf': 'Remove configuration in key-value format'
        },
        'cmd alias': {
            'cfg': 'conf',
            'config': 'conf',
            'configuration': 'conf'
        },
        'config': dict()
    },
    'up': {
        'cmd': {
            'co': 'Update CO data of some date yyyymmdd',
            'cm': 'Update CM data of some date yyyymmdd',
            'fm': 'Update FM data of some date yyyymmdd',
            'pm': 'Update PM data of some date yyyymmdd'
        },
        'cmd_alias': {
            'common_object': 'co',
            'configuration': 'cm',
            'configuration_management': 'cm',
            'alarm': 'fm',
            'fx_alarm': 'fm',
            'performance': 'pm',
            'performance_management': 'pm'
        },
        'co': dict(),
        'cm': dict(),
        'fm': dict(),
        'pm': dict()
    },
    'chk': {
        'cmd': {
            'co': 'Update CO data of some date yyyymmdd, then check',
            'cm': 'Update CM data of some date yyyymmdd, then check'
        },
        'cmd_alias': {
            'common_object': 'co',
            'configuration': 'cm',
            'configuration_management': 'cm'
        },
        'co': dict(),
        'cm': dict()
    },
    'exec': dict() # Take files
}

parser = argparse.ArgumentParser( description= "SQL Execution Module" )
parser.add_argument('cus_ID', type= str, help= 'Customer ID like "TWM" or "KHS"')
parser.add_argument('path', type= str, help= 'File path')
args = parser.parse_args()

##
## Strategy
##
## When you find some key-value like (k: None) deep in the nested `cmd_set', it's a valid command,
## else not.
##
