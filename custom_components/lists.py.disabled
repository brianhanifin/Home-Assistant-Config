"""Component to manage lists."""
import asyncio
import logging
import uuid
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.core import callback
from homeassistant.components import http
from homeassistant.components.http.data_validator import (RequestDataValidator)
from homeassistant.util.json import load_json, save_json

ATTR_NAME = 'name'
ATTR_ITEM_ID = 'item_id'
ATTR_CATEGORY_ID = 'category_id'
ATTR_LIST_ID = 'list_id'

DOMAIN = 'lists'
DEPENDENCIES = ['http']
_LOGGER = logging.getLogger(__name__)
CONFIG_SCHEMA = vol.Schema({DOMAIN: {}}, extra=vol.ALLOW_EXTRA)

ITEM_UPDATE_SCHEMA = vol.Schema({
    'complete': bool,
    'id': str,
    ATTR_CATEGORY_ID: str,
    ATTR_LIST_ID: str,
    ATTR_NAME: str,
})
PERSISTENCE = '.lists.json'

SERVICE_ADD_LIST = 'add_list'
SERVICE_ADD_CATEGORY = 'add_category'
SERVICE_ADD_ITEM = 'add_item'
SERVICE_COMPLETE_ITEM = 'complete_item'
SERVICE_DELETE_LIST = 'delete_list'
SERVICE_DELETE_CATEGORY = 'delete_category'
SERVICE_CLEAR_COMPLETED = 'clear_completed'

SERVICE_LIST_SCHEMA = vol.Schema({
    vol.Required(ATTR_NAME): vol.Any(None, cv.string)
})

SERVICE_CATEGORY_SCHEMA = vol.Schema({
    vol.Required(ATTR_NAME): vol.Any(None, cv.string),
    vol.Optional(ATTR_LIST_ID, default='0'): vol.Any(None, cv.string)
})

SERVICE_ITEM_SCHEMA = vol.Schema({
    vol.Required(ATTR_NAME): vol.Any(None, cv.string),
    vol.Optional(ATTR_CATEGORY_ID, default='0'): vol.Any(None, cv.string),
    vol.Optional(ATTR_LIST_ID, default='0'): vol.Any(None, cv.string)
})

SERVICE_ITEM_COMPLETE_SCHEMA = vol.Schema({
    vol.Required(ATTR_ITEM_ID): vol.Any(None, cv.string),
    vol.Optional(ATTR_CATEGORY_ID, default='0'): vol.Any(None, cv.string),
    vol.Optional(ATTR_LIST_ID, default='0'): vol.Any(None, cv.string)
})

SERVICE_DELETE_LIST_SCHEMA = vol.Schema({
    vol.Required(ATTR_LIST_ID): vol.Any(None, cv.string)
})

SERVICE_DELETE_CATEGORY_SCHEMA = vol.Schema({
    vol.Required(ATTR_CATEGORY_ID): vol.Any(None, cv.string),
    vol.Optional(ATTR_LIST_ID, default='0'): vol.Any(None, cv.string)
})

SERVICE_CLEAR_COMPLETED_SCHEMA = vol.Schema({
    vol.Required(ATTR_LIST_ID): vol.Any(None, cv.string)
})

@asyncio.coroutine
def async_setup(hass, config):
    """Initialize the lists."""
    @asyncio.coroutine
    def add_list_service(call):
        """Add list with `name`."""
        data = hass.data[DOMAIN]
        name = call.data.get(ATTR_NAME)
        if name is not None:
            data.async_add_list(name)

    @asyncio.coroutine
    def add_category_service(call):
        """Add a category with `name`."""
        data = hass.data[DOMAIN]
        name = call.data.get(ATTR_NAME)
        list_id = call.data.get(ATTR_LIST_ID)
        if name is not None:
            data.async_add_category(name, list_id)

    @asyncio.coroutine
    def add_item_service(call):
        """Add an item with `name`."""
        data = hass.data[DOMAIN]
        name = call.data.get(ATTR_NAME)
        list_id = call.data.get(ATTR_LIST_ID)
        category_id = call.data.get(ATTR_CATEGORY_ID)
        if name is not None:
            data.async_add_item(name, list_id, category_id)

    @asyncio.coroutine
    def complete_item_service(call):
        """Mark the item provided via `name` as completed."""
        data = hass.data[DOMAIN]
        item_id = call.data.get(ATTR_ITEM_ID)
        list_id = call.data.get(ATTR_LIST_ID)
        category_id = call.data.get(ATTR_CATEGORY_ID)
        if item_id is None:
            return

        my_list = data.lists[list_id]

        if my_list is None:
            _LOGGER.error("Removing of item failed: list_id %d cannot be found", list_id)
            return

        category = my_list['categories'][category_id]

        if category is None:
            _LOGGER.error("Removing of item failed: category_id %d cannot be found", category_id)
            return

        item = category['items'][item_id]

        if item is None:
            _LOGGER.error("Removing of item failed: name_id %d cannot be found", item_id)
            return

        item['complete'] = True
        data.async_update_item(list_id, category_id, item_id, item)

    @asyncio.coroutine
    def delete_list_service(call):
        """Delete a list with `list_id`."""
        data = hass.data[DOMAIN]
        list_id = call.data.get(ATTR_LIST_ID)

        if list_id is not None and list_id is not '0':
            data.async_delete_list(list_id)

    @asyncio.coroutine
    def delete_category_service(call):
        """Delete a category with `category_id`."""
        data = hass.data[DOMAIN]
        list_id = call.data.get(ATTR_LIST_ID)
        category_id = call.data.get(ATTR_CATEGORY_ID)

        if list_id is not None and category_id is not None and category_id is not '0':
            data.async_delete_category(list_id, category_id)
            
    @asyncio.coroutine
    def clear_completed_service(call):
        """Clear completed items with `list_id`."""
        data = hass.data[DOMAIN]
        list_id = call.data.get(ATTR_LIST_ID)

        if list_id is not None:
            data.async_clear_completed(list_id)

    data = hass.data[DOMAIN] = ListsData(hass)
    yield from data.async_load()

    hass.services.async_register(
        DOMAIN, SERVICE_ADD_LIST, add_list_service, schema=SERVICE_LIST_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_ADD_CATEGORY, add_category_service, schema=SERVICE_CATEGORY_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_ADD_ITEM, add_item_service, schema=SERVICE_ITEM_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_COMPLETE_ITEM, complete_item_service, schema=SERVICE_ITEM_COMPLETE_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_DELETE_LIST, delete_list_service, schema=SERVICE_DELETE_LIST_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_DELETE_CATEGORY, delete_category_service, schema=SERVICE_DELETE_CATEGORY_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_CLEAR_COMPLETED, clear_completed_service, schema=SERVICE_CLEAR_COMPLETED_SCHEMA
    )

    hass.http.register_view(ListsView)

    return True


class ListsData:
    """Class to hold lists data."""

    def __init__(self, hass):
        """Initialize the lists."""
        self.hass = hass
        self.lists = {}

    @callback
    def async_add_list(self, name):
        """Add a list"""
        new_list = {
            'name': name,
            'id': uuid.uuid4().hex + '',
            'categories': {
                '0': {
                        'name': 'Uncategorized',
                        'id': '0',
                        'items': {}
                    }
            }
        }

        self.lists[new_list.get('id')] = new_list
        self.hass.async_add_job(self.save)
        return new_list

    @callback
    def async_add_category(self, name, list_id):
        """Add a category."""
        new_category = {
            'name': name,
            'id': uuid.uuid4().hex + '',
            'list_id': list_id,
            'items': {}
        }

        self.lists[list_id]['categories'][new_category.get('id')] = new_category
        self.hass.async_add_job(self.save)
        return new_category

    @callback
    def async_add_item(self, name, list_id, category_id):
        """Add a list item."""
        item = {
            'name': name,
            'id': uuid.uuid4().hex + '',
            'list_id': list_id,
            'category_id': category_id,
            'complete': False
        }
        
        _LOGGER.error(self.lists)

        self.lists[list_id]['categories'][category_id]['items'][item.get('id')] = item
        self.hass.async_add_job(self.save)
        return item

    @callback
    def async_delete_list(self, list_id):
        """Delete a list item."""
        self.lists.pop(list_id, None)
        self.hass.async_add_job(self.save)

    @callback
    def async_delete_category(self, list_id, category_id):
        """Delete a category item."""
        self.lists[list_id]['categories'].pop(category_id, None)
        self.hass.async_add_job(self.save)

    @callback
    def async_update_list(self, list_id, info):
        """Update a list."""
        list = self.lists[list_id]

        if list is None:
            raise KeyError

        info = ITEM_UPDATE_SCHEMA(info)
        list.update(info)
        self.hass.async_add_job(self.save)
        return list

    @callback
    def async_update_category(self, list_id, category_id, info):
        """Update a category."""
        new_list = self.lists[list_id]

        if new_list is None:
            raise KeyError

        category = new_list['categories'][category_id]

        if category is None:
            raise KeyError

        info = ITEM_UPDATE_SCHEMA(info)
        category.update(info)
        self.hass.async_add_job(self.save)
        return category

    @callback
    def async_update_item(self, list_id, category_id, item_id, info):
        """Update a list item."""
        new_list = self.lists[list_id]

        if new_list is None:
            raise KeyError

        category = new_list['categories'][category_id]

        if category is None:
            raise KeyError

        item = category['items'][item_id]

        if item is None:
            raise KeyError

        info = ITEM_UPDATE_SCHEMA(info)
        item.update(info)
        self.hass.async_add_job(self.save)
        return item

    @callback
    def async_clear_completed(self, list_id):
        """Clear completed items."""
        
        
        for c, category in self.lists[list_id]['categories'].items():
            non_complete_items = {}
            for i, item in category['items'].items():
                if not item['complete']:
                    non_complete_items[item['id']] = item
            category['items'] = non_complete_items
        self.hass.async_add_job(self.save)

    @asyncio.coroutine
    def async_load(self):
        """Load items."""
        def load():
            """Load the items synchronously."""
            return load_json(self.hass.config.path(PERSISTENCE),
                default={'0': {
                                'name': 'Inbox',
                                'id': '0',
                                'categories': {
                                    '0': {
                                        'name': 'Uncategorized',
                                        'id': '0',
                                        'items': {}
                                    }
                                }
                            }
                        }
                    )

        self.lists = yield from self.hass.async_add_job(load)

    def save(self):
        """Save the items."""
        save_json(self.hass.config.path(PERSISTENCE), self.lists)


class ListsView(http.HomeAssistantView):
    """View to retrieve list content."""

    url = '/api/lists'
    name = "api:lists"

    @callback
    def get(self, request):
        """Retrieve list items."""
        return self.json(request.app['hass'].data[DOMAIN].lists)