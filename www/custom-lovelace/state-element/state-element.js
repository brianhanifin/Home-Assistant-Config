class StateAttributeElement extends HTMLElement {
  set hass(hass) {
    const entityId = this.config.entity;
    const prefix_string = this.config.prefix
    const show_empty = this.config.show_empty
    const attr = this.config.attribute;
    const state = hass.states[entityId].attributes[attr];
    const card = document.createElement('state-attribute-element');
    if (state.length != 0) {
      if (prefix_string) {
        this.innerHTML = prefix_string + state;
      } else {
        this.innerHTML = state;
      }
    } else if (show_empty == true) {
      if (prefix_string) {
        this.innerHTML = prefix_string + state;
      } else {
        this.innerHTML = state;
      }
    }
  }
  setConfig(config) {
    if (!config.entity) {
      throw new Error('You need to define an entity');
    }
    if (!config.attribute) {
      throw new Error('You need to define an attribute');
    }
    if (!config.show_empty) {
      config.show_empty = false;
    }
    this.config = config;
  }

  getCardSize() {
    return 1;
  }
}
customElements.define('state-attribute-element', StateAttributeElement);