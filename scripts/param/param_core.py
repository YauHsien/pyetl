# Applying arguments in sequence to the following dict(),
# and if None is met, it's a complete command with valid arguments.
cmd_set = {
    'cmd': set(['list', 'update', 'check', 'execute', 'config']),
    'cmd_alias': dict(),
    'list': {
        'cmd': set(['config', 'datasource', 'database']),
        'config': None, # adding dict() dynamically
        'datasource': dict(),
        'database': dict()
    },
    'update': {
        'cmd': set(['co', 'cm', 'fm', 'pm']),
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
    'check': {
        'cmd': set(['co', 'cm',]),
        'cmd_alias': {
            'common_object': 'co',
            'configuration': 'cm',
            'configuration_management': 'cm'
        },
        'co': dict(),
        'cm': dict()
    },
    'execute': dict(),
    'config': {
        'cmd': set(['add', 'remove', 'list']),
        'add': dict(),
        'remote': dict(),
        'list': None
    }
}
