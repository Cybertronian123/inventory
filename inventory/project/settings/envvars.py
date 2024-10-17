from inventory.core.utils.collections import deep_update
from inventory.core.utils.settings import get_settings_from_environment

"""
This takes env variables with a matching prefix, strips out the prefix, and adds it to global variables

For example:
export INVENTORYSETTINGS_IN_DOCKER=true (environment variable)

Could then be referenced as a global as:
IN_DOCKER (where the value would be True)
"""


deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX)) # type: ignore